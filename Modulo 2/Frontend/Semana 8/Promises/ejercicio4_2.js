function getUser() {
  return fetch("https://reqres.in/api/users/23", {
          headers: { "x-api-key": "reqres-free-v1" },
        })
      .then(response => {
        if (response.status === 404) {
          throw ("Usuario no encontrado");
        };
        return response.json();
      }).then(response => {
        console.log("JSON recibido:",response.data)
        return (response)
      }).catch(
        error => {
        console.log('3. Hubo un problema: ',error);
  });
};

getUser();