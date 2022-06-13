// console.log(Math.floor((Math.random() * 10) + 1));

"Return a random number between 1 and 100"
// console.log(Math.floor((Math.random() * 100) + 1));

// var readlineSync = require('readline-sync');
// var userName = readlineSync.question('May I have your name? ');
// console.log('Hi ',userName,'!');
// var favFood = readlineSync.question('What is your favorite food? ')
// //   hideEchoBack: true // The typed text on screen is hidden by `*` (default).
// // });
// console.log('Oh, ' + userName + ' loves ' + favFood + '!');
var readlineSync = require('readline-sync');
if (readlineSync.keyInYN('Do you want this module?')) {
  // 'Y' key was pressed.
  console.log('Installing now...');
  // Do something...
} else {
  // Another key was pressed.
  console.log('Searching another...');
  // Do something...
}