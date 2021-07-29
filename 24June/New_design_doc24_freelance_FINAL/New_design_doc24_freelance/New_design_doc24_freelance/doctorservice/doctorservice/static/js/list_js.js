window.onload = function() {
    function azaza(){
 $('.modal').hide();
 }
 $(document).on('show.bs.modal', '.modal', function () {
 $(this).appendTo('body');
 });
 }