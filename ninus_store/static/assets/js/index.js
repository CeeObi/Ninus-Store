alert("Ready?");
document.querySelector("h1").style.fontSize="70px";
document.querySelector("h1").style.color="purple";

function toToggle(){
    document.querySelector(".product-hover-overlay").classList.toggle("visible")
};
document.querySelector(".product-lists").addEventListener("mouseenter", toToggle);
document.querySelector(".product-lists").addEventListener("mouseleave", toToggle);


$('#pixz_source').on( "click", function(){
    var _data = $("#pixz_sorc2").attr('src');
    console.log(_data)
    $('#pixz_srcs3').attr('src' , _data);
});