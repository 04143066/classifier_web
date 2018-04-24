function output() {
    if ($(".form").hasClass("hide")) {

        $(".form").removeClass("hide");
    } else {
        $(".form").addClass("hide");
    }
    console.log('finish');
}