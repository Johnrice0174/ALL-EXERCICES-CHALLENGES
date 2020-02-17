var database = [
	{
		username: "johnrice",
		password: "nlbp007",
	}
];

var newsFeed = [
	{
		username: "Hillel",
		timeline: "The exercices are so easy!"
	}
	,
	{
		username: "Fred",
		timeline: "Je suis une bille mais diplômé!"
	}
];

var userNamePrompt = prompt("What's your username?");
var passwordPrompt = prompt("What's your password?");

function signIn(user, pass){
	if (user === database[0].username && pass === database[1].password) {
		console.log(newsFeed);
	}
	else {
		alert("Sorry, wrong username or/and password")
	}
}

signIn(userNamePrompt, passwordPrompt);