





$("#submit").click(function(){

	var data = {
		username: $("#username").val(),
		password: $("#password").val()
	}; 


	$.ajax({
		url: "http://127.0.0.1:8001/api-token-auth/", 
	    type: "POST",
	    data: data,
		success: function(res){
	    	// console.log(res.token);
			localStorage.setItem("token", res.token);
			window.location.href = "usercenter.html";

		},
	    error: function (jqXHR, textStatus, errorThrown)
	    {
	         console.log(jqXHR, textStatus, errorThrown);
	         alert("用户名或密码错误！");
	    }    
	});



});



