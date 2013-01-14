<html>
  <head>
    <title>Aid Coordination Explorer</title>
    <link type="text/css" rel="stylesheet" href="stile.css"/>
    <script type="text/javascript" src="js/jquery-1.6.1.min.js"></script>
    <script type="text/javascript" src="js/protovis-r3.3.js"></script>
  </head>
  <body>
   <div class="wrapper">
    <div id="header">
       <h1>Aid Coordination Explorer</h1>
    </div>
    <div id="mainmenu">
      <a href='index.php'>Bipartite Plots</a><a href='unipartite.php'>Consistency Plots</a><div class="here" id="last">Rankings</div>
    </div>
    <div class="content home">
      <div id="menu-left">
        <div class="here-left" id="top-left">Country Ranking</div>
        <a href="institution-rank.php">Organization Ranking</a>
        <a href="issue-rank.php">Issue Ranking</a>
      </div>
      <div id="content-right">
          <table id="rank">
<tr class="top-select rankcolumn"><th>Rank</th><th class="countrycolumn">Country</th><th class="rcolumn">IC</th></tr>
<tr><td class="rankcolumn">1</td><td class="countrycolumn">El Salvador</td><td class="rcolumn">124.89</td></tr>
<tr><td class="rankcolumn">2</td><td class="countrycolumn">Iraq</td><td class="rcolumn">122.83</td></tr>
<tr><td class="rankcolumn">3</td><td class="countrycolumn">Mauritius</td><td class="rcolumn">120.63</td></tr>
<tr><td class="rankcolumn">4</td><td class="countrycolumn">Chile</td><td class="rcolumn">115.81</td></tr>
<tr><td class="rankcolumn">5</td><td class="countrycolumn">Iran</td><td class="rcolumn">107.23</td></tr>
<tr><td class="rankcolumn">6</td><td class="countrycolumn">Liberia</td><td class="rcolumn">105.28</td></tr>
<tr><td class="rankcolumn">7</td><td class="countrycolumn">Syria</td><td class="rcolumn">96.51</td></tr>
<tr><td class="rankcolumn">8</td><td class="countrycolumn">Panama</td><td class="rcolumn">96.51</td></tr>
<tr><td class="rankcolumn">9</td><td class="countrycolumn">Pakistan</td><td class="rcolumn">96.51</td></tr>
<tr><td class="rankcolumn">10</td><td class="countrycolumn">Afghanistan</td><td class="rcolumn">96.51</td></tr>
<tr><td class="rankcolumn">11</td><td class="countrycolumn">Gambia</td><td class="rcolumn">91.43</td></tr>
<tr><td class="rankcolumn">12</td><td class="countrycolumn">Benin</td><td class="rcolumn">91.43</td></tr>
<tr><td class="rankcolumn">13</td><td class="countrycolumn">Bosnia and Herzegovina</td><td class="rcolumn">90.07</td></tr>
<tr><td class="rankcolumn">14</td><td class="countrycolumn">Serbia</td><td class="rcolumn">87.73</td></tr>
<tr><td class="rankcolumn">15</td><td class="countrycolumn">Albania</td><td class="rcolumn">87.73</td></tr>
<tr><td class="rankcolumn">16</td><td class="countrycolumn">Cameroon</td><td class="rcolumn">86.86</td></tr>
<tr><td class="rankcolumn">17</td><td class="countrycolumn">Tunisia</td><td class="rcolumn">85.78</td></tr>
<tr><td class="rankcolumn">18</td><td class="countrycolumn">Macedonia</td><td class="rcolumn">85.78</td></tr>
<tr><td class="rankcolumn">19</td><td class="countrycolumn">Jamaica</td><td class="rcolumn">85.78</td></tr>
<tr><td class="rankcolumn">20</td><td class="countrycolumn">Ecuador</td><td class="rcolumn">85.78</td></tr>
<tr><td class="rankcolumn">21</td><td class="countrycolumn">Mauritania</td><td class="rcolumn">84.44</td></tr>
<tr><td class="rankcolumn">22</td><td class="countrycolumn">Sri Lanka</td><td class="rcolumn">82.72</td></tr>
<tr><td class="rankcolumn">23</td><td class="countrycolumn">Niger</td><td class="rcolumn">82.72</td></tr>
<tr><td class="rankcolumn">24</td><td class="countrycolumn">Sierra Leone</td><td class="rcolumn">81.27</td></tr>
<tr><td class="rankcolumn">25</td><td class="countrycolumn">Mexico</td><td class="rcolumn">80.42</td></tr>
<tr><td class="rankcolumn">26</td><td class="countrycolumn">Argentina</td><td class="rcolumn">80.42</td></tr>
<tr><td class="rankcolumn">27</td><td class="countrycolumn">Papua New Guinea</td><td class="rcolumn">79.48</td></tr>
<tr><td class="rankcolumn">28</td><td class="countrycolumn">Myanmar</td><td class="rcolumn">78.96</td></tr>
<tr><td class="rankcolumn">29</td><td class="countrycolumn">Lebanon</td><td class="rcolumn">77.21</td></tr>
<tr><td class="rankcolumn">30</td><td class="countrycolumn">Jordan</td><td class="rcolumn">77.21</td></tr>
<tr><td class="rankcolumn">31</td><td class="countrycolumn">Honduras</td><td class="rcolumn">77.21</td></tr>
<tr><td class="rankcolumn">32</td><td class="countrycolumn">Botswana</td><td class="rcolumn">77.21</td></tr>
<tr><td class="rankcolumn">33</td><td class="countrycolumn">Ghana</td><td class="rcolumn">75.06</td></tr>
<tr><td class="rankcolumn">34</td><td class="countrycolumn">Guinea-Bissau</td><td class="rcolumn">74.24</td></tr>
<tr><td class="rankcolumn">35</td><td class="countrycolumn">Costa Rica</td><td class="rcolumn">74.24</td></tr>
<tr><td class="rankcolumn">36</td><td class="countrycolumn">Zambia</td><td class="rcolumn">73.53</td></tr>
<tr><td class="rankcolumn">37</td><td class="countrycolumn">Nicaragua</td><td class="rcolumn">73.53</td></tr>
<tr><td class="rankcolumn">38</td><td class="countrycolumn">Yemen</td><td class="rcolumn">72.38</td></tr>
<tr><td class="rankcolumn">39</td><td class="countrycolumn">Romania</td><td class="rcolumn">72.38</td></tr>
<tr><td class="rankcolumn">40</td><td class="countrycolumn">Uruguay</td><td class="rcolumn">71.11</td></tr>
<tr><td class="rankcolumn">41</td><td class="countrycolumn">Paraguay</td><td class="rcolumn">71.11</td></tr>
<tr><td class="rankcolumn">42</td><td class="countrycolumn">Armenia</td><td class="rcolumn">71.11</td></tr>
<tr><td class="rankcolumn">43</td><td class="countrycolumn">Dominican Republic</td><td class="rcolumn">70.19</td></tr>
<tr><td class="rankcolumn">44</td><td class="countrycolumn">Ukraine</td><td class="rcolumn">68.93</td></tr>
<tr><td class="rankcolumn">45</td><td class="countrycolumn">Ivory Coast</td><td class="rcolumn">68.93</td></tr>
<tr><td class="rankcolumn">46</td><td class="countrycolumn">Kazakhstan</td><td class="rcolumn">68.12</td></tr>
<tr><td class="rankcolumn">47</td><td class="countrycolumn">Gabon</td><td class="rcolumn">68.12</td></tr>
<tr><td class="rankcolumn">48</td><td class="countrycolumn">Chad</td><td class="rcolumn">68.12</td></tr>
<tr><td class="rankcolumn">49</td><td class="countrycolumn">Azerbaijan</td><td class="rcolumn">68.12</td></tr>
<tr><td class="rankcolumn">50</td><td class="countrycolumn">Republic of Congo</td><td class="rcolumn">67.13</td></tr>
<tr><td class="rankcolumn">51</td><td class="countrycolumn">Peru</td><td class="rcolumn">64.34</td></tr>
<tr><td class="rankcolumn">52</td><td class="countrycolumn">Namibia</td><td class="rcolumn">64.34</td></tr>
<tr><td class="rankcolumn">53</td><td class="countrycolumn">Mozambique</td><td class="rcolumn">64.34</td></tr>
<tr><td class="rankcolumn">54</td><td class="countrycolumn">Morocco</td><td class="rcolumn">64.34</td></tr>
<tr><td class="rankcolumn">55</td><td class="countrycolumn">Mali</td><td class="rcolumn">64.34</td></tr>
<tr><td class="rankcolumn">56</td><td class="countrycolumn">Lao People Democratic Republic</td><td class="rcolumn">64.34</td></tr>
<tr><td class="rankcolumn">57</td><td class="countrycolumn">Haiti</td><td class="rcolumn">64.34</td></tr>
<tr><td class="rankcolumn">58</td><td class="countrycolumn">Colombia</td><td class="rcolumn">64.34</td></tr>
<tr><td class="rankcolumn">59</td><td class="countrycolumn">Burkina Faso</td><td class="rcolumn">64.34</td></tr>
<tr><td class="rankcolumn">60</td><td class="countrycolumn">Algeria</td><td class="rcolumn">64.34</td></tr>
<tr><td class="rankcolumn">61</td><td class="countrycolumn">Senegal</td><td class="rcolumn">61.41</td></tr>
<tr><td class="rankcolumn">62</td><td class="countrycolumn">Togo</td><td class="rcolumn">60.95</td></tr>
<tr><td class="rankcolumn">63</td><td class="countrycolumn">Tajikistan</td><td class="rcolumn">60.32</td></tr>
<tr><td class="rankcolumn">64</td><td class="countrycolumn">Malawi</td><td class="rcolumn">58.74</td></tr>
<tr><td class="rankcolumn">65</td><td class="countrycolumn">Latvia</td><td class="rcolumn">57.90</td></tr>
<tr><td class="rankcolumn">66</td><td class="countrycolumn">Cambodia</td><td class="rcolumn">57.90</td></tr>
<tr><td class="rankcolumn">67</td><td class="countrycolumn">Bulgaria</td><td class="rcolumn">57.90</td></tr>
<tr><td class="rankcolumn">68</td><td class="countrycolumn">Madagascar</td><td class="rcolumn">56.77</td></tr>
<tr><td class="rankcolumn">69</td><td class="countrycolumn">Central African Republic</td><td class="rcolumn">56.77</td></tr>
<tr><td class="rankcolumn">70</td><td class="countrycolumn">Guinea</td><td class="rcolumn">56.30</td></tr>
<tr><td class="rankcolumn">71</td><td class="countrycolumn">Libya</td><td class="rcolumn">55.15</td></tr>
<tr><td class="rankcolumn">72</td><td class="countrycolumn">Ethiopia</td><td class="rcolumn">55.15</td></tr>
<tr><td class="rankcolumn">73</td><td class="countrycolumn">China</td><td class="rcolumn">55.15</td></tr>
<tr><td class="rankcolumn">74</td><td class="countrycolumn">Brazil</td><td class="rcolumn">55.15</td></tr>
<tr><td class="rankcolumn">75</td><td class="countrycolumn">Democratic Republic of Congo</td><td class="rcolumn">54.04</td></tr>
<tr><td class="rankcolumn">76</td><td class="countrycolumn">Guatemala</td><td class="rcolumn">53.61</td></tr>
<tr><td class="rankcolumn">77</td><td class="countrycolumn">Nepal</td><td class="rcolumn">50.79</td></tr>
<tr><td class="rankcolumn">78</td><td class="countrycolumn">Zimbabwe</td><td class="rcolumn">48.25</td></tr>
<tr><td class="rankcolumn">79</td><td class="countrycolumn">Swaziland</td><td class="rcolumn">48.25</td></tr>
<tr><td class="rankcolumn">80</td><td class="countrycolumn">Philippines</td><td class="rcolumn">48.25</td></tr>
<tr><td class="rankcolumn">81</td><td class="countrycolumn">Eritrea</td><td class="rcolumn">48.25</td></tr>
<tr><td class="rankcolumn">82</td><td class="countrycolumn">Timor-Leste</td><td class="rcolumn">46.32</td></tr>
<tr><td class="rankcolumn">83</td><td class="countrycolumn">Nigeria</td><td class="rcolumn">45.41</td></tr>
<tr><td class="rankcolumn">84</td><td class="countrycolumn">India</td><td class="rcolumn">45.41</td></tr>
<tr><td class="rankcolumn">85</td><td class="countrycolumn">Angola</td><td class="rcolumn">45.41</td></tr>
<tr><td class="rankcolumn">86</td><td class="countrycolumn">Moldova</td><td class="rcolumn">44.54</td></tr>
<tr><td class="rankcolumn">87</td><td class="countrycolumn">Bangladesh</td><td class="rcolumn">43.87</td></tr>
<tr><td class="rankcolumn">88</td><td class="countrycolumn">Venezuela</td><td class="rcolumn">42.89</td></tr>
<tr><td class="rankcolumn">89</td><td class="countrycolumn">Uganda</td><td class="rcolumn">42.89</td></tr>
<tr><td class="rankcolumn">90</td><td class="countrycolumn">Sudan</td><td class="rcolumn">42.89</td></tr>
<tr><td class="rankcolumn">91</td><td class="countrycolumn">Lesotho</td><td class="rcolumn">40.63</td></tr>
<tr><td class="rankcolumn">92</td><td class="countrycolumn">Bolivia</td><td class="rcolumn">40.63</td></tr>
<tr><td class="rankcolumn">93</td><td class="countrycolumn">Kosovo</td><td class="rcolumn">35.09</td></tr>
<tr><td class="rankcolumn">94</td><td class="countrycolumn">Burundi</td><td class="rcolumn">35.09</td></tr>
<tr><td class="rankcolumn">95</td><td class="countrycolumn">Turkmenistan</td><td class="rcolumn">29.69</td></tr>
<tr><td class="rankcolumn">96</td><td class="countrycolumn">South Africa</td><td class="rcolumn">28.95</td></tr>
<tr><td class="rankcolumn">97</td><td class="countrycolumn">Rwanda</td><td class="rcolumn">28.95</td></tr>
<tr><td class="rankcolumn">98</td><td class="countrycolumn">Malaysia</td><td class="rcolumn">27.57</td></tr>
<tr><td class="rankcolumn">99</td><td class="countrycolumn">Kenya</td><td class="rcolumn">27.57</td></tr>
<tr><td class="rankcolumn">100</td><td class="countrycolumn">Egypt</td><td class="rcolumn">27.57</td></tr>
<tr><td class="rankcolumn">101</td><td class="countrycolumn">Uzbekistan</td><td class="rcolumn">24.13</td></tr>
<tr><td class="rankcolumn">102</td><td class="countrycolumn">Kyrgyzstan</td><td class="rcolumn">24.13</td></tr>
<tr><td class="rankcolumn">103</td><td class="countrycolumn">Belarus</td><td class="rcolumn">24.13</td></tr>
<tr><td class="rankcolumn">104</td><td class="countrycolumn">Tanzania</td><td class="rcolumn">19.30</td></tr>
<tr><td class="rankcolumn">105</td><td class="countrycolumn">Georgia</td><td class="rcolumn">17.55</td></tr>
<tr><td class="rankcolumn">106</td><td class="countrycolumn">Indonesia</td><td class="rcolumn">14.85</td></tr>
<tr><td class="rankcolumn">107</td><td class="countrycolumn">Vietnam</td><td class="rcolumn">12.87</td></tr>
<tr><td class="rankcolumn">108</td><td class="countrycolumn">Turkey</td><td class="rcolumn">0.00</td></tr>
<tr><td class="rankcolumn">109</td><td class="countrycolumn">Thailand</td><td class="rcolumn">0.00</td></tr>
<tr><td class="rankcolumn">110</td><td class="countrycolumn">Mongolia</td><td class="rcolumn">0.00</td></tr>
          </table>
      </div>
    </div>
   </div>
   <div class="footer">
     <a href=''>About</a> - <a href='http://www.di.unipi.it/~coscia/publications.htm'>Michele Coscia</a> - <a href='http://www.hks.harvard.edu/centers/cid'>Center for International Development</a> - <a href='http://www.harvard.edu/'>Harvard University</a>
   </div>
  </body>
</html>
