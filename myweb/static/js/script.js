var content1 = document.getElementById("content-1");
var content2 = document.getElementById("content-2")
var content3 = document.getElementById("content-3")

var toggle1 = 0;
var toggle2 = 0;
var toggle3 = 0;

function acco1(){
    if(toggle1==0){
        content1.style.display = 'block';
        toggle1 = 1;
    }else{
        content1.style.display = 'none';
        toggle1 = 0;
    }
}

function acco2(){
    if(toggle2==0){
        content2.style.display = 'block';
        toggle2 = 1;
    }else{
        content2.style.display = 'none';
        toggle2 = 0;
    }
}
function acco3(){
    if(toggle3==0){
        content3.style.display = 'block';
        toggle3 = 1;
    }else{
        content3.style.display = 'none';
        toggle3 = 0;
    }
}
$(document).ready(function(){
    $('.slider').slick({
      slidesToShow: 3,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 1000,
      dots: false,
      arrows: false,
    });
  });
  