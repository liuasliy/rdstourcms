require.config({
    paths: {
        'jquery': [
            'jquery-v1.10.2'
        ],
        'flexslider':'jquery.flexslider-min',
        'lazyload':'jquery.lazyload.min'
    },
    shim: {
        'flexslider': {
            deps: ['jquery']
        },
        'lazyload': {
            deps: ['jquery']
        }
    }

});
require(['jquery', 'flexslider','lazyload'],
    function($) {
        $(".banner").flexslider({
            animation:'fade',
            slideshowSpeed:'3000',
            pauseOnHover:'false',
        });
//share
        $('#side-share').hover(function () {
            $(this).find('.share-box').addClass('active');
        }, function () {
            $(this).find('.share-box').removeClass('active')
        })
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
        //list-city-num
        var liarr = $('.project-city li'),temp =[];
        for(var i = 0;i<liarr.length;i++){
            temp.push(liarr.eq(i).find('a').text());
        }
        function unique(liarr){
            var tmp = new Array();
            for(var i in liarr){
                if(tmp.indexOf(liarr[i])==-1){
                    tmp.push(liarr[i]);
                }
            }
            return tmp;
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
        //photodetils-pinglun
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
        //replyemotions
        function replace_em(str){
            var areaval = $('.comuser-textarea textarea').val();
            var pattern =new RegExp("\\((.| )+?\\)","igm");
            var textarr = areaval.match(pattern);
            areaval = areaval.replace(/\</g,'&lt;');
            areaval = areaval.replace(/\>/g,'&gt;');
            areaval = areaval.replace(/\n/g,'<br/>');
            areaval = areaval.replace(/\(/g,'');
            areaval = areaval.replace(/\)/g,'');
            if(textarr){
                for(var i=0;i<textarr.length;i++){
                    var item = textarr[i].split(/[()]/)[1];
                    console.log(item);
                    var llist = $('.face-icon ul li');
                    for(var n=0;n<llist.length;n++){
                        if(item == llist.eq(n).attr('title')){
                            var newstr = llist.eq(n).html();
                        }
                    }
                    areaval = areaval.replace(item,newstr);
                }
                str = areaval;
                return str;
            }
            else{
                return str;
            }

        }
        $('.face-icon1').show();
        $('.face-tab li').each(function () {
            $(this).click(function (e) {
                $(this).addClass('cur').siblings().removeClass('cur');
                var num = $(this).index();
                $('.face-icon'+(num+1)).show().siblings('.face-icon').hide();
                e.stopPropagation();
            })
        })
        $('.face-btn i').click(function (e) {
            $('.face-pop').show();
            e.stopPropagation();
        })
        $(document).click(function () {
            $('.face-pop').hide();
        })

        $.ajax( {
            type: "post",
            dataType : 'json',
            url : '/static/js/emotions.json',
            success : function(data) {
                var legth = data.konglong.length;
                var legth2 = data.changy.length;
                for(var i = 0;i<legth;i++){
                    $('.face-icon2 ul').append('<li title="'+ data.konglong[i].title +'"><img src="' + data.konglong[i].imgurl + '" /></li>')
                }
                for(var i = 0;i<legth2;i++){
                    $('.face-icon1 ul').append('<li title="'+ data.changy[i].title +'"><img src="' + data.changy[i].imgurl + '" /></li>')
                }
                $('.face-icon ul li').each(function () {
                    $(this).click(function () {
                        var areaval = $('.comuser-textarea textarea').val();
                        var valText = areaval + '('+$(this).attr('title')+')';
                        $('.comuser-textarea textarea').val(valText).focus();
                        $('.face-pop').hide();
                    })
                })
            }
        });

        //comments-biaoqing
        $('.btn-submit').click(function () {
            var areaval = $('.comuser-textarea textarea').val();
            if(areaval == ""){
                $('.comuser-textarea').append('<div class="textarea-tips">«Î ‰»Î∆¿¬€ƒ⁄»›~</div>')
                setTimeout(function () {
                    $('.textarea-tips').remove()
                },2000)
                return false;
            }else{
                $('.comuser-textarea textarea').css('opacity',0).val(replace_em(areaval));
            }

        })

        //lazyload
        //tour-details
        $("img.rd_lazyload").lazyload({
            effect: "fadeIn",
            threshold :20,
            data_attribute:"src",
            placeholder:'images/img-load.png'
        });

        $(".tour-article img.rd_lazyload").each(function () {
            $(this).parent('p').css('text-indent','0');
            var tname = $(this).attr('alt');
            var thtml = '<div class="site-info"><i class="fa fa-map-signs"></i>'+tname+'</div>';
            $(this).after(thtml);
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

});

require([
    '/static/js/photoswipe.min.js',
    '/static/js/photoswipe-ui-default.min.js'
], function( PhotoSwipe, PhotoSwipeUI_Default ) {

    var initPhotoSwipeFromDOM = function(gallerySelector) {

        var parseThumbnailElements = function(el) {
            var thumbElements = el.childNodes,
                numNodes = thumbElements.length,
                items = [],
                el,
                childElements,
                thumbnailEl,
                size,
                item;

            for(var i = 0; i < numNodes; i++) {
                el = thumbElements[i];

                // include only element nodes
                if(el.nodeType !== 1) {
                    continue;
                }

                childElements = el.children;

                size = el.getAttribute('data-size').split('x');

                // create slide object
                item = {
                    src: el.getAttribute('href'),
                    w: parseInt(size[0], 10),
                    h: parseInt(size[1], 10),
                    author: el.getAttribute('data-author')
                };

                item.el = el; // save link to element for getThumbBoundsFn

                if(childElements.length > 0) {
                    item.msrc = childElements[0].getAttribute('src'); // thumbnail url
                    if(childElements.length > 1) {
                        item.title = childElements[1].innerHTML; // caption (contents of figure)
                    }
                }


                var mediumSrc = el.getAttribute('data-med');
                if(mediumSrc) {
                    size = el.getAttribute('data-med-size').split('x');
                    // "medium-sized" image
                    item.m = {
                        src: mediumSrc,
                        w: parseInt(size[0], 10),
                        h: parseInt(size[1], 10)
                    };
                }
                // original image
                item.o = {
                    src: item.src,
                    w: item.w,
                    h: item.h
                };

                items.push(item);
            }

            return items;
        };

        // find nearest parent element
        var closest = function closest(el, fn) {
            return el && ( fn(el) ? el : closest(el.parentNode, fn) );
        };

        var onThumbnailsClick = function(e) {
            e = e || window.event;
            e.preventDefault ? e.preventDefault() : e.returnValue = false;

            var eTarget = e.target || e.srcElement;

            var clickedListItem = closest(eTarget, function(el) {
                return el.tagName === 'A';
            });

            if(!clickedListItem) {
                return;
            }

            var clickedGallery = clickedListItem.parentNode;

            var childNodes = clickedListItem.parentNode.childNodes,
                numChildNodes = childNodes.length,
                nodeIndex = 0,
                index;

            for (var i = 0; i < numChildNodes; i++) {
                if(childNodes[i].nodeType !== 1) {
                    continue;
                }

                if(childNodes[i] === clickedListItem) {
                    index = nodeIndex;
                    break;
                }
                nodeIndex++;
            }

            if(index >= 0) {
                openPhotoSwipe( index, clickedGallery );
            }
            return false;
        };

        var photoswipeParseHash = function() {
            var hash = window.location.hash.substring(1),
                params = {};

            if(hash.length < 5) { // pid=1
                return params;
            }

            var vars = hash.split('&');
            for (var i = 0; i < vars.length; i++) {
                if(!vars[i]) {
                    continue;
                }
                var pair = vars[i].split('=');
                if(pair.length < 2) {
                    continue;
                }
                params[pair[0]] = pair[1];
            }

            if(params.gid) {
                params.gid = parseInt(params.gid, 10);
            }

            return params;
        };

        var openPhotoSwipe = function(index, galleryElement, disableAnimation, fromURL) {
            var pswpElement = document.querySelectorAll('.pswp')[0],
                gallery,
                options,
                items;

            items = parseThumbnailElements(galleryElement);

            // define options (if needed)
            options = {

                galleryUID: galleryElement.getAttribute('data-pswp-uid'),

                getThumbBoundsFn: function(index) {
                    // See Options->getThumbBoundsFn section of docs for more info
                    var thumbnail = items[index].el.children[0],
                        pageYScroll = window.pageYOffset || document.documentElement.scrollTop,
                        rect = thumbnail.getBoundingClientRect();

                    return {x:rect.left, y:rect.top + pageYScroll, w:rect.width};
                },

                addCaptionHTMLFn: function(item, captionEl, isFake) {
                    if(!item.title) {
                        captionEl.children[0].innerText = '';
                        return false;
                    }
                    captionEl.children[0].innerHTML = item.title +  '<br/><small>Photo: ' + item.author + '</small>';
                    return true;
                }

            };


            if(fromURL) {
                if(options.galleryPIDs) {
                    // parse real index when custom PIDs are used
                    // http://photoswipe.com/documentation/faq.html#custom-pid-in-url
                    for(var j = 0; j < items.length; j++) {
                        if(items[j].pid == index) {
                            options.index = j;
                            break;
                        }
                    }
                } else {
                    options.index = parseInt(index, 10) - 1;
                }
            } else {
                options.index = parseInt(index, 10);
            }

            // exit if index not found
            if( isNaN(options.index) ) {
                return;
            }



            var radios = document.getElementsByName('gallery-style');
            for (var i = 0, length = radios.length; i < length; i++) {
                if (radios[i].checked) {
                    if(radios[i].id == 'radio-all-controls') {

                    } else if(radios[i].id == 'radio-minimal-black') {
                        options.mainClass = 'pswp--minimal--dark';
                        options.barsSize = {top:0,bottom:0};
                        options.captionEl = false;
                        options.fullscreenEl = false;
                        options.shareEl = false;
                        options.bgOpacity = 0.85;
                        options.tapToClose = true;
                        options.tapToToggleControls = false;
                    }
                    break;
                }
            }

            if(disableAnimation) {
                options.showAnimationDuration = 0;
            }

            // Pass data to PhotoSwipe and initialize it
            gallery = new PhotoSwipe( pswpElement, PhotoSwipeUI_Default, items, options);

            // see: http://photoswipe.com/documentation/responsive-images.html
            var realViewportWidth,
                useLargeImages = false,
                firstResize = true,
                imageSrcWillChange;

            gallery.listen('beforeResize', function() {

                var dpiRatio = window.devicePixelRatio ? window.devicePixelRatio : 1;
                dpiRatio = Math.min(dpiRatio, 2.5);
                realViewportWidth = gallery.viewportSize.x * dpiRatio;


                if(realViewportWidth >= 1200 || (!gallery.likelyTouchDevice && realViewportWidth > 800) || screen.width > 1200 ) {
                    if(!useLargeImages) {
                        useLargeImages = true;
                        imageSrcWillChange = true;
                    }

                } else {
                    if(useLargeImages) {
                        useLargeImages = false;
                        imageSrcWillChange = true;
                    }
                }

                if(imageSrcWillChange && !firstResize) {
                    gallery.invalidateCurrItems();
                }

                if(firstResize) {
                    firstResize = false;
                }

                imageSrcWillChange = false;

            });

            gallery.listen('gettingData', function(index, item) {
                if( useLargeImages ) {
                    item.src = item.o.src;
                    item.w = item.o.w;
                    item.h = item.o.h;
                } else {
                    item.src = item.m.src;
                    item.w = item.m.w;
                    item.h = item.m.h;
                }
            });

            gallery.init();
        };

        // select all gallery elements
        var galleryElements = document.querySelectorAll( gallerySelector );
        for(var i = 0, l = galleryElements.length; i < l; i++) {
            galleryElements[i].setAttribute('data-pswp-uid', i+1);
            galleryElements[i].onclick = onThumbnailsClick;
        }

        // Parse URL and open gallery if it contains #&pid=3&gid=1
        var hashData = photoswipeParseHash();
        if(hashData.pid && hashData.gid) {
            openPhotoSwipe( hashData.pid,  galleryElements[ hashData.gid - 1 ], true, true );
        }
    };

    initPhotoSwipeFromDOM('.demo-gallery');
});