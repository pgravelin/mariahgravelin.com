$(document).ready(function(){
    $(".sidenav").sidenav();
});

$(document).ready(function(){
    $(".modal").modal();
    $(".dropdown-trigger").dropdown();
});

$(document).ready(function(){
    $("#homepage").css("background-image");
    $("#homepage").fadeIn(1100);
});

var $grid = $('.grid').masonry({
    // options
    itemSelector: '.grid-item',
    columnWidth: '.grid-sizer',
    percentPosition: true
});

$grid.imagesLoaded().progress( function() {
    $grid.masonry('layout');
});

// $(function(){  // $(document).ready shorthand
//     $(".monster").fadeIn("slow");
// });
  
$(document).ready(function() {
    /* Every time the window is scrolled ... */
    $(window).scroll( function(){
        /* Check the location of each desired element */
        $(".hideme").each( function(i){
            
            var bottom_of_object = $(this).position().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();
            
            /* If the object is completely visible in the window, fade it it */
            if( bottom_of_window > bottom_of_object ){
                
                $(this).animate({"opacity":"1"}, 1500);
            }
        }); 
    });
});