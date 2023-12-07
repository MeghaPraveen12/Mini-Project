let header = document.querySelector('header');

window.addEventListener('scroll', () =>{
  header.classList.toggle('shadow', window.scrollY > 0);
});

let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onclick = () =>{
  menu.classList.toggle('bx-x');
  navbar.classList.toggle('active');
}

var swiper = new Swiper(".home", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
      delay: 2500,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });

  var swiper = new Swiper(".coming-container", {
    spaceBetween: 20,
    loop: true,
    centeredSlides: true,
    autoplay: {
      delay: 2000,
      disableOnInteraction: false,
    },
    breakpoints:
    {
        0: 
        {
            slidesPerView: 2,
        },
        568: 
        {
            slidesPerView: 3,
        },
        768: 
        {
            slidesPerView: 4,
        },
        968: 
        {
            slidesPerView: 5,
        },
    }
  });

  function searchComingMovies() {
    var input, filter, swiperSlides, a, txtValue;
    input = document.getElementById('search-input');
    filter = input.value.toUpperCase();
    swiperSlides = document.querySelectorAll('.coming-container .swiper-slide');

    swiperSlides.forEach(function(slide) {
        a = slide.getElementsByTagName('h3')[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            slide.style.display = '';
        } else {
            slide.style.display = 'none';
        }
    });
}
