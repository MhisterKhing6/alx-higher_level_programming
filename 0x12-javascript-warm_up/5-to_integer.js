#!/usr/bin/node
import { argv } from 'node:process';
if (Number(argv[2])) {
  console.log('My first number: ', parseInt(argv[2]));
} else {
  console.log('Not a number');
}
