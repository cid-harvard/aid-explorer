<html>
  <head>
    <title>Aid Coordination Explorer</title>
    <link type="text/css" rel="stylesheet" href="stile.css"/>
    <script type="text/javascript" src="js/jquery-1.6.1.min.js"></script>
    <script type="text/javascript" src="js/protovis-r3.3.js"></script>
    <script>
var dataIssue = [
["Malnutrition",0.21029,0.08502,"#f0f"],
["Electricity",0.11997,0.03575,"#00f"],
["climate change",0.12577,0.22245,"#f0f"],
["Housing",0.22752,0.03009,"#00f"],
["economic growth",0.07144,0.00388,"#f0f"],
["HIV/AIDS",0.54659,0.29251,"#f0f"],
["Reconstruction",-0.15589,-0.10486,"#00f"],
["primary school",-0.08511,0.01919,"#00f"],
["Corruption",0.30379,0.04502,"#f0f"],
["Transportation",0.26578,0.13705,"#00f"],
["democracy",0.55454,0.19683,"#f0f"],
["environmental sustainability",-0.04267,0.09062,"#f0f"],
["humanitarian assistance",0.12993,0.18423,"#00f"],
["infant mortality",0.39132,0.27918,"#f0f"],
["criminal justice",0.20549,0.18153,"#00f"],
["Manufacturing",0.04192,-0.04139,"#00f"],
["Tourism",0.12256,-0.02564,"#00f"],
["Hospital",0.29492,0.16001,"#00f"],
["natural disaster",0.17525,0.18865,"#f0f"],
["Banking system",0.14973,0.08164,"#00f"],
["job creation",-0.22261,-0.15186,"#f0f"],
["Sanitation",0.56638,0.25779,"#00f"],
["Gender",0.10123,0.00902,"#f0f"],
["Refugee",0.51420,0.34303,"#f0f"],
["Technological development",0.24836,0.17284,"#f0f"],
["rural development",0.25153,0.25968,"#f0f"],
["small and medium enterprise",0.34974,0.12530,"#00f"],
["school completion",0.53856,0.11878,"#f0f"],
["Human rights",0.39392,0.33273,"#f0f"],
["Homicides",0.12883,0.09934,"#f0f"],
["Microenterprise",0.33352,0.01117,"#00f"],
["Poverty reduction",0.30603,0.22915,"#f0f"],
["civil war",0.21239,0.14723,"#f0f"],
["Agriculture",0.28840,0.09606,"#00f"]
];

var dataInstitution = [
["World Vision International",0.35881,0.49079,4.148460062],
["Maktoum Foundation",-0.11945,0.00744,4.050976037],
["United Nations Relief and Works Agency for Palestine Refugees",0.23764,0.39356,3.836610986],
["Federal Ministry for Economic Cooperation and Development",0.27612,0.39582,4.101580247],
["Google Org",0.03154,0.24188,3.707895067],
["Seven fund",-0.19152,0.00567,3.388092276],
["China Development Bank",0.08111,0.23754,4.042800855],
["Concern Worldwide",0.41018,0.34197,4.241473339],
["World Health Organization",0.18606,0.18288,3.583046113],
["United Nations Office for Project Services",0.31463,0.43801,4.102389409],
["Turkish International Cooperation and Development Agency",-0.11063,-0.25645,3.896121568],
["United Nations Educational, Scientific and Cultural Organization",0.53224,0.35528,4.286793938],
["Canadian International Development Agency",0.58454,0.64358,4.483443954],
["Arab Fund for Economic & Social Development",-0.06826,-0.05232,4.106855679],
["Japan International Cooperation Agency",0.33363,0.46626,4.350955898],
["United Nations Democracy Fund",-0.15266,-0.13543,2.621567671],
["North American Development Bank",-0.01134,-0.14400,2.752125610],
["Agencia Brasileira de Cooperacao",0.28376,0.03176,2.372696119],
["Medair",0.40896,0.52812,3.902384031],
["Swiss Agency for Development and Cooperation",0.15994,0.31904,4.062354189],
["United States Agency for International Development",0.63066,0.74154,4.564163024],
["United Nations High Commissioner for Refugees",0.30064,0.36327,4.152680993],
["Abu Dhabi Fund for Development",0.03589,-0.06721,3.542584107],
["United Nations Centre for Human Settlements",0.50650,0.38368,3.978899203],
["African Capacity Building Foundation",0.40832,0.44199,3.906239541],
["United Nations Environment Programme",0.45665,0.31277,4.143870156],
["Human Rights Watch",0.62989,0.63459,2.597652723],
["MacArthur Foundation",0.09076,-0.01642,3.726384294],
["Hewlett Foundation",0.18426,0.24751,4.060170790],
["Norwegian Agency for Development Cooperation",0.36476,0.26493,4.172342271],
["Skoll Foundation",-0.17995,-0.01102,3.690126320],
["Direct Relief International",0.21766,-0.06688,3.433621091],
["Grameen Foundation",0.28082,0.27288,4.078591375],
["Helvetas",0.37377,0.20407,3.600579369],
["Global Environment Facility",0.46900,0.39960,4.177840517],
["Inter-American Development Bank",0.43045,0.21580,4.480066023],
["American Refugee Committee",0.34522,0.46366,3.544918235],
["Childreach",0.32427,0.35879,3.176992276],
["Adventist development and relief agency",0.61789,0.56249,3.939703974],
["Australian Agency for International Development",0.27352,0.67631,4.344962567],
["Nordic Development Fund",0.47753,0.30839,4.106059324],
["Irish Aid",0.29352,0.10290,4.016928289],
["Dubai Cares",-0.04504,0.05907,2.752931974],
["US African Development Foundation",0.28225,0.27403,4.048691163],
["Aga Khan Development Network",0.28299,0.18773,4.012785516],
["Instituto Portugues de Apoio ao Desenvolvimento",0.07892,0.17002,3.594174034],
["Slovak Aid",0.18012,-0.11423,3.932446073],
["International Fund for Agricultural Development",0.41793,0.56322,4.248583695],
["International Committee of the Red Cross",0.30914,0.31274,4.201156255],
["International Development Research Centre",0.11097,0.06130,4.293816963],
["Finnish Department for International Development Co-operation",-0.03772,0.10775,2.807354922],
["Austria Wirtschaftsservice Gesellschaft",0.14199,0.28088,4.246157119],
["Human Rights Council",0.12970,0.25028,2.577394122],
["French Development Agency",0.37562,0.39809,4.106233860],
["Italian Development Cooperation Programme",0.19016,0.20168,3.639598289],
["Caribbean Development Bank",0.28794,0.34030,4.145341335],
["World Relief",0.35227,0.46778,4.136834351],
["Medical Assistance Program International",0.08960,0.03738,3.121928095],
["Islamic Development Bank",-0.08802,-0.06114,4.322173696],
["Doctors Without Borders",0.32208,0.42260,4.080689904],
["Fast Track Initiative Catalytic Fund",0.26399,0.26815,4.354248492],
["Global Fund to Fight Aids, Tuberculosis and Malaria",0.59045,0.53756,4.064030255],
["United Nations Development Programme",0.66371,0.71840,4.524838688],
["Accion International",0.54573,0.29947,3.889036244],
["United Way International",0.28178,0.08718,3.856880580],
["United Nations Development Fund for Women",0.50625,0.71135,4.150731277],
["Action Against Hunger",0.21803,0.27098,4.133793254],
["Oxfam International",0.36266,0.30076,4.193256298],
["Food and Agriculture Organization",0.28799,0.20234,2.537979817],
["Danish International Development Agency",0.10999,0.32609,3.928105905],
["Swedish International Development Cooperation Agency",0.50979,0.56216,4.282146901],
["Multilateral Investment Guarantee Agency",0.25591,0.23800,4.080790427],
["Novartis Foundation",0.16863,0.09966,2.793390070],
["Shell Foundation",-0.09548,0.12392,3.563380930],
["West African Development Bank",0.56039,0.52662,4.309817365],
["Case Foundation",0.31450,0.07343,2.461792678],
["Ashoka",0.08174,0.06165,4.054426981],
["Lemelson Foundation",0.03045,-0.01956,3.669622844],
["Schwab Foundation",-0.24818,-0.06918,3.394671778],
["Catholic Overseas Development Agency",0.05513,0.19946,4.246078254],
["Arab Bank for Economic Development in Africa",0.15580,0.32152,3.754617473],
["Asian Development Bank",0.27967,0.52993,4.461935777],
["United Nations Capital Development Fund",0.46438,0.58306,4.038034759],
["World Concern",0.40077,0.61253,4.015173993],
["Netherlands Ministry of Development Cooperation",0.20245,0.19038,4.440865967],
["Salvation Army International Headquarters",0.01150,-0.00854,2.407470026],
["Spanish Agency for International Cooperation",0.50793,0.70712,4.453254828],
["AmeriCares Disaster Relief and Humanitarian Aid Organization",0.02813,-0.08562,1.000000000],
["American Jewish World Service",0.50205,0.53671,3.640205034],
["Bill and Melinda Gates Foundation",0.17835,0.37502,4.374882958],
["Japan Bank for International Cooperation",0.43076,-0.01022,4.172556051],
["Israel's Agency for International Development Cooperation",-0.07022,0.23147,3.929913778],
["Japan Official Development Assistance",0.29568,0.50999,4.482081426],
["Eurasia Foundation",0.14528,-0.03949,3.265972521],
["Agence d'Aide a la Cooperation Technique Et au Developpement",-0.01532,-0.17608,3.848884617],
["Joint United Nations Programme on HIV/AIDS",0.07508,0.12258,2.029478266],
["World Bank",0.33277,0.27519,4.333588243],
["Lux-Development",0.36681,0.37732,3.635495233],
["Food For The Hungry",0.48932,0.55435,4.034880980],
["High Commissioner of Human Rights",0.25923,0.12842,3.178373100],
["Ford Foundation",0.10024,-0.07514,4.215087665],
["Global Alliance for Vaccines & Immunization",0.13951,0.38576,4.298755960],
["International Cooperation and Development Fund",0.50138,0.14914,3.020959802],
["Rockefeller Brothers Fund",0.27983,0.23830,3.682566757],
["Millennium Challenge Corporation",0.32921,0.30352,4.295230046],
["Amnesty International",0.70392,0.66499,3.396071780],
["Hellenic Aid",0.09752,0.29086,4.099100141],
["Save the Children",0.12402,0.24263,4.346113776],
["Grameen Bank",0.05506,0.13313,4.370384691],
["United Nations Conference on Trade and Development",0.19005,0.32496,4.233279220],
["Carlos Slim Foundation",0.21441,-0.12514,4.318761817],
["China Development Industrial Bank",0.01899,0.22448,2.287783720],
["Belgian Technical Cooperation",0.25957,0.52465,3.851979178],
["European Bank for Reconstruction and Development",0.15791,0.14654,3.701503412],
["Soros Foundation",0.21180,0.33088,3.804573907],
["Korea International Cooperation Agency",0.13707,0.20851,3.447789855],
["African Development Bank",0.55537,0.44252,4.452719306],
["Refugees International",0.43062,0.52605,3.672811624],
["UK Department for International Development",0.45523,0.44357,4.393809638],
["Kauffman foundation",-0.01794,-0.04273,3.807354896],
["Acumen Fund",0.13594,0.06898,4.065890876],
["International Monetary Fund",0.48698,0.46266,3.905832962],
["American Friends Service Committee",0.22955,0.88111,3.663078081],
["Inter-American Foundation",0.35041,0.11461,3.517095813],
["Cooperative for Assistance and Relief Everywhere",0.60503,0.60169,4.438851234],
["OPEC Fund for International Development",0.43649,0.41626,4.027213986],
["Austrian Development Agency",0.15233,0.40918,3.854900684],
["Andean Development Corporation",0.45030,0.41771,4.164631048],
["Liechtensteinische Entwicklungsdienst",-0.00372,0.38538,2.500000000],
["Church World Service",0.44577,0.30553,4.049329277],
["World Food Programme",0.60980,0.51577,4.467666104],
["Mo Ibrahim Foundation",0.44862,0.32403,3.596987938],
["Life for Relief and Development",0.09205,-0.00268,3.208430142],
["European Investment Bank",0.60695,0.25993,4.310772970],
["Atlantic Philanthropies",0.29132,0.76040,3.585005503],
["Mercy Corps International",0.26728,0.40053,4.496953251],
["Waleed bin Talal Foundation",-0.12864,-0.03922,3.169925001],
["Development Alternatives Inc.",0.38485,0.30458,4.163808072],
["New Zealand Agency for International Development",0.21424,0.54621,4.500752295],
["Belgian Policy Plan for Development Cooperation",-0.22250,0.00224,3.000000000],
["Christian Reformed World Relief Committee",0.29258,0.38975,3.765180557],
["IBM International Foundation",-0.13855,-0.31567,2.521928095],
["Deutsche Gesellschaft fur Internationale Zusammenarbeit",0.25448,0.31479,3.635063713],
["American Red Cross",0.34916,0.34134,2.798955518],
["Islamic Relief Worldwide",0.24588,0.57018,3.537959468],
["Congo Basin Forest Fund",0.34859,0.33217,3.127157015],
["Christian Aid",0.15005,0.23421,4.260153690],
["Rockefeller Foundation",-0.06955,-0.07128,4.358105286],
["EuropeAid Development and Cooperation",0.01848,0.13668,3.683746090],
["Lutheran World Relief",0.32309,0.45145,3.912384360],
["German Development Bank",0.30106,0.48883,4.155291054]
];

var dataCountry = [
["Turkmenistan",0.01860,0.01165,"#00f"],
["Lithuania",0.05939,-0.12934,"#0f0"],
["Cambodia",0.21404,0.23429,"#00f"],
["Ethiopia",0.38475,0.45840,"#f00"],
["Swaziland",0.23118,0.33919,"#f00"],
["Argentina",0.37377,0.44968,"#f90"],
["Bolivia",0.14209,0.61293,"#f90"],
["Cameroon",0.29239,0.44243,"#f00"],
["Burkina Faso",0.06141,0.39700,"#f00"],
["Ghana",0.21310,0.15145,"#f00"],
["Guatemala",0.20140,0.59348,"#f90"],
["Bosnia and Herzegovina",0.04162,0.15506,"#0f0"],
["Liberia",0.16042,0.03268,"#f00"],
["Jamaica",0.11117,0.14407,"#f90"],
["Tanzania",0.20962,0.12762,"#f00"],
["Gabon",0.05992,0.33881,"#f00"],
["Yemen",0.05692,0.05279,"#00f"],
["Pakistan",0.29057,0.26641,"#00f"],
["Albania",0.09933,-0.24727,"#0f0"],
["Kosovo",0.02565,0.52240,"#0f0"],
["India",0.10755,0.31821,"#00f"],
["Azerbaijan",0.00065,-0.06721,"#00f"],
["Lesotho",0.18057,0.50193,"#f00"],
["Kenya",0.23937,0.13903,"#f00"],
["Tajikistan",0.03484,0.08425,"#00f"],
["Turkey",0.16231,0.03676,"#00f"],
["Afghanistan",0.27727,0.39743,"#00f"],
["Bangladesh",0.25245,-0.04189,"#00f"],
["Eritrea",0.18862,0.25124,"#f00"],
["Mongolia",0.00890,-0.02470,"#00f"],
["Rwanda",0.29989,0.31477,"#f00"],
["Peru",0.34696,0.60621,"#f90"],
["Republic of Congo",0.00413,0.44807,"#f00"],
["Malawi",0.20428,0.34961,"#f00"],
["Benin",0.08129,0.54120,"#f00"],
["Togo",0.01931,0.33459,"#f00"],
["China",0.19022,0.51180,"#00f"],
["Armenia",-0.02273,-0.06307,"#00f"],
["Dominican Republic",0.16447,0.37577,"#f90"],
["Ukraine",0.19776,0.27063,"#0f0"],
["Libya",0.33846,0.27522,"#f00"],
["Indonesia",-0.07067,0.03916,"#00f"],
["Central African Republic",0.07844,0.19922,"#f00"],
["Mauritius",0.15162,0.06706,"#f00"],
["Vietnam",0.15531,0.12871,"#00f"],
["Mali",0.16407,0.37380,"#f00"],
["Russia",0.19471,0.31195,"#0f0"],
["Bulgaria",0.22445,0.13725,"#0f0"],
["Romania",0.13099,0.16747,"#0f0"],
["Angola",0.03929,0.17066,"#f00"],
["Chad",0.13705,0.45090,"#f00"],
["South Africa",-0.08163,0.02667,"#f00"],
["Democratic Republic of Congo",0.12181,0.46354,"#f00"],
["Malaysia",0.11768,-0.16434,"#00f"],
["Senegal",0.31371,0.47367,"#f00"],
["Mozambique",0.24768,0.35573,"#f00"],
["Uganda",0.40216,0.26262,"#f00"],
["Niger",0.13413,0.12678,"#f00"],
["Brazil",0.12971,0.19468,"#f90"],
["Guinea",0.10336,0.29840,"#f00"],
["Panama",0.01040,0.19947,"#f90"],
["Lao People Democratic Republic",0.31405,0.35870,"#00f"],
["Costa Rica",0.22812,0.25602,"#f90"],
["Ivory Coast",0.10212,0.21958,"#f00"],
["Nigeria",0.13967,-0.11622,"#f00"],
["Ecuador",-0.00429,0.47601,"#f90"],
["Belarus",0.02100,-0.05636,"#0f0"],
["Iran",0.46396,0.61105,"#00f"],
["Algeria",0.21259,0.21361,"#f00"],
["El Salvador",0.20726,0.47892,"#f90"],
["Chile",0.22213,0.67622,"#f90"],
["Thailand",0.15948,-0.21280,"#00f"],
["Haiti",0.29562,0.47875,"#f90"],
["Iraq",0.31421,0.47494,"#00f"],
["Sierra Leone",0.22206,0.57115,"#f00"],
["Georgia",0.07225,0.32520,"#00f"],
["Gambia",0.10359,0.37826,"#f00"],
["Philippines",-0.00440,0.01081,"#00f"],
["Moldova",-0.01554,-0.16110,"#0f0"],
["Morocco",0.11434,-0.05847,"#f00"],
["Croatia",0.07527,0.08896,"#0f0"],
["Guinea-Bissau",0.16785,0.39179,"#f00"],
["Estonia",0.14937,0.03386,"#0f0"],
["Uruguay",0.03400,0.42345,"#f90"],
["Lebanon",-0.07421,0.09928,"#00f"],
["Uzbekistan",-0.04026,-0.03661,"#00f"],
["Tunisia",0.15522,0.01122,"#f00"],
["Timor-Leste",0.11347,0.39175,"#00f"],
["Colombia",0.33566,0.16931,"#f90"],
["Burundi",0.07497,0.25264,"#f00"],
["Nicaragua",0.12098,0.57606,"#f90"],
["Madagascar",0.17905,0.46864,"#f00"],
["Sudan",0.22985,0.26333,"#f00"],
["Nepal",0.30411,0.44394,"#00f"],
["Venezuela",0.10190,0.08781,"#f90"],
["Zambia",0.20937,0.39219,"#f00"],
["Papua New Guinea",0.05348,0.31149,"#00f"],
["Zimbabwe",0.03784,-0.00818,"#f00"],
["Jordan",0.19169,0.28016,"#00f"],
["Kazakhstan",0.05626,0.24217,"#00f"],
["Mauritania",0.10940,0.13662,"#f00"],
["Kyrgyzstan",-0.06788,-0.06374,"#00f"],
["Macedonia",0.10096,-0.03875,"#0f0"],
["Sri Lanka",0.21989,-0.07476,"#00f"],
["Latvia",0.10368,-0.04602,"#0f0"],
["Syria",0.22353,0.07546,"#00f"],
["Honduras",0.07832,0.59508,"#f90"],
["Myanmar",0.23711,0.19333,"#00f"],
["Mexico",-0.00964,0.28024,"#f90"],
["Egypt",0.05176,0.18171,"#f00"],
["Serbia",0.08874,0.14483,"#0f0"],
["Paraguay",0.04118,0.36103,"#f90"],
["Namibia",0.19751,0.30187,"#f00"],
["Botswana",0.21595,0.44660,"#f00"]
];
    </script>
  </head>
  <body>
   <div class="wrapper">
    <div id="header">
       <h1>Aid Coordination Explorer</h1>
    </div>
    <div id="mainmenu">
      <a href='index.php'>Bipartite Spaces</a><a href='unipartite.php'>Unipartite Spaces</a><div class="here" id="last">Rankings</div>
    </div>
    <div class="content home">
      <div id="menu-left">
        <div class="here-left">Comparison Plots</div>
        <a href="country-rank.php">Country Ranking</a>
        <a href="institution-rank.php">Organization Ranking</a>
        <a href="issue-rank.php">Issue Ranking</a>
      </div>
      <div id="content-right">
          <table>
          <tr>
          <td class="tre">
            <div class="top-select">
              Country Comparison
            </div>
            <div id="plot-country">
            </div>
<script>
      /* Sizing and scales. */
      var w = 250,
          h = 250,
          x = pv.Scale.linear(-0.25, 0.5).range(0, w),
          y = pv.Scale.linear(-0.3, 0.75).range(0, h);
          c = pv.Scale.linear(-1, 1).range("black", "black");

      /* The root panel. */
      var vis = new pv.Panel()
          .canvas('plot-country')
          .width(w)
          .height(h)
          .bottom(50)
          .left(55)
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
         .data(["Issue Rank"])
         .left(-30)
         .bottom(h/2)
         .font("16pt Arial")
         .textAlign("center")
         .textAngle(-Math.PI/2);

      vis.add(pv.Label)
         .data(["Organization Rank"])
         .left(w/2)
         .bottom(-35)
         .font("16pt Arial")
         .textAlign("center");

      /* The dot plot! */
      vis.add(pv.Panel)
         .data(dataCountry)
         .add(pv.Dot)
         .left(function(d) {return x(d[1])})
         .bottom(function(d) {return y(d[2])})
         .strokeStyle(function(d) {return d[3]})
         .fillStyle(function() {return this.strokeStyle().alpha(.2)})
         .title(function(d) {return d[0]});

      vis.render();
</script>
          </td>
          <td class="tre">
            <div class="top-select">
              Organization Comparison
            </div>
<div id="plot-institution"></div>
<script>
      /* Sizing and scales. */
      var w = 250,
          h = 250,
          x = pv.Scale.linear(-0.33, 0.8).range(0, w),
          y = pv.Scale.linear(-0.33, 0.8).range(0, h);
          c = pv.Scale.log(3, 4.6).range("blue", "red");

      /* The root panel. */
      var vis = new pv.Panel()
          .canvas('plot-institution')
          .width(w)
          .height(h)
          .bottom(50)
          .left(55)
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
         .data(["Issue Rank"])
         .left(-30)
         .bottom(h/2)
         .font("16pt Arial")
         .textAlign("center")
         .textAngle(-Math.PI/2);

      vis.add(pv.Label)
         .data(["Country Rank"])
         .left(w/2)
         .bottom(-35)
         .font("16pt Arial")
         .textAlign("center");

      /* The dot plot! */
      vis.add(pv.Panel)
         .data(dataInstitution)
         .add(pv.Dot)
         .left(function(d) {return x(d[1])})
         .bottom(function(d) {return y(d[2])})
         .strokeStyle(function(d) {return c(d[3])})
         .fillStyle(function() {return this.strokeStyle().alpha(.2)})
         .title(function(d) {return d[0]});

      vis.render();
</script>
          </td>
          <td class="tre">
            <div class="top-select">
              Issue Comparison
            </div>
            <div id="plot-issue">
            </div>
<script>
      /* Sizing and scales. */
      var w = 250,
          h = 250,
          x = pv.Scale.linear(-0.33, 0.66).range(0, w),
          y = pv.Scale.linear(-0.2, 0.4).range(0, h);
          c = pv.Scale.log(3, 4.6).range("blue", "red");

      /* The root panel. */
      var vis = new pv.Panel()
          .canvas('plot-issue')
          .width(w)
          .height(h)
          .bottom(50)
          .left(55)
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
         .data(["Organization Rank"])
         .left(-30)
         .bottom(h/2)
         .font("16pt Arial")
         .textAlign("center")
         .textAngle(-Math.PI/2);

      vis.add(pv.Label)
         .data(["Country Rank"])
         .left(w/2)
         .bottom(-35)
         .font("16pt Arial")
         .textAlign("center");

      /* The dot plot! */
      vis.add(pv.Panel)
         .data(dataIssue)
         .add(pv.Dot)
         .left(function(d) {return x(d[1])})
         .bottom(function(d) {return y(d[2])})
         .strokeStyle(function(d) {return d[3]})
         .fillStyle(function() {return this.strokeStyle().alpha(.2)})
         .title(function(d) {return d[0]});

      vis.render();
</script>
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
