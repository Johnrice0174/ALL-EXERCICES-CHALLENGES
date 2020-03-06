document.getElementsByClassName('navelem');
document.getElementById('nav');
document.getElementsByTagName('p');

document.
//------------------------------------

document.querySelector("p");
document.querySelector(".parag");
// querySelector render only THE FIRST ELEMENT
// so make for all :
document.querySelectorAll('p');
// Select CHILDRENS or B element comming after A element
document.querySelectorAll('h1 + p');
document.querySelectorAll('body > div');
document.querySelector('p:first-child');
//----
var btn = document.querySelector(".btn");
console.log(btn);

//---------
btn.textContent = "Click Me";
btn.innerHTML = "<b>Click Me</b>";
// GET Attribute
var link = document.getElementsByTagName('a');
console.log(link);

link.getAttribute('href');
// SET Attribute
link.setAttribute('href','https://duckduckgo.com/');
// CSS
link.style.size = "2em";
// ADD/REMOVE class
link.classList.add('one');
link.classList.remove('one');
link.classList.toggle('one'); //on = add _ off = remove! use with button is good
