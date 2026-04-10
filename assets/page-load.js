(function () {
    function activatePage() {
        setTimeout(function () {
            document.body.classList.add("page-loaded");
        }, 180);
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", function () {
            requestAnimationFrame(activatePage);
        });
    } else {
        requestAnimationFrame(activatePage);
    }
})();
