   // Animation effect - fly to cart. Inspired by (c) 2013 @ElmahdiMahmoud - fikra-masri.by
   $(function () {
      $('.addProductBtn').on('click', function () {
         const cart = $('.fa-shopping-cart');
         const imgToDrag = $(this).closest('.card').find("img").eq(0);

         if (imgToDrag) {
            const imgClone = imgToDrag.clone();

            imgClone.offset({
               top: imgToDrag.offset().top,
               left: imgToDrag.offset().left
            })
               .css({
                  'opacity': '0.5',
                  'position': 'absolute',
                  'height': '150px',
                  'width': '150px',
                  'z-index': '100'
               })
               .appendTo('body')
               .animate({
               width: "75px",
               height: "75px",
               top: cart.offset().top + 10,
               left: cart.offset().left + 10,
            });

            // Delete clone
            imgClone.animate({
               'width': 0,
               'height': 0,
            }, function () {
               $(this).detach();
            });
         }
      });
   });