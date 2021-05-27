const open = document.getElementById("button");
open.addEventListener("click",function(){
    if (open.getAttribute('class')==='deactivate'){
        document.getElementById("menu").style.width = "250px";
        document.getElementById("main").style.marginLeft = "250px";
        open.setAttribute("class","activate")
    }else{
        document.getElementById("menu").style.width = 0;
        document.getElementById("main").style.marginLeft = 0;
        open.setAttribute("class","deactivate")
    }
});
