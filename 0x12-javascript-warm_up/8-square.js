#!/usr/bin/node
const size = process.argv[2];
if (isNaN(parseInt(size))) {
  console.log('Missing size');
} else {
  if (size > 0) {
    const pattern = 'X'.repeat(size);
    for (let i = 0; i < size; i++) {
      console.log(pattern);
    }
  }
}
