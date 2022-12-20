#!/usr/bin/node
import { argv } from 'node:process';
if (argv.length < 3) {
  console.log('0');
} else if (argv.length === 3) {
  console.log('0');
} else {
  for (let i = 2; i < argv.length; i++) {
    argv[i] = Number(argv[i]);
  }
  console.log(argv.sort().reverse()[1]);
}
