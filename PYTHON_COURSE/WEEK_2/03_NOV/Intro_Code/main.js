// vax x = parseInt(prompt("Enter a number to square"));
// alert("The answer is " + square(x));

// function square(x){
// 	return x*x;
// }
// alert(square(x))

var name = prompt("سلام שלום  Please enter your name:");

// function square_my_number(num){ //

function my_func(){
	console.log("This is a function");
	var religion = prompt("Enter your religion:");
	alert("Your religion is " + religion)
}
my_func();

// function add(num1, num2){
// 	return num1 + num2;
// }

// alert(add(5,19))


var actualAge = parseInt(prompt("How old are you?"));
var actualYear = parseInt(prompt("What is the actual Year?"));

alert("You were born in " + (actualYear - actualAge));

function exercice(a, b, c){
	return a * b - c;
}
var a = parseInt(prompt("Enter a number:"));
var b = parseInt(prompt("Multiplied by "));
var c = parseInt(prompt("the result substracted by "));

alert("The final result is " + exercice(a, b, c));

var countries = [
	"USA",
	"Israel",
	"India",
	"England",
	"France",
	"Mexico"
]

var text = "This is some useless text";
//cela cherche à partir de la combientieme lettre le mot useless commence//
alert(text.indexOf("useless"));
//Cela affiche des lettres du texte entre X et Y lettres//
alert(text.substring(13, 20)); // = useless
alert(text.substring(13, 10)); // = me

// cela transforme les majuscules en minuscules //
var text = "THIS IS A STRING";
alert(text.toLowerCase());
// cela transforme les minuscules en majuscules //
var text = "this is a string";
alert(text.toUpperCase());


var text = "this is a string";
alert(st(text));

function cap_first(st){                       //1 a fin//
	return text[0].toUpperCase() + st.substring(1,);
}

function addHeading(text, div_id){
	document.getElementById(div_id).innerHTML = "<h1>"+text+"</h1>";
}

function changeColor(my_color, div_id){
	document.getElementById(div_id).style.color = my_color;
}