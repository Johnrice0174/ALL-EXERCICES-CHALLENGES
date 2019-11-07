// EXERCICE 1 //

// var choices = ['white', 'red', 'orange', 'yellow', 'pink', 'blue', 'green', 'beige', 'brown', 'purple'];
// for (var i = 0; i < choices.length; i++) {
//     alert('My ' + (i + 1) + ' choice is ' + choices[i]);
// }

// for (var i = 0; i < choices.length; i++) {
//     var choiceNum = i + 1;
//     var choiceNumSuffix;
//     if (choiceNum == 1) {
//         choiceNumSuffix = 'st';
//     } else if (choiceNum == 2) {
//         choiceNumSuffix = 'nd';
//     } else if (choiceNum == 3) {
//         choiceNumSuffix = 'rd';
//     } else {
//         choiceNumSuffix = 'th';
//     }
//     alert('My ' + choiceNum + choiceNumSuffix + ' choice is ' + choices[i]);
// }

// EXERCICE 2 //

// var nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'];
// for (var i = 0; i <= nums.length; i++) {
//     if (i === 0){
//         alert(i + " is even");
//     }
//     else if (i % 2 === 0) {
//         alert(i + " is even");   
//     }
//     else {
//         alert(i + " is odd");
//     }
// }

// EXERCICE 3 //

// var names = ["john", "sarah", 23, "Rudolf", 34];

// for (var i = 0; i < names.length; i++) {
//     if (typeof names[i] !== "string") {
//         continue;
//     }
//     if (names[i].charAt(0).toUpperCase() == names[i][0]) {
//         alert(names[i]);
//     }
//     else {
//         names[i] = names[i][0].toUpperCase() + names[i].substracting(1,)
//         alert(names[i]);
//     }
// }

// EXERCICE 5 //

var num = parseInt(prompt("Please choose an integer: "));

while (num < 10){
    var num = parseInt(prompt("Please choose an other integer: "));
}