function isEven (){
    console.log ("The number is even!");
};

function isOdd (){
    console.log ("The number is odd!");
};

function checkNumber (number, callbackFunction1, callbackFunction2){
    if ((number % 2) == 0){
        callbackFunction1();
    }
    else {
        callbackFunction2();
    };
}

checkNumber(8, isOdd, isEven);
checkNumber(5, isOdd, isEven);