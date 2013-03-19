var color = d3.scale.linear()
  .domain([0, d3.selectAll("tbody tr")[0].length-1])
  .interpolate(d3.interpolateRgb)
  .range(["#dddddd", "#cc3355"])
d3.selectAll("tbody tr").select("td span").style("background", function(d, i){
  return color(i);
});

