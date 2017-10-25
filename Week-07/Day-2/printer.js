'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)

function printer(input){
    var parameter_list = ""
    for(var i = 0; i <= arguments.length - 1; i++){
        parameter_list += arguments[i] + '\n';
    }
    console.log(parameter_list)
}

printer("Barbi", "CEO")