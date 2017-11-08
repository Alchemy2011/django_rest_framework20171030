
var address_chosen = 0;


$.ajax({
	url: "http://127.0.0.1:8001/computer/cart_list/", 
	headers: myheader(),
	success: function(res){
    	console.log(res);


		$("#view").html("");

		for (var i = 0; i < res.results.length; i++) {

			$("#view").append(
		      '<tr>'+
		        '<td><img class="img-responsive" style="max-height:60px;" src="' + res.results[i].product.image + '"></td>'+
		        '<td>' + res.results[i].product.model + '</td>'+
		        '<td>' + res.results[i].price + '</td>'+
		        '<td>' + res.results[i].quantity + '</td>'+
		        '<td>' + (res.results[i].price * res.results[i].quantity) + '</td>'+
    			'<td>' + res.results[i].address.delivery_address + ' --- ' + res.results[i].address.contact_person + ' --- ' + res.results[i].address.contact_mobile_phone + '</td>'+		
		        '<th class="gotoDetails" value="'+ res.results[i].id +'"><button>删除</button></th>'+
		        '<th class="gotoDetails2" value="'+ res.results[i].id +'"><button>下单</button></th>'+

		      '</tr>'
			);    	

			$(".gotoDetails").click(function(){

				$.ajax({
					url: "http://127.0.0.1:8001/computer/order_rud/" + $(this).attr("value") + "/", 
	    			type: "DELETE",					
					headers: myheader(),
					success: function(res){
				    	console.log(res);
						window.location.href = "usercart.html";

					},
				    error: function (jqXHR, textStatus, errorThrown)
				    {
				         console.log(jqXHR, textStatus, errorThrown);
				    }    
				});

			});	

			$(".gotoDetails2").click(function(){

				$.ajax({
					url: "http://127.0.0.1:8001/computer/order_rud/" + $(this).attr("value") + "/", 
	    			type: "PATCH",					
					headers: myheader(),
					success: function(res){
				    	console.log(res);
						window.location.href = "order_success.html";

					},
				    error: function (jqXHR, textStatus, errorThrown)
				    {
				         console.log(jqXHR, textStatus, errorThrown);
				    }    
				});

			});	

		};


	},
    error: function (jqXHR, textStatus, errorThrown)
    {
         console.log(jqXHR, textStatus, errorThrown);
    }    
});









