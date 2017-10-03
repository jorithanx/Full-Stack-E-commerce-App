$(window).on("scroll", function () {
   // fixed the shopping card when scrolling down
   if ($(window).scrollTop() > 38) {
      $('#cart').css({
         "position": "fixed",
         "top": "50px",
         "right": "30px",
         "z-index": "1001",
         "padding": "10px",
         "border": "1.5px solid #4279bd",
         "border-radius": "14px",
         "background": "#052c5c",
      });
   } else {
      $('#cart').css({
         "position": "absolute",
         "top": "9px",
         "right": "155px",
         "border": "",
         "background": "none",
      });
   }
});

// Animation when clicking a button "add a new product" into shopping cart
$(".addProductBtn").on("click", function () {
   $(".badge").addClass("zoom");

   setTimeout(function () {
      $(".badge").removeClass("zoom");
   }, 1000);
});
// hobby-session-2
