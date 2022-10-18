#!/usr/bin/node

const filename = process.argv.slice(2)[0];
const chaine = process.argv.slice(2)[1];
const fs = require('fs');

fs.writeFile(filename, chaine, (err) => {
  if (err) {
    console.log(err);
  }
});
