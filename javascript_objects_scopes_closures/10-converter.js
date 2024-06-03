#!/usr/bin/node

exports.converter = function (base) {
  return function convert (number) {
    return number < base ? '' + (number < 10 ? number : String.fromCharCode(number + 87)) : convert((number / base) | 0) + '' + (number % base < 10 ? number % base : String.fromCharCode(number % base + 87));
  };
};
