$(document).ready(function() {
   $("#homepage").css("background-image");
   $("#homepage").fadeIn(1100);
});

$(".grid").imagesLoaded(function() {
   $(".grid-item").each(function() {
        $(this).fadeIn(1100);
   });
});

 // Get the modal
var modal = $(".modal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var modalImg = $("#modal-img")

$("img").each(function() {
   $(this).on("click", function() {
      modal.css("display", "block");
      modalImg.attr("src", $(this).attr("src"));
      console.log("WHO");
   });
});

var span = $(".close");
span.on("click", function() {
   modal.css("display", "none");
});