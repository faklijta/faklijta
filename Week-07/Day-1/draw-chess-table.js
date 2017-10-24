'use strict';

// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % % 
//  % % % %
//
let lineCount = 8
for (let i = 1; i <= lineCount; i++){
    console.log(' %'.repeat(lineCount/2));
    console.log(' ' + ' %'.repeat(lineCount/2));
}
