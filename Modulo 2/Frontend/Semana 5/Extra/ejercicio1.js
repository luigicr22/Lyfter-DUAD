const invert = (string) => {
    let stringInverted = "";
    for (let number=(string.length-1); number >= 0; number--){
        stringInverted = stringInverted.concat(string[number]);
    };
    return stringInverted;
}

console.log(invert("JavaScript"));