#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const wedgeAntillesId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body).results;
    const movieCount = movies.reduce((count, movie) => {
      const characters = movie.characters;
      const isWedgeAntillesPresent = characters.some(url => url.includes(`${wedgeAntillesId}/`));
      return isWedgeAntillesPresent ? count + 1 : count;
    }, 0);
    console.log(movieCount);
  }
});
