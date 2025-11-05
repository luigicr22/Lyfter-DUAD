async function getUser (user){
    try{
        const response = await fetch(`https://reqres.in/api/users/${user}`, {
          headers: { "x-api-key": "reqres-free-v1" },
        });
        if (response.status === 404) {
          throw "Usuario no encontrado";
        }
        const data = await response.json();
        console.log("3. JSON recibido:", data.data);
    } catch (error){
        console.log('3. Hubo un problema: ',error);
    }
}

async function getUsers () {
    await getUser(2);
    await getUser(3);
    await getUser(4);
}

getUsers();