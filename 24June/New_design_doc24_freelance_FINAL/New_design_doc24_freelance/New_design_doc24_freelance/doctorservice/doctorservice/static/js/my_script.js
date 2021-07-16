//$(document).ready(function(){
function selectSearchType() {
    var x = document.getElementById("service_type").value;
//    var x = document.getElementsByClassName

    switch (x){
        case 'Doctor':{
            $('#tog').toggleClass('del');
            $('#mog').toggleClass('del');
// Disable #x
            $( "#tog" ).prop( "disabled", true );
            $( "#tog" ).css( "display", "none !important" );
            console.log(1);

// Enable #x
             $( "#mog" ).prop( "disabled", false );
            break;
        }
        case 'Serviciu':{
            $('#tog').toggleClass('del');
            $('#mog').toggleClass('del');
// Disable #x
            $( "#tog" ).prop( "disabled", false );

// Enable #x
             $( "#mog" ).prop( "disabled", true );
            break;
        }
    }
}



//$(document).ready(function(){
    function selectSearchTypeNew() {
        var x = document.getElementById("service_type").value;
    //    var x = document.getElementsByClassName
    
        switch (x){
            case 'Doctor':{
                $('#tog').toggleClass('del');
                $('#mog').toggleClass('del');
    // Disable #x
                // $( "#tog" ).prop( "disabled", true );
                $( "#tog" ).css('display','none !important');
                $('#mog').css('display','block !important');
                console.log(1);
    
    // Enable #x
                //  $( "#mog" ).prop( "disabled", false );
                break;
            }
            case 'Serviciu':{
                $('#tog').toggleClass('del');
                $('#mog').toggleClass('del');
                $( "#tog" ).css('display','block !important');
                $('#mog').css('display','none !important');
    // Disable #x
                // $( "#tog" ).prop( "disabled", false );
    
    // Enable #x
                //  $( "#mog" ).prop( "disabled", true );
                break;
            }
        }
    }
    
