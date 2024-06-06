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

    const getCharacters = () => {
      const promises = characterUrls.map((url, index) => {
        return new Promise((resolve, reject) => {
          request(url, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              const character = JSON.parse(body);
              resolve({ index, name: character.name });
            }
          });
        });
      });

      Promise.all(promises)
        .then((characters) => {
          characters.sort((a, b) => a.index - b.index);
          characters.forEach((character) => {
            console.log(character.name);
          });
        })
        .catch((error) => {
          console.log(error);
        });
    };

    if (movie.characters.length > 0) {
      getCharacters();
    }
  }
});
