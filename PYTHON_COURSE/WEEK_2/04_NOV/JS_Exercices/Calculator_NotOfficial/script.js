var touches = document.getElementsByClassName('touche');
var reponse = document.getElementById("reponse")


var expression = ""
for (var i = 0; i < touches.length; i++) {
    touches[i].onclick =
        function() {
            if (this.textContent != "=") {
                expression += this.textContent;
                reponse.textContent = expression
            } else {
                reponse.textContent = eval(expression);
                expression = eval(expression)
            }
        }


}