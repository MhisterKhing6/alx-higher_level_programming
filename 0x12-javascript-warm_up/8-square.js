#!/usr/bin/env node
import { argv } from 'node:process';
if (Number(argv[2])) {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    let x = '';
    for (let j = 0; j < parseInt(argv[2]); j++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
