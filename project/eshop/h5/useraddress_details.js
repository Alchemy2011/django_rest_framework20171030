

var url = window.location.href;

var id = url.split("?")[1].split("=")[1];


$.ajax({
	url: "http://127.0.0.1:8001/computer/delivery_address_rud/" + id + "/", 
	headers: myheader(),
	success: function(res){
    	console.log(res);

    	$("#contact_person").val(res.contact_person);
    	$("#contact_mobile_phone").val(res.contact_mobile_phone);
    	$("#delivery_address").val(res.delivery_address);



	},
    error: function (jqXHR, textStatus, errorThrown)
    {
         console.log(jqXHR, textStatus, errorThrown);
    }    
});





$("#update").click(function(){

	var data = {
		contact_person: $("#contact_person").val(),
		contact_mobile_phone: $("#contact_mobile_phone").val(),		
		delivery_address: $("#delivery_address").val()
	}; 


	$.ajax({
		url: "http://127.0.0.1:8001/computer/delivery_address_rud/" + id + "/", 
	    type: "PATCH",
	    data: data,
		headers: myheader(),	    
		success: function(res){
	    	console.log(res);
	    	window.location.href = "useraddress.html";	    	
		},
	    error: function (jqXHR, textStatus, errorThrown)
	    {
	         console.log(jqXHR, textStatus, errorThrown);
	    }    
	});



});




$("#delete").click(function(){

	$.ajax({
		url: "http://127.0.0.1:8001/computer/delivery_address_rud/" + id + "/", 
	    type: "DELETE",
		headers: myheader(),	    
		success: function(res){
	    	// console.log(res);
	    	window.location.href = "useraddress.html";
		},
	    error: function (jqXHR, textStatus, errorThrown)
	    {
	         console.log(jqXHR, textStatus, errorThrown);
	    }    
	});



});

