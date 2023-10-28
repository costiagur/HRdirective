myfunc = new Object();

//*********************************************************************************** */
myfunc.submitorder = function(){ //request can be insert or update
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    if (document.getElementById("ordernum_in").value != ''){
        alert("ניסיון לרשום לראשונה הוראה קיימת");
    }

    
    fdata.append("emp_in",document.getElementById("emp_in").value);

    fdata.append("target_in",document.getElementById("target_in").value);

    fdata.append("subject_in",document.getElementById("subject_in").value);

    fdata.append("start_in",document.getElementById("start_in").value);

    fdata.append("end_in",document.getElementById("end_in").value);

    fdata.append("text_in",document.getElementById("text_in").value);

    fdata.append("reference_in",document.getElementById("reference_in").value);

    fdata.append("end_in",document.getElementById("end_in").value);

    fdata.append("doc3",document.getElementById("doc3").files[0]);

    xhr.open('POST',"http://localhost:"+ui.port,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            console.log(this.responseText)

            resobj = JSON.parse(this.responseText);

            if (resobj[0] == "Error"){
                alert(resobj[1])
            }
            else{
                myfunc.download(resobj[0],resobj[1])
            }
        }
        else if (this.readyState == 4 && this.status != 200){
            alert(this.responseText)
        }
    }

    xhr.send(fdata);     
}


//********************************************************************************************* */
myfunc.download = function(filename, filetext){

    var a = document.createElement("a");

    document.body.appendChild(a);

    a.style = "display: none";

    a.href = 'data:application/octet-stream;base64,' + filetext;

    a.download = filename;

    a.click();

    document.body.removeChild(a);

}
//********************************************************************************************* */
myfunc.oneorarea = function(){
    if (document.getElementById("insselect").value == "0"){
        document.getElementById("emp_in").classList.remove("dontdisplay")
        document.getElementById("emp_area").classList.add("dontdisplay")
    }
    else if (document.getElementById("insselect").value == "1"){
        document.getElementById("emp_in").classList.add("dontdisplay")
        document.getElementById("emp_area").classList.remove("dontdisplay")
    }
}