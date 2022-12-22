#!/usr/bin/node
let text;
if (process.argv[2] !== undefined) {
  text = process.argv[2];
} else {
  text = 'undefined';
}
console.log(text.concat(' is ', process.argv[3]));
