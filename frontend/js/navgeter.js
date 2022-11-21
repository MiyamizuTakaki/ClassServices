//导航栏目录
window.onload = function () {
    document.getElementById("firstinfo").onclick = ajaxfirstinfo;//个人首选信息
    document.getElementById("mySchedules").onclick = ajaxmyclass;//我的课堂
    /*document.getElementById("showtest").onclick = ajaxshowtest;//我的测试（教师可以添加测试）
    document.getElementById("schoolinfo").onclick = ajaxschoolinfo;//通勤信息
    document.getElementById("mydevice").onclick = ajaxmydevice;//设备信息
    document.getElementById("useradmin").onclick = ajaxuseradmin;//我的账号（教师账号）
    document.getElementById("adminsetting").onclick = adminsetting;//后台设置
    document.getElementById("setSchedule").onclick = setSchedule;//课表设置
    document.getElementById("setUser").onclick = setSchedule;//用户管理*/
//各功能页面登录
    document.getElementById("mySchedule").onclick = function() {
        xhr.open("GET", "http://localhost:63341/school/myclass/" + this.id + ".html", true);
        xhr.send();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                document.getElementById("getset").innerHTML = xhr.responseText;
            }
        }
    };//我的课表
    /*document.getElementById("searchSchedule").onclick = ajaxmyclass;//查询课表
    document.getElementById("Setreminders").onclick = ajaxmyclass;//设置提醒*/

    /*document.getElementById("recentlytested").onclick = ajaxshowtest;//最近测试
    document.getElementById("historytest").onclick = ajaxshowtest;//历史测试
    document.getElementById("Managetests").onclick = ajaxshowtest;//管理测试

    document.getElementById("CommutingInformation").onclick = ajaxschoolinfo;//通勤信息
    document.getElementById("historicalcommute").onclick = ajaxschoolinfo;//历史通勤
    document.getElementById("Managecommute").onclick = ajaxschoolinfo;//管理通勤

    document.getElementById("accountinformation").onclick = ajaxuseradmin;//我的账户信息
    document.getElementById("changePassword").onclick = ajaxuseradmin;//修改密码
    document.getElementById("bindaccount").onclick = ajaxuseradmin;//绑定账号

    document.getElementById("timetable").onclick = setSchedule;//查询课表
    document.getElementById("Coursegroup").onclick = setSchedule;//课程组

    document.getElementById("queryuser").onclick = ajaxuseradmin;//查询用户
    document.getElementById("usergroup").onclick = usergroup;//用户组
    document.getElementById("userlist").onclick = userlist;//用户列表
    document.getElementById("Adduser").onclick = Adduser;//添加用户*/
    function ajaxfirstinfo() {
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://localhost:63341/school/firstinfo/main.html", true);
        xhr.send();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                document.getElementById("maininfo").innerHTML = xhr.responseText;
            }
        }
    }

    function ajaxmyclass() {
        var xhr = new XMLHttpRequest();
        if (this.id === "mySchedules") {
            xhr.open("GET", "http://localhost:63341/school/myclass.html", true);
            xhr.send();
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    document.getElementById("maininfo").innerHTML = xhr.responseText;
                }
            }
        } else {
            xhr.open("GET", "http://localhost:63341/school/myclass/" + this.id + ".html", true);
            xhr.send();
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    document.getElementById("getset").innerHTML = xhr.responseText;
                }
            }
        }

    }
}