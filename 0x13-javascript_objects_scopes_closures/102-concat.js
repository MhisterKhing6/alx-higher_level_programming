#!/usr/bin/node
fs = require('fs');
let fileread1 = " ";

fs.readFile(process.argv[2], (err, data) => {
    fileread1 += data.toString();
});

console.log(fileread1.toString());
