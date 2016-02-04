window.onload = function () {
    //运行瀑布流主函数
    PBL('photowrap', 'photobox');
    //模拟数据
    var data = [
        {
            'src': '1.jpg',
            'title': '素材家园-sucaijiayuan.com',
            'name': 'name',
            'namepic': '1.jpg',
            'views': '22',
            'comments': '33'
        },
        {
            'src': '2.jpg',
            'title': '素材家园-sucaijiayuan.com',
            'name': 'name',
            'namepic': '1.jpg',
            'views': '22',
            'comments': '33'
        },
        {
            'src': '3.jpg',
            'title': '素材家园-sucaijiayuan.com',
            'name': 'name',
            'namepic': '1.jpg',
            'views': '22',
            'comments': '33'
        },

    ];


    //设置滚动加载
    window.onscroll = function () {
        //校验数据请求
        if (getCheck()) {
            var wrap = document.getElementById('photowrap');
            for (i in data) {
                //创建box
                var box = document.createElement('div');
                box.className = 'photobox';
                wrap.appendChild(box);
                //创建info
                var info = document.createElement('div');
                info.className = 'info';
                box.appendChild(info);
                //创建pic
                var pic = document.createElement('div');
                pic.className = 'pic';
                info.appendChild(pic);
                //创建img-a
                var ima = document.createElement('a');
                ima.style.height = 'auto';
                pic.appendChild(ima);
                //创建img
                var img = document.createElement('img');
                img.src = 'images/' + data[i].src;
                img.style.height = 'auto';
                ima.appendChild(img);
                //创建title
                var title = document.createElement('div');
                title.className = 'title';
                info.appendChild(title);
                //创建a标记
                var a = document.createElement('a');
                a.innerHTML = data[i].title;
                title.appendChild(a);
                //创建canvo
                var canvo = document.createElement('div');
                canvo.className = 'canvo';
                info.appendChild(canvo);
                //创业html
                var caa = document.createElement('a');
                canvo.appendChild(caa);
                var caimg = document.createElement('img');
                caimg.src = 'images/' + data[i].namepic;
                caa.appendChild(caimg);
                var cadiv = document.createElement('div');
                cadiv.className = 'text';
                cadiv.innerHTML = data[i].name;
                caa.appendChild(cadiv);

                var fdiv = document.createElement('div');
                fdiv.className = 'fright';
                canvo.appendChild(fdiv);
                var fvi = document.createElement('div');
                fvi.className = 'views';
                var fivi = document.createElement('i');
                var ficom = document.createElement('i');
                fivi.className = 'icon iconfont';
                ficom.className = 'icon iconfont';
                fivi.innerHTML = '&#xe605;';
                ficom.innerHTML = '&#xe600;';
                var fcom = document.createElement('div');
                var fspan01 = document.createElement('span');
                var fspan02 = document.createElement('span');
                var fsa = document.createElement('a');
                fspan01.innerHTML = data[i].views;
                fspan02.innerHTML = data[i].comments;
                fcom.className = 'comments';
                fcom.appendChild(fsa);
                fvi.appendChild(fivi);
                fvi.appendChild(fspan01);
                fsa.appendChild(ficom);
                fsa.appendChild(fspan02);
                fdiv.appendChild(fvi);
                fdiv.appendChild(fcom);


            }
            PBL('photowrap', 'photobox');
        }
    }
}
/**
 * 瀑布流主函数
 * @param  wrap    [Str] 外层元素的ID
 * @param  box    [Str] 每一个box的类名
 */
function PBL(wrap, box) {
    //	1.获得外层以及每一个box
    var wrap = document.getElementById(wrap);
    var boxs = getClass(wrap, box);
    //	2.获得屏幕可显示的列数
    var boxW = boxs[0].offsetWidth;
    var colsNum = Math.floor(document.documentElement.clientWidth / boxW);
    wrap.style.width = boxW * colsNum + 'px';//为外层赋值宽度
    //	3.循环出所有的box并按照瀑布流排列
    var everyH = [];//定义一个数组存储每一列的高度
    for (var i = 0; i < boxs.length; i++) {
        if (i < colsNum) {
            everyH[i] = boxs[i].offsetHeight;
        } else {
            var minH = Math.min.apply(null, everyH);//获得最小的列的高度
            var minIndex = getIndex(minH, everyH); //获得最小列的索引
            getStyle(boxs[i], minH, boxs[minIndex].offsetLeft, i);
            everyH[minIndex] += boxs[i].offsetHeight;//更新最小列的高度
        }
    }
}
/**
 * 获取类元素
 * @param  warp        [Obj] 外层
 * @param  className    [Str] 类名
 */
function getClass(wrap, className) {
    var obj = wrap.getElementsByTagName('*');
    var arr = [];
    for (var i = 0; i < obj.length; i++) {
        if (obj[i].className == className) {
            arr.push(obj[i]);
        }
    }
    return arr;
}
/**
 * 获取最小列的索引
 * @param  minH     [Num] 最小高度
 * @param  everyH [Arr] 所有列高度的数组
 */
function getIndex(minH, everyH) {
    for (index in everyH) {
        if (everyH[index] == minH) return index;
    }
}
/**
 * 数据请求检验
 */
function getCheck() {
    var documentH = document.documentElement.clientHeight;
    var scrollH = document.documentElement.scrollTop || document.body.scrollTop;
    return documentH + scrollH >= getLastH() ? true : false;
}
/**
 * 获得最后一个box所在列的高度
 */
function getLastH() {
    var wrap = document.getElementById('photowrap');
    var boxs = getClass(wrap, 'photobox');
    return boxs[boxs.length - 1].offsetTop + boxs[boxs.length - 1].offsetHeight;
}
/**
 * 设置加载样式
 * @param  box    [obj] 设置的Box
 * @param  top    [Num] box的top值
 * @param  left    [Num] box的left值
 * @param  index [Num] box的第几个
 */
var getStartNum = 0;//设置请求加载的条数的位置
function getStyle(box, top, left, index) {
    if (getStartNum >= index) return;
    $(box).css({
        'position': 'absolute',
        'top': top,
        "left": left,
        "opacity": "0"
    });
    $(box).stop().animate({
        "opacity": "1"
    }, 999);
    getStartNum = index;//更新请求数据的条数位置
}
