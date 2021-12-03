func = function(){
    location.reload();
}
timer = setInterval(func, 10000);
window.onfocus = func;
window.onclick = func;
// window.onblur = func;
// window.onmouseenter = func;
// document.addEventListener("visibilitychange", function() {
//     // hidden visible
//     if (document.visibilityState == 'visible'){
//         location.reload();
//     }
// }
