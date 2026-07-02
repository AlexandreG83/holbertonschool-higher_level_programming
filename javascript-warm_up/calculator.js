#!/usr/bin/node

function add (a, b) {
  return a + b;
}

function sub (a, b) {
  return a - b;
}

function mul (a, b) {
  return a * b;
}

function div (a, b) {
  return a / b;
}

function mod (a, b) {
  return a % b;
}

const x = Number(process.argv[2]);
const op = process.argv[3];
const y = Number(process.argv[4]);

if (op === '+') {
  console.log(add(x, y));
} else if (op === '-') {
  console.log(sub(x, y));
} else if (op === '*') {
  console.log(mul(x, y));
} else if (op === '/') {
  console.log(div(x, y));
} else if (op === '%') {
  console.log(mod(x, y));
} else {
  console.log('Utilisation : ./calculator.js <nombre> <opération> <nombre>');
}