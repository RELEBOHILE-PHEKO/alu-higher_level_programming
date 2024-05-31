#!/usr/bin/node
const myobject = {
  type: 'object',
  value: 12
};
console.log(myobject);

myobject.incr = function () {
  this.value++;
};

myobject.incr();
console.log(myobject);
myobject.incr();
console.log(myobject);
myobject.incr();
console.log(myobject);
