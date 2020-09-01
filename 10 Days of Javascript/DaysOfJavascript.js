//Day 0: Hello, World!--------------------------------------------------------------------

function greeting(parameterVariable) {
    // This line prints 'Hello, World!' to the console:
    console.log('Hello, World!');

    // Write a line of code that prints parameterVariable to stdout using console.log:
    console.log(parameterVariable)
}

//Day 0: Data Types-------------------------------------------------------------------------

function performOperation(secondInteger, secondDecimal, secondString) {
    // Declare a variable named 'firstInteger' and initialize with integer value 4.
    const firstInteger = 4;

    // Declare a variable named 'firstDecimal' and initialize with floating-point value 4.0.
    const firstDecimal = 4.0;

    // Declare a variable named 'firstString' and initialize with the string "HackerRank".
    const firstString = 'HackerRank ';

    // Write code that uses console.log to print the sum of the 'firstInteger' and 'secondInteger' (converted to a Number        type) on a new line.
    console.log(firstInteger + Number(secondInteger))

    // Write code that uses console.log to print the sum of 'firstDecimal' and 'secondDecimal' (converted to a Number            type) on a new line.
    console.log(firstDecimal + Number(secondDecimal))

    // Write code that uses console.log to print the concatenation of 'firstString' and 'secondString' on a new line. The        variable 'firstString' must be printed first.
    console.log(firstString.concat(secondString))
}

//Day 1: Arithmetic Operators------------------------------------------------------------------

function getArea(length, width) {
    let area;
    area = length * width
    return area;
}

/**
*   Calculate the perimeter of a rectangle.
*
*	length: The length of the rectangle.
*   width: The width of the rectangle.
*
*	Return a number denoting the perimeter of a rectangle.
**/
function getPerimeter(length, width) {
    let perimeter;
    perimeter = (length + width)*2
    return perimeter;
}

//Day 2: Loops--------------------------------------------------------------------------------------

function vowelsAndConsonants(s) {
    for (let i = 0; i < s.length; i++){
        if("aeiou".includes(s[i])){
            console.log(s[i])
        }
    }
    for (let i = 0; i < s.length; i++){
        if(!"aeiou".includes(s[i])){
            console.log(s[i])
        }
    }
}

//Day 7: Regular Expressions I

