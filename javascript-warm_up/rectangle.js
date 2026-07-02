#!/usr/bin/node

const x = Number(process.argv[2]);
const y = Number(process.argv[3]);

if (isNaN(y)) {
  console.log('Missing size in y');
  if (isNaN(x)) {
    console.log('Missing size in x');
  }
} else {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < y; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}