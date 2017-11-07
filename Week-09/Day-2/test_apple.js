'use strict';

var test = require('tape');
var getApple = require('./apple');

test('print apple', function (t) {
  var actual = getApple('apple');
  var expected = 'apple';

  t.equal(actual, expected);
  t.end();
});