const celsiusArray = [0,18,25,30];

const farenheitArray = celsiusArray.map((temp)=>{
    return (temp * 9/5)+32;
})

farenheitArray.forEach((element)=>{console.log(element);})