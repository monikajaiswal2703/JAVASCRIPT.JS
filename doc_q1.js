// var readlineaSync=require('readline-sync')
// var n=readlineaSync.questionInt("enter first number")
// var n1=readlineaSync.questionInt("enter first number")
// if (n>n1){
//     console.log(n,"max number");
// }
// else if(n1>n){
//     console.log(n1,"max number")

// }
// else{
//     console.log("min number")
// }


var readlineaSync=require('readline-sync')
var n=readlineaSync.questionInt("enter first number")
var n1=readlineaSync.questionInt("enter first number")
var n2=readlineaSync.questionInt("enter first number")
if (n>n1 & n>n2){
    console.log(n,"max number");
}
else if(n1>n & n1>n2){
    console.log(n1,"max number");
}
else if (n2>n & n2>n1){
    console.log(n2,"max number");
}
else{
    console.log("min number")
}