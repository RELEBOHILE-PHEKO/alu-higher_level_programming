#!/usr/bin/node

exports.converter = function(base) {
    return function convert(number) {
        return number < base ? '' + number : convert(~~(number / base)) + '' + number % base;
    };
};

