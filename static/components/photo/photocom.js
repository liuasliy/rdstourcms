/**
 * Created by liuas on 2016/11/17.
 */

define(['jquery','handlebars','waterfall'], function($) {
    $(function () {
        $('#container').waterfall({
            itemCls: 'item',
            colWidth: 280,
            fitWidth: true,
            gutterWidth: 15,
            gutterHeight: 15,
            maxPage: 28,
            checkImagesLoaded: true,
            dataType: 'html',
            callbacks: {
                loadingFinished: function($loading, isBeyondMaxPage) {
                    if (!isBeyondMaxPage) {
                        $loading.show();
                    } else {
                        $loading.hide();
                        $('#waterfall-message').html('<p class="no-more">没有更多了</p>')

                    }
                },
                renderData: function (data, dataType) {
                    var tpl,
                        template;

                    if ( dataType === 'json' ||  dataType === 'jsonp'  ) { // json or jsonp format
                        tpl = $('#waterfall-tpl').html();
                        template = Handlebars.compile(tpl);

                        return template(data);
                    } else { // html format
                        return data;

                    }
                }
            },
            path: function(page) {
                return '/ajax_get_photo/?page=' + page;
            }

        });
    })

});