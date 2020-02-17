/*
var str = "hey";
var str2 = "everyone";

var newStr = str + " " + str2;
//the quotation with space to make a space//
*/

/* LONG STRING :

let longString = "dawda wdkaldijaw daldadkawlk djkawldk" +
                 "dawod jaw djawo dkaopwdk aopdkawdkapwdaw" +
                 "wjdioawkjd aoj dkp aowdk aowldkao.";

//At the end of each line to indicate that the string will continue //
//on the next line. Make sure there is no space or any other character after the backslash//

let longString = "This is a very long string which needs \
to wrap across multiple lines because \
otherwise my code is unreadable.";
*/


//exercice 1//
// var adressNumber = "5,";
// var adressStreet = "I live in BenYehuda";
// var country = "in Israel";
// var global_adress = adressStreet + " " + adressNumber + " " + country;

// window.onload = function color(){
// 	document.getElementById('title').style.color = 'red';
// };
// document.querySelector('h1').textContent = 'Exercice 1';
// document.write(global_adress).innerText = global_adress;

//exercice 3//
// document.querySelector('h1').textContent = 'Exercice 3';

// var newDog = "Chihuaha";
// var length = newDog.length;

// window.onload = function color(){
// 	document.getElementById('title').style.color = 'red';
// };
// document.write(length).innerText = length;
// alert(length);

/* varname.arrondir(nombre apres la virgule);
var op = 10.6789
op.toFixed(0);           // returns 11
op.toFixed(2);           // returns 10.68
*/
/*
NaN = Not a Number !!!!!!
*/

//exercice 4 //

// var birthYear = 1999;
// var futureYear = 2050;
// var age = futureYear - birthYear;
// var result = "I will be " + age + " " + "in " + futureYear;

// window.onload = function color(){
// 	document.getElementById('title').style.color = 'red';
// };

// document.querySelector('h1').textContent = 'Exercice 4';
// document.write(result).innerText = result;

/* ARRAYS
 example[number of elements] = ["elem0", "elem1", etc...];

 var colors = ["white","green","blue"];
 colors[2];
 il y a 3 ITEMS mais on met 2 car WHITE = elem0 !!
*/

// Exercice 2 //
// var pets = ["cat", " dog", " fish", " rabbit", " cow"];

// window.onload = function color(){
//     document.getElementById('title').style.color = 'red';
// };
// document.querySelector('h1').textContent = 'Exercice 2';

// document.write(pets[1]).innerText = pets[1];

// pets.push(" horse");

// document.write(pets).innerText = pets;

// Exercice 1 conditionals //

// var num = prompt("Choose an integer: ");

// 	if (num%2 == 0){
// 		alert(num + " is an even number");
// 	}
// 	else{
// 		alert(num + " is not an even number");
// 	}

// Exercice 2 Conditionals //

// var x = prompt("Choose an integer : ");
// var y = prompt("Choose an other integer : ");

// if (x > y){
// 	alert("Your biggest number is " + x);
// }
// else if (x < y){
// 	alert("Your biggest number is " + y);
// }
// else{
// 	alert("your numbers are the same value")
// }

// Exercice 3 Conditionals //

// var language = prompt("Wich language do you speak?");

// if (language == "french" || language == "French"){
// 	alert("Bonjour!");
// }
// else if (language == "english" || language == "English"){
// 	alert("Hello");
// }
// else if (language == "hebrew" || language == "Hebrew"){
// 	alert("CHALOM");
// }
// else if (language == "arabic" || language == "Arabic"){
// 	alert("SALAM");
// }
// else {
// 	alert(":) <3")
// }

// Exercice 4 Conditionals //

var grade1 = parseInt(prompt("Please give me a grade between 0 to 100:"));
var grade2 = parseInt(prompt("a second one:"));
var grade3 = parseInt(prompt("an other:"));
var grade4 = parseInt(prompt("the fourth and last:"));
var coef = parseInt(prompt("Please give me a coefficient"));
var userGrade = [];
var userCoefficient = [];
var average;

userCoefficient.length 
userGrade.length

if (100 <= grade1 <=0 || 100 <= grade2 <=0 || 100 <= grade3 <=0 || 100 <= grade4 <=0 || ){
    alert("ُERROR! Is it so hard to give a CORRECT number ?!")
}
average = ((grade1 + grade2 + grade3 + grade4) * coef) / 4 / coef;

alert(average);

// Exercice 5 Conditionals //

    var grade = prompt('Please enter your grade (0-100)');
    switch (grade){
    case (grade > 90):
        alert('A');
        break;
    case (grade <= 90 || grade > 80):
        alert('B');
        break;
    case (grade <= 80 || grade >= 70):
        alert('C');
        break;
    case (grade < 70):
        alert('D');
        break;
    default:
        alert('I didn\'t understand');
    }