// var a=Number("3.14")    // returns 3.14
// b  =     // returns 0
// c=Number("")        // returns 0
// d=String(99)   // returns NaN
// console.log(typeof b,c,typeof d)

// let y = "5";      // y is a string
// let x = + y;      // x is a number
// console.log(y)

// let y = "John";   // y is a string
// let x = + y;      // x is a number (NaN)
// console.log(x)


// var a=parseFloat("34")
// console.log(a)

// let a=parseInt(1234); console.log(typeof a,a)

// let x=123
// let a=String(x)         // returns a string from a number variable x
// let b=String(123)       // returns a string from a number literal 123
// let c=String(100 + 23)  // returns a string from a number from an expression
// console.log(a,b,c)

// console.log(x.toString())
// console.log((123).toString())
// console.log((100 + 23).toString())

"Converting Dates to Numbers"
// d = new Date();
// console.log(Number(d))         // returns 1404568027739

// d = new Date();
// console.log(d.getTime())        // returns 1404568027739

"Converting Dates to strings"
// console.log(String(Date()))  // returns "Thu Jul 17 2014 15:38:19 GMT+0200 (W. Europe Daylight Time)"


// "Converting Booleans to Strings"
// console.log(String(false))      // returns "false"
// String(true)       // returns "true"

// "Converting Booleans to number"
// console.log(Number(false))      // returns 0
// String(true)       // returns 1


"Automatic Type Conversion"
// console.log(5 + null)    // returns 5         because null is converted to 0
// console.log("5" + null)  // returns "5null"   because null is converted to "null"
// console.log("5" + 2)     // returns "52"      because 2 is converted to "2"
// console.log("5" - 2  )   // returns 3         because "5" is converted to 5
// console.log("5" * "2")   // returns 10        because "5" and "2" are converted to 5 and 2

// if myVar = {name:"Fjohn"}  // toString converts to "[object Object]"
// if myVar = [1,2,3,4]       // toString converts to "1,2,3,4"
// if myVar = new Date()      // toString converts to "Fri Jul 18 2014 09:08:55 GMT+0200"