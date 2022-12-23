#!/usr/bin/node
// A square template that inherit from a rectangle
const square = require('./5-square');
class Square extends square {
  charPrint (C) {
    if (!C) {
      C = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(C.repeat(this.height));
    }
  }
}
module.exports = Square;
