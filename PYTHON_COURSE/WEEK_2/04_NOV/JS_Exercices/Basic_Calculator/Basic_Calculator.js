var num1 = parseInt(prompt("Please enter an integer:"));
var num2 = parseInt(prompt("Please enter one more:"));

var sum = num1 + num2;
var sub = num1 - num2;
var mult = num1 * num2;
var div = num1 / num2;

var answer = "The result of your numbers is: For Sum = " + sum + "; For Sub = " + sub + "; For Mult = " + mult + "; For Div = " + div;
alert(answer).innerText = answer;