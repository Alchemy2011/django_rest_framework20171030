var unMap = [{
    type : "phone",
    noticeText : "邮箱"
},{
    type : "email",
    noticeText : "手机号"
}];


var unIndex = 0,
    unCurrentLatitude = unMap[unIndex],
    // _untypeWrap = $(".untype-wrap"),
    isIframe = self!=top;



$(".change-type").on("click",function(){
    changeType();
})

function changeType(){
    unIndex = !unIndex;
    unCurrentLatitude = unMap[unIndex ? 1 : 0];
    $(".action-item").eq(unIndex ? 0 : 1).addClass("dn");
    $(".action-item").eq(unIndex ? 1 : 0).removeClass("dn").find("input").focus();
    // _untypeWrap.removeClass("dn").eq(unIndex ? 0 : 1).addClass("dn");
    // $(".change-type").find("em").text(unCurrentLatitude.noticeText);
    loginObj.type = unCurrentLatitude.type;
    localStorage.setItem("login-email-notice",true);
}

function loginSuccess(callback) {
    var $form = $("form#hiddenForm");
    if ($form && $form.data('action')) {
        callback = $form.data('action');
        if ($form.attr('method') == 'GET') {
            location.replace(callback);
        } else {
            $form.attr('action', callback);
            $form.submit();
        }
    } else {
        location.href = callback;
    }
}

var loginObj = {
    prefix_code : "",
    type : "phone",
    value : "",
    password : "",
    callback : ""
    
}



$(".login").on("click",function(){
    formBridgeServer($(this),"/user/login",loginObj,function(data){
        if(isIframe){
            // parent.loginIframe.reload();
            window.parent.postMessage({ 
                act: 'reload'
                // msg: {
                //     answer: '我接收到啦！'
                // }
            }, '*');
        }else{
            if(data.data.need_bind){
                location.href = "/bind_phone?callback=" + data.data.callback;
            }else if(data.data.need_mobile_validate){
                location.href = "/validate_phone";
            }else if(data.data.callback) {
                loginSuccess(data.data.callback);
            }else{
                location.href = "/settings";
            } 
        }
        
    })

})


// if(){  
//    alert('在iframe中');    
// }  
// console.log(self,top) 


$(".skip-btn").on("click",function(){
    var skipUrl = $(this).data("url");
    if(isIframe){
        window.parent.postMessage({ 
            act: 'skip',
            msg: {
                url: baseHost + skipUrl
            }
        }, '*');
        // parent.loginIframe.skip(baseHost + skipUrl);
    }else{
        location.href = skipUrl;
    }
    
})

$(".social-icons span").on("click",function(){

    if($(this).data("type")){

        var thirdUrl = "/api/v1/third/login/" + $(this).data("type") + "?callback=" + $(".callback").data("value");

        if(isIframe){
            window.parent.postMessage({ 
                act: 'skip',
                msg: {
                    url: baseHost +  thirdUrl
                }
            }, '*');
            // parent.loginIframe.skip(baseHost +  thirdUrl);
        }else{
            location.href = thirdUrl;
        }
    

    }else{

        changeType();
        if($(this).hasClass("login-phone")){
            $(this).removeClass("login-phone");
        }else{
            $(this).addClass("login-phone");
        }
    }

})


if(getRequest()["from"] == "vmovier"){
    $(".vmovier-notice").removeClass("dn");
}









