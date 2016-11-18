/**
 * Created by liuas on 2016/11/17.
 */

define(['jquery'], function($) {
    $(function () {
        $('input[name="identification"]').attr('placeholder','请输入电子邮件或者用户名~');
        $('input[name="password"]').attr('placeholder','密码~')

        $('input[name="username"]').attr('placeholder','字母、数字等,用户名唯一~');
        $('input[name="email"]').attr('placeholder','邮箱地址~');
        $('input[name="password1"]').attr('placeholder','不少于6位~')
        $('input[name="password2"]').attr('placeholder','再次确认~')

        $('.ac-userpass .dd-fix').each(function () {
            $(this).click(function () {
                $(this).hide();
                $(this).prev().hide();
                $(this).siblings('.set-pwmail').slideDown();
            })
        })
        $('.ac-userpass .ac-sub-cancel').each(function () {
            $(this).click(function () {
                $(this).parents('.set-pwmail').hide();
                $(this).parents('.set-pwmail').prevAll().show();
            })
        })
    })


});