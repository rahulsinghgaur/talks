$(document).ready(function(){
	$('#action_menu_btn').click(function(){
		$('.action_menu').toggle();
	});
		});


const r = '<div class="d-flex justify-content-start mb-4">'+'<div class="img_cont_msg">'+'<img src="/static/profile.png" class="rounded-circle user_img_msg"></div>'+'<div class="msg_cotainer">'+'{msg}'+'<span class="msg_time">8:40 AM, Today</span>'+'</div></div>'

const s = '<div class="d-flex justify-content-end mb-4">'+'<div class="msg_cotainer_send">'+'{msg}'+'<span class="msg_time_send">8:55 AM, Today</span></div>'+'<div class="img_cont_msg">'+'<img src="/static/profile.png" class="rounded-circle user_img_msg"></div></div>'
var tym=0;
var pdata =0;
var receiver;
function chatclicked(p) {
	if(tym>0){
		receiver =null;
		pdata=0
		clearInterval(tym)
		$('#chatbox').empty();
	}
	receiver = p;
	var e = document.getElementsByClassName("isactive");
	for(var i = 0;i<e.length;i++){
		if(e[i].classList.contains("active")){
			e[i].classList.remove("active")
		}
	}
	var element = document.getElementsByClassName(p);
	element[0].classList.add("active");


	document.getElementsByClassName("chatname")[0].innerHTML="Chat with "+p;
	document.getElementsByClassName("online_status")[0].innerHTML="Online";
	tym =setInterval(function () {
		receive(sender,p)
	},1000)
	
}



function receive(sender,receiver) {
	var arr = [sender,receiver]
	arr = arr.sort();
	$.get('/msg/' + arr[0] + ':' + arr[1], function (data) {
			if(pdata<data.length){
				pdata=data.length
				$('#chatbox').empty();
			if (data.length !== 0) {
				for (var i = 0; i < data.length; i++) {
					if (data[i].sender===sender){
						var box = s.replace('{msg}',data[i].message);
						$('#chatbox').append(box);
						var objDiv = document.getElementById("chatbox")
						objDiv.scrollTop = objDiv.scrollHeight;
						}else{
							var box = r.replace('{msg}',data[i].message)
							$('#chatbox').append(box);
							var objDiv = document.getElementById("chatbox")
							objDiv.scrollTop = objDiv.scrollHeight;
						}

			}
		}}
	})
}
function checkEnter(){
	var message = document.getElementById("txt");
	message.addEventListener("keyup", function(event) {
		if (event.keyCode === 13) {
		 	event.preventDefault();
			send()
		}
	  })
}

function send() {
	var message = document.getElementById("txt").value;
	var arr = [sender,receiver]
	arr = arr.sort();
	dic = JSON.stringify({
		"key":arr[0]+":"+arr[1],
    	'sender':sender,
		'receiver':receiver,
    	'message':message,
    	'timestamp':"20:14:10"
	})
	$.post('/msg/',dic, function (data) {

    })
	document.getElementById("txt").value="";
   
}


