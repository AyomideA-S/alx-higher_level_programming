#!/usr/bin/node
function factorial (a) {
  if (a <= 1 || isNaN(a)) {
    return 1;
  } else {
    return a * factorial(--a);
  }
}

console.log(factorial(parseInt(process.argv[2])));
