
function stringsToArray (originalString)
{
    let newArray = [];
    let startIndex = 0
    for (let index = 0; index <= originalString.length; index++){
        if (originalString.charAt(index)===" " || index == originalString.length){
            newArray.push(originalString.slice(startIndex,index));
            startIndex = index;
        }
    }
    return newArray
};

const originalString = "This is a string!";
const arrayStrings = stringsToArray(originalString);
arrayStrings.forEach(element => {console.log(element);});