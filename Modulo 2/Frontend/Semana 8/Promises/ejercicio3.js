const listStrings = ["very", "dogs", "cute", "are"];
let text= "";

function correctPhrase (string){
  text += string + ' ';
}

const promise1 = new Promise(resolve => {
    setTimeout(() => resolve(correctPhrase(listStrings[0])), 300);
  });

const promise2 = new Promise(resolve => {
    setTimeout(() => resolve(correctPhrase(listStrings[1])), 100);
  });

const promise3 = new Promise(resolve => {
    setTimeout(() => resolve(correctPhrase(listStrings[2])), 400);
  });

const promise4 = new Promise(resolve => {
    setTimeout(() => resolve(correctPhrase(listStrings[3])), 200);
  });

Promise.all([promise1, promise2, promise3, promise4]).then(()=>console.log(text));
