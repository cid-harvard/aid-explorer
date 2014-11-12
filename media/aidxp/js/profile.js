function draw(plotclass, plotid) {

 var margin = {top: 20, right: 20, bottom: 50, left: 60},
    width = 725 - margin.left - margin.right,
    height = 710 - margin.top - margin.bottom;

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

 d3.json("/explore/profile/" + pageid + "/" + plotclass + "/" + plotid + "/", function(error, data) {

  data.points.forEach(function(d) {
    d.y = +d.y;
    d.x = +d.x;
  });

  x.domain(d3.extent(data.points, function(d) { return d.x; }));
  y.domain(d3.extent(data.points, function(d) { return d.y; }));

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
      .attr("x", width / 2)
      .attr("y", (height - y(axisOrigin)) + 40)
      .style("text-anchor", "middle")
      .style("font-size", "18")
      .style("cursor", "default")
      .text(data.x_axis);
    //.append("title")
    //  .text(data.x_tooltip);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis.tickPadding(x(1)))
      .attr("transform", "translate(" + x(1) + ", 0)")
    .append("text")
      .attr("class", "label")
      .attr("transform", "rotate(-90)")
      .attr("x", -height / 2)
      .attr("y", -x(1) - 50)
      .attr("dy", ".74em")
      .style("text-anchor", "middle")
      .style("font-size", "18")
      .style("cursor", "default")
      .text(data.y_axis);
    //.append("title")
    //  .text(data.y_tooltip);


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
      .on("click", function(d) { window.location.replace("/explore/profile/" + d.id  + "/"); })
      .on("mouseover", function() { d3.select(this).style("fill", "#BA093E"); })
      .on("mouseout", function() { d3.select(this).style("fill", "#000000"); });

  //svg.selectAll("g.x line")
  //    .attr("y1", -y(axisOrigin) + 10)
  //    .attr("y2", height - y(axisOrigin))
  //    .style("stroke", "#000000")
  //    .style("stroke-opacity", ".2");

  //svg.selectAll("g.y line")
  //    .attr("x1", -x(1))
  //    .attr("x2", width - x(1))
  //    .style("stroke", "#000000")
  //    .style("stroke-opacity", ".2");

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
     gravity: 's',
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

  $("div#profile-legend").html("<h3>Interpretation</h3><div>" + data.interpretation + "<br />Need help with the terminology? Check out the <a href='/about/glossary/'>Glossary</a>!</div>");
 });

 if(plotclass == "bipartite") {
  $("div#question-text").html("How does " + pagename + " relate to <select id='target-entity'></select> ? <button class='alignright' onclick='toggleShareDiv();'>Share</button><span id='sharelink' onclick='selectText(\"sharelink\")'>http://aidxp.atlas.cid.harvard.edu/explore/static/profile/" + pageid + "/bipartite/" + plotid + "/</span>");
  getList(othertype);
 } else {
  $("div#question-text").html("How does " + pagename + " relate to all " + plotid + "? <button class='alignright' onclick='toggleShareDiv();'>Share</button><span id='sharelink' onclick='selectText(\"sharelink\")'>http://www.atlas.cid.harvard.edu/explore/static/profile/" + pageid + "/consistency/" + plotid + "/</span>");
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
     toggleRankType("default", plotid);
  } else {
     draw(plottype, plotid);
  }
});

$('.profile-switcher').change(function() {
  window.location.replace("/explore/profile/" + this.value  + "/");
});

function togglePlotType(caller, newtype, plotclass) {
  if(plotclass == "bipartite") {
    if(othertype != newtype) {
       thirdtype = othertype;
       othertype = newtype;
     }
     plotid = giveMeARandomId(othertype);
  } else {
     plotid = newtype;
  }
  $(".here").removeClass("here");
  caller.addClass("here");
  $("div#plot").html("");
  draw(plotclass, plotid);
}

function toggleRankType(caller, type) {
  /*
  $.getJSON("/explore/profile/" + pageid + "/bipartite_rank/" + type + "/", function(data) {
     var tbl_body = "<table><thead><tr><th>Rank</th><th>" + type + "</th><th>R</th></tr></thead>";
     $.each(data.points, function(key, obj) {
        tbl_body += "<tr><td><span>" + (key + 1) + "</span></td><td><a href='/explore/profile/" + obj.id + "'>" + obj.name + "</a></td><td>" + obj.rca + "</td></tr>";
     })
     tbl_body += "</table>";
     $("div#plot").html("<br />" + tbl_body);
     var color = d3.scale.linear()
        .domain([0, d3.selectAll("tbody tr")[0].length-1])
        .interpolate(d3.interpolateRgb)
        .range(["#dddddd", "#cc3355"])
     d3.selectAll("tbody tr").select("td span").style("background", function(d, i){
        return color(i);
     });
   });
  */

  d3.json("/explore/profile/" + pageid + "/bipartite_rank/" + type + "/", function(error, data) {

    if(caller != "default") {
       $(".here").removeClass("here");
       caller.addClass("here");
    }

    $("div#question-text").html("What are the " + type + " most related to " + pagename + "? <button class='alignright' onclick='toggleShareDiv();'>Share</button><span id='sharelink' onclick='selectText(\"sharelink\")'>http://www.atlas.cid.harvard.edu/explore/static/profile/" + pageid + "/bipartite_rank/" + type + "/</span>");
    $("div#profile-legend").html("<h3>Interpretation</h3><div>" + data.interpretation + "<br /><br />Need help with the terminology? Check out the <a href='/about/glossary/'>Glossary!</a></div>");

    $("div#plot").html("<br />");

    var chart = d3.select("div#plot").append("svg")
      .attr("class", "chart")
      .attr("width", "99%")
      .attr("height", 25 * data.points.length);

    var x = d3.scale.linear()
      .domain([0, d3.max(data.points, function(d){ return d.rca; })])
      .range([0, d3.select("div#plot svg").style("width")]);

    chart.selectAll("rect")
      .data(data.points)
    .enter().append("rect")
      .attr("y", function(d, i) { return i * 25; })
      .attr("width", function(d) { return x(d.rca);})
      .attr("height", 24)
      .on("click", function(d) { window.location.replace("/explore/profile/" + d.id  + "/"); })
      .style("cursor", "pointer");

    chart.selectAll("text")
      .data(data.points)
    .enter().append("text")
      .attr("x", 5)
      .attr("y", function(d, i) { return (i * 25) + 17; })
      .text(function(d) { return d.name;})
      .on("click", function(d) { window.location.replace("/explore/profile/" + d.id  + "/"); })
      .style("cursor", "pointer");
  });
}

function getList(type) {
 $.getJSON("/explore/profile/" + pageid + "/list/" + type, function(data){
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
     url: "/explore/profile/" + pageid + "/relations/" + type,
     dataType: 'json',
     async: false,
     success: function(data) {
       v = data[Math.floor(Math.random() * data.length)].id;
     }
   });
   return v;
}


$(".chzn-select").chosen().change(function(e){
    var new_url = "/explore/profile/" + this.value + "/";
    window.location = new_url;
    return false;
});

function toggleShareDiv() {
   $("span#sharelink").toggle();
   selectText("sharelink");
}

function selectText(element) {
    var doc = document, text = doc.getElementById(element), range, selection;
    if (doc.body.createTextRange) { //ms
        range = doc.body.createTextRange();
        range.moveToElementText(text);
        range.select();
    } else if (window.getSelection) { //all others
        selection = window.getSelection();
        range = doc.createRange();
        range.selectNodeContents(text);
        selection.removeAllRanges();
        selection.addRange(range);
    }
}
