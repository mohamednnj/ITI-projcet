 // login from action
 const modal = document.getElementById("loginModal");
 const btn = document.getElementById("btn-login");
 const closeBtn = document.getElementsByClassName("close")[0];
 
 var messageElement = document.getElementById('message');
//  var messageElement2 = document.getElementById('messagee');
 var messageExists = messageElement !== null;
 
 console.log(messageExists); 
 
 if (messageExists){
     modal.style.display = "block";
 }
 btn.onclick = function() {
     modal.style.display = "block";
 }
 
 closeBtn.onclick = function() {
     modal.style.display = "none";
 }
 