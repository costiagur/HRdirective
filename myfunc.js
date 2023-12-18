myfunc = new Object();

//*********************************************************************************** */
myfunc.orderertype = function(){
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    fdata.append("request","orderertype");

    xhr.open('POST',"http://localhost:"+ui.port,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            console.log(this.responseText)

            resobj = JSON.parse(this.responseText);

            if (resobj[0] == "Error"){
                alert(resobj[1])
            }
            else{
                document.getElementById("username").innerHTML = resobj[1].username

                if(resobj[1].orderertype == "orderer"){
                    document.getElementsByTagName("body")[0].classList.add("w3-sand")
                    document.getElementById("ordertype").innerHTML = "מתן הוראה"
                    document.getElementById("submit_bt").innerHTML = "שלח לאישור"
                }
                else if (resobj[1].orderertype == "manager"){
                    document.getElementsByTagName("body")[0].classList.add("w3-pale-red")
                    document.getElementById("ordertype").innerHTML = "אישור הוראה"
                    document.getElementById("submit_bt").innerHTML = "אשר הוראה"
                }
                else if (resobj[1].orderertype == "searcher"){
                    document.getElementsByTagName("body")[0].classList.add("w3-pale-green")
                    document.getElementById("ordertype").innerHTML = "חיפוש הוראה"
                }

                for (eachfield of document.getElementsByClassName("inputfield")){
                    if (eachfield.contains(resobj[1].orderertype)){
                        eachfield.classList.remove("nodisplay")
                    }
                    else{
                        eachfield.classList.add("nodisplay")
                    }
                }
            }    
        }
        else if (this.readyState == 4 && this.status != 200){
            alert(this.responseText)
        }
    }

    xhr.send(fdata);        
}
//*********************************************************************************** */
myfunc.clearfields = function(){
    for (eachfield of document.querySelectorAll("input, textarea")){
        eachfield.value="";
    }
    document.getElementById("enddate_in").value = "2099-12-31";

}
//*********************************************************************************** */
myfunc.getidname = function(this_value,this_id){
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();
    
    fdata.append("request","searchidname")
    fdata.append("this_id",this_id)
    fdata.append("this_value",this_value)
    
    xhr.open('POST',"http://localhost:"+ui.port,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            console.log(this.responseText)

            resobj = JSON.parse(this.responseText);

            if (resobj[0] == "Error"){
                alert(resobj[1])
            }
            else{
                empid_list = ""
                empname_list = ""
                
                for (smallobj of resobj[1]){
                    console.log(smallobj)
                    empid_list += `<option value=${smallobj.empid}></option>`
                    empname_list += `<option value="${smallobj.empname}"></option>`
                }

                document.getElementById("empid_list").innerHTML = empid_list;
                document.getElementById("empname_list").innerHTML = empname_list;
            }
        }
        else if (this.readyState == 4 && this.status != 200){
            alert(this.responseText)
        }
    }

    xhr.send(fdata);     
}

//*********************************************************************************** */
myfunc.submit = function(){ //request can be insert or update
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    fdata.append("in1",document.getElementById("in1").value);

    fdata.append("in2",document.getElementById("in2").value);

    fdata.append("doc1",document.getElementById("doc1").files[0]);

    fdata.append("doc2",document.getElementById("doc2").files[0]);

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
