





$("#submit").click(function(){

	var data = {
		username: $("#username").val(),
		password: $("#password").val()
	}; 


	$.ajax({
		url: "http://127.0.0.1:8001/computer/user_create/", 
	    type: "POST",
	    data: data,
		success: function(res){
	    	console.log(res);
	    	alert("注册成功");
			// localStorage.setItem("token", res.token);
			window.location.href = "userlogin.html";

		},
	    error: function (jqXHR, textStatus, errorThrown)
	    {
	         console.log(jqXHR, textStatus, errorThrown);
	    }    
	});



});



