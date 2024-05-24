#!/usr/bin/node
const axios = require('axios');

async function fetchCharacter(url) {
  try {
    const response = await axios.get(url);
    return response.data.name;
  } catch (error) {
    console.error(`Error fetching character from ${url}: ${error.message}`);
    return null;
  }
}

async function starwarsCharacters(filmId) {
  try {
    const filmResponse = await axios.get(`https://swapi-api.hbtn.io/api/films/${filmId}`);
    const characters = filmResponse.data.characters;

    for (const characterUrl of characters) {
      const characterName = await fetchCharacter(characterUrl);
      if (characterName) {
        console.log(characterName);
      }
    }
  } catch (error) {
    console.error(`Error fetching Star Wars characters for film ${filmId}: ${error.message}`);
  }
}

const filmID = process.argv[2];
if (!filmID) {
  console.error("Usage: ./script.js <filmID>");
} else {
  starwarsCharacters(filmID);
}
