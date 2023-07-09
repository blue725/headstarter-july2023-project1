window.addEventListener("load", ()=>{
    const input= document.getElementById("upload");
    const filewrapper = document.getElementById("filewrapper");

    input.addEventListener("change", (e)=>{
        let fileName = e.target.files[0].name;
        let fileType = e.target.value.split(".").pop();
        fileshow(fileName, fileType);
    })

    const fileshow = (fileName, fileType) =>{
        const showFileboxElement = document.createElement("div");
        showFileboxElement.classList.add("showFilebox");
        const leftElement = document.createElement("div");
        leftElement.classList.add("left");
        const fileTypeElement = document.createElement("span");
        fileTypeElement.classList.add("fileType");
        fileTypeElement.innerHTML=fileType;
        leftElement.append(fileTypeElement);
        const fileTitleElement = document.createElement("h3");
        fileTitleElement.innerHTML=fileName;
        leftElement.append(fileTitleElement);
        showFileboxElement.append(leftElement);
        const rightElement = document.createElement("div");
        rightElement.classList.add("right");
        showFileboxElement.append(rightElement);
        const crossElement = document.createElement("span");
        crossElement.innerHTML="&#215;";
        rightElement.append(crossElement);
        filewrapper.append(showFileboxElement);

        crossElement.addEventListener("click", ()=>{
            filewrapper.removeChild(showFileboxElement);
        })
    }

})