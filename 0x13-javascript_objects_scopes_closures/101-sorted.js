#!/usr/bin/node
const dict = require('./101-data').dict;
const newdict = {};
for (const value of Object.values(dict)) {
  const ls = [];
  for (const key of Object.keys(dict)) {
    if (value === dict[key]) {
      ls.push(key.toString());
    }
  }
  newdict[value.toString()] = ls;
}
console.log(dict);
console.log(newdict);
