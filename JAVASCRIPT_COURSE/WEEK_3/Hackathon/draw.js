
/*----- FROM TUTORIAL https://www.youtube.com/watch?v=9TcU2C1AACw ----*/
// const cvs = document.getElementById('canvas');
// const ctx = cvs.getContext('2d');

/*------- LOAD IMAGES  ------ */
// let fruit = newImage();
// fruit.src="https://filacoahuila.com/wp-content/uploads/2019/11/Icon-Red-Apple-Christmas-Eve-have-a-beautiful.jpg";
// let audioEffect = newAudio();
// audioEffect.src = "";
// audioEffect.play();

/*-------- DRAW IMAGES -------*/
// ctx.drawImage(fruit,40,50,25,25);

/*-------- DRAW RECTANGLE -------*/
// ctx.fillStyle = "red";
// ctx.fillRect (100,300,30,30);


/*----- FROM TUTORIALhttps://www.youtube.com/watch?v=21eSpMtJwrc ----*/
const cvs = document.getElementById('canvas');
const ctx = cvs.getContext('2d');
const scale = 10;
const rows = canvas.height / scale;
const columns = canvas.width / scale;

var snake;

(function setup() {
  snake = new Snake();
  fruit = new Fruit();
  fruit.pickLocation();
  // console.log(fruit);

  window.setInterval(() => {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    fruit.draw();
    snake.update();
    snake.draw();

    if (snake.eat(fruit)) {
      // console.log("EATING");
      fruit.pickLocation();
    }

  }, 250);
}())

window.addEventListener('keydown', ((evt) => {
  // console.log(evt);
  const direction = evt.key.replace('Arrow', '');
  // console.log(direction);
  snake.changeDirection(direction);
}))
