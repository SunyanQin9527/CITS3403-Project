function showLogin() {
    $("#loginForm").show();
    $("#registerForm").hide();
}

function showRegister() {
    $("#registerForm").show();
    $("#loginForm").hide();
}

function searchRequests() {
    var query = $("#searchQuery").val();
    // 通过AJAX请求搜索请求
    // 更新页面上的#requestsList部分
}
