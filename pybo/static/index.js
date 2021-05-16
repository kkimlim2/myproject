const buttons = document.querySelectorAll('button');
for(let i=0;i<buttons.length;i++){
    var temp = buttons[i];
    temp.addEventListener("click",function(){
        var mode = this.getAttribute('class');
            if (mode ==="hide"){
                this.setAttribute("class","detailed");
                var name = this.getAttribute("id");
                var content = document.getElementById(name+" casting");
                content.style.display="none";

            } else{
                this.setAttribute("class","hide");
                var name = this.getAttribute("id");
                var content = document.getElementById(name+" casting");
                content.style.display="block";
            }
    });
}
