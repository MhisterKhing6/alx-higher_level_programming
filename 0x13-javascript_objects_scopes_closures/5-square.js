#!/usr/bin/node
// A square template that inherit from a rectangle
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
