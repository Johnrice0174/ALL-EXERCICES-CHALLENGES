// EX 1 //

var family = {
	father: "Abdallah ibn Adam",
	mother: "Jamila bint Musa",
	firstChild: "Ismail ibn Abdallah",
	secondChild: "Yasmin bint Abdallah",
	pet: "Tarik the Cat",
}
 for (i in family) { //afficher propriétés //
 	console.log(i);
 }

 for (x in family) { //afficher les valeurs //
 	console.log(family[x]);
 }

 // EX 2 //

 var building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent:  {
        "Sarah": [3, 2000],
        "Dan":  [4, 1000],
        "David": [1, 10],
    },
}

// console.log(building.number_levels);

// var sum = building.number_of_apt_by_level["1"] + building.number_of_apt_by_level["3"];
// console.log("Number of flats in the first level is " + building.number_of_apt_by_level["1"] + " Number of flats in the third level is " + building.number_of_apt_by_level["3"] + "Sum of flats in these 2 levels is " + sum);

// console.log("The name of the second tenant is " + building.name_of_tenants[1] + " and he has " + building.number_of_rooms_and_rent["Dan"][0] + " rooms");

var sumRentSD = building.number_of_rooms_and_rent["Sarah"][1] + building.number_of_rooms_and_rent["David"][1];
var danRent = building.number_of_rooms_and_rent["Dan"][1];
if (sumRentSD > danRent){
	var newRent = parseInt(prompt("You have to increase the rent of Dan: " ));
	danRent = newRent;
}
else 
	console.log("nothing to report")


// EXERCICE 3 //

var myGroceries = ["banana", "apple", "orange"]; 

var prices = {    
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
}

function myBill() {
	for (){
		if(myGroceries[] === prices[]){
		var bill = myGroceries[] + prices[];
		console.log("You have paid for your groceries " + bill + "$");
		}
	}
}
myBill();

// EXERCICE 4 //

var firstProfil = {
	name : "Suzanne",
	mass : 45,
	height : 165,
	bmi : function(mass, height){
		return mass / height **2;
	}
}

var secondProfil = {
	name : "Elyas",
	mass : 60,
	height : 185,
	bmi : function(mass, height){
		return mass / height **2;}
}

// console.log(firstProfil.bmi(firstProfil.mass, firstProfil.height));

function compare(a,b){
	if (a.bmi === b.bmi){
		console.log("The BMI of the both of them is the same ");
	}
	else if (a.bmi < b.bmi) {
		console.log(a.name + " has the lower BMI");
	}
	else{
		console.log(b.name + " has the biggest BMI");
	}
}
console.log(compare(firstProfil,secondProfil));