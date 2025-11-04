function checkNames(nameList1, nameList2, printNames){
    for (name1 of nameList1){
        for (name2 of nameList2){
            if (name1 == name2){
                printNames(name1);
                break;
            };
        };
    };
};

const nameList1 = ['Dak Prescott', 'Javonte Williams', 'CeeDee Lamb', 'George Pickens', 'KaVontae Turpin'];
const nameList2 = ['Hunter Luepke', 'CeeDee Lamb', 'Jake Ferguson', 'KaVontae Turpin', 'Luke Schoonmaker'];

checkNames(nameList1,nameList2,(name)=>{console.log(name)});