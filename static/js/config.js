require.config({
    paths: {
        'jquery': 'jquery-v1.10.2',
        'flexslider':'jquery.flexslider-min',
        'lazyload':'jquery.lazyload.min',
        'handlebars':'handlebars',
        'waterfall':'waterfall.min',
        'ckeditor':'../ckeditor/ckeditor/ckeditor',
        'ckeditorinit':'../ckeditor/ckeditor-init',

        'common':'../components/common/common',
        'sign':'../components/common/sign',
        'upload':'../components/common/upload',

        'rdscommon':'../components/index/rdscommon',
        'rdspswipe':'../components/index/rdspswipe',
        'travcom':'../components/travel/travcom',
        'travdetails':'../components/travel/travdetails',

        'photocom':'../components/photo/photocom',
        'photodetail':'../components/photo/photodetail'
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
require(['jquery'],function($) {
        $(function() {
            for( var i=0;i<__funcList.length;i++) {
                __funcList[i]();
            }
        });
});

