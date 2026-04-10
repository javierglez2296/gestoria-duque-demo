(function () {
    function activatePage() {
        document.body.classList.add("page-loaded");
    }

    if (document.readyState === "complete") {
        requestAnimationFrame(activatePage);
    } else {
        window.addEventListener("load", function () {
            requestAnimationFrame(activatePage);
        });
    }
})();
