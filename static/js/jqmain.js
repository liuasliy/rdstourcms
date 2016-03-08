$(function () {
   $('.nav-button button').click(function () {
       $('.nav-menu').addClass('bounceInLeft');
   })
    $('.nav-menu  h3').click(function () {
        $('.nav-menu').animate({width:'0px'})
    })
})