document.querySelector("h1").style.color = "magenta";
document.body.style.backgroundColor = "#ccccff";

// 1. Find and store the element we want to listen to events on.
var clickerButton = document.getElementById("clicker");
// 2. Define the function that will respond to the event.
//callback func.
var onButtonClick = function() {
	clickerButton.textContent = "Yeees Mooore:3";
};
// 3. Add the event listener for the element and function
// or anonymous func "inline"
    clickerButton.addEventListener("click", onButtonClick);

var effectwo = function(){
	clickerButton.style.backgroundColor = "red";
}
var effecthree = function(){
	clickerButton.style.backgroundColor = "orange";
}
var effecfour = function(){
	clickerButton.style.backgroundColor = "yellow";
}
// function setInterval1() {
//   setInterval(function(){ effectwo(); }, 3000);
// }
clickerButton.addEventListener("click", effectwo);
clickerButton.addEventListener("click", setInterval(function(){ effecthree(); }, 2000));
clickerButton.addEventListener("click", setInterval(function(){ effecfour(); }, 4000));

