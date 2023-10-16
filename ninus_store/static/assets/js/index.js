document.querySelector("h1").style.fontSize="70px";

function toToggle(){
    document.querySelector(".product-hover-overlay").classList.toggle("visible")
};
document.querySelector(".product-lists").addEventListener("mouseenter", toToggle);
document.querySelector(".product-lists").addEventListener("mouseleave", toToggle);
