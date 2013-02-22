function draw(plotclass, plotid) {

 var margin = {top: 20, right: 20, bottom: 50, left: 60},
    width = 750 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

 var x = d3.scale.log()
    .range([0, width]);


 if(plotclass == "bipartite") {
  var y = d3.scale.log()
    .range([height, 10]);
 } else {
  var y = d3.scale.linear()
    .range([height, 10]);
 }

 var s = d3.scale.log()
    .range([1, 2]);

 var color = d3.scale.category10();

 var numberFormat = d3.format("g");

 function logFormat(d) {
    return d >= 1 ? numberFormat(d) : d >= 0.1 ? numberFormat(d.toPrecision(1)) : numberFormat(d.toPrecision(2));
 }

 var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom")
    .ticks("10", logFormat);

 var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    .ticks("10", logFormat);

 var svg = d3.select("div#plot").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

 d3.json("/aidxp/explore/profile/" + pageid + "/" + plotclass + "/" + plotid + "/", function(error, data) {

  data.points.forEach(function(d) {
    d.y = +d.y;
    d.x = +d.x;
  });

  x.domain(d3.extent(data.points, function(d) { return d.x; })).nice();
  y.domain(d3.extent(data.points, function(d) { return d.y; })).nice();

  if(plotclass == "bipartite") {
    axisOrigin = 1;
  } else {
    axisOrigin = 0;
  }

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + y(axisOrigin) + ")")
      .call(xAxis.tickPadding(height - y(axisOrigin)))
    .append("text")
      .attr("class", "label")
      .attr("x", width)
      .attr("y", (height - y(axisOrigin)) + 40)
      .style("text-anchor", "end")
      .text(data.x_axis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis.tickPadding(x(1)))
      .attr("transform", "translate(" + x(1) + ", 0)")
    .append("text")
      .attr("class", "label")
      .attr("transform", "rotate(-90)")
      .attr("y", -x(1) - 50)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text(data.y_axis);

  svg.selectAll(".dot")
      .data(data.points)
    .enter().append("circle")
      .attr("class", "dot")
      .attr("cx", function(d) { return x(d.x); })
      .attr("cy", function(d) { return y(d.y); })
      .style("stroke", "#000000")
      .style("fill", "#000000")
      .style("fill-opacity", ".25")
      .attr("r", function(d) { return s(d.size); } )
      .on("click", function(d) { window.location.replace("/aidxp/explore/profile/" + d.id  + "/"); })
      .on("mouseover", function() { d3.select(this).style("fill", "#BA093E"); })
      .on("mouseout", function() { d3.select(this).style("fill", "#000000"); });

  svg.selectAll("g.x line")
      .attr("y1", -y(axisOrigin) + 10)
      .attr("y2", height - y(axisOrigin)) 
      .style("stroke", "#000000")
      .style("stroke-opacity", ".2");

  svg.selectAll("g.y line")
      .attr("x1", -x(1))
      .attr("x2", width - x(1))
      .style("stroke", "#000000")
      .style("stroke-opacity", ".2");

  svg.selectAll("path");

  if(plotclass == "bipartite") {
   svg.append("text")
      .text(data.plot_title)
      .attr("x", width / 2)
      .style("text-anchor", "middle");

   svg.append("line")
    .attr("class", "trend")
    .attr("x1", x(data.trendline.x1))
    .attr("y1", y(data.trendline.y1))
    .attr("x2", x(data.trendline.x2))
    .attr("y2", y(data.trendline.y2))
    .style("stroke", "#BA093E")
    .style("stroke-width", 2)
    .on("mouseover", function() { d3.select(this).style("stroke-width", 4); })
    .on("mouseout", function() { d3.select(this).style("stroke-width", 2); });

   $(".trend").tipsy({
     gravity: 'w',
     html: true,
     title: function() {
       var d = this.__data__, l = data.trendlabel;
       return l;
     }
   });
  }

  $(".dot").tipsy({ 
     gravity: 'w', 
     html: true, 
     title: function() {
       var d = this.__data__, l = d.label + "<hr />" + data.x_axis + ": " + d.x + "<br />" + data.y_axis + ": " + d.y;
       return l; 
     }
  });
 });

 if(plotclass == "bipartite") {
  $("div#question-text").html("How does " + pagename + " relate to <select id='target-entity'></select> over " + thirdtype + "?");
  getList(othertype);
 } else {
  $("div#question-text").html("How does " + pagename + " relate to all " + plotid + "?");
 }
}

$(document).ready(function(){
  if(plotid == -1) {
    if(pagetype == "IS") {
      othertype = "Countries";
      thirdtype = "Organizations";
    } else {
      othertype = "Issues";
      if(pagetype == "OR") {
        thirdtype = "Countries";
      } else {
        thirdtype = "Organizations";
      }
    }
    plotid = giveMeARandomId(othertype);
    plottype = "bipartite";
  }
  if(plottype == "bipartite_rank") {
     toggleRankType(plotid);
  } else {
     draw(plottype, plotid);
  }
});

$('.profile-switcher').change(function() {
  window.location.replace("/aidxp/explore/profile/" + this.value  + "/");
});

function togglePlotType(newtype, plotclass) {
  if(plotclass == "bipartite") {
    if(othertype != newtype) {
       thirdtype = othertype;
       othertype = newtype;
     }
     plotid = giveMeARandomId(othertype);
  } else {
     plotid = newtype;
  }
  $("div#plot").html("");
  draw(plotclass, plotid);
}

function toggleRankType(type) {
  $.getJSON("/aidxp/explore/profile/" + pageid + "/bipartite_rank/" + type + "/", function(data) {
     var tbl_body = "<table><thead><tr><th>Rank</th><th>" + type + "</th><th>R</th></tr></thead>";
     $.each(data, function(key, obj) {
        tbl_body += "<tr><td><span>" + (key + 1) + "</span></td><td><a href='/aidxp/explore/profile/" + obj.id + "'>" + obj.name + "</a></td><td>" + obj.rca + "</td></tr>";
     })
     tbl_body += "</table>";
     $("div#question-text").html("What are the " + type + " most related to " + pagename + "?");
     $("div#plot").html("<br />" + tbl_body);
     var color = d3.scale.linear()
        .domain([0, d3.selectAll("tbody tr")[0].length-1])
        .interpolate(d3.interpolateRgb)
        .range(["#7cbde2", "#fb9496"])
     d3.selectAll("tbody tr").select("td span").style("background", function(d, i){
        return color(i);
     });
   });
}

function getList(type) {
 $.getJSON("/aidxp/explore/profile/" + pageid + "/list/" + type, function(data){
    var html = '';
    var len = data.length;
    for (var i = 0; i< len; i++) {
        if(data[i].id != plotid) {
           html += '<option value="' + data[i].id + '">' + data[i].name + '</option>';
        } else {
           html += '<option value="' + data[i].id + '" selected="selected">' + data[i].name + '</option>';
        }
    }
    $("select#target-entity").html(html);
    $("select#target-entity").chosen();
    $("select#target-entity").chosen().change(function(){
      $("div#plot").html("");
      plotid = $(this).val();
      draw("bipartite", plotid);
    });
 });
}

function imgError(image){
    image.onerror = "";
    image.src = "/media/aidxp/img/404.png";
    return true;
}

function giveMeARandomId(type) {
   $.ajax({
     url: "/aidxp/explore/profile/" + pageid + "/relations/" + type,
     dataType: 'json',
     async: false,
     success: function(data) {
       v = data[Math.floor(Math.random() * data.length)].id;
     }
   });
   return v;
}


$(".chzn-select").chosen().change(function(e){
    var new_url = "/aidxp/explore/profile/" + this.value + "/";
    window.location = new_url;
    return false;
});
