function getPokemon(idPokemon) {
  return fetch(`https://pokeapi.co/api/v2/pokemon/${idPokemon}`)
    .then(response => {
      if (response.status === 404) {
        throw new Error("Pokémon no encontrado");
      }
      return response.json();
    })
    .then(pokemon => {return pokemon.forms[0].name})
    .catch(error => {
      console.error("Hubo un problema:", error.message);
    });
}

Promise.any([getPokemon(4), getPokemon(7), getPokemon(10)])
  .then(resultados => console.log(resultados));