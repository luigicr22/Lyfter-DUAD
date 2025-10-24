function notRepeated (listNumbers) {
    const listNotRepeated = [];
    for (const number of listNumbers){
        let repeated = false;
        for(index = 0; index < listNotRepeated.length; index++){
            if (number == listNotRepeated[index]){
                repeated = true;
                break;
            }
        };
        if (repeated == false){
            listNotRepeated.push(number);
        };
    };
    return listNotRepeated;
}

console.log(notRepeated([1,2,3,2,4,1,5]));
