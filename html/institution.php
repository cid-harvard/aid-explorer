<html>
  <head>
    <title>Aid Coordination Explorer</title>
    <link type="text/css" rel="stylesheet" href="stile.css"/>
    <script type="text/javascript" src="js/jquery-1.6.1.min.js"></script>
    <script type="text/javascript" src="js/protovis-r3.2.js"></script>
    <script type="text/javascript">
      $(document).ready(function(){
        $("select#inst").change(function(){
          $("div#concernactivityrca").load("php/load_conceractivityrcalist_from_inst.php", "inst=" + $("select#inst option:selected").val());
        });
      });
    </script>
  </head>
  <body>
   <div class="wrapper">
    <div id="header">
       <h1>Aid Coordination Explorer</h1>
    </div>
    <div id="mainmenu">
      <a href='index.php'>Bipartite Plots</a><div class="here">Consistency Plots</div><a href='country-rank.php' id="last">Rankings</a>
    </div>
    <div class="content home">
      <div id="menu-left">
        <a href="unipartite.php" id="top-left">Country</a>
        <div class="here-left">Organization</div>
        <a href="issue.php">Issue</a>
      </div>
      <div id="content-right">
        <form name="countryform" onsubmit="return false;">
          <table>
          <tr>
          <td>
            <div class="top-select">
              Country
            </div>
            <select name="inst" id="inst">
            <?
            $handle = @fopen("files/institution_list", "r");
            while (($buffer = fgets($handle, 4096)) !== false) {
               $buffer = str_replace("\n", "", $buffer);
               $value = urlencode($buffer);
               echo "<option value=\"$value\">$buffer</option>";
            }
            fclose($handle);
            ?>
            </select>
<script>
 function loadplot_1() {
   $.get("php/load_plot_synergy.php?subject=" + $("select#inst option:selected").val() + "&type=org_issue", function(data){
      var plotDataJSON = jQuery.parseJSON(data);
      $("#plot-1").html('');
      /* Sizing and scales. */
      var w = 400,
          h = 400,
          x = pv.Scale.linear(plotDataJSON.min_x - (plotDataJSON.min_x * 0.01), plotDataJSON.max_x + 0.1).range(0, w),
          y = pv.Scale.linear(plotDataJSON.min_y - (plotDataJSON.min_y * 0.01), plotDataJSON.max_y + 0.1).range(0, h),
          s = pv.Scale.log(plotDataJSON.min_s, plotDataJSON.max_s).range(1, 100),
          c = pv.Scale.log(1, 100).range("black", "black");

      /* The root panel. */
      var vis = new pv.Panel()
          .canvas('plot-1')
          .width(w)
          .height(h)
          .bottom(45)
          .left(45)
          .right(10)
          .top(5);

      /* Y-axis and ticks. */
      vis.add(pv.Rule)
         .data(y.ticks())
         .bottom(y)
         .strokeStyle("#BCBDC0")
         .anchor("left").add(pv.Label)
         .visible(true)
         .text(y.tickFormat);

      /* X-axis and ticks. */
      vis.add(pv.Rule)
         .data(x.ticks())
         .left(x)
         .strokeStyle("#BCBDC0")
         .anchor("bottom").add(pv.Label)
         .visible(true)
         .text(x.tickFormat);

      vis.add(pv.Label)
         .data(["Organization-Issue R"])
         .left(-30)
         .bottom(h/2)
         .font("10pt Arial")
         .textAlign("center")
         .textAngle(-Math.PI/2);

      vis.add(pv.Label)
         .data(["Organization-Issue a"])
         .left(w/2)
         .bottom(-35)
         .font("10pt Arial")
         .textAlign("center");

      //vis.add(pv.Line)
      //   .data(plotDataJSON.trendline)
      //   .interpolate("linear")
      //   .left(function(d) x(d.x))
      //   .bottom(function(d) y(d.y))
      //   .lineWidth(3);

      vis.add(pv.Rule)
         .data(pv.range(1))
         .bottom(y(1))
         .strokeStyle("black");

      vis.add(pv.Rule)
         .data(pv.range(1))
         .left(x(0))
         .strokeStyle("black");

      /* The dot plot! */
      vis.add(pv.Panel)
         .data(plotDataJSON["countries"])
         .add(pv.Dot)
         .left(function(d) {return x(d.x)})
         .bottom(function(d) {return y(d.y)})
         .strokeStyle(function(d) {return c(d.s)})
         .fillStyle(function() {return this.strokeStyle().alpha(.2)})
         .size(function(d) {return s(d.s)})
         .title(function(d) {return d.label});

      vis.render();
   });
 }

 function loadplot_2() {
   $.get("php/load_plot_synergy.php?subject=" + $("select#inst option:selected").val() + "&type=org_country", function(data){
      var plotDataJSON = jQuery.parseJSON(data);
      $("#plot-2").html('');
      /* Sizing and scales. */
      var w = 400,
          h = 400,
          x = pv.Scale.linear(plotDataJSON.min_x - (plotDataJSON.min_x * 0.01), plotDataJSON.max_x + 0.1).range(0, w),
          y = pv.Scale.linear(plotDataJSON.min_y - (plotDataJSON.min_y * 0.01), plotDataJSON.max_y + 0.1).range(0, h),
          s = pv.Scale.log(plotDataJSON.min_s, plotDataJSON.max_s).range(1, 100),
          c = pv.Scale.log(1, 100).range("black", "black");

      /* The root panel. */
      var vis = new pv.Panel()
          .canvas('plot-2')
          .width(w)
          .height(h)
          .bottom(45)
          .left(45)
          .right(10)
          .top(5);

      /* Y-axis and ticks. */
      vis.add(pv.Rule)
         .data(y.ticks())
         .bottom(y)
         .strokeStyle("#BCBDC0")
         .anchor("left").add(pv.Label)
         .visible(true)
         .text(y.tickFormat);

      /* X-axis and ticks. */
      vis.add(pv.Rule)
         .data(x.ticks())
         .left(x)
         .strokeStyle("#BCBDC0")
         .anchor("bottom").add(pv.Label)
         .visible(true)
         .text(x.tickFormat);

      vis.add(pv.Label)
         .data(["Country-Organization R"])
         .left(-30)
         .bottom(h/2)
         .font("10pt Arial")
         .textAlign("center")
         .textAngle(-Math.PI/2);

      vis.add(pv.Label)
         .data(["Country-Organization a"])
         .left(w/2)
         .bottom(-35)
         .font("10pt Arial")
         .textAlign("center");

      //vis.add(pv.Line)
      //   .data(plotDataJSON.trendline)
      //   .interpolate("linear")
      //   .left(function(d) x(d.x))
      //   .bottom(function(d) y(d.y))
      //   .lineWidth(3);

      vis.add(pv.Rule)
         .data(pv.range(1))
         .bottom(y(1))
         .strokeStyle("black");

      vis.add(pv.Rule)
         .data(pv.range(1))
         .left(x(0))
         .strokeStyle("black");

      /* The dot plot! */
      vis.add(pv.Panel)
         .data(plotDataJSON["countries"])
         .add(pv.Dot)
         .left(function(d) {return x(d.x)})
         .bottom(function(d) {return y(d.y)})
         .strokeStyle(function(d) {return c(d.s)})
         .fillStyle(function() {return this.strokeStyle().alpha(.2)})
         .size(function(d) {return s(d.s)})
         .title(function(d) {return d.label});

      vis.render();
   });
 }

 loadplots = function() {
    loadplot_1();
    loadplot_2();
 }

 $(document).ready(loadplots);
 $("select#inst").change(loadplots);
</script>
          </td>
          <tr>
          <td id="plot_container">
          <div class="top-select">
              Consistency Plots
          </div>
          <div id="plot-1">
            
          </div>
          <div id="plot-2">
            
          </div>
          </td>
          </tr>
          </table>
        </form>
      </div>
    </div>
   </div>
   <div class="footer">
     <a href=''>About</a> - <a href='http://www.di.unipi.it/~coscia/publications.htm'>Michele Coscia</a> - <a href='http://www.hks.harvard.edu/centers/cid'>Center for International Development</a> - <a href='http://www.harvard.edu/'>Harvard University</a>
   </div>
  </body>
</html>
