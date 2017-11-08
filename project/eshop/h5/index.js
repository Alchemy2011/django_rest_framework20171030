

$.ajax({
	url: "http://127.0.0.1:8001/computer/product_list/?limit=9&ordering=-sold", 
	success: function(res){
    	console.log(res);

		$("#view_count").html(
	    		"总数：" + res.count + "<br>" +
	    		"<br><br>"
			);  

		$("#view").html("");

		for (var i = 0; i < res.results.length; i++) {

			var temp_tags = res.results[i].tags;

			$("#view").append(

'<div style="height:200px;" class="col-xs-4 col-sm-4 col-md-4 col-lg-4 gotoDetails" value="' + res.results[i].id + '">' +
  '<img class="img-responsive" style="max-height:160px;margin-left:auto;margin-right:auto;" src="' + res.results[i].image + '">' +
  '<div style="text-align:center;padding-left:0px;">' + res.results[i].price + '</div>' +
  '<div style="text-align:center;padding-left:0px;">' + res.results[i].model + '</div>' +
'</div>'

				);    	

			$(".gotoDetails").click(function(){
				console.log($(this).attr("value"));
				window.location.href = "product_details.html?id=" + $(this).attr("value");
			});	

		};

}});






