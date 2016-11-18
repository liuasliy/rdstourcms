/**
 * Created by liuas on 2016/11/17.
 */

define(['jquery'], function($) {
    $(function () {
        //details-share
        $('#side-share').hover(function () {
            $(this).find('.share-box').addClass('active');
        }, function () {
            $(this).find('.share-box').removeClass('active')
        })
        var lourl = window.location.href;
        var traId = lourl.split('/')[4];
        //dianzan
        $('.click-heart').click(function () {
            $('.fav-note').show();
            var url = "/like_photo/"+traId;
        $('.fav-note iframe').attr('src',url);
        setTimeout(function () {
            $('.fav-note').hide();
            $('.fav-note iframe').attr('src','');
        },2000);
        })

        //photodetails
        $('img.rd_lazyload').each(function () {
            var img = new Image();
            img.src =$(this).attr("data-src") ;
            var _w = parseInt($(window).width());
            imgReady(img.src, function () {
                if(this.width>=_w){
                    $('img.rd_lazyload').css("width","100%").css("height","auto");
                }
                else{
                    $('img.rd_lazyload').css("width",this.width+'px').css("height",this.height+'px');
                }
            });
        })
        //topcomment
        $('.topcomment').on('click', function () {
            $('.po-commentbox').addClass('active');
        })
        $('.po-commentbox .fa-close').on('click', function () {
            $(this).parent().removeClass('active');
        })
        //
        $('.po-reply_tar').click(function (e) {
            $('.pocomform').addClass('comfocus');
            e.stopPropagation();
        })
        $(document).click(function () {
            $('.pocomform').removeClass('comfocus');
        })
    })

});