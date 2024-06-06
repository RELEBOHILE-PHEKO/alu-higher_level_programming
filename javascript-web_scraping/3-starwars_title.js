#!/usr/bin/node
const request = require('request');

const episodeId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${episodeId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
