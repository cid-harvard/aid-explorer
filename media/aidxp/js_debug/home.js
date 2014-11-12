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
