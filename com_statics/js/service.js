/**
	* 完成课时
	* @example finishLesson(1);
	* @param {Number} lesson 课程
*/
function finishLesson(lesson) {
	
	alert("恭喜，你已经完成HBuilder入门课程。你可以用其它开发工具试试写这几十行代码，至少比HBuilder慢5倍！更重要的是，你很难找到这么爽的编码体验。");
}

function getToken() {
	var data = {
		"username": "admin",
		"password": "tp249hyh"
	};
	$.ajax({
			type: 'post',
			url: "http://localhost/api/token/",
			data: data,
			success: function(result) {
				console.log('s', result)
				if (!result.err && result.token) {
					console.log('token:', result.token);
					$("#token").text(result.token);
					localStorage.token = result.token;
				}else{
					console.log('err:', result)
				}
			},
			error: function(result) {
				console.log('e', result)
			},
			complete: function(result) {
				console.log('c', result)
			}
	});
}

function checkToken(token) {
	token = token ? token : $('#token').text();
	token = token ? token : localStorage.token;
	var data = {
		"token": token
	}
	$.ajax({
			type: 'post',
			url: "http://localhost/api/token-verify/",
			data: data,
			success: function(result) {
				console.log(result)
				if (!result.err && result.token) {
					console.log('token:', result.token);
					$("#checkToken").text(result.token);
				}else{
					console.log('err:', result)
				}
			},
			error: function(result) {
				console.log(result)
			},
			complete: function(result) {
				console.log('c', result)
			}
	});
}

function refreshToken(token) {
	token = token ? token : $('#token').text();
	token = token ? token : localStorage.token;
	var data = {
		"token": token
	}
	$.ajax({
			type: 'post',
			url: "http://localhost/api/token-refresh/",
			data: data,
			success: function(result) {
				console.log('s', result)
				if (!result.err && result.token) {
					console.log('token:', result.token);
					$('#refreshToken').text(result.token);
					localStorage.token = result.token;
				}else{
					console.log('err:', result)
				}
			},
			error: function(result) {
				console.log('e', result)
			},
			complete: function(result) {
				console.log('c', result)
			}
	});
}

function getData(){
    $.ajax({
        headers:{
            'Authorization':'JWT '+localStorage.token  //注意：jwt后面有个空格
        },
        type:"get",
        url:"http://localhost/api/rest_learn/",
        success:function(result){
           console.log(result);
//         $('#refreshToken').text(result);
        }
    })
}