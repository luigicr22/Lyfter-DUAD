function getUser() {
  return fetch("https://reqres.in/api/users/2", {
          headers: { "x-api-key": "reqres-free-v1" },
        })
      .then(response => response.json())
      .then(response => {
        console.log("JSON recibido:",response.data)
        return(response)
      })
}

getUser();