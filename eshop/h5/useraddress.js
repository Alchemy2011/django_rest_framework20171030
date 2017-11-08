


$.ajax({
	url: "http://127.0.0.1:8001/computer/delivery_address_lc/", 
	headers: myheader(),
	success: function(res){
    	console.log(res);

		$("#view").html("");

		for (var i = 0; i < res.results.length; i++) {

			$("#view").append(

'<div style="padding-top:20px;" class="col-xs-12 col-sm-12 col-md-12 col-lg-12" value="' + res.results[i].id + '">' +
  '<div style="text-align:left;padding-left:0px;">收货地址' + (i+1) + '</div>' +
  '<div style="text-align:left;padding-left:0px;">联系人：' + res.results[i].contact_person + '</div>' +  
  '<div style="text-align:left;padding-left:0px;">联系电话：' + res.results[i].contact_mobile_phone + '</div>' +  
  '<div style="text-align:left;padding-left:0px;">收货地址：' + res.results[i].delivery_address + '</div>' +  

  '<button type="submit" class="btn btn-default gotoDetails" id="create" value="' + res.results[i].id + '">管理</button>'+

'</div>'

			);    	

			$(".gotoDetails").click(function(){
				console.log($(this).attr("value"));
				window.location.href = "useraddress_details.html?id=" + $(this).attr("value");
			});	

		};


	},
    error: function (jqXHR, textStatus, errorThrown)
    {
         console.log(jqXHR, textStatus, errorThrown);
    }    
});





$("#create").click(function(){

	var data = {
		contact_person: $("#contact_person").val(),
		contact_mobile_phone: $("#contact_mobile_phone").val(),		
		delivery_address: $("#delivery_address").val()
	}; 


	$.ajax({
		url: "http://127.0.0.1:8001/computer/delivery_address_lc/", 
	    type: "POST",
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

