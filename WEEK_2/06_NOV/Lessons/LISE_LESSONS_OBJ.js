var answer = prompt("what is your name?");
var person = {
	firstName : "Sarah",
	lastName : "",
	eyeColor : "green",
	favouriteFood : "Sushis"
	eat : function (){
		console.log("I love " + this.favouriteFood);
	}
}
person.eat();