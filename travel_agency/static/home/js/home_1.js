$(document).ready(function () {
    var parallaxSlider;
    var parallaxSliderOptions = {
        speed: 1000,
        autoplay: true,
        parallax: true,
        loop: true,
        grabCursor: true,
        centerSlides: true,
        pagination: {
            el: '.parallax-slider .swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.parallax-slider .next-ctrl',
            prevEl: '.parallax-slider .prev-ctrl',
        },
        on: {
            init: function () {
                let swiper = this;
                for (let i = 0; i < swiper.slides.length; i++) {
                    $(swiper.slides[i]).find('.slide_image').attr({
                        'data-swiper-parallax': 0.75 * swiper.width,
                    });
                    $(swiper.slides[i]).find('.slide_content').attr('data-swiper-parallax', 0.5 * swiper.width);
                }
            }
        }
    };

    parallaxSlider = new Swiper(".parallax-slider", parallaxSliderOptions);
    $(window).on('resize', function () {
        parallaxSlider.destroy();
        parallaxSlider = new Swiper('.parallax-slider', parallaxSliderOptions);
    });
});