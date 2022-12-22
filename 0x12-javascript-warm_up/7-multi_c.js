#!/usr/bin/node
let x = process.argv[2];
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  while (x-- > 0) {
    console.log('C is fun');
  }
}
