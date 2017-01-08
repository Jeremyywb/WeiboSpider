$('.dot:nth-child(1)').click(function(){
  $('.inside').animate({
    'width' : '20%'
  }, 500);
});
$('.dot:nth-child(2)').click(function(){
  $('.inside').animate({
    'width' : '40%'
  }, 500);
});
$('.dot:nth-child(3)').click(function(){
  $('.inside').animate({
    'width' : '60%'
  }, 500);
});
$('.dot:nth-child(4)').click(function(){
  $('.inside').animate({
    'width' : '80%'
  }, 500);
});
if ($('#switch1').not(':checked')){
     $('.modal').unwrap('<div class="mask"></div>');
    $('.modal').hide();
    $('.modal').addClass('nobox');
    $('.dot').click(function(){
    var modal = $(this).attr('id');
    $('article.nobox').hide()
    $('article.nobox.' + modal).fadeIn(200)
  });

}
$("#switch1").click(function(){
  if ($('#switch1').is(':checked')){


       $('article').removeClass("nobox");
    $('.modal').wrap('<div class="mask"></div>')
    $('.mask').click(function(){
      $(this).fadeOut(300);
      $('.mask article').animate({
        'top' : '-100%'
      }, 300)
    });

    $('.dot').click(function(){
      var modal = $(this).attr('id');
      $('.mask').has('article.' + modal).fadeIn(300);
      $('.mask article.' + modal).fadeIn(0).animate({
        'top' : '10%'
      }, 300);
    });
  
  } else {

    
    $('.modal').unwrap('<div class="mask"></div>');
    $('.modal').hide();
    $('.modal').addClass('nobox');
    $('.dot').click(function(){
    var modal = $(this).attr('id');
    $('article.nobox').hide()
    $('article.nobox.' + modal).fadeIn(200)
  });

 }
})

// copy

// $('.dot:nth-child(1)').click(function(){
//   $('.inside').animate({
//     'width' : '20%'
//   }, 500);
// });
// $('.dot:nth-child(2)').click(function(){
//   $('.inside').animate({
//     'width' : '40%'
//   }, 500);
// });
// $('.dot:nth-child(3)').click(function(){
//   $('.inside').animate({
//     'width' : '60%'
//   }, 500);
// });
// $('.dot:nth-child(4)').click(function(){
//   $('.inside').animate({
//     'width' : '80%'
//   }, 500);
// });
// if ($('#switch1').not(':checked')){
//   $('.modal').wrap('<div class="mask"></div>')
//     $('.mask').click(function(){
//       $(this).fadeOut(300);
//       $('.mask article').animate({
//         'top' : '-100%'
//       }, 300)
//     });

//     $('.dot').click(function(){
//       var modal = $(this).attr('id');
//       $('.mask').has('article.' + modal).fadeIn(300);
//       $('.mask article.' + modal).fadeIn(0).animate({
//         'top' : '10%'
//       }, 300);
//     });
// }
// $("#switch1").click(function(){
//   if ($('#switch1').is(':checked')){
    
//     $('.modal').unwrap('<div class="mask"></div>');
//     $('.modal').hide();
//     $('.modal').addClass('nobox');
//     $('.dot').click(function(){
//     var modal = $(this).attr('id');
//     $('article.nobox').hide()
//     $('article.nobox.' + modal).fadeIn(200)
//   });
//   } else {
//     $('article').removeClass("nobox");
//     $('.modal').wrap('<div class="mask"></div>')
//     $('.mask').click(function(){
//       $(this).fadeOut(300);
//       $('.mask article').animate({
//         'top' : '-100%'
//       }, 300)
//     });

//     $('.dot').click(function(){
//       var modal = $(this).attr('id');
//       $('.mask').has('article.' + modal).fadeIn(300);
//       $('.mask article.' + modal).fadeIn(0).animate({
//         'top' : '10%'
//       }, 300);
//     });
//   }
// })
