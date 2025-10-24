function countWords (string){
    const counter = {};
    string = string.replaceAll(/[.,;:]/g,"");
    string = string.toLowerCase();
    const listWords = string.split(" ");
    for (const word of listWords){
        if (counter[word] == undefined){
            counter[word] = 1;
        }
        else{
            counter[word] += 1;
        }
    }
    return counter
}

const originalString = "This is a test. This test is simple.";
const counterWords = countWords(originalString);
console.log (counterWords);