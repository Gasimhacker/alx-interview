#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(filmUrl, function (error, response, body) {
  if (error || (response.statusCode !== 200)) { return; }

  const film = JSON.parse(body);
  const characters = film.characters;

  function makeRequest (index) {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], (error, response, body) => {
      if (error || (response.statusCode !== 200)) { return; }

      const character = JSON.parse(body);
      console.log(character.name);
      makeRequest(index + 1);
    });
  }

  makeRequest(0);
});
