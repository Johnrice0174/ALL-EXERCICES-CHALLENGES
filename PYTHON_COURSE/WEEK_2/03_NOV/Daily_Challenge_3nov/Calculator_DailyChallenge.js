var num1 = 0;
var num2 = 0;
var result;
var symbol;

function my_f(click) {
    if (click == "+"){
        symbol = "+";
    }
    else if (click == "-"){
        symbol = "-";
    }
    else if (click == "*"){
        symbol = "*";
    }
    else if (click == "/"){
        symbol = "/";
    }

    //calculation//
    else if (click == "="){
        if(symbol == "+"){
                result = num1 + num2;
        }
        else if (symbol == "-"){
                result = num1 - num2;
        }
        else if (symbol == "*"){
                result = num1 * num2;
        }
        else if (symbol == "/"){
                result = num1 / num2;
        }
        alert(result)
        location.reload(); // to refresh\clear //
    }
    else {
        if (num1 == 0){
                num1 = click;
        }
        else {
                num2 = click;
        }
    }

}

