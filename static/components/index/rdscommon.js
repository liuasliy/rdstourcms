/**
 * Created by liuas on 2016/11/17.
 */

define(['jquery','flexslider','lazyload'], function($) {
    $(function () {
        $(".banner").flexslider({
            animation:'fade',
            slideshowSpeed:'3000',
            pauseOnHover:'false',
        });

        //login
        $('.drop-trigger').hover(function () {
            $('.login-item').show();
        }, function () {
            $('.login-item').hide();
        })
        $('.login-item').hover(function () {
            $('.drop-trigger').addClass('drop-active');
            $('.login-item').show();
        }, function () {
            $('.login-item').hide();
            $('.drop-trigger').removeClass('drop-active');
        })

        //lazyload
        $("img.rd_lazyload").lazyload({
            effect: "fadeIn",
            threshold :20,
            data_attribute:"src",
            placeholder:'images/img-load.png'
        });
    })


});