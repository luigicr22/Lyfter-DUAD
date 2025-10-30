function printSecretMessage (stringrepeated){
    let secretMessage = "";
    for (string of stringrepeated){
        secretMessage = secretMessage.concat(string, " ");
    }
    console.log (secretMessage);
};

function checkRepeated (file1, file2, callbackFunction3){
    file1 = file1.split("\r\n");
    file2 = file2.split("\r\n");
    let stringsRepeated = [];
    
    for (word1 of file1){
        for (word2 of file2){
            if(word1 == word2){
                stringsRepeated.push(word1);
                break;
            }
        };
    };
    callbackFunction3(stringsRepeated);
};

function readFile2(file1, path, callbackFunction2){
    const fs = require('fs');
    fs.readFile(path,'utf8',(err, file2) => {
        if (err) {
            console.error('Error reading file:', err);
        }
        else{
            callbackFunction2(file1, file2, printSecretMessage);
        }
    });
};

function readFile1(path, callbackFunction1){
    const fs = require('fs');
    fs.readFile(path,'utf8',(err, file1) => {
        if (err) {
            console.error('Error reading file:', err);
        }
        else{
            path = './Modulo 2/Frontend/Semana 7/Ejercicio 2/file2.txt';
            callbackFunction1(file1, path, checkRepeated);
        }
    });
};

const path= './Modulo 2/Frontend/Semana 7/Ejercicio 2/file1.txt';
readFile1(path, readFile2);