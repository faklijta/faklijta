'use strict';

var test = require('tape');
var sumList = require('./sum');

test('sum two elements', function (t) {
  var actual = sumList([1, 2]);
  var expected = 3;

  t.equal(actual, expected);
  t.end();
});