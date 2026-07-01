#!/usr/bin/node

const argc = process.argv.slice(2).map(Number);

if (argc.length < 2) {
  console.log(0);
} else {
  let max = -Infinity;
  let secondMax = -Infinity;
  for (let i = 0; i < argc.length; i++) {
    if (argc[i] > max) {
      secondMax = max;
      max = argc[i];
    } else if (argc[i] > secondMax && argc[i] !== max) {
      secondMax = argc[i];
    }
  }
  console.log(secondMax);
}
