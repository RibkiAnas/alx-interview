#!/usr/bin/node
const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);

async function getCharacterName (url) {
  const { body } = await requestPromise(url);
  const character = JSON.parse(body);
  console.log(character.name);
}

async function getCharactersOfMovie (movieId) {
  const { body } = await requestPromise(`https://swapi-api.alx-tools.com/api/films/${movieId}/`
  );
  const movie = JSON.parse(body);
  for (const characterUrl of movie.characters) {
    await getCharacterName(characterUrl);
  }
}

const movieId = process.argv[2];
getCharactersOfMovie(movieId);
