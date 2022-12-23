#!/usr/bin/node
// Creating an empty rectangle template
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '#';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < (this.width - 1); j++) {
        str += '#';
      }
      console.log(str);
      str = '#';
    }
  }
}
module.exports = Rectangle;
