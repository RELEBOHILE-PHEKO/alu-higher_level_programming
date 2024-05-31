#!/usr/bin/node
function factorial (n) { // Add a space before the parentheses
  if (isNaN(n) || n < 0) return 1;
  if (n === 0) return 1;
  return n * factorial(n - 1);
}
console.log(factorial(parseInt(process.argv[2])));
