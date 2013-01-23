function draw(uri) {

if(pagetype == "IS") {
   xAxisLabel = "Issue R";
} else if(pagetype == "CO") {
   xAxisLabel = "Country R";
} else {
   xAxisLabel = "Organization R";
}

if(othertype == "Issues") {
   yAxisLabel = "Issue R";
} else if(othertype == "Countries") {
   yAxisLabel = "Country R";
} else {
   yAxisLabel = "Organization R";
}


var margin = {top: 20, right: 20, bottom: 50, left: 60},
    width = 750 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.log()
    .range([0, width]);

var y = d3.scale.log()
    .range([height, 0]);

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

d3.json(uri, function(error, data) {

  data.points.forEach(function(d) {
    d.y = +d.y;
    d.x = +d.x;
  });

  x.domain(d3.extent(data.points, function(d) { return d.x; })).nice();
  y.domain(d3.extent(data.points, function(d) { return d.y; })).nice();

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + y(1) + ")")
      .call(xAxis.tickPadding(height - y(1)))
    .append("text")
      .attr("class", "label")
      .attr("x", width)
      .attr("y", (height - y(1)) + 40)
      .style("text-anchor", "end")
      .text(xAxisLabel);

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
      .text(yAxisLabel);

  svg.selectAll(".dot")
      .data(data.points)
    .enter().append("circle")
      .attr("class", "dot")
      .attr("r", 3.5)
      .attr("cx", function(d) { return x(d.x); })
      .attr("cy", function(d) { return y(d.y); })
      .style("fill", "#000000");

  svg.selectAll("g.x line")
      .attr("y1", -y(1))
      .attr("y2", height - y(1)) 
      .style("stroke", "#000000")
      .style("stroke-opacity", ".2");

  svg.selectAll("g.y line")
      .attr("x1", -x(1))
      .attr("x2", width - x(1))
      .style("stroke", "#000000")
      .style("stroke-opacity", ".2");

  svg.selectAll("path");

  $(".dot").tipsy({ 
     gravity: 'w', 
     html: true, 
     title: function() {
       var d = this.__data__, l = d.label;
       return l; 
     }
  });
});

$("div#question-text").html("How do <select id='target-entity'></select> and " + pagename + " coordinate over " + thirdtype + "?");
getList(othertype);
}

$(document).ready(function(){
  if(pagetype == "IS") {
    othertype = "Countries";
    thirdtype = "Organizations";
    plotid = (35 + Math.floor(Math.random() * 113));
  } else {
    othertype = "Issues";
    if(pagetype == "OR") {
       thirdtype = "Countries";
    } else {
       thirdtype = "Organizations";
    }
    plotid = (1 + Math.floor(Math.random() * 33));
  }
  draw("bipartite/" + plotid + "/");
});

function togglePlotType(newtype) {
  othertype = newtype;
  if(newtype == "Organizations") {
     plotid = (149 + Math.floor(Math.random() * 152));
  } else if(newtype == "Countries") {
     plotid = (35 + Math.floor(Math.random() * 113));
  } else {
     plotid = (1 + Math.floor(Math.random() * 33));
  }
  $("div#plot").html("");
  draw("bipartite/" + plotid + "/");
}

function getList(type) {
 $.getJSON('list/' + type, function(data){
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
    $("select#target-entity").change(function(){
      $("div#plot").html("");
      plotid = $(this).val();
      draw("bipartite/" + plotid + "/");
    });
 });
}

function imgError(image){
    image.onerror = "";
    image.src = "/media/aidxp/img/404.png";
    return true;
}
