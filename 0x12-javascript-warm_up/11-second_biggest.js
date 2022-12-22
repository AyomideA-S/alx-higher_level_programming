#!/usr/bin/node
let i = 2;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let max = 0;
  let max2 = 0;
  while (process.argv[i] !== undefined) {
    const num = parseInt(process.argv[i]);
    if (num > max) {
      max2 = max;
      max = num;
    } else if (num > max2) {
      max2 = num;
    }
    i++;
  }
  console.log(max2);
}
