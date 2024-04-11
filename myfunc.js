myfunc = new Object();
myfunc.state = {};
myfunc.state["-1"] = "נדחה"
myfunc.state["0"] = "ממתין לאישור"
myfunc.state["1"] = "מאושר"

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
//*********************************************************************************** */
myfunc.alert = function(msg){
    document.getElementById("alert_dg_msg").innerHTML = msg
    document.getElementById("alert_dg").showModal();
    
}

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
                myfunc.alert(resobj[1])
            }
            else{
                document.getElementById("username").innerHTML = resobj[1].username
                document.getElementById("submit_bt").setAttribute("disabled","");
                document.getElementById("update_bt").setAttribute("disabled","");
                document.getElementById("cancel_bt").setAttribute("disabled","");
                document.getElementById("orderer_in").innerHTML = resobj[1].orderertype;

                if(resobj[1].orderertype == "orderer"){
                    document.getElementsByTagName("body")[0].classList.remove("w3-pale-red")
                    document.getElementsByTagName("body")[0].classList.remove("w3-pale-green")
                    document.getElementsByTagName("body")[0].classList.add("w3-sand")
                    document.getElementById("ordertype").innerHTML = "מתן הוראה"
                    document.getElementById("submit_bt").innerHTML = "שלח לאישור"
                    document.getElementById("cancel_bt").innerHTML = "מחק הוראה"
                    document.getElementById("cancel_dg_msg").innerHTML = "האם למחוק הוראה? לא ניתן יהיה לשחזרה לאחר מחיקה."
                    document.getElementById("submit_bt").removeAttribute("disabled");
                    document.getElementById("update_bt").removeAttribute("disabled");                
                    document.getElementById("cancel_bt").removeAttribute("disabled");                

                }
                else if (resobj[1].orderertype == "manager"){
                    document.getElementsByTagName("body")[0].classList.remove("w3-sand")
                    document.getElementsByTagName("body")[0].classList.remove("w3-pale-green")
                    document.getElementsByTagName("body")[0].classList.add("w3-pale-red")
                    document.getElementById("ordertype").innerHTML = "אישור הוראה"
                    document.getElementById("submit_bt").innerHTML = "אשר הוראה"
                    document.getElementById("cancel_bt").innerHTML = "דחה הוראה"
                    document.getElementById("cancel_dg_msg").innerHTML = "האם לדחות הוראה ולהחזירה לתיקונים?"
                    document.getElementById("submit_bt").removeAttribute("disabled");
                    document.getElementById("cancel_bt").removeAttribute("disabled");
                    document.getElementById("state_sch").value = 0 //run search on all awaiting authorization
                    myfunc.search()

                }
                else if (resobj[1].orderertype == "searcher"){
                    document.getElementsByTagName("body")[0].classList.remove("w3-sand")
                    document.getElementsByTagName("body")[0].classList.remove("w3-pale-red")
                    document.getElementsByTagName("body")[0].classList.add("w3-pale-green")
                    document.getElementById("ordertype").innerHTML = "חיפוש הוראה"
                    document.getElementById("search_bt").innerHTML = "חפש הוראה"
                }

                for (eachfield of document.getElementsByClassName("inputfield")){
                    if (resobj[1].orderertype == "orderer" || resobj[1].orderertype == "manager" || resobj[1].orderertype == "searcher"){
                        eachfield.classList.remove("nodisplay")
                    }
                    else{
                        eachfield.classList.add("nodisplay")
                    }
                }

            }    
        }
        else if (this.readyState == 4 && this.status != 200){
            myfunc.alert(this.responseText)
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
    document.getElementById("existingfile").innerHTML="";
    document.getElementById("existinglist").innerHTML="";
    document.getElementById("showdata_order").innerHTML="";
    myfunc.orderertype()
}
//*********************************************************************************** */
myfunc.getidname = function(this_value,this_id){
    
    if(this_value == "רשימה" && this_id == "empname_in"){
        document.getElementById("empid_in").value = "000000000";
        return
    }

    if(this_value == "000000000" && this_id == "empid_in"){
        document.getElementById("empname_in").value = "רשימה";
        return
    }

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
                myfunc.alert(resobj[1])
            }
            else{
                empid_list = ""
                empname_list = ""

                if (resobj[1].length == 1){
                    document.getElementById("empid_in").value = resobj[1][0].empid
                    document.getElementById("empname_in").value = resobj[1][0].empname
                    myfunc.tempselectbyempid(resobj[1][0].empid)
                    document.getElementById("empid_in").classList.add("flashinsert")
                    document.getElementById("empname_in").classList.add("flashinsert")
                }
                else{
                    document.getElementById("empid_in").classList.remove("flashinsert")
                    document.getElementById("empname_in").classList.remove("flashinsert")

                    for (smallobj of resobj[1]){
                        empid_list += `<option value=${smallobj.empid}></option>`
                        empname_list += `<option value="${smallobj.empname}"></option>`
                    }                       
                }
                document.getElementById("empid_list").innerHTML = empid_list;
                document.getElementById("empname_list").innerHTML = empname_list;
            }
        }
        else if (this.readyState == 4 && this.status != 200){
            myfunc.alert(this.responseText)
        }
    }

    xhr.send(fdata);     
}
//*********************************************************************************** */
myfunc.loadtypes = function(){
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();
    
    fdata.append("request","loadtypes")
    
    xhr.open('POST',"http://localhost:"+ui.port,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            console.log(this.responseText)

            resobj = JSON.parse(this.responseText);

            if (resobj[0] == "Error"){
                myfunc.alert(resobj[1])
            }
            else{
                let type_list = ""
                for (eachelem of resobj[1]){
                    type_list += `<option value="${eachelem}"></option>`
                }

                document.getElementById("type_list").innerHTML = type_list;
            }
        }
        else if (this.readyState == 4 && this.status != 200){
            myfunc.alert(this.responseText)
        }
    }

    xhr.send(fdata);     

}
//*********************************************************************************** */
myfunc.submit = function(update){ //request can be insert or update
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    var required = document.querySelectorAll("input[required], textarea")
    var anyempty = 0
    
    for(let eachelem of required){
        if (eachelem.value == ""){
            eachelem.classList.add("redcolor")
            anyempty++
        }
        else{
            eachelem.classList.remove("redcolor")
        }
    }

    if (anyempty > 0){
        return
    }

    if (update == 1){
        fdata.append("request","update")
    }
    else if (update == 2){
        fdata.append("request","submit")
    }
    else{
        fdata.append("request","submit")
        if (document.getElementById("orderer_in").innerHTML == "manager" && document.getElementById("runind_in").value == ""){
            document.getElementById("authsubmit_nonexistrunid_dg").showModal()
            return
        }
    }

    fdata.append("runind_in",document.getElementById("runind_in").value);

    fdata.append("addressee_in",document.getElementById("addressee_in").value);

    fdata.append("type_in",document.getElementById("type_in").value);

    fdata.append("empid_in",document.getElementById("empid_in").value);

    fdata.append("startdate_in",document.getElementById("startdate_in").value);

    fdata.append("enddate_in",document.getElementById("enddate_in").value);

    fdata.append("text_in",document.getElementById("text_in").value);
    
    fdata.append("reference_in",document.getElementById("reference_in").value);

    fdata.append("reffile_in",document.getElementById("reffile_in").files[0]);

    fdata.append("listfile_in",document.getElementById("listfile_in").files[0]);

    xhr.open('POST',"http://localhost:"+ui.port,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            console.log(this.responseText)

            resobj = JSON.parse(this.responseText);

            if (resobj[0] == "Error"){
                myfunc.alert(resobj[1])
            }
            else{
                myfunc.tempselectbyempid(document.getElementById("empid_in").value)
            }
        }
        else if (this.readyState == 4 && this.status != 200){
            myfunc.alert(this.responseText)
        }
    }

    xhr.send(fdata);     
}
//********************************************************************************************* */
myfunc.tempselectbyempid = function(empid){
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    fdata.append("request","selectempid")

    fdata.append("empid",empid);

    xhr.open('POST',"http://localhost:"+ui.port,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            console.log(this.responseText)

            resobj = JSON.parse(this.responseText);

            if (resobj[0] == "Error"){
                myfunc.alert(resobj[1])
            }
            else{
                myfunc.searchresults(resobj)
            }
        }
        else if (this.readyState == 4 && this.status != 200){
            myfunc.alert(this.responseText)
        }
    }

    xhr.send(fdata); 

}
//********************************************************************************************* */
myfunc.getfilerunind = function(runind,filetype){
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    fdata.append("request","getfilerunind")

    fdata.append("runind",runind);

    fdata.append("filetype",filetype);

    xhr.open('POST',"http://localhost:"+ui.port,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            console.log(this.responseText)

            resobj = JSON.parse(this.responseText);

            if (resobj[0] == "Error"){
                myfunc.alert(resobj[1])
            }
            else{
                myfunc.download(resobj[1].filename,resobj[1].filedata)
            }
        }
        else if (this.readyState == 4 && this.status != 200){
            myfunc.alert(this.responseText)
        }
    }

    xhr.send(fdata); 
}
//********************************************************************************************* */
myfunc.loadbyrunind = function(runind){
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    fdata.append("request","loadbyrunind")

    fdata.append("runind",runind);

    xhr.open('POST',"http://localhost:"+ui.port,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            console.log(this.responseText)

            resobj = JSON.parse(this.responseText);

            if (resobj[0] == "Error"){
                myfunc.alert(resobj[1])
            }
            else{
                document.getElementById("runind_in").value = resobj[1].runind
                document.getElementById("state_in").value = resobj[1].state
                document.getElementById("addressee_in").value = resobj[1].addressee
                document.getElementById("type_in").value = resobj[1].ordercapt
                document.getElementById("empid_in").value = resobj[1].empid
                myfunc.getidname(resobj[1].empid,"empid_in");
                document.getElementById("startdate_in").value = resobj[1].startdate
                document.getElementById("enddate_in").value = resobj[1].enddate
                document.getElementById("text_in").value = resobj[1].ordertext
                document.getElementById("reference_in").value = resobj[1].reference
                
                if (eachrow.filename != null && eachrow.filename != ""){
                    document.getElementById("existingfile").innerHTML = `${eachrow.filename}<a href="#" onclick="myfunc.getfilerunind(${resobj[1].runind},'reffile')"><img src='download.png'></a>`
                }
                if (eachrow.listfilename != null && eachrow.listfilename != ""){
                    document.getElementById("existinglist").innerHTML = `${eachrow.listfilename}<a href="#" onclick="myfunc.getfilerunind(${resobj[1].runind},'listfile')"><img src='download.png'></a>`
                }

                if(document.getElementById("orderer_in").innerHTML == "orderer"){
                    document.getElementById("submit_bt").setAttribute("disabled", "");
                }

                if(resobj[1].state == 1 && document.getElementById("orderer_in").innerHTML == "manager"){
                    document.getElementById("submit_bt").setAttribute("disabled", "");
                }

            }
        }
        else if (this.readyState == 4 && this.status != 200){
            myfunc.alert(this.responseText)
        }
    }

    xhr.send(fdata);     
}
//********************************************************************************************* */
myfunc.cancel = function(){

    if(document.getElementById("runind_in").value == "" || document.getElementById("runind_in").value == undefined){
        myfunc.alert("לא נבחרה הוראה לביטול")
        return
    }

    if (document.getElementById("orderer_in").innerHTML == "orderer"){
        document.getElementById("cancel_dg").showModal();
    }
    else if (document.getElementById("orderer_in").innerHTML == "manager"){
        myfunc.authdecline()
    }
}

//********************************************************************************************* */
myfunc.cancel_proceed = function(){

    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    document.getElementById("cancel_dg").close()

    runind = document.getElementById("runind_in").value

    fdata.append("request","cancel")

    fdata.append("runind",runind);

    xhr.open('POST',"http://localhost:"+ui.port,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            console.log(this.responseText)

            resobj = JSON.parse(this.responseText);

            if (resobj[0] == "Error"){
                myfunc.alert(resobj[1])
            }
            else{
                myfunc.alert(resobj[1])
                myfunc.tempselectbyempid(document.getElementById("empid_in").value)
            }
        }
        else if (this.readyState == 4 && this.status != 200){
            myfunc.alert(this.responseText)
        }
    }

    xhr.send(fdata);     
}
//********************************************************************************************* */
myfunc.authdecline = function(){

    var xhr = new XMLHttpRequest();
    var fdata = new FormData();
   
    fdata.append("request","decline")
    
    fdata.append("runind",document.getElementById("runind_in").value);
    fdata.append("managername",document.getElementById("username").innerHTML);
 
    xhr.open('POST',"http://localhost:"+ui.port,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            console.log(this.responseText)

            resobj = JSON.parse(this.responseText);

            if (resobj[0] == "Error"){
                myfunc.alert(resobj[1])
            }
            else{
                myfunc.alert(resobj[1])
                myfunc.tempselectbyempid(document.getElementById("empid_in").value)
            }
        }
        else if (this.readyState == 4 && this.status != 200){
            myfunc.alert(this.responseText)
        }
    }

    xhr.send(fdata);     
}
//********************************************************************************************* */
myfunc.search = function(){
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    fdata.append("request","search")

    fdata.append("empid",document.getElementById("empid_sch").value);

    fdata.append("empname",document.getElementById("empname_sch").value);

    fdata.append("startdate",document.getElementById("startdate_sch").value);

    fdata.append("enddate",document.getElementById("enddate_sch").value);

    fdata.append("ordercap",document.getElementById("type_sch").value);

    fdata.append("ordtxt",document.getElementById("txt_sch").value);

    fdata.append("regexp",(document.getElementById("regexp_sch").checked)? true:false);

    fdata.append("state",document.getElementById("state_sch").value);

    fdata.append("listnum",document.getElementById("listnum_sch").value);  

    console.log(fdata)

    xhr.open('POST',"http://localhost:"+ui.port,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            console.log(this.responseText)

            resobj = JSON.parse(this.responseText);

            if (resobj[0] == "Error"){
                myfunc.alert(resobj[1])
            }
            else{
                myfunc.searchresults(resobj)
            }
        }
        else if (this.readyState == 4 && this.status != 200){
            myfunc.alert(this.responseText)
        }
    }

    xhr.send(fdata); 

}
//********************************************************************************************** */
myfunc.searchresults = function(resobj){

    table = `<table class="w3-table w3-bordered"><thead><tr>`
    table +="<td></td><th>זהות</th><th>שם</th><th>אל</th><th>כותרת</th><th>תחילה</th><th>סיום</th><th>תאור</th><th>מאת</th><th>קובץ</th><th>קובץ רשימה</th><th>מצב</th><th>מספר רשימה</th><th>תאריך קליטה</th></thead>"
    table +="<tbody>"
    for (eachrow of resobj[1]){

        reffile = ""
        if(eachrow.filename == ""){
            reffile = ""
        }
        else{
            reffile = `<a href="#" onclick="myfunc.getfilerunind(${eachrow.runind},'reffile')"><img src='download.png'></a>`
        }
        
        listfile = ""
        if(eachrow.listfilename == ""){
            listfile = ""
        }
        else{
            listfile = `<a href="#" onclick="myfunc.getfilerunind(${eachrow.runind},'listfile')"><img src='download.png'></a>`
        }

        table += `<tr data-runind="${eachrow.runind}" data-empid="${eachrow.empid}">`
        table += `<td><a href="#" onclick="myfunc.loadbyrunind(${eachrow.runind})"><img src="open_in_full.png"></a></td>`
        table += `<td>${eachrow.empid}</td>`
        table += `<td>${eachrow.empname}</td>`
        table += `<td>${eachrow.addressee}</td>`
        table += `<td>${eachrow.ordercapt}</td>`
        table += `<td>${eachrow.startdate}</td>`
        table += `<td>${eachrow.enddate}</td>`
        table += `<td>${eachrow.ordertext}</td>`
        table += `<td>${eachrow.username}</td>`
        table += `<td>${reffile}</td>`
        table += `<td>${listfile}</td>`
        table += `<td>${myfunc.state[eachrow.state.toString()]}</td>`
        table += `<td>${eachrow.listnum}</td>`
        table += `<td>${eachrow.ordertime}</td>`
        table += "</tr>"
    }

    table += "</tbody></table>"
    document.getElementById("showdata_order").innerHTML = table
}

//********************************************************************************************* */
myfunc.printpdf = function(){
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    fdata.append("request","printpdf")

    fdata.append("runind",document.getElementById("runind_in").value);

    xhr.open('POST',"http://localhost:"+ui.port,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            console.log(this.responseText)

            resobj = JSON.parse(this.responseText);

            if (resobj[0] == "Error"){
                myfunc.alert(resobj[1])
            }
            else{
 
                myfunc.download(resobj[1].filename,resobj[1].orderfile)
            }
        }
        else if (this.readyState == 4 && this.status != 200){
            myfunc.alert(this.responseText)
        }
    }

    xhr.send(fdata);     
}