//we add an img logo 
// var logo = document.createElement("IMG");
// logo.setAttribute("src", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS35DvNpk4tZw1ww2a-wyeMabM3qio5k42JV9pFdxd8hKnwlJBZkQ&s");
// logo.setAttribute("width", "100");
// logo.setAttribute("height", "60");
// document.body.appendChild(logo);

//we declare our divID in a variable!
var root = document.getElementById('root');
// document.getElementsByTagName("div")[0].setAttribute("id", "root");
//we declare our Input creation in a variable
var input = document.createElement('input');

//we put the input into the div!
root.appendChild(input);

//we declare our button creation in a variable
var button1 = document.createElement('button');
//we add the text we want to be showed into the button
button1.textContent = "Add";

//we put the button into the div!
root.appendChild(button1);
//we declare the UL creation in a variable
var ul = document.createElement('ul');
//we put the button into the div!
root.appendChild(ul);


var button2 = document.createElement('button');/*in these parentheses we always put the name of the tag!
										      we dont put the name or our variable or something else!*/
button2.textContent = "Delete";//we add the text we want to be showed into the button
//we put the button into the div!
root.appendChild(button2);
//function > happen something by clicking on the button (eventListener)
button1.addEventListener("click", function(){;
	//we declare the IL creation in a variable
    var li = document.createElement('li');
    //we declare the SPAN creation in a variable
    var span = document.createElement('span');
    //we want to stock the input.value(what we type) in a span!
    span.textContent = input.value;
    //the child of li is a span!
    li.appendChild(span);
    //we declare our small button creation in a variable
    var but = document.createElement('button');/*in these parentheses we always put the name of the tag!
										      we dont put the name or our variable or something else!*/
    but.textContent = "X";//we will see a X in the small button
    //we add an ID to our small buttons
    but.setAttribute('id','but_small');
    //we add a function to our small button cause we want that happen something when we click on it!
    but.setAttribute('onclick', 'f_suppr(this)'); //"this" is pointing/designating ...
    //another child of LI is our small button
    li.appendChild(but);
    //and LI is the child of UL !!
    ul.appendChild(li);
    //we want that after clicking to ADD button, it removes/deletes what we writed in the input zone!
    input.value="";
})
//function > happen something by clicking on the button (eventListener)
//we want this button to delete all the list (li)
button2.addEventListener("click", function(){
    ul.innerHTML="";// "" = nothing !! so we want NOTHING into the UL!
})
//It will remove ONE LI, the li concerned by the small button we click on!
function f_suppr(x){
   x.parentNode.remove();
}

ul.addEventListener("click", function(donef){
	if(donef.target.tagName === "LI"){
		donef.target.classList.toggle("done");
	}
}, false);