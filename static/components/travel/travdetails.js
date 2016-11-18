/**
 * Created by liuas on 2016/11/17.
 */

define(['jquery','flexslider','lazyload'], function($) {
    $(function () {
        //lazyload
        $("img.rd_lazyload").lazyload({
            effect: "fadeIn",
            threshold :20,
            data_attribute:"src",
            placeholder:'images/img-load.png'
        });
        //
        $(".side-swap").flexslider({
            animation:'fade',
            slideshowSpeed:'3000',
            pauseOnHover:'false',
            directionNav: false,
            controlNav: false,
        });
        //details-share
        $('#side-share').hover(function () {
            $(this).find('.share-box').addClass('active');
        }, function () {
            $(this).find('.share-box').removeClass('active')
        })
        //tour-details
        $(".tour-article img.rd_lazyload").each(function () {
            $(this).parent('p').css('text-indent','0');
            var tname = $(this).attr('alt');
            var thtml = '<div class="site-info"><i class="fa fa-map-signs"></i>'+tname+'</div>';
            $(this).after(thtml);
        })
        //
        var lourl = window.location.href;
        var traId = lourl.split('/')[4];
        //dianz
        $('.click-heart').click(function () {
            $('.fav-note').show();
            var url = "/like_tarvels/"+traId;
            $('.fav-note iframe').attr('src',url);
            setTimeout(function () {
                $('.fav-note').hide();
                $('.fav-note iframe').attr('src','');
            },2000);
        })
        //shoucang
        $('.click-fav').click(function () {
            $('.fav-note').show() ;
            var url = "/addfav/"+traId;
        $('.fav-note iframe').attr('src',url);
        setTimeout(function () {
            $('.fav-note').hide();
            $('.fav-note iframe').attr('src','');
        },2000);
    })
    })
    var setDir = function(){
        var a = $('.tour-article');
        var b = a.find('strong');
        b.each(function (index) {
            var dirName = $(this).text();
            if(index<10){
                var aHtml = '<li><span class="direct-num">'+'0'+(index+01)+'/</span><a href="#'+(index+1)+'">'+dirName+'</a></li>';
            }
            else{
                var aHtml = '<li><span class="direct-num">'+(index+01)+'/</span><a href="#'+(index+1)+'">'+dirName+'</a></li>';
            }
            $('.tour-directory ul').append(aHtml);
        })
    };
    var postFix = function () {
        var sidelemt = $('.side-postion_fix'); //得到导航对象
        var win = $(window); //得到窗口对象
        win.scroll(function () {
            var ofsethei = sidelemt.offset().top-win.scrollTop();
            var sidswhei = $('.side-swap').offset().top-win.scrollTop();
            var foothei = $('.footer').offset().top-win.scrollTop();
            if(ofsethei <=10){
                sidelemt.addClass('rds-side_fix');
            }
            if(sidswhei >= -250){
                sidelemt.removeClass('rds-side_fix');
            }
            if(foothei <= 150){
                sidelemt.removeClass('rds-side_fix');
            }
        })
        var length = $('.project-related li').length;
        if(length > 3){
            for(var i=3;i<length;i++){
                $('.project-related li').eq(i).remove();
            }
        }
    };
    
    return {
        detailDir: setDir,
        postFix: postFix
    }

});