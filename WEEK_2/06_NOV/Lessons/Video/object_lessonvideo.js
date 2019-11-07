// OBJECTS //


var user = {
	name: "John",
	age: 34,
	hobby: "Writting";
	isMarried: false,
	spells: ["hello", "salam", "chalom"],
	//function inside object = METHOD//
	shout: function(){
		console.log("SALLUUUUT!");
	}
}

//Ajouter un element à l'objet//

objectname.newelement = "elementname";
user.favouriteColor = "White";

// Modifier un element //

objectname.newelement = "elementmodified";
user.isMarried = true;

// LIST//

var list = [
	{
		username: "adrian",
		password: "secret"
	},
	{
		username: "lea",
		password: "123",
	}
]

// afficher message d'erreur //
console.erreur("FATAL ERROR!");

// NULL //

var emptyObj = {}; //possible ajout valeur//
var nullObj = null; //impossible dajouter une valeur//