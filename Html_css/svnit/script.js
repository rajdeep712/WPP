const slides_images = Array.from(document.getElementsByClassName('pic'));
const prev_button = document.querySelector('.prev');
const next_button = document.querySelector('.next');

let counter = 0;

prev_button.addEventListener('click' , () => {
    counter --;
    if(counter === -1) {
        counter = 9;
    }
    change_image();
});

next_button.addEventListener('click' , () => {
    counter ++;
    if(counter === 10) {
        counter = 0;
    }
    change_image();
});


setInterval(() => {
    counter += 1;
    if(counter === 10) {
        counter = 0;
    }
    change_image();
} , 4000);



function change_image() {
    slides_images.forEach((element) => {
        element.style.transform = `translateX(-${counter*100}%)`;
    });
}