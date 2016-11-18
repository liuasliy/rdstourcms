/**
 * Created by liuas on 2016/11/17.
 */

define(['jquery','lazyload'], function($) {
    //list-city-num
    $(function () {
        //lazyload
        $("img.rd_lazyload").lazyload({
            effect: "fadeIn",
            threshold :20,
            data_attribute:"src",
            placeholder:'images/img-load.png'
        });
        //
        var liarr = $('.project-city li'),temp =[];
        for(var i = 0;i<liarr.length;i++){
            temp.push(liarr.eq(i).find('a').text());
        }
        $('.city-total p a').text(unique(temp).length);
        var cityli = unique(temp);
        $('.project-city ul').children('li').remove();
        $('.project-city ul').show();
        for(var n in cityli){
            if(n<8){
                $('.project-city ul').append('<li><a href="/city/'+cityli[n]+'" target="_blank">'+cityli[n]+'</a></li>');
            }
        }
    })

    function unique(liarr){
        var tmp = new Array();
        for(var i in liarr){
            if(tmp.indexOf(liarr[i])==-1){
                tmp.push(liarr[i]);
            }
        }
        return tmp;
    }
});