/*
$.ajaxSetup({cache:false});

curSpan = 1;

window.setInterval(function(){
  $("#q" + curSpan).fadeOut(400, function() {
     $.ajax({
        url: "/question/",
        dataType: 'json',
        async: false,
        success: function(data) {
           $("#q" + curSpan).html("<a href='/explore/" + data.hrefText + "'>" + data.aText + "</a>");
           $("#q" + curSpan).fadeIn();
           curSpan++;
           if(curSpan == 12) {
              curSpan = 1;
           }
        }
     });
  });
}, 3000);
*/

curSpan = 1;

entitymap = Array();
entitymap[0] = "Agriculture";
entitymap[1] = "Banking system";
entitymap[2] = "Manufacturing";
entitymap[3] = "Housing";
entitymap[4] = "Transportation";
entitymap[5] = "Electricity";
entitymap[6] = "Sanitation";
entitymap[7] = "Primary school";
entitymap[8] = "Hospital";
entitymap[9] = "Tourism";
entitymap[10] = "Microenterprise";
entitymap[11] = "Small and medium enterprise";
entitymap[12] = "Criminal justice";
entitymap[13] = "Reconstruction";
entitymap[14] = "Humanitarian assistance";
entitymap[15] = "Poverty reduction";
entitymap[16] = "Economic growth";
entitymap[17] = "Rural development";
entitymap[18] = "Climate change";
entitymap[19] = "Environmental sustainability";
entitymap[20] = "Job creation";
entitymap[21] = "Technological development";
entitymap[22] = "Homicides";
entitymap[23] = "Civil war";
entitymap[24] = "Natural disaster";
entitymap[25] = "Gender";
entitymap[26] = "Democracy";
entitymap[27] = "Hiv/aids";
entitymap[28] = "Refugee";
entitymap[29] = "School completion";
entitymap[30] = "Infant mortality";
entitymap[31] = "Malnutrition";
entitymap[32] = "Human rights";
entitymap[33] = "Corruption";
entitymap[34] = "Afghanistan";
entitymap[35] = "Albania";
entitymap[36] = "Algeria";
entitymap[37] = "Angola";
entitymap[38] = "Argentina";
entitymap[39] = "Armenia";
entitymap[40] = "Azerbaijan";
entitymap[41] = "Bangladesh";
entitymap[42] = "Belarus";
entitymap[43] = "Benin";
entitymap[44] = "Bolivia";
entitymap[45] = "Bosnia and herzegovina";
entitymap[46] = "Botswana";
entitymap[47] = "Brazil";
entitymap[48] = "Bulgaria";
entitymap[49] = "Burkina faso";
entitymap[50] = "Burundi";
entitymap[51] = "Cambodia";
entitymap[52] = "Cameroon";
entitymap[53] = "Central african republic";
entitymap[54] = "Chad";
entitymap[55] = "Chile";
entitymap[56] = "China";
entitymap[57] = "Colombia";
entitymap[58] = "Costa rica";
entitymap[59] = "Democratic republic of congo";
entitymap[60] = "Dominican republic";
entitymap[61] = "Ecuador";
entitymap[62] = "Egypt";
entitymap[63] = "El salvador";
entitymap[64] = "Eritrea";
entitymap[65] = "Ethiopia";
entitymap[66] = "Gabon";
entitymap[67] = "Gambia";
entitymap[68] = "Georgia";
entitymap[69] = "Ghana";
entitymap[70] = "Guatemala";
entitymap[71] = "Guinea";
entitymap[72] = "Guinea-bissau";
entitymap[73] = "Haiti";
entitymap[74] = "Honduras";
entitymap[75] = "India";
entitymap[76] = "Indonesia";
entitymap[77] = "Iran";
entitymap[78] = "Iraq";
entitymap[79] = "Ivory coast";
entitymap[80] = "Jamaica";
entitymap[81] = "Jordan";
entitymap[82] = "Kazakhstan";
entitymap[83] = "Kenya";
entitymap[84] = "Kosovo";
entitymap[85] = "Kyrgyzstan";
entitymap[86] = "Lao people democratic republic";
entitymap[87] = "Latvia";
entitymap[88] = "Lebanon";
entitymap[89] = "Lesotho";
entitymap[90] = "Liberia";
entitymap[91] = "Libya";
entitymap[92] = "Macedonia";
entitymap[93] = "Madagascar";
entitymap[94] = "Malawi";
entitymap[95] = "Malaysia";
entitymap[96] = "Mali";
entitymap[97] = "Mauritania";
entitymap[98] = "Mauritius";
entitymap[99] = "Mexico";
entitymap[100] = "Moldova";
entitymap[101] = "Mongolia";
entitymap[102] = "Morocco";
entitymap[103] = "Mozambique";
entitymap[104] = "Myanmar";
entitymap[105] = "Namibia";
entitymap[106] = "Nepal";
entitymap[107] = "Nicaragua";
entitymap[108] = "Niger";
entitymap[109] = "Nigeria";
entitymap[110] = "Pakistan";
entitymap[111] = "Panama";
entitymap[112] = "Papua new guinea";
entitymap[113] = "Paraguay";
entitymap[114] = "Peru";
entitymap[115] = "Philippines";
entitymap[116] = "Republic of congo";
entitymap[117] = "Romania";
entitymap[118] = "Rwanda";
entitymap[119] = "Senegal";
entitymap[120] = "Serbia";
entitymap[121] = "Sierra leone";
entitymap[122] = "South africa";
entitymap[123] = "Sri lanka";
entitymap[124] = "Sudan";
entitymap[125] = "Swaziland";
entitymap[126] = "Syria";
entitymap[127] = "Tajikistan";
entitymap[128] = "Tanzania";
entitymap[129] = "Thailand";
entitymap[130] = "Timor-leste";
entitymap[131] = "Togo";
entitymap[132] = "Tunisia";
entitymap[133] = "Turkey";
entitymap[134] = "Turkmenistan";
entitymap[135] = "Uganda";
entitymap[136] = "Ukraine";
entitymap[137] = "Uruguay";
entitymap[138] = "Uzbekistan";
entitymap[139] = "Venezuela";
entitymap[140] = "Vietnam";
entitymap[141] = "Yemen";
entitymap[142] = "Zambia";
entitymap[143] = "Zimbabwe";
entitymap[144] = "Accion international";
entitymap[145] = "Action against hunger";
entitymap[146] = "Acumen fund";
entitymap[147] = "Adventist development and relief agency";
entitymap[148] = "African capacity building foundation";
entitymap[149] = "African development bank";
entitymap[150] = "Aga khan development network";
entitymap[151] = "Agence d'aide a la cooperation technique et au developpement";
entitymap[152] = "Agencia brasileira de cooperacao";
entitymap[153] = "American friends service committee";
entitymap[154] = "American jewish world service";
entitymap[155] = "American red cross";
entitymap[156] = "American refugee committee";
entitymap[157] = "Americares disaster relief and humanitarian aid organization";
entitymap[158] = "Amnesty international";
entitymap[159] = "Andean development corporation";
entitymap[160] = "Arab bank for economic development in africa";
entitymap[161] = "Arab fund for economic & social development";
entitymap[162] = "Ashoka";
entitymap[163] = "Asian development bank";
entitymap[164] = "Atlantic philanthropies";
entitymap[165] = "Australian agency for international development";
entitymap[166] = "Austrian development agency";
entitymap[167] = "Austria wirtschaftsservice gesellschaft";
entitymap[168] = "Belgian policy plan for development cooperation";
entitymap[169] = "Belgian technical cooperation";
entitymap[170] = "Bill and melinda gates foundation";
entitymap[171] = "Canadian international development agency";
entitymap[172] = "Caribbean development bank";
entitymap[173] = "Case foundation";
entitymap[174] = "Childreach";
entitymap[175] = "Christian aid";
entitymap[176] = "Christian reformed world relief committee";
entitymap[177] = "Church world service";
entitymap[178] = "Concern worldwide";
entitymap[179] = "Congo basin forest fund";
entitymap[180] = "Cooperative for assistance and relief everywhere";
entitymap[181] = "Danish international development agency";
entitymap[182] = "Deutsche gesellschaft fur internationale zusammenarbeit";
entitymap[183] = "Development alternatives inc.";
entitymap[184] = "Direct relief international";
entitymap[185] = "Doctors without borders";
entitymap[186] = "Eurasia foundation";
entitymap[187] = "Europeaid development and cooperation";
entitymap[188] = "European bank for reconstruction and development";
entitymap[189] = "European investment bank";
entitymap[190] = "Fast track initiative catalytic fund";
entitymap[191] = "Federal ministry for economic cooperation and development";
entitymap[192] = "Finnish department for international development co-operation";
entitymap[193] = "Food and agriculture organization";
entitymap[194] = "Food for the hungry";
entitymap[195] = "Ford foundation";
entitymap[196] = "French development agency";
entitymap[197] = "German development bank";
entitymap[198] = "Global alliance for vaccines & immunization";
entitymap[199] = "Global environment facility";
entitymap[200] = "Global fund to fight aids, tuberculosis and malaria";
entitymap[201] = "Google org";
entitymap[202] = "Grameen bank";
entitymap[203] = "Grameen foundation";
entitymap[204] = "Hellenic aid";
entitymap[205] = "Helvetas";
entitymap[206] = "Hewlett foundation";
entitymap[207] = "High commissioner of human rights";
entitymap[208] = "Human rights council";
entitymap[209] = "Human rights watch";
entitymap[210] = "Ibm international foundation";
entitymap[211] = "Instituto portugues de apoio ao desenvolvimento";
entitymap[212] = "Inter-american development bank";
entitymap[213] = "Inter-american foundation";
entitymap[214] = "International committee of the red cross";
entitymap[215] = "International cooperation and development fund";
entitymap[216] = "International development research centre";
entitymap[217] = "International fund for agricultural development";
entitymap[218] = "International monetary fund";
entitymap[219] = "Irish aid";
entitymap[220] = "Islamic development bank";
entitymap[221] = "Islamic relief worldwide";
entitymap[222] = "Israel's agency for international development cooperation";
entitymap[223] = "Italian development cooperation programme";
entitymap[224] = "Japan bank for international cooperation";
entitymap[225] = "Japan international cooperation agency";
entitymap[226] = "Japan official development assistance";
entitymap[227] = "Joint united nations programme on hiv/aids";
entitymap[228] = "Kauffman foundation";
entitymap[229] = "Korea international cooperation agency";
entitymap[230] = "Lemelson foundation";
entitymap[231] = "Liechtensteinische entwicklungsdienst";
entitymap[232] = "Life for relief and development";
entitymap[233] = "Lutheran world relief";
entitymap[234] = "Lux-development";
entitymap[235] = "Macarthur foundation";
entitymap[236] = "Medair";
entitymap[237] = "Medical assistance program international";
entitymap[238] = "Mercy corps international";
entitymap[239] = "Millennium challenge corporation";
entitymap[240] = "Multilateral investment guarantee agency";
entitymap[241] = "Netherlands ministry of development cooperation";
entitymap[242] = "New zealand agency for international development";
entitymap[243] = "Nordic development fund";
entitymap[244] = "North american development bank";
entitymap[245] = "Norwegian agency for development cooperation";
entitymap[246] = "Novartis foundation";
entitymap[247] = "Opec fund for international development";
entitymap[248] = "Oxfam international";
entitymap[249] = "Poland development co-operation department";
entitymap[250] = "Refugees international";
entitymap[251] = "Rockefeller brothers fund";
entitymap[252] = "Rockefeller foundation";
entitymap[253] = "Romania official development assistance";
entitymap[254] = "Salvation army international headquarters";
entitymap[255] = "Save the children";
entitymap[256] = "Schwab foundation";
entitymap[257] = "Seven fund";
entitymap[258] = "Shell foundation";
entitymap[259] = "Skoll foundation";
entitymap[260] = "Slovak aid";
entitymap[261] = "Soros foundation";
entitymap[262] = "Spanish agency for international cooperation";
entitymap[263] = "Swedish international development cooperation agency";
entitymap[264] = "Swiss agency for development and cooperation";
entitymap[265] = "Turkish international cooperation and development agency";
entitymap[266] = "Uk department for international development";
entitymap[267] = "United nations capital development fund";
entitymap[268] = "United nations centre for human settlements";
entitymap[269] = "United nations conference on trade and development";
entitymap[270] = "United nations democracy fund";
entitymap[271] = "United nations development fund for women";
entitymap[272] = "United nations development programme";
entitymap[273] = "United nations educational, scientific and cultural organization";
entitymap[274] = "United nations environment programme";
entitymap[275] = "United nations high commissioner for refugees";
entitymap[276] = "United nations office for project services";
entitymap[277] = "United nations relief and works agency for palestine refugees";
entitymap[278] = "United states agency for international development";
entitymap[279] = "United way international";
entitymap[280] = "Us african development foundation";
entitymap[281] = "West african development bank";
entitymap[282] = "World bank";
entitymap[283] = "World concern";
entitymap[284] = "World food programme";
entitymap[285] = "World health organization";
entitymap[286] = "World relief";
entitymap[287] = "World vision international";
entitymap[288] = "Abu dhabi fund for development";
entitymap[289] = "Carlos slim foundation";
entitymap[290] = "Catholic overseas development agency";
entitymap[291] = "China development bank";
entitymap[292] = "China development industrial bank";
entitymap[293] = "Dubai cares";
entitymap[294] = "Maktoum foundation";
entitymap[295] = "Mo ibrahim foundation";
entitymap[296] = "Waleed bin talal foundation";

window.setInterval(function(){
  $("#q" + curSpan).fadeOut(400, function() {
     qid = Math.floor(Math.random() * 303) + 1;
     switch(qid) {
        case 298: $("#q" + curSpan).html("<a href='/explore/network/1/'>What Aid Organization is related to each other Aid Organization?</a>"); break;
        case 299: $("#q" + curSpan).html("<a href='/explore/network/2/'>What Country is related to each other Country for the Aid Organizations?</a>"); break;
        case 300: $("#q" + curSpan).html("<a href='/explore/network/3/'>What Issue is related to each other Issue according to the Aid Organization?</a>"); break;
        case 301: $("#q" + curSpan).html("<a href='/explore/ranking/1/'>What Aid Organization is more consistent in the Countries it is serving?</a>"); break;
        case 302: $("#q" + curSpan).html("<a href='/explore/ranking/2/'>What Country is more consistent in the Issues it is served on?</a>"); break;
        case 303: $("#q" + curSpan).html("<a href='/explore/ranking/3/'>What Issue is served more consistently by the Aid Organizations?</a>"); break;
        default: {
           qid2 = Math.floor(Math.random() * 5);
           if(qid <= 34) {
              switch(qid2) {
                 case 1: $("#q" + curSpan).html("<a href='/explore/static/profile/" + qid + "/consistency/Organizations/'>How does " + entitymap[qid - 1] + " relate to all Organizations?</a>"); break;
                 case 2: $("#q" + curSpan).html("<a href='/explore/static/profile/" + qid + "/consistency/Countries/'>How does " + entitymap[qid - 1] + " relate to all Countries?</a>"); break;
                 case 3: $("#q" + curSpan).html("<a href='/explore/static/profile/" + qid + "/bipartite_rank/Organizations/'>What are the Organizations more related to " + entitymap[qid - 1] + "?</a>"); break;
                 case 4: $("#q" + curSpan).html("<a href='/explore/static/profile/" + qid + "/bipartite_rank/Countries/'>What are the Countries more related to " + entitymap[qid - 1] + "?</a>"); break;
              }
           } else if(qid <= 144) {
              switch(qid2) {
                 case 1: $("#q" + curSpan).html("<a href='/explore/static/profile/" + qid + "/consistency/Organizations/'>How does " + entitymap[qid - 1] + " relate to all Organizations?</a>"); break;
                 case 2: $("#q" + curSpan).html("<a href='/explore/static/profile/" + qid + "/consistency/Issues/'>How does " + entitymap[qid - 1] + " relate to all Issues?</a>"); break;
                 case 3: $("#q" + curSpan).html("<a href='/explore/static/profile/" + qid + "/bipartite_rank/Organizations/'>What are the Organizations more related to " + entitymap[qid - 1] + "?</a>"); break;
                 case 4: $("#q" + curSpan).html("<a href='/explore/static/profile/" + qid + "/bipartite_rank/Issues/'>What are the Issues more related to " + entitymap[qid - 1] + "?</a>"); break;
              }
           } else {
              switch(qid2) {
                 case 1: $("#q" + curSpan).html("<a href='/explore/static/profile/" + qid + "/consistency/Issues/'>How does " + entitymap[qid - 1] + " relate to all Issues?</a>"); break;
                 case 2: $("#q" + curSpan).html("<a href='/explore/static/profile/" + qid + "/consistency/Countries/'>How does " + entitymap[qid - 1] + " relate to all Countries?</a>"); break;
                 case 3: $("#q" + curSpan).html("<a href='/explore/static/profile/" + qid + "/bipartite_rank/Issues/'>What are the Issues more related to " + entitymap[qid - 1] + "?</a>"); break;
                 case 4: $("#q" + curSpan).html("<a href='/explore/static/profile/" + qid + "/bipartite_rank/Countries/'>What are the Countries more related to " + entitymap[qid - 1] + "?</a>"); break;
              }
           }
        }
     }
     $("#q" + curSpan).fadeIn();
     curSpan++;
     if(curSpan == 12) {
        curSpan = 1;
     }
  });
}, 3000);
