#!/usr/bin/node
import { argv } from 'node:process';
function factorial (a) {
  if (Number(a) === 0 || isNaN(a)) {
    return 1;
  } else {
    return Number(a) * factorial(Number(a) - 1);
  }
}

console.log(factorial(argv[2]));
