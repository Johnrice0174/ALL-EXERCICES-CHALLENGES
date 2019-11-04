// var array = [" Banana", " Apples", " Oranges", " Blueberries"];

window.onload = function color(){
    document.getElementById('title').style.color = 'red';
};
document.querySelector('h1').textContent = 'DAILY CHALLENGE 04 Nov';

// // document.write(array).innerText = array;

// array.splice(0, 1);

// // document.write(array).innerText = array;

// array.sort();

// array.push(" Kiwi");

// // document.write(array).innerText = array;

// array.splice(0, 1);

// array.reverse();

// document.write(array).innerText = array;


 // DAILY CHALLENGE ! ACCESS TO ORANGE //
var array2 = [" Banana", [" Apples", [" Oranges"], " Blueberries"]];

var array3 = array2[1];

var array4 = array3[1];


document.write(array3[1]).innerText = array3[1];
