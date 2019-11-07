/*
Une fonction qui ne RETURN rien, est UNDEFINNED.
Si on ne met pas RETURN, Lorsque l'on appellera la fonction plus tard cela ne donnera pas la reponse espérée
VOIR :
*/
var name = "Adrian";
function namechange() {
	name = "John";
	console.log("My name is " + name);
	return name;
}

console.log("My name is " + name + " but my second name is " + namechange());


/* Others Fuctions */
function sing() {
	console.log("Laisse moi mettre mon gilet jaune!");
	console.log("YEAH YEAH YEAH YEAH");
	console.log("Laisse moi mettre mon gilet jaune!");
	console.log("YEAH YEAH YEAH YEAH");
}
sing();

function sing2(){
	console.log("Et c'truc là c'est plus qu'un gilet!");
	console.log("J'le mets pour défendre mes idées");
	console.log("Laisse moi mettre mon gilet jaune!");
	console.log("YEAH YEAH YEAH YEAH");
}
sing2();

// !!! CI DESSUS EST FONCTIONNEL MAIS REPETITIF !!! //

function sing(song) {
	console.log(song);
}
	sing("Laisse moi mettre mon gilet jaune!");
	sing("YEAH YEAH YEAH YEAH");
	sing("Laisse moi mettre mon gilet jaune!");
	sing("YEAH YEAH YEAH YEAH");
	sing("Et c'truc là c'est plus qu'un gilet!");
	sing("J'le mets pour défendre mes idées");
	sing("Laisse moi mettre mon gilet jaune!");
	sing("YEAH YEAH YEAH YEAH");


	function multiply(a, b){
		console.log(a, b); //verif si ça marche, affiche la fonction mais pas la valeur resultante//
		return a * b; // return Solution à undefined! Return affiche le resultat//
		return a + b; //Ce Return Ne sera pas lu car sela sort de la fonction. 1 SEUL return par fonction SAUF AVEC DES CONDITIONS //
	}
	multiply(5, 10);

	function multiplication(a, b){
		if (a > 10 || b > 10){
			return "that's too hard";
		} else {
			return a*b;
		}
		return a*b;
	}
	multiplication(5, 10);


function mult(a, b) {
	return a*b;
}

var total = mult(4, 5);
alert(total);

parameters
arguments