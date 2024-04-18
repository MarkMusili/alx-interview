#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

function getCharacterName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}

request(url, async function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;
    for (let i = 0; i < characters.length; i++) {
      const name = await getCharacterName(characters[i]);
      console.log(name);
    }
  }
});
