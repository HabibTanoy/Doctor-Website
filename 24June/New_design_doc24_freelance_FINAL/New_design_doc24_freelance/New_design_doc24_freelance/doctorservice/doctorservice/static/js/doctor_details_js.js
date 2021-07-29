window.onload = function() {
    function azaza(){
    $('.modal').hide();
    }
    $(document).on('show.bs.modal', '.modal', function () {
      $(this).appendTo('body');
    });
    }
    
$(document).ready(function(){
    var c = document.getElementById("containing_comments").childElementCount;
    
    if (c <3) {
    $("#loadmore").css("visibility","hidden");
        $("#loadless").css("visibility","visible");
        $("#containing_comments").css("height","100%");
    
    }else{

        $("#loadmore").css("visibility","visible");
        $("#loadless").css("visibility","hidden");

    }
 });

    $("#loadmoretext").click(function(){

    var less = document.getElementById('loadless');
    var more = document.getElementById('loadmore');
    // more is click
    $("#containing_comments").css("height","100%");

    more.style.visibility = 'hidden';
    less.style.visibility = 'visible';
    });

    $("#loadlesstext").click(function(){

    var less = document.getElementById('loadless');
    var more = document.getElementById('loadmore');
    // less is click
    $("#containing_comments").css("height", "416px");

    more.style.visibility = 'visible';
    less.style.visibility = 'hidden';
    });

    
    $(window).scroll(function() {
        let scroll_position = $(window).scrollTop();
        let offset = $('#sidebar').offset();
        // console.log(scroll_position);
        if(scroll_position > 2700){
            if(offset.top > 170 && offset.top <= 180){
            $("#sidebar").offset({ top: offset.top, left: offset.left});
        }
        }else{  
            if(window.innerWidth < 760){
                var bottom = $('#main-body').position().top + $('#main-body').height();
                $("#sidebar").offset({ top: bottom-430, left: offset.left});
            }else{
                if(scroll_position == 0){
                    // console.log('0');
                     $("#sidebar").offset({ top: 255, left: offset.left});
                }
                    // $("#sidebar").offset({ top: 138, left: offset.left});
            }
             
        }
        });
