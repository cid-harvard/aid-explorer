<?  
header("Cache-Control: no-cache");
$issue_occurrences = array();
$issue_rcas = array();

$handle = @fopen("../files/20120501country_issue_rca_aidweb_2", "r");
while (($buffer = fgets($handle, 4096)) !== false) {
   $buffer = str_replace("\n", "", $buffer);
   $fields = explode("\t", $buffer);
   if(str_replace(" ", "_", $fields[1]) == $_GET["issue"]){
      $issue_occurences[$fields[0]] = $fields[2];
      $issue_rcas[$fields[0]] = $fields[3];
   }
}
fclose($handle);

$country_occurrences = array();
$country_rcas = array();

$handle = @fopen("../files/20120501org_country_rca_aidweb", "r");
while (($buffer = fgets($handle, 4096)) !== false) {
   $buffer = str_replace("\n", "", $buffer);
   $fields = explode("\t", $buffer);
   if(str_replace("'", "\'", $fields[0]) == $_GET["inst"]){
      $country_occurrences[$fields[1]] = $fields[2];
      $country_rcas[$fields[1]] = $fields[3];
   }
}
fclose($handle);

$handle = @fopen("../files/20120501organization_issue_poweregressions_anneal_2", "r");
while (($buffer = fgets($handle, 4096)) !== false) {
   $buffer = str_replace("\n", "", $buffer);
   $fields = explode("\t", $buffer);
   if(urlencode($fields[0]) == urlencode(str_replace("\\", "", $_GET["inst"])) && str_replace(" ", "_", $fields[1]) == $_GET["issue"]){
      $a = (float) $fields[2];
      $b = (float) $fields[3];
   }
}
fclose($handle);

$minx = 100;
$maxx = 0;
$miny = 100;
$maxy = 0;
$minc = 100000000;
$maxc = 0;
$mins = 100000000;
$maxs = 0;
$json_output = "{\"countries\":[";
foreach($country_occurrences as $key => $value) {
   if($issue_rcas[$key] != "") {
      if((float)$country_rcas[$key] < $minx) $minx = (float)$country_rcas[$key];
      if((float)$country_rcas[$key] > $maxx) $maxx = (float)$country_rcas[$key];
      if((float)$issue_rcas[$key] < $miny) $miny = (float)$issue_rcas[$key];
      if((float)$issue_rcas[$key] > $maxy) $maxy = (float)$issue_rcas[$key];
      if((int)$value < $mins) $mins = (int)$value;
      if((int)$value > $maxs) $maxs = (int)$value;
      if((int)$issue_occurences[$key] < $minc) $minc = (int)$issue_occurences[$key];
      if((int)$issue_occurences[$key] > $maxc) $maxc = (int)$issue_occurences[$key];
      $json_output .= "{\"label\": \"$key\", \"x\": $country_rcas[$key], \"y\": $issue_rcas[$key], \"s\": $value, \"c\": $issue_occurences[$key]},";
   }
}
$fitline_left_x = $minx;
$fitline_right_x = $maxx;
$fitline_left_y = $b * pow($fitline_left_x, $a);
$fitline_right_y = $b * pow($fitline_right_x, $a);

$json_output = substr($json_output, 0, -1).'],';
$json_output .= "\"min_x\": $minx, \"max_x\": $maxx, \"min_y\": $miny, \"max_y\": $maxy, \"min_c\": $minc, \"max_c\": $maxc, \"min_s\": $mins, \"max_s\": $maxs, \"trendline\":[{\"x\": $fitline_left_x, \"y\": $fitline_left_y},{\"x\": $fitline_right_x, \"y\": $fitline_right_y}]}";
echo $json_output;
?>
