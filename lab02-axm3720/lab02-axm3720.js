//Aditya Mishra
//1001663720
//07/03/2022

//Q1.
var inputtable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; 
//array has a number between 1 and 10.

console.log("Q1. = \n", inputtable, "\n"); //print the array

//*********************************************************************//

//Q2a.
var fiveTable; //Set of multiples of 5 between 1 and 51

//function for multiples of five
function multiple_of_five(num) 
{
    return num * 5;
}

//Assigning the value 
//using function to find the multiples of 5
fiveTable = inputtable.map(multiple_of_five); 

//b.
var thirteenTable; //Set of multiples of 13 between 1 and 131

//function for multiples of 13
function multiple_of_thirteen(num) 
{
    return num * 13;
} 

//Assigning the value 
//using function to find the multiples of 13
thirteenTable = inputtable.map(multiple_of_thirteen);

//c.
var squaresTable; // Set of squares of the numbers in inputtable

//function to get array of square of values
function square(num)
{
    return num * num;
}

//Assigning the value 
//using function to find the square of numbers from inputtable
squaresTable = inputtable.map(square);


//printing Q2. a, b and c for multiples of 5, multiples of 13 and square /
//of number between one and ten

console.log("Q2a. = ", fiveTable); 
console.log("Q2b. = ", thirteenTable);
console.log("Q2c. = ", squaresTable , "\n");

//*****************************************************************************//

//Q3
//Array of numbers between one and hundred
var hundred = [1, 2, 3, 4, 5, 6, 7, 8, 9,
    10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
    30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
    40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
    50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
    60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
    70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
    80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
    90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
    100]; 

//variable for Q3
var oddMultiple;

//function to find if the value is multiple of 5.
function multiple_of_five_odd(num) 
{
    if (num % 5 == 0) // using if to detemine if the num is divisible by 5
    {
        if (num % 2 == 1) // using if to determine if it is odd
        {
            return num;
        }
    }
}

oddMultiple = hundred.filter(multiple_of_five_odd); // using filter to pass only the values that satisfy the condition
console.log("Q3 = \n", oddMultiple, "\n");

//*****************************************************************************//


//variable for Q4
var evenMultiple;

function multiple_of_seven_even(num) 
{
    if (num % 7 == 0) //using if to detemine if the num is divisible by 7
    {
        if (num % 2 == 0) // using if to determine if it is even
        {
            return num;
        }
    }
}

evenMultiple = hundred.filter(multiple_of_seven_even);

var sumMultipleEven; //variable to store reduce function output

function sum(total, num) 
{
    return num + total;
}

sumMultipleEven = evenMultiple.reduce(sum); //passing function as a parameter to another function

console.log("Q4. = \n", "Sum of even multiples of 7 = ", sumMultipleEven, "\n" );

//*****************************************************************************//
//Q5
//variable to store the volume of a cylinder
var vol;

//function provided by the professor
function cylinder_volume(r, h){ 
    var volume = 0.0; 
    volume = 3.14 * r * r * h; // formula for cylinder volume
    return volume; 
} 

// volumne of a cylinder with radius: r = 5 and height: h = 10
vol = cylinder_volume(5, 10); 
console.log("Q5a. = ", vol, "\n");

// volumne of a cylinder with radius: r = 5 and height: h = 10
vol = cylinder_volume(5, 17); 
console.log("Q5b. = ", vol, "\n");

// volumne of a cylinder with radius: r = 5 and height: h = 10
vol = cylinder_volume(5, 11); 
console.log("Q5c. = ", vol, "\n");

//*****************************************************************************//
//Q6
console.log("Q6 = \n"); 

//function provdided by the professor.
makeTag = function (beginTag, endTag) 
{
    return function (textcontent) 
    {
        return beginTag + textcontent + endTag;
    }
}

table = makeTag("<table>\n", "</table>"); //title of table
row = makeTag("<tr>\n", "</tr>\n");//defining row of cells in a row
info = makeTag("<td>", "</td>\n"); //info or data stored in the table row

//data stored in table row
firstRow = row("Living Being \n" + "Kingdom\n" + "Lifespan\n");

//features of the contents stored in table
firstInfo = info("Cow") + info("Animalia") + info("15-20 yrs");
secondRow = row(firstInfo); // pusing the info into the second row of the data

secondInfo = info("Tortoise") + info("Animalia") + info("150 yrs");
thirdRow = row(secondInfo); //pusing the info into the third row of the data

tableInfo = table(firstRow + secondRow + thirdRow);//adding all the row 
console.log(tableInfo, "\n"); //printing the info provided in the table

//*****************************************************************************//

