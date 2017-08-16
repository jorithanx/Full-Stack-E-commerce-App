// Disabled seach button when input is empty
$(document).ready(function () {
   let searchBtn = $('#searchBtn');
   let searchInput = $('#searchInput');

   if (searchInput.val().length === 0) {
      searchBtn.css({"cursor": "not-allowed"});
   }

   searchInput.keyup(function () {          
      if ($(this).val().length > 0) {
         searchBtn.prop('disabled', false);
         searchBtn.css({"cursor": "pointer"});
      } else {
         searchBtn.prop('disabled', true);
         searchBtn.css({"cursor": "not-allowed"});
      }
   });
});