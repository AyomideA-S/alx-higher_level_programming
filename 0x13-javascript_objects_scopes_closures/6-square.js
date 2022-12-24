#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super();
    this.size = size;
  }

  print () {
    const pattern = 'X'.repeat(this.size);
    for (let i = 0; i < this.size; i++) {
      console.log(pattern);
    }
  }

  double () {
    this.size *= 2;
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const pattern = c.repeat(this.size);
    for (let i = 0; i < this.size; i++) {
      console.log(pattern);
    }
  }
}
module.exports = Square;
