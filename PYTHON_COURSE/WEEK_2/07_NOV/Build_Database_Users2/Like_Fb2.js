var database = [
	{
		username: "johnrice",
		password: "nlbp007",
	},
	{
		username: "user2",
		password: "2a",
	},
	{
		username: "user3",
		password: "3a",
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
	},
	{
		username: "Simon",
		timeline: "je vous conseille de regarder les vidéos du cours!"
	}
];


function signIn(username, password){
	if (username === database[0].username && password === database[1].password) {
		console.log(newsFeed);
	}
	else {
		alert("Sorry, wrong username or/and password")
	}
}


var userNamePrompt = prompt("What\'s your username?");
var passwordPrompt = prompt("What\'s your password?");

signIn(userNamePrompt, passwordPrompt);