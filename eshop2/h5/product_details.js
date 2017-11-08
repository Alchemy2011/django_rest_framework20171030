
var url = window.location.href;

var id = url.split("?")[1].split("=")[1];


$.ajax({
	url: "http://127.0.0.1:8001/computer/product_retrieve/" + id + "/", 
	success: function(res){
    	console.log(res);

    	$("#img").attr("src", res.image);

    	$("#price").html(res.price);
    	$("#model").html(res.model);
    	$("#description").html(res.description);
    	$("#manufacturer").html(res.manufacturer);

}});





$("#addtocart").click(function(){

	var quantity = $("#quantity").val();

	data = {quantity:quantity, product:id};

	console.log(data);

	$.ajax({
		url: "http://127.0.0.1:8001/computer/order_create/", 
	    type: "POST",
	    data: data,
		headers: myheader(),	    
		success: function(res){
	    	console.log(res);
	    	alert("已成功添加到购物车！")    	

		},
	    error: function (jqXHR, textStatus, errorThrown)
	    {
	        console.log(jqXHR, textStatus, errorThrown);
	    	alert("咦，好像出错了！请确认您已经设定默认收货地址!")    		         
	    }    
	});



});


