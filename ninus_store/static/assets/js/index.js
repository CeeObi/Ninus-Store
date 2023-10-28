document.querySelector("h1").style.fontSize="70px";

document.querySelector("h1").style.color="red";

$('.pixz_sorc2').mouseover(function(){
    var img_modal_src=$(this).attr('src');
    var img_modal_id = $(this).attr('id');
    var setat = "/" + "productdetail" +"/" + img_modal_id;
    $('#modal_name_2').attr('action', setat);
    $('.pixz_srcs3').attr('src' , img_modal_src);
});




