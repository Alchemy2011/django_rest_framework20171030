
var url = window.location.href;
console.log(url); 

var id = url.split("?")[1].split("=")[1];
console.log(id); 


$.ajax({
	url: "http://127.0.0.1:8001/blog/post_rud/" + id + "/",
	success: function(res){
    	console.log(res);

    	var tags = "";
		for (var j = 0; j < res.tags.length; j++) {
		    tags += (res.tags[j].name + "  ")
		}


    	$("#view").append(
	    		"编号：" + res.id + "<br>" +
	    		"标题：" + res.title + "<br>" +
	    		"类别：" + res.category.name + "<br>" +
	    		"标签：" + tags
    		);


}});
