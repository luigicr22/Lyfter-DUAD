const myArray = [1,2,3,4];
let oddArray = [];
for (const element of myArray){
    if ((element%2)===0){
        oddArray.push(element);
    }
}
console.log("Usando For");
oddArray.forEach((element)=>{console.log(element);});

console.log("Usando Filter");
const oddArray2 = myArray.filter((element)=>{return ((element % 2) === 0);});
oddArray2.forEach((element)=>{console.log(element);});