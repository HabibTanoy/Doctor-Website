$("#loadmoretext").click(function(){

    var less = document.getElementById('loadless');
   var more = document.getElementById('loadmore');
                                                           // more is click
       $("#alllink1").css("height","100%");
       $("#alllinkcontainer1").css("height","100%");
       more.style.visibility = 'hidden';
       less.style.visibility = 'visible';
});

$("#loadlesstext").click(function(){

    var less = document.getElementById('loadless');
   var more = document.getElementById('loadmore');
                                                        // less is click
       $("#alllink1").css("height", "249px");
       $("#alllinkcontainer1").css("height", "322px");
       more.style.visibility = 'visible';
       less.style.visibility = 'hidden';
});


   $("#loadmoretext2").click(function(){

    var less = document.getElementById('loadless2');
   var more = document.getElementById('loadmore2');
                                                           // more is click
       $("#allinone2").css("height", "100%");
       more.style.visibility = 'hidden';
       less.style.visibility = 'visible';
});

$("#loadlesstext2").click(function(){

    var less = document.getElementById('loadless2');
   var more = document.getElementById('loadmore2');
                                                        // less is click
       $("#allinone2").css("height", "278px");
       
       more.style.visibility = 'visible';
       less.style.visibility = 'hidden';
});

   $(window).scroll(function() {
   let scroll_position = $(window).scrollTop();
   let offset = $('#sidebar').offset();
   if(scroll_position > 2700){
//    if(offset.top > 170 && offset.top <= 180){
    //    $("#sidebar").offset({ top: offset.top, left: offset.left});
//    }
   }else{
       //$("#sidebar").offset({ top: 190, left: offset.left});
   }
   });

       $(document).ready(function(){
   var c = document.getElementById("linkcontainer").childElementCount;
   
   if (c <24) {
   $("#loadmore").css("visibility","hidden");
       $("#loadless").css("visibility","visible");
       $("#alllink1").css("height","100%");
       $("#alllinkcontainer1").css("height","100%");
   }else{

       $("#loadmore").css("visibility","visible");
       $("#loadless").css("visibility","hidden");

   }

       
   // var p1 = document.getElementById("place1").childElementCount;
   // var p2 = document.getElementById("place2").childElementCount;
   // var p3 = document.getElementById("place3").childElementCount;
   // var p4 = document.getElementById("place4").childElementCount;
   // var c2 = (p1 + p2 + p3 + p4);

   // if (c2 <24) {
   // $("#loadmore2").css("visibility","hidden");
   // 	$("#loadless2").css("visibility","visible");
   // 	$("#allinone2").css("height","100%");
   
   // }else{

   // 	$("#loadmore2").css("visibility","visible");
   // 	$("#loadless2").css("visibility","hidden");

   // }

       });