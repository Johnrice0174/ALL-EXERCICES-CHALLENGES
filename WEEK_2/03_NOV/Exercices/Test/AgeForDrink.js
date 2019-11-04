var age = parseInt(prompt("How old are you?"));
var country = prompt("Enter country");

if (country == "USA" && age >= 21){
	alert("Here is a beer");
}
else if (country != "USA" && age >= 18){
	alert("Here is a beer");
}
else {
	alert("Here is a soda");
}


// if (age <= 18 && country != "USA" || (age >= 21 && country == "USA") ){
// 	alert("");
// }

//Ask the user for 2 numbers. Alert the bigger one.

var num1 = parseInt(prompt("Enter an Integer:"));
var num2 = parseInt(prompt("Enter an other Integer:"));

if (num1 > num2) {
	alert("the bigger number is " +num1);
}
else if (num2 > num1) {
	alert("the bigger number is " +num2);
}

var x = 1;
console.log(x);
silly();
console.log(x);

function silly(){
	x =5;
	console.log(x);
}