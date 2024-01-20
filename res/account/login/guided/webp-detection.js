document.documentElement.classList.remove("no-js");
function checkWebP(callback) {
    var webP = new Image();
    webP.onload = webP.onerror = function () {
        callback(webP.height == 2);
    };
    webP.src = 'data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA';
}
;
checkWebP(function (support) {
    if (support) {
        document.documentElement.classList.add("webp");
    } else {
        document.documentElement.classList.add("no-webp");
    }
});
