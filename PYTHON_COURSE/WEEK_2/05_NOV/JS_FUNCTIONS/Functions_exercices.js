// EXERCICE 1 //

// var me = 20;
// function nrj(mum, dad){
//       var mum = me * 2;
//       var dad = mum * 1.2;
//     return mum;
// }
// function fun(mum, dad){
//       var mum = me * 2;
//       var dad = mum * 1.2;
//     return dad;
// }
// console.log("Ma mère a " + nrj() + " et mon père a " + fun());

// EXERCICE 2 //
//1//

function hotel_cost(nights, price){

	while (true){
		nights = parseInt(prompt("How many nights you stay?"));
		if (nights === "" || nights < 0){
			nights = parseInt(prompt("How many nights you stay?"));
		}
		else if (nights === 0){
			alert("Why searching for price if you don't come at all?!-_-");
			break;
		}
		else if (nights > 0){
			var price = nights * 140;
			alert("It will cost you " + price + "$");
			break;
		}
    }
}

// hotel_cost();

//2//

function plane_ride_cost(city, price){

	while (true){
		city = prompt("Where would you like to flight?");
		if (city === "" || city <= 0 || city > 0){
 			city = prompt("Where would you like to flight?");
 		}
		else if (city === "London" || city === "london" || city === "londres" || city === "Londres"){
			var price = "It will cost you 183$";
			return alert(price);
			break;
		}
		else if (city === "Paris" || city === "paris"){
			var price = "It will cost you 220$";
			return alert(price);
			break;
		}
		else {
			var price = "It will cost you 300$";
			return alert(price);
			break;
		}
	}
}
plane_ride_cost();

// plane_ride_cost();

//3//

function rentral_car_cost(rent, price){

	while (true){
		rent = parseInt(prompt("How many days you need the car?"));
		if (rent === "" || rent < 0){
			rent = parseInt(prompt("How many days you need the car?"));
		}
		else if (rent === 0){
			alert("Why searching for price if you don't come at all?!-_-");
			break;
		}
		else if (rent >=3 && rent < 7){
			var price = (rent * 40) - 20;
			alert("You get 20$ discount! It will cost you " + price + "$");
			break;
		}
		else if (rent >= 7){
			var price = (rent * 40) - 50;
			alert("You get 50$ discount! It will cost you " + price + "$");
			break;
		}
		else if (rent === 1 || rent === 2){
			var price = rent * 40;
			alert("It will cost you " + price + "$");
			break;
		}
    }
}

rentral_car_cost();

//4//

function trip_cost(night, city, rent, totalCost){
	var totalCost = hotel_cost() + plane_ride_cost() + rentral_car_cost();

	return alert("The plane tickets cost: " + plane_ride_cost() + ",$ The car rent cost: " + rentral_car_cost() + ",$ The hotel cost: " + hotel_cost() + "$");
}
	alert("The plane tickets cost: " + plane_ride_cost() + ",$ The car rent cost: " + rentral_car_cost() + ",$ The hotel cost: " + hotel_cost() + "$");

trip_cost();