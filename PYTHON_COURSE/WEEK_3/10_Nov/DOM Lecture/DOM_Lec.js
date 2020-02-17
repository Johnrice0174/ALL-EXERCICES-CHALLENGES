// document.createElement("ul");

// var listElements = document.createElement("li");

// document.querySelectorAll("li").innerHTML = "Hellloooo";

// document.querySelectorAll("li").style.background = "lightblue";

// var body = document.querySelector("body");
// var list = document.createElement("ul");

// var pets = ["cat", "rabbit", "horse"];

// for (pet of pets){
// 	let list_item = document.createElement("li");
// 	list_item.innerText = pet;
// 	list.appendChild(list_item);
// } 

// body.appendChild(list); /*in the case you can put this line wherever
							/*you want*/

// var button = document.querySelector("button");

// var list = prompt("Please add a new element to your list");

// if (list != null) {
//   document.querySelector("ol").innerHTML = list;
// }

document.querySelector("h1").classList.add("lightblue", "yellowback");

var list = document.querySelector("ol");
var button = document.querySelector("button");
var input = document.querySelector("input");

button.addEventListener("click", addListItem);
								//addListItem is an anonymous func.
function addListItem(){
	let text = input.value;

	if(text == ""){
		return;
	}

	let list_item = document.createElement("li");
	list_item.innerText = text;
	list.appendChild(list_item);
	input.value = ""; //pour clear la barre d'input apres avoir validé
}

//WE CAN ALSO MAKE LIKE THAT :

button.addEventListener("click", function(){
	let text = input.value;

	if(text == ""){
		return;
	}

	let list_item = document.createElement("li");
	list_item.innerText = text;
	list.appendChild(list_item);
	input.value = "";
})