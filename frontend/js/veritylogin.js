$(document).ready(function () {
    token = $.cookie('users_token')
    console.log(token)
    $.post("/cookiess",
        {
            users_token: token
        },
        function (detail) {
            console.log(detail)
            if (detail["code"] == "0") {
                $(function () {
                    $.removeCookie('users_token')
                    window.location.href = "./";
                })
            }
        });
});