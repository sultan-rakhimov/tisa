// nav
(function () {
    var nav = $("nav"),
        menu = $("nav i"),
        main = $("main"),
        open = false,
        hover = false;

    menu.on("click", function () {
        open = !open ? true : false;
        nav.toggleClass("menu-active");
        main.toggleClass("menu-active");
        nav.removeClass("menu-hover");
        main.removeClass("menu-hover");
        console.log(open);
    });

    menu.hover(
        function () {
            if (!open) {
                nav.addClass("menu-hover");
                main.addClass("menu-hover");
            }
        },
        function () {
            nav.removeClass("menu-hover");
            main.removeClass("menu-hover");
        }
    );
})();

// contact
var layer1 = document.getElementById("layer1");
scroll = window.pageYOffset;
document.addEventListener("scroll", function (e) {
    var offset = window.pageYOffset;
    scroll = offset;
    layer1.style.width = 100 + scroll / 5 + "%";
});

var layer2 = document.getElementById("layer2");
scroll = window.pageYOffset;
document.addEventListener("scroll", function (e) {
    var offset = window.pageYOffset;
    scroll = offset;
    layer2.style.width = 100 + scroll / 5 + "%";
    layer2.style.left = scroll / 50 + "%";
});

var text = document.getElementById("text");
scroll = window.pageYOffset;
document.addEventListener("scroll", function (e) {
    var offset = window.pageYOffset;
    scroll = offset;
    layer2.style.width = 100 + scroll / 5 + "%";
    text.style.top = -scroll / 20 + "%";
});