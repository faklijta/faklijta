'use strict';

var test = require('tape');
var summing = require('./sum');

test('sum two elements', function (t) {
  var actual = summing([1, 4]);
  var expected = 5;

  t.equal(actual, expected);
  t.end();
});

test('empty list', function (t) {
    var actual = summing([]);
    var expected = 0;
  
    t.equal(actual, expected);
    t.end();
  });

  test('sum one elements', function (t) {
    var actual = summing([1]);
    var expected = 1;
  
    t.equal(actual, expected);
    t.end();
  });

  test('sum multiple elements', function (t) {
    var actual = summing([1, 2, 3, 4]);
    var expected = 10;
  
    t.equal(actual, expected);
    t.end();
  });

//   test('sum null', function (t) {
//     var actual = summing(null);
//     var expected = 'not valid input';
  
//     t.equal(actual, expected);
//     t.end();
//   });

//   test('sum string', function (t) {
//     var actual = summing(["hello"]);
//     var expected = 'not valid input';
  
//     t.equal(actual, expected);
//     t.end();
//   });