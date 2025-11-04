function validateInput (number, positiveCallback, negativeCallback){
    if (number > 0){
        positiveCallback(number);
    }
    else{
        negativeCallback(number);
    };
};

validateInput(8,(number)=>{console.log("Valid number: "+number)},(number)=>{console.log("Invalid number: "+number)});
validateInput(0,(number)=>{console.log("Valid number: "+number)},(number)=>{console.log("Invalid number: "+number)});
validateInput(-8,(number)=>{console.log("Valid number: "+number)},(number)=>{console.log("Invalid number: "+number)});