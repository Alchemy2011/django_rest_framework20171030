
var url = window.location.href;

var category = url.split("?")[1].split("=")[1];
console.log(category); 

switch(category) {
    case "1":
        $("#title").html("笔记本");
        break;
    case "2":
        $("#title").html("平板电脑");
        break;
    case "3":
        $("#title").html("一体机");
        break;
    case "4":
        $("#title").html("台式机");
        break;
    case "5":
        $("#title").html("服务器");
        break;                        
    default:
        $("#title").html("产品分类");
}


var global_prev = "";
var global_next = "";


$.ajax({
	url: "http://127.0.0.1:8001/computer/product_list_by_category/?ordering=-sold&category="+category, 
	success: function(res){
    	console.log(res);

        if (res.next != null){
            console.log("还有数据");
            global_next = res.next;
        }else{
            console.log("没有啦");
            global_next = "";           
        }

        if (res.previous != null){
            console.log("还有数据");
            global_prev = res.previous;
        }else{
            console.log("没有啦");
            global_prev = "";           
        }

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







$("#prev").click(function(){

    $.ajax({
        url: global_prev, 
        success: function(res){
            console.log(res);

            console.log("hey2:"+global_prev.split("page=")[1]);            
            $("#page_no").html((global_prev.split("page=")[1])?(global_prev.split("page=")[1]):"1");

            if (res.previous != null){
                console.log("还有数据");
                global_prev = res.previous;
            }else{
                console.log("没有啦");
                global_prev = "";           
            }

            if (res.next != null){
                console.log("还有数据");
                global_next = res.next;
            }else{
                console.log("没有啦");
                global_next = "";           
            }

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

});




$("#next").click(function(){

    $.ajax({
        url: global_next, 
        success: function(res){
            console.log(res);

            $("#page_no").html(global_next.split("page=")[1]);

            if (res.previous != null){
                console.log("还有数据");
                global_prev = res.previous;
            }else{
                console.log("没有啦");
                global_prev = "";           
            }

            if (res.next != null){
                console.log("还有数据");
                global_next = res.next;
            }else{
                console.log("没有啦");
                global_next = "";           
            }

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

});







$(".manufacturer").click(function(){
    console.log($(this).attr("value"));

    $.ajax({
        url: "http://127.0.0.1:8001/computer/product_list_by_category_manufacturer/?ordering="+$(this).attr("ordering")+"&category="+category+"&manufacturer="+$(this).attr("value"), 
        success: function(res){
            console.log(res);
            $("#page_no").html("1");

            if (res.next != null){
                console.log("还有数据");
                global_next = res.next;
            }else{
                console.log("没有啦");
                global_next = "";           
            }

            if (res.previous != null){
                console.log("还有数据");
                global_prev = res.previous;
            }else{
                console.log("没有啦");
                global_prev = "";           
            }

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






}); 










$(".ordering").click(function(){
    console.log($(this).attr("value"));


    $.ajax({
        url: "http://127.0.0.1:8001/computer/product_list_by_category/?ordering="+$(this).attr("value")+"&category="+category, 
        success: function(res){
            console.log(res);
            $("#page_no").html("1");

            if (res.next != null){
                console.log("还有数据");
                global_next = res.next;
            }else{
                console.log("没有啦");
                global_next = "";           
            }

            if (res.previous != null){
                console.log("还有数据");
                global_prev = res.previous;
            }else{
                console.log("没有啦");
                global_prev = "";           
            }

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







}); 



