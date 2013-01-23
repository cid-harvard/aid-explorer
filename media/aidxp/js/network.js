function draw(uri) {
 var width = 900,
     height = 600;

 var color = nodeColor(uri);

 var force = d3.layout.force()
    .linkDistance(40)
    .size([width, height])
    .gravity(1);

 svg = d3.select("div#plot")
    .append("svg:svg")
    .attr("width", width)
    .attr("height", height)
    .attr("pointer-events", "all")
    .append('svg:g')
    .call(d3.behavior.zoom().on("zoom", redraw))
    .append('svg:g');

 svg.append('svg:rect')
    .attr('width', width)
    .attr('height', height)
    .attr('fill', 'white');

 d3.json("network/" + uri, function(error, graph) {
   force
      .nodes(graph.nodes)
      .links(graph.links)
      .charge(function(d) { return (-256 * nodeSize(d.size));})
      .start();

   var link = svg.selectAll("line.link")
      .data(graph.links)
      .enter().append("line")
      .attr("class", "link")
      .style("stroke", "#000000")
      .style("stroke-opacity", ".1")
      .style("stroke-width", function(d){return linkWidth(d.weight);});

   var node = svg.selectAll("circle.node")
      .data(graph.nodes)
      .enter().append("circle")
      .attr("class", "node")
      .attr("r", function(d){return nodeSize(d.size);})
      .call(force.drag)
      .style("fill", function(d) { return color(d.type); });
      //.on("click", function(d) { window.location.href = "." });

   //node.append("title")
   //   .text(function(d) { return d.name; });

   force.on("tick", function() {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node.attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
   });

  $(".node").tipsy({
     gravity: 'w',
     html: true,
     title: function() {
       var d = this.__data__, l = d.name;
       return l;
     }
  });
 });
}

function redraw() {
   svg.attr("transform", "translate(" + d3.event.translate + ") scale(" + d3.event.scale + ")");
}

$(document).ready(function(){
   draw(pagetype);
});

function linkWidth(w) {
   if(pagetype == "OR") {
      if(w < 342259) {
         return (w / 48894) + 1
      } else {
         return (w / 1490000) + 8
      }
   }
}

function nodeSize(w) {
   if(pagetype == "OR") {
      if(w < 0.0976) {
         return (w * 180) + 3;
      } else {
         return (w * 11.3) + 20;
      }
   }
}

function nodeColor(uri) {
   if(uri == "OR") {
      return d3.scale.linear()
    .domain([0.6377, 4.246, 4.9864])
    .range(["rgb(102,204,255)", "rgb(102,204,255)", "red"]);
   }
}
