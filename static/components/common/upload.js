/**
 * Created by liuas on 2016/11/17.
 */

define(['jquery','ckeditor','ckeditorinit'], function($) {
    $(function () {
        $('#id_image').hide();
        $('#id_image').parents('li').append('<label for="id_image" class="upload">上传图片</label>' +
            '<div class="filename"></div>');
        $('#id_image').change(function () {
            $('.filename').html($('#id_image').val());
        })
//
        $('#id_bigimage').hide();
        $('#id_bigimage').parents('li').append('<label for="id_bigimage" class="upload">上传图片</label>' +
            '<div class="filename02"></div>');
        $('#id_bigimage').change(function () {
            $('.filename02').html($('#id_bigimage').val());
        })
    })


});