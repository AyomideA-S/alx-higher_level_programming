#!/usr/bin/node
const _Square = require('./5-square');

class Square extends _Square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const pattern = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(pattern);
    }
  }
}
module.exports = Square;
