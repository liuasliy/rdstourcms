/**
 * Created by liuas on 2016/11/17.
 */

define(['jquery'], function($) {
    $(function () {
        $('input[name="identification"]').attr('placeholder','����������ʼ������û���~');
        $('input[name="password"]').attr('placeholder','����~')

        $('input[name="username"]').attr('placeholder','��ĸ�����ֵ�,�û���Ψһ~');
        $('input[name="email"]').attr('placeholder','�����ַ~');
        $('input[name="password1"]').attr('placeholder','������6λ~')
        $('input[name="password2"]').attr('placeholder','�ٴ�ȷ��~')

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