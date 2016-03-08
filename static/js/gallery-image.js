(function($) { $(document).ready(function() { new grid3D(document.getElementById('grid3d'));
        var container = document.querySelector('#gallery-container');
        var msnry;
        imagesLoaded(container, function() { msnry = new Masonry(container, { itemSelector: '.gallery-image', transitionDuration: '0.3s', columnWidth: container.querySelector('.gallery-image') }) }); }); })(jQuery);;
(function($) { $(document).ready(function() { $('.toggle-menu').jPushMenu(); }); })(jQuery);


