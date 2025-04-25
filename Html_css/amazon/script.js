const back_img_cont = document.querySelector('.back-img');
const m_backs = ["m-back/1.png","m-back/2.png","m-back/3.png","m-back/4.png","m-back/5.png"];
const p_backs = ["back1.jpg","back2.jpg","back3.jpg","back4.jpg","back5.jpg"];
let images = m_backs;
let index = 0;
if(window.innerWidth<600) {
    images = m_backs;
}
else {
    images = p_backs;
}

function changeBack() {
    if(window.innerWidth<600) {
        back_img_cont.style.maxWidth = "500px";
        back_img_cont.style.width = "100%";
        back_img_cont.style.backgroundImage = "url('m-back/1.png')";
        back_img_cont.style.backgroundSize = "cover";
        images = m_backs;
        index = 0;
    }
}

setInterval(() => {
    index++;
    if(index>=4) {
        index = 0;
    }
    back_img_cont.style.backgroundImage = `url('${images[index]}')`;
},5000)

changeBack();
window.addEventListener('resize',changeBack());