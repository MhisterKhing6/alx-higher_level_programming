#!/usr/bin/node
import { argv } from 'node:process';
if (Number(argv[2])) {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
