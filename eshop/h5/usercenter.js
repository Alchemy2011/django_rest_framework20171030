


$.ajax({
	url: "http://127.0.0.1:8001/computer/user_info/", 
	headers: myheader(),
	success: function(res){
    	console.log(res);
		$("#id").html("id：" + res.id);
		$("#username").html("用户名：" + res.username);
		$("#email").html("邮箱：" + res.email);
		$("#last_name").html("姓：" + res.last_name);
		$("#first_name").html("名：" + res.first_name);
		$("#date_joined").html("注册时间：" + res.date_joined.substring(0,10));
		$("#mobile_phone").html("手机号：" + res.profile_of.mobile_phone);


	},
    error: function (jqXHR, textStatus, errorThrown)
    {
         console.log(jqXHR, textStatus, errorThrown);
         window.location.href = "userlogin.html";
    }    
});




$("#logout").click(function(){

	localStorage.removeItem('token');
	window.location.href = "usercenter.html";

});


