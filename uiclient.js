ui = new Object();

ui.port = 50000

ui.user = ''

//********************************************************************************** */
window.addEventListener('beforeunload',function(event){ //when closing browser, close python
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    fdata.append("request",'close'); //prepare files

    xhr.open('POST',"http://localhost:"+ui.port, true);

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(xhr.responseText);
        }
    };
    
    xhr.send(fdata);
    
})
//********************************************************************************** */
window.addEventListener('load',function(event){
    ui.onloadfunc()
})
//******************************************************************************************** */

ui.onloadfunc = function(){

    var xhr = new XMLHttpRequest();
    var fdata = new FormData();

    fdata.append("request",'hrdirective'); //parol

    xhr.open('POST',"http://localhost:"+ui.port, true);

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(xhr.responseText);

            res = JSON.parse(xhr.responseText);

            ui.port = res.port;

            ui.user = res.args.user

            if (res.args.user == 'constanting'){
                ui.navbarshow(1)
            }
            else if (res.args.user == 'gidonz'){
                ui.navbarshow(2)
            }
            else {
                ui.navbarshow(1)
            }
            

            for (let each of resobj[0]){
                dlstr += '<option value = ' + each[0] + '>'
            }
            document.getElementById("dept_list").innerHTML = dlstr;

            dlstr = "";

            for (let each of resobj[1]){
                dlstr += '<option value = ' + each[0] + '>'
            }
            document.getElementById("primetype_list").innerHTML = dlstr;
        }
    };
    
    xhr.send(fdata);
}

//*********************************************************************************** */
ui.submit_basic = function(){ //request can be insert or update
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
                ui.download(resobj[0],resobj[1])
            }
        }
    }

    xhr.send(fdata);     
}


//********************************************************************************************* */
ui.download = function(filename, filetext){

    var a = document.createElement("a");

    document.body.appendChild(a);

    a.style = "display: none";

    a.href = 'data:application/octet-stream;base64,' + filetext;

    a.download = filename;

    a.click();

    document.body.removeChild(a);

}

//************************************************************************************ */
ui.navbarshow = function(choiseid){
    var navas = document.getElementsByClassName("a_navbar"); 

    if (choiseid==1){
        document.getElementById("navbar_order").style.display = 'block';
        document.getElementById("navbar_authorize").style.display = 'none';        
    }
    else if (choiseid==2){
        document.getElementById("navbar_order").style.display = 'none';
        document.getElementById("navbar_authorize").style.display = 'block';
    }

    for (i=0;i<navas.length;i++){
        if (navas[i].id == "navbar"+choiseid)
            navas[i].classList.add("active");
        else{
            navas[i].classList.remove("active");
        }
    }
}
//********************************************************************************************* */
ui.getempname = function(calltype = "onchange"){
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();
    var dlstr1 = "";
    var dlstr2 = "";

    if (calltype == "onchange"){
        if (document.getElementById("empid_in").value == 9){
            document.getElementById("empname_in").value = "רשימה";
            document.getElementById("reshimatxt_in").style.display = 'block';
        }
        else{
            fdata.append("func","getempname");
            fdata.append("empid",document.getElementById("empid_in").value);
            document.getElementById("reshimatxt_in").style.display = 'none';
            ui.loadprevorders();               
        }
    }
    else if (calltype == "oninput"){
        if (document.getElementById("empname_in").value == "רשימה"){
            document.getElementById("reshimatxt_in").style.display = 'block';
            document.getElementById("empid_in").value = 9
        }
        else{
            fdata.append("func","searchname");
            fdata.append("empname",document.getElementById("empname_in").value);
            document.getElementById("reshimatxt_in").style.display = 'none';       
        }
    }

    xhr.open('POST',ui.host,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            resobj = JSON.parse(this.responseText);

            console.log(resobj);

            if (calltype == "onchange"){
                document.getElementById("empname_in").value = resobj[0];    
            }
            
            else if (calltype == "oninput"){

                for (let each of resobj){
                    dlstr1 += '<option value = ' + each[0] + '>'
                    dlstr2 += '<option value = "' + each[1] + '">'
                }
                document.getElementById("empid_list").innerHTML = dlstr1;
                document.getElementById("empname_list").innerHTML = dlstr2;
            }
        }
    }

    xhr.send(fdata);
}
//********************************************************************************************** */
ui.loadprevorders = function(){
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();
    var dlstr = '<tbody>';

    document.getElementById("reshimatxt_in").style.display = 'none';

    fdata.append("func","loadprevorders");
    fdata.append("empid",document.getElementById("empid_in").value);

    xhr.open('POST',ui.host,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            resobj = JSON.parse(this.responseText);

            console.log(resobj);

            dlstr += "<tr><th>סוג הוראה</th><th>תחילה</th><th>סיום</th><th>הוראה</th><th>תאריך הוראה</th><th>בוצעה</th></tr>"

            for (let each of resobj){
                dlstr += "<tr>"
                
                for(var i=0;i<6;i++){
                    dlstr += "<td>" + each[i] + '</td>'
                }
                dlstr += "</tr>"
            }

            dlstr += "</tbody>"
            
            document.getElementById("prevorders").innerHTML = dlstr;
        }
    }

    xhr.send(fdata);
}
//*********************************************************************************** */
ui.submit_temp = function(){ //request can be insert or update
    var xhr = new XMLHttpRequest();
    var fdata = new FormData();
    var fileobj = document.getElementById("reffiles_in").files;

    fdata.append("func","inserttemporder");
    
    fdata.append("department",document.getElementById("dept_in").value);

    fdata.append("primetype",document.getElementById("primetype_in").value);

    fdata.append("subtype",document.getElementById("subtype_in").value);

    fdata.append("empid",document.getElementById("empid_in").value);

    fdata.append("empname",document.getElementById("empname_in").value);

    fdata.append("startin",document.getElementById("start_in").value);

    fdata.append("endin",document.getElementById("end_in").value);

    fdata.append("textin",document.getElementById("text_in").value);

    fdata.append("referencein",document.getElementById("reference_in").value);

    if (document.getElementById('reshimatxt_in') != undefined && document.getElementById('reshimatxt_in').style.display == 'block'){ //if reshima exists
        fdata.append("reshimatxt",document.getElementById("reshimatxt_in").value);   
    }

    for (var i = 0; i < fileobj.length; i++){
        
        fdata.append("docfile" + i, fileobj[i]);
    }

    xhr.open('POST',ui.host,true)

    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {   
            resobj = JSON.parse(this.responseText);

            console.log(resobj);

            window.alert(resobj);
        }
    }

    xhr.send(fdata);     
}
//***************************************************************************************** */
ui.reshima = function(){
    
    var reshimatxt = document.getElementById("reshimatxt_in");
    
    if(reshimatxt.style.display=='none'){
        reshimatxt.style.display = 'block'
    }
    else{
        reshimatxt.style.display = 'none'
    }

}

//***************************************************************************************** */
ui.clearcells = function(){
    var inputs = document.getElementsByTagName('input');

    for(var i=0; i<inputs.length; i++){
        inputs(i).value = '';
    }
    
    document.getElementById("reshimatxt_in").value = '';
}

//****************************************************************************************** */

