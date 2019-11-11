/* EXERCICE 1 */
var sd = document.querySelector("div");
console.log(sd);
var gd = document.getElementsByTagName("div");
console.log(gd);

var sunli = document.querySelector("ul");
console.log(sunli);
var gunli = document.getElementsByTagName("ul");
console.log(gunli);

var li2 = document.querySelector("li").nextElementSibling;
console.log(li2);
var li3 = document.getElementsByTagName("li")[1];
console.log(li3);

/* EXERCICE 2 */

document.body.querySelector("div").style.background = "lightblue";
document.body.querySelector("div").style.padding = "50px 50px 50px 50px";
document.body.querySelector("li").style.display = "none";
document.body.getElementsByTagName("li")[1].style.border = "thick solid #0000FF";

document.body.style.fontSize = "30px";

//bonus:


/* EXERCICE 3 */

let table = document.body.firstElementChild;
