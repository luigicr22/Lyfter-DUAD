async function getUser (){
    console.log("1. Enviando request");
    try{
        const response = await fetch("https://reqres.in/api/users/2", {
          headers: { "x-api-key": "reqres-free-v1" },
        });
        console.log("2. Response recibido");
        const data = await response.json();
        console.log("3. JSON recibido:", data.data);
    } catch (error){
        console.log('3. Hubo un problema:',error);
    }
}

getUser();
console.log("4. Programa terminado");