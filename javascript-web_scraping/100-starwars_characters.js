#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    const getCharacters = (url, index) => {
      request(url, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);

          if (index < characterUrls.length - 1) {
            getCharacters(characterUrls[index + 1], index + 1);
          }
        }
      });
    };

    if (characterUrls.length > 0) {
      getCharacters(characterUrls[0], 0);
    }
  }
});
