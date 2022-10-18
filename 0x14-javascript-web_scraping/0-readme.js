#!/usr/bin/node

const filename = process.argv.slice(2)[0];
const fs = require('fs');

fs.readFile(filename, (err, data) => {
  if (err) throw err;
  console.log(data.toString());
});
