// nav -------------------------------------------------------------
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
    });
    main.on("click", function () {
        if (open) {
            open = false;
            nav.removeClass("menu-active");
            main.removeClass("menu-active");
            console.log('Gotta remove')
        }

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
