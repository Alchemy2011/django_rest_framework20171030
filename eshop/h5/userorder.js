
var address_chosen = 0;


$.ajax({
	url: "http://127.0.0.1:8001/computer/order_list/", 
	headers: myheader(),
	success: function(res){
    	console.log(res);


		$("#view").html("");

		for (var i = 0; i < res.results.length; i++) {

			status_text = ""

			switch (res.results[i].status) {
			    case "1":
			        status_text = "尚未付款";
			        break;
			    case "2":
			        status_text = "已付款";
			        break;
			    case "3":
			        status_text = "送货中";
			        break;
			    case "4":
			        status_text = "完成";
			        break;
			}


			$("#view").append(

  '<tr>'+
    '<td>' + res.results[i].id + '</td>'+
    '<td>' + status_text + '</td>'+
    '<td><img class="img-responsive" style="max-height:60px;" src="' + res.results[i].product.image + '"></td>'+
    '<td>' + res.results[i].product.model + '</td>'+
    '<td>' + res.results[i].price + '</td>'+
    '<td>' + res.results[i].quantity + '</td>'+
    '<td>' + (res.results[i].price * res.results[i].quantity) + '</td>'+
    '<td>' + res.results[i].address.delivery_address + ' --- ' + res.results[i].address.contact_person + ' --- ' + res.results[i].address.contact_mobile_phone + '</td>'+		
  '</tr>'


				);    	

			$(".gotoDetails").click(function(){
				console.log($(this).attr("value"));
				window.location.href = "userorder_detail.html?id=" + $(this).attr("value");
			});	

		};



    	return 0;


    	cart = res.results[0].cart
		cart = JSON.parse(cart);
    	console.log(cart);


		$("#view").html("");

		for (i in cart) {

			$("#view").append(
		      '<tr>'+
		        '<td><img class="img-responsive" style="max-height:60px;" src="http://127.0.0.1:8001/media/' + cart[i].image + '"></td>'+
		        '<td>' + cart[i].model + '</td>'+
		        '<td>' + cart[i].price + '</td>'+
		        '<td>' + cart[i].quantity + '</td>'+
		        '<td>' + (cart[i].price * cart[i].quantity) + '</td>'+
		        '<th class="gotoDetails" value=""><button>删除</button></th>'+
		      '</tr>'
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



			$(".gotoDetails").click(function(){
				console.log($(this).attr("value"));
				// window.location.href = "useraddress_details.html?id=" + $(this).attr("value");
			});	





