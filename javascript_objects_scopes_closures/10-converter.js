#!/usr/bin/node
function converter(base) {
    return function(number) {
        if (number < base) {
            return '' + number;
        } else {
            return converter(base)(Math.floor(number / base)) + '' + number % base;
        }
    };
}

exports.converter = converter;

