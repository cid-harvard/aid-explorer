<html>
  <head>
    <title>Aid Coordination Explorer</title>
    <link type="text/css" rel="stylesheet" href="stile.css"/>
    <script type="text/javascript" src="js/jquery-1.6.1.min.js"></script>
    <script type="text/javascript" src="js/protovis-r3.2.js"></script>
    <script type="text/javascript">
      $(document).ready(function(){
        $("select#country").change(function(){
          $("div#concernactivityrca").load("php/load_institutionrcalist_from_country.php", "country=" + $("select#country option:selected").val());
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
      <div class="here">Bipartite Plots</div><a href='unipartite.php'>Consistency Plots</a><a href='country-rank.php' id="last">Rankings</a>
    </div>
    <div class="content home">
      <div id="menu-left">
        <div class="here-left">Country-Organization</div>
        <a href="institution-issue.php">Organization-Issue</a>
        <a href="country-issue.php">Country-Issue</a>
      </div>
      <div id="content-right">
        <form name="countryform" onsubmit="return false;">
          <table>
          <tr>
          <td>
            <div class="top-select">
              Country
            </div>
            <select name="country" id="country">
            <?
            $handle = @fopen("files/country_list", "r");
            while (($buffer = fgets($handle, 4096)) !== false) {
               $buffer = str_replace("\n", "", $buffer);
               $value = str_replace(" ", "_", $buffer);
               echo "<option value=\"$value\">$buffer</option>";
            }
            fclose($handle);
            ?>
            </select>
          </td>
          <td>
          <div id="concernactivityrca">
            <div class="top-select">
              Organization
            </div>
            <form name="issueform" onsubmit="return false;">
            <select name="institution" id="institution"></select>
            </form>
          </div>
          </td>
          <tr>
          <td colspan=2 id="plot_container">
          <div class="top-select">
              Bipartite Plot
          </div>
          <div id="plot">
            
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
