var color = d3.scale.linear()
  .domain([0, d3.selectAll("tbody tr")[0].length-1])
  .interpolate(d3.interpolateRgb)
  .range(["#7cbde2", "#fb9496"])
d3.selectAll("tbody tr").select("td span").style("background", function(d, i){
  return color(i);
})

