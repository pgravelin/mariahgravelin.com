$(document).ready(function() {
   $("#homepage").css("background-image");
   $("#homepage").fadeIn(1100);
});

$(".grid").imagesLoaded(function() {
   $(".grid-item").each(function() {
        $(this).fadeIn(1100);
   });
});

var modal = $(".modal");
var modalImg = $("#modal-img")

$("img").each(function() {
   $(this).on("click", function() {
      modal.css("display", "block");
      modalImg.attr("src", $(this).attr("src"));
   });
});

var span = $(".close");
span.on("click", function() {
   modal.css("display", "none");
});