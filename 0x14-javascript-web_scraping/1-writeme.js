#!/usr/bin/node
const fs = require('s');
const fileName = process.argv[2];
const fileContent = process.argv[3];

fs.writeFile(fileName, content, 'utf-8', (err) => {
    if (err) {
        console.log(err);
    }
});
