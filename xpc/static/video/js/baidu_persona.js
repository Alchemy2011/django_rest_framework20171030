if (userid) {
	// 百度用户画像
	var _dxt = _dxt || [];
	_dxt.push(["_setUserId", userid]);
	(function() {        var hm = document.createElement("script");
	    hm.src = "//datax.baidu.com/x.js?si=&dm=www.xinpianchang.com";
	    var s = document.getElementsByTagName("script")[0];
	    s.parentNode.insertBefore(hm, s);
	})();
}
