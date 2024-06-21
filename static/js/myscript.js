var listArray = [];

// ############## SOO-MODE##############
function mode(x){
    if (x==0){
        
        document.getElementById('1').style.display='block'
        document.getElementById('2').style.display='block'
        document.getElementById('3').style.display='block'
        document.getElementById('4').style.display='block'
        document.getElementById('5').style.display='none'
        document.getElementById('6').style.display='none'
    }else{
        
        document.getElementById('1').style.display='block'
        document.getElementById('2').style.display='none'
        document.getElementById('3').style.display='none'
        document.getElementById('4').style.display='none'
        document.getElementById('5').style.display='block'
        document.getElementById('6').style.display='block'
    }
        
}
// ############## END SOO-MODE##############





// ###################### SOO SHOW OLD SOO ##########
function show_SOO_table(){
  console.log("fddf")
  document.getElementById("SOO_table").style.display="table"
}


// ###################### END SOO SHOW OLD SOO ##########

// ############## SOO-EXAHSUT FAN##############
function exhaust(y){
    if (y==1){
        
        document.getElementById('Duty/Standby Exhaust/Return motors').style.display='none';
        document.getElementById('Duty/Standby Exhaust/Return motors label').style.display='none';
        document.getElementById("Duty/Standby Exhaust/Return motors").checked = false;
        
       
    }else{
        document.getElementById('Duty/Standby Exhaust/Return motors').style.display='inline';
        document.getElementById('Duty/Standby Exhaust/Return motors label').style.display='inline';
        // document.getElementById('VFD return label').style.display='none';
        // document.getElementById("VFD on return(PT)").checked = false;
        
        
        
    }
}
// ##############END SOO-EXAHSUT FAN##############
// ############## SOO-SCR##############
function scr(z){
    if (z==1){
        
        document.getElementById('SCR label').style.display='none';
        document.getElementById('SCR').style.display='none';
        document.getElementById("SCR").checked = false;
        
        
       
    }else if(z==2){
        document.getElementById('SCR label').style.display='inline';
        document.getElementById('SCR').style.display='inline';
        
        
        
    }
}
// ##############END SOO-SCR##############
// ############## SOO-MODEL##############
function getselectedunit1(){
  var value = document.getElementById("Model").value;
  if (value=='PETRA Package Unit'){
      console.log('PPH')
      
      document.getElementById('Emergency switch for ACCU label').style.display='none';
      document.getElementById('Emergency switch for AHU label').style.display='none';
      
      document.getElementById("Emergency switch for ACCU").checked = false;
      document.getElementById("Emergency switch for AHU").checked = false;
      document.getElementById('Emergency switch label').style.display='inline';
      
      
     
  }else if(value=='PETRA Ducted Split Unit'){
    console.log('DSP')
    document.getElementById('Emergency switch label').style.display='none';
    document.getElementById("Emergency switch").checked = false;

    document.getElementById('Emergency switch for ACCU label').style.display='inline';
      document.getElementById('Emergency switch for AHU label').style.display='inline';
      
      
      
      
  }
}
// ##############END SOO-MODEL##############
// ############## SOO-DAMPERS##############
function dampers(i){
    if (i==1){
        
        document.getElementById('Inlet damper label').style.display='inline';
        document.getElementById('Inlet damper').style.display='inline';
        
        
        
       
    }else if(i==2){
        document.getElementById('Inlet damper label').style.display='none';
        document.getElementById('Inlet damper').style.display='none';
        document.getElementById('Inlet damper').checked = false;
        
        
        
    }
}
// ##############END SOO-DAMPERS##############

// ##############SOO- controller##############
function getselectedcontroller(){
    var value = document.getElementById("sel").value;
    if (value=='Carel'){
        
        document.getElementById('Extended Keypad For(POL) label').style.display='none';
        document.getElementById('Extended Keypad For(POL)').checked = false;
        document.getElementById('Extended Keypad(PGD) label').style.display='inline';
        document.getElementById('Inverter comp Fresh label').style.display='inline';
        document.getElementById('Inverter comp non Fresh label').style.display='inline';
        document.getElementById('TH Tune Thermostat label').style.display='inline';   
    }else if(value=='Siemens'){
        document.getElementById('Extended Keypad(PGD) label').style.display='none';
        document.getElementById('Extended Keypad(PGD)').checked = false;
        document.getElementById('Inverter comp Fresh label').style.display='none';
        document.getElementById('Inverter comp Fresh').checked = false;
        document.getElementById('Inverter comp non Fresh label').style.display='none';
        document.getElementById('Inverter comp non Fresh').checked = false;
        document.getElementById('TH Tune Thermostat label').style.display='none';
        document.getElementById('TH Tune Thermostat').checked = false;
        document.getElementById('Extended Keypad For(POL) label').style.display='inline';
    }
    else{}

}
// ############## end controller##############
// ############## inverter compressor##############
function inv(i){
    
    var value = document.getElementById("sel").value;
    console.log(value)
        if (i===1 & value==='Carel'){
            console.log('carel+fresh')
            document.getElementById('Inverter comp Fresh label').style.display='inline';
            document.getElementById('Inverter comp Fresh').style.display='inline';
            document.getElementById('Inverter comp non Fresh label').style.display='none';
            document.getElementById('Inverter comp non Fresh').style.display='none';
            document.getElementById('Inverter comp non Fresh').checked = false;

        }else if(i===2 & value==='Carel'){
            console.log('carel+nonfresh')
            document.getElementById('Inverter comp Fresh label').style.display='none';
            document.getElementById('Inverter comp Fresh').style.display='none';
            document.getElementById('Inverter comp non Fresh label').style.display='inline';
            document.getElementById('Inverter comp non Fresh').style.display='inline';
            document.getElementById('Inverter comp Fresh').checked = false;
  
        }else if (value==='siemens'){
            console.log('siemens')
            document.getElementById('Inverter comp Fresh label').style.display='none';
            document.getElementById('Inverter comp Fresh').style.display='none';
            document.getElementById('Inverter comp non Fresh label').style.display='none';
            document.getElementById('Inverter comp non Fresh').style.display='none';
            document.getElementById('Inverter comp non Fresh').checked = false;
            document.getElementById('Inverter comp Fresh').checked = false;
        
            }  
        } 

// ############## end inverter compressor##############



// ############## pointlist--options##############
function myFunction() {
    // Get the checkbox
    var checkBox1 = document.getElementById("DX1");
    var checkBox2 = document.getElementById("HEATER1");
    var checkBox3 = document.getElementById("HWCTS1");
    var checkBox4 = document.getElementById("GH1");
    var checkBox5 = document.getElementById("SD1");
    var checkBox6 = document.getElementById("DPS1");
    var checkBox7 = document.getElementById("DPS3");
    var checkBox8 = document.getElementById("EF1VFD");
    var checkBox9 = document.getElementById("CWCTS1");
    var checkBox10 = document.getElementById("SF1VFD");
    var checkBox11 = document.getElementById("SR1_Failure_Alarm");
    
    if (checkBox1.checked == true){
        document.getElementById("DX2").style.display='inline';
    } else {
        document.getElementById("DX2").style.display='none';
    }

    if (checkBox2.checked == true){
        document.getElementById("HEATER2").style.display='inline';
    } else {
        document.getElementById("HEATER2").style.display='none';
    }

    if (checkBox3.checked == true){
        document.getElementById("HWCTS2").style.display='inline';
    } else {
        document.getElementById("HWCTS2").style.display='none';
    }

    if (checkBox4.checked == true){
        document.getElementById("GH2").style.display='inline';
    } else {
        document.getElementById("GH2").style.display='none';
    }

    if (checkBox5.checked == true){
        document.getElementById("SD2").style.display='inline';
    } else {
        document.getElementById("SD2").style.display='none';
    }
    if (checkBox6.checked == true){
        document.getElementById("DPS2").style.display='inline';
    } else {
        document.getElementById("DPS2").style.display='none';
    }
    if (checkBox7.checked == true){
        document.getElementById("DPS4").style.display='inline';
    } else {
        document.getElementById("DPS4").style.display='none';
    }

    if (checkBox8.checked == true){
        document.getElementById("EF2VFD").style.display='inline';
    } else {
        document.getElementById("EF2VFD").style.display='none';
    }
    if (checkBox9.checked == true){
      document.getElementById("CWCTS2").style.display='inline';
    } else {
      document.getElementById("CWCTS2").style.display='none';
    }
    if (checkBox10.checked == true){
      document.getElementById("SF2VFD").style.display='inline';
      console.log("fsdfsdf")
    } else {
      document.getElementById("SF2VFD").style.display='none';
    }
    if (checkBox11.checked == true){
      console.log("fsdfsdf")
      document.getElementById("SR2_Failure_Alarm").style.display='inline';
    } else {
      document.getElementById("SR2_Failure_Alarm").style.display='none';
    }

  }

// ##############END pointlist--options##############

function tt(){
    console.log('in here in')
    let value=document.getElementById("alarm_message").value
    console.log(value)
    if (value !== ''){
      console.log(value)
      console.log("hello here2323")
      alert("soo already exist with same name and same country, please change them to accept it")

    }
  
   
 
  
}

///// ############## point list --UNIT MODEL'S SENSORS############
function getselectedunit(){
    var unit = document.getElementById("UModelPL").value;
    
    if (unit=='PPH'){
        console.log("pph")
        document.getElementById('CCWCTS').style.display='none';
        document.getElementById('CWCTS1').checked = false;
        document.getElementById('WFS').style.display='none';
        document.getElementById('WATER FLOW SWITCH FAULT1').checked = false;
        document.getElementById('SR').style.display='inline';
        
        
        
          
    }else if(unit=='WPPH'){
        console.log("wpph")
        document.getElementById('CCWCTS').style.display='inline';
        document.getElementById('WFS').style.display='inline';
        document.getElementById('SR').style.display='none';
        document.getElementById('SR1 Failure Alarm').checked = false;
        
      
    }
    else{
      document.getElementById('CCWCTS').style.display='inline';
      document.getElementById('WFS').style.display='inline';
      document.getElementById('SR').style.display='inline';
    }

}



// #################SOO-TABLE FILTER#############
document.addEventListener("DOMContentLoaded",()=>{
  document.querySelectorAll(".search-input").forEach(inputField =>{
    const tableRows = inputField.closest("table").querySelectorAll("tbody tr");
    const headercell=inputField.closest("th");
    const otherheadercells=inputField.closest("tr").querySelectorAll("th");
    const columnindex=Array.from(otherheadercells).indexOf(headercell);
    const searchablecells=Array.from(tableRows).map(row => row.querySelectorAll("td")[columnindex]);
    inputField.addEventListener("input",() =>{
      const searchquery=inputField.value.toLowerCase();

      for (const tablecell of searchablecells){
        const row=tablecell.closest("tr");
        const values=tablecell.textContent.toLocaleLowerCase().replace("," , "");
        row.style.visibility=null;
        if(values.search(searchquery) === -1){
          row.style.visibility="collapse";
        }
      }
    })

    
  });
});
// #################END SOO-TABLE FILTER#############

// ###################### HEATER SHOW TABLE ##########


function show_heater_table(){
  console.log("fddf")
  // document.getElementById("heater_table").style.display="table"
  document.getElementById("heater_sides1").style.display="inline"
  document.getElementById("heater_sides2").style.display="inline"
  document.getElementById("table_output").style.display="inline"
}


// ###################### END HEATER SHOW TABLE  ##########

window.onload = function(){
  var modal = document.getElementById("myModal");
  var btn1 = document.getElementById("New_User");
  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];
  btn1.onclick = function() {
    
    console.log("fsdfsdf")
    modal.style.display = "block";
    
  }



  span.onclick = function() {
    modal.style.display = "none";
  }

  document.getElementById("close-button").addEventListener('click',function(e){
    modal.style.display = "none";
  })


}





//###################components add more compressors#################
$(document).ready(function() {

 

  var x = 0; //initlal text box count
  
  $('#co_voltage').change(function(){ 
    
    var co_voltage = $('#co_voltage').find(":selected").val();
  if (co_voltage==='208V-3-60Hz' || co_voltage==='220V-3-60Hz'||co_voltage==='230V-3-60Hz'){

    $('#co_add_compressor_220').css('display','inline');
    $('#co_add_compressor_460').css('display','none');  
    $('#co_add_fans_220').css('display','inline');
    $('#co_add_fans_460').css('display','none'); 
   
  }
  else if(co_voltage==='460V-3-60Hz' ||co_voltage==='480V-3-60Hz'){

    $('#co_add_compressor_220').css('display','none');
    $('#co_add_compressor_460').css('display','inline');  
    $('#co_add_fans_220').css('display','none');
    $('#co_add_fans_460').css('display','inline');
  
  }
  else{
    $(".newcompressors").empty();
    $('#co_add_compressor_220').css('display','none');
    $('#co_add_compressor_460').css('display','none');
    $('#co_add_fans_220').css('display','none');
    $('#co_add_fans_460').css('display','none'); 
  }


  var max_fields      = 5; //maximum input boxes allowed
  var add_button_220     = $(".co_add_compressor_220"); //Add button-220 ID
  var add_button_460     = $(".co_add_compressor_460"); //Add button-460 ID
  var newdiv=$(".newcompressors");

  
  $(add_button_460).click(function(e){ //on add input button click
    e.preventDefault();
    if(x <= max_fields){ //max input box allowed
      x++; //text box increment
      var input1 =  '<div><select class="co_comp_brand" name="co_comp_brand[]" id="co_comp_brand'+x+'" required>\
                        <option value="--">--</option>\
                        <option value="Danfoss">Danfoss</option>\
                        <option value="Copeland">Copeland</option>\
                      </select>\
                      <select class="co_comp_hp_460" name="co_comp_hp_460[]" id="co_comp_hp_460'+x+'" required>\
                        <option value="--">--</option>\
                        <option value="10">10HP</option>\
                        <option value="13">13HP</option>\
                        <option value="15">15HP</option>\
                        <option value="25">25HP</option>\
                      </select>\
                      <select class="co_comp_460" name="co_comp_460[]" id="co_comp_460'+x+'" required>\
                        <option value="--">--</option>\
                        <option value="ZP120_KCE_TFD">ZP120-KCE-TFD</option>\
                        <option value="ZPD120_KCE_TFD">ZPD120-KCE-TFD</option>\
                        <option value="VZH088AGANA">VZH088AGANA</option>\
                        <option value="VZH117AGANA">VZH117AGANA</option>\
                        <option value="SH161-A4ALC">SH161-A4ALC</option>\
                        <option value="ZP182_KCE_TWD">ZP182-KCE-TWD</option>\
                        <option value="ZP295_KCE_TWC">ZP295-KCE-TWC</option>\
                        <option value="ZP296_KCE_TE5">ZP296-KCE-TE5</option>\
                      </select>\
                      <button class="btn btn-outline-danger remove_field" type="button">Remove</button>\
                      <br></div>'
      $(newdiv).append(input1);
     
    }
                      
  else{
    alert('You can add maximum 6 input fields.');
  }
  
  return false
});



///////////////////////////////////////

$(document).on("change",".co_comp_brand", function(e){ 
  e.preventDefault();
  $(this).nextAll(".co_comp_hp_460").val('--');
  $(this).nextAll(".co_comp_460").val('--');
  $(this).nextAll(".co_comp_hp_460").find("option").show();
  $(this).nextAll(".co_comp_460").find("option").show();
  var brand=$(this).find(":selected").val();
  
  if (brand==="Copeland"){
    // console.log(this);
    
    $(this).nextAll(".co_comp_hp_460").find("option[value='10']").show();
    $(this).nextAll(".co_comp_hp_460").find("option[value='13']").show();
    $(this).nextAll(".co_comp_hp_460").find("option[value='15']").show();
    $(this).nextAll(".co_comp_hp_460").find("option[value='25']").show();

  }
  else if(brand==="Danfoss"){
    // console.log(this);
    $(this).nextAll(".co_comp_hp_460").find("option[value='13']").show();
    $(this).nextAll(".co_comp_hp_460").find("option[value='15']").show();
    $(this).nextAll(".co_comp_hp_460").find("option[value='10']").hide();
    $(this).nextAll(".co_comp_hp_460").find("option[value='25']").hide();
  }
  else{
    $(this).nextAll(".co_comp_hp_460").find("option[value='10']").show();
    $(this).nextAll(".co_comp_hp_460").find("option[value='13']").show();
    $(this).nextAll(".co_comp_hp_460").find("option[value='15']").show();
    $(this).nextAll(".co_comp_hp_460").find("option[value='25']").show();
  }
});


/////////////////////////////////////////////////////
$(document).on("change",".co_comp_hp_460", function(){ 
  var brand = $(this).prevAll(".co_comp_brand").val();
  console.log(brand);
  var comp_hp_460 = $(this).find(":selected").val();
  console.log(comp_hp_460);


  if (comp_hp_460==="10" & brand==="Copeland"){
    $(this).nextAll(".co_comp_460").find("option").hide();
    $(this).nextAll(".co_comp_460").find("option[value='ZP120_KCE_TFD']").show();
    $(this).nextAll(".co_comp_460").find("option[value='ZPD120_KCE_TFD']").show();
    
    // console.log(this);
  }
  else if(comp_hp_460==="25" & brand==="Copeland"){
    $(this).nextAll(".co_comp_460").find("option").hide();
    $(this).nextAll(".co_comp_460").find("option[value='ZP295_KCE_TWC']").show();
    $(this).nextAll(".co_comp_460").find("option[value='ZP296_KCE_TE5']").show();
    
    // console.log(this);
  }
  else if(comp_hp_460==="13" & brand==="Danfoss"){
    $(this).nextAll(".co_comp_460").find("option").hide();
    $(this).nextAll(".co_comp_460").find("option[value='VZH088AGANA']").show();
    $(this).nextAll(".co_comp_460").find("option[value='SH161-A4ALC']").show();
    
    
    
    // console.log(this);
  }
  else if(comp_hp_460==="15" & brand==="Danfoss"){
    // $(this).nextAll(".co_comp_460").find("option").hide();
    // $(this).nextAll(".co_comp_460").find("option[value='VZH117AGANA']").show();
    $(this).nextAll(".co_comp_460").val('VZH117AGANA')

  }
  else if(comp_hp_460==="15" & brand==="Copeland"){
    $(this).nextAll(".co_comp_460").find("option").hide();
    $(this).nextAll(".co_comp_460").find("option[value='ZP182_KCE_TWD']").show();
    $(this).nextAll(".co_comp_460").find("option[value='VZH117AGANA']").show();


  }

  });

/////////////////////////////////////////////////////

  $(add_button_220).click(function(e){ //on add input button click
  e.preventDefault();
  
      if(x <= max_fields){ //max input box allowed
          x++; //text box increment
          var input1 =  '<div><select class="co_comp_brand" name="co_comp_brand[]" id="co_comp_brand'+x+'" required>\
                            <option value="--">--</option>\
                            <option value="Danfoss">Danfoss</option>\
                            <option value="Copeland">Copeland</option>\
                          </select>\
                          <select class="co_comp_hp_220" name="co_comp_hp_220[]" id="co_comp_hp_220'+x+'" required>\
                            <option value="--">--</option>\
                            <option value="4">4HP</option>\
                            <option value="5">5HP</option>\
                            <option value="8">8HP</option>\
                            <option value="9">9HP</option>\
                            <option value="10">10HP</option>\
                            <option value="12">12HP</option>\
                            <option value="13">13HP</option>\
                            <option value="15">15HP</option>\
                            <option value="20">20HP</option>\
                            <option value="25">25HP</option>\
                            <option value="30">30HP</option>\
                          </select>\
                          <select class="co_comp_220" name="co_comp_220[]" id="co_comp_220'+x+'" required>\
                            <option value="--">--</option>\
                            <option value="SH120_A3ABE">SH120-A3ABE</option>\
                            <option value="SH161_A3_ALC/I/P06">SH161-A3-ALC/I/P06</option>\
                            <option value="SH184_A3ALC">SH184-A3ALC</option>\
                            <option value="SH240_A3ABE_D/P11">SH240-A3ABE-D/P11</option>\
                            <option value="SH295_A3ABE_D/P11">SH295_A3ABE_D/P11</option>\
                            <option value="SH380_A3ABE_D/P11">SH380-A3ABE-D/P11</option>\
                            <option value="ZP61_KCE_TF5">ZP61-KCE-TF5</option>\
                            <option value="ZP90_KCE_TF7">ZP90-KCE-TF7</option> \
                            <option value="ZP103_KCE_TF5">ZP103-KCE-TF5</option> \
                            <option value="ZP120_KCE_TF5">ZP120-KCE-TF5</option> \
                            <option value="ZP137_KCE_TF5">ZP137-KCE-TF5</option> \
                            <option value="ZP154_KCE_TE5">ZP154-KCE-TE5</option> \
                            <option value="ZP182_KCE_TW5">ZP182-KCE-TW5</option> \
                            <option value="ZP236_KCE_TE5">ZP236-KCE-TE5</option> \
                            <option value="ZP296_KCE_TE5">ZP296-KCE-TE5</option> \
                            <option value="ZP385_KCE_TE5">ZP385-KCE-TE5</option> \
                            <option value="VZH035CJANB">VZH035CJANB</option> \
                            <option value="VZH044CJANB/M">VZH044CJANB/M</option> \
                            <option value="VZH065CJANB">VZH065CJANB</option> \
                            <option value="VZH088BJANA/I/P06">VZH088BJANA/I/P06</option> \
                            <option value="VZH088CJAN">VZH088CJAN</option> \
                          </select>\
                          <button class="btn btn-outline-danger remove_field" type="button">Remove</button>\
                          <br></div>'
          $(newdiv).append(input1);
         
        }
                          
      else{
        alert('You can add maximum 6 input fields.');
      }
      
      return false
  });
//////////////////////////////////////////////////
  $(document).on("change",".co_comp_brand", function(e){ 
    e.preventDefault();
    $(this).nextAll(".co_comp_hp_220").val('--');
    $(this).nextAll(".co_comp_220").val('--');
    var brand=$(this).find(":selected").val();
    
    if (brand==="Copeland"){
      // console.log(this);
      
      $(this).nextAll(".co_comp_hp_220").find("option[value='4']").hide();
      $(this).nextAll(".co_comp_hp_220").find("option[value='5']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='8']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='9']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='10']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='12']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='13']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='15']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='20']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='25']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='30']").show();


    }
    else if(brand==="Danfoss"){
      // console.log(this);
      $(this).nextAll(".co_comp_hp_220").find("option[value='4']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='5']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='8']").hide();
      $(this).nextAll(".co_comp_hp_220").find("option[value='9']").hide();
      $(this).nextAll(".co_comp_hp_220").find("option[value='10']").hide();
      $(this).nextAll(".co_comp_hp_220").find("option[value='12']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='13']").hide();
      $(this).nextAll(".co_comp_hp_220").find("option[value='15']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='20']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='25']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='30']").show();

     
       
    
    }
    else{
      $(this).nextAll(".co_comp_hp_220").find("option[value='4']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='5.58']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='5']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='8']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='9']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='10']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='12']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='13']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='15']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='20']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='25']").show();
      $(this).nextAll(".co_comp_hp_220").find("option[value='30']").show();
      
    }
    
  });
       
    $(document).on("change",".co_comp_hp_220", function(){ 
      var brand = $(this).prevAll(".co_comp_brand").val();
      console.log(brand);
      var comp_hp_220 = $(this).find(":selected").val();
      console.log(comp_hp_220);


      if (comp_hp_220==="5" & brand==="Copeland"){
        
        $(this).nextAll(".co_comp_220").val('ZP61_KCE_TF5');
        // console.log(this);
      }

      else if(comp_hp_220==="8" & brand==="Copeland"){
        $(this).nextAll(".co_comp_220").val('ZP90_KCE_TF7');
      }
      else if(comp_hp_220==="9" & brand==="Copeland"){
        $(this).nextAll(".co_comp_220").val('ZP103_KCE_TF5');
      }
      else if(comp_hp_220==="10"& brand==="Copeland" ){
        $(this).nextAll(".co_comp_220").val('ZP120_KCE_TF5');
      }
      else if(comp_hp_220==="12"& brand==="Copeland" ){
        $(this).nextAll(".co_comp_220").val('ZP137_KCE_TF5');
      }
      else if(comp_hp_220==="13" & brand==="Copeland"){
        $(this).nextAll(".co_comp_220").val('ZP154_KCE_TE5');
      }
      else if(comp_hp_220==="15" & brand==="Copeland"){
        $(this).nextAll(".co_comp_220").val('ZP182_KCE_TW5');
        
      }
      else if(comp_hp_220==="20" & brand==="Copeland"){
        $(this).nextAll(".co_comp_220").val('ZP236_KCE_TE5');
      }
      else if(comp_hp_220==="25" & brand==="Copeland"){
        $(this).nextAll(".co_comp_220").val('ZP296_KCE_TE5');
      }
      else if(comp_hp_220==="30" & brand==="Copeland"){
        $(this).nextAll(".co_comp_220").val('ZP385_KCE_TE5');
      }
      else if(comp_hp_220==="4"& brand==="Danfoss"){
        $(this).nextAll(".co_comp_220").val('VZH035CJANB');
      }
      else if(comp_hp_220==="5" & brand==="Danfoss"){
        $(this).nextAll(".co_comp_220").val('VZH044CJANB/M');
      }
      else if(comp_hp_220==="12" & brand==="Danfoss"){
        $(this).nextAll(".co_comp_220").val('VZH065CJANB');
      }
      else if(comp_hp_220==="15" & brand==="Danfoss"){
        $(this).nextAll(".co_comp_220").val('VZH088BJANA/I/P06');
      }
      else if(comp_hp_220==="20" & brand==="Danfoss"){
        $(this).nextAll(".co_comp_220").val('SH240_A3ABE_D/P11');
      }
      else if(comp_hp_220==="25" & brand==="Danfoss"){
        $(this).nextAll(".co_comp_220").val('SH295_A3ABE_D/P11');
      }
      else if(comp_hp_220==="30" & brand==="Danfoss"){
        $(this).nextAll(".co_comp_220").val('SH380_A3ABE_D/P11');
      }
      else{
        $(this).nextAll(".co_comp_220").val('--');
      }
      
    });
   

 
 
////////////////////////////////////////////////////////////////

  $(document).on("click",".remove_field", function(e){ //user click on remove text
    
    e.preventDefault(); 
    $(this).parent('div').remove(); 
    x--;
   
    
    return false
    });

/////////// condser fans///////////////
  $(document).on("change","#co_cond", function(e){ 

    var cond_model = $(this).find(":selected").val();
    console.log(cond_model);
    if (cond_model!=="No Condenser Fans" & cond_model!==" "){
      $(this).nextAll("#co_cond_qty").css("display","inline")
      $(this).nextAll("#co_cond_vee").css("display","inline")
      $(this).nextAll("#co_cond_speed").css("display","inline")
    }
    else{
      $(this).nextAll("#co_cond_qty").hide();
      $(this).nextAll("#co_cond_vee").hide();
      $(this).nextAll("#co_cond_speed").hide();
    }

  });
///////////end condser fans///////////////



/////////////////supply fan /////////////////
var x2=0
var max_fields1      = 2; //maximum input boxes allowed
var co_add_fans     = $(".co_add_fans"); //Add button-fans ID

var newdiv1=$(".newfans");


$(co_add_fans).click(function(e){ //on add input button click
  e.preventDefault();
 
      if(x2 <= max_fields1){ //max input box allowed
          x2++; //text box increment
          var input2 =  '<div><select class="co_fans_type" name="co_fans_type[]" id="co_fans_type'+x2+'" required>\
                            <option value="--">--</option>\
                            <option value="Supply">Supply</option>\
                            <option value="Exhaust">Exhaust</option>\
                            <option value="Return">Return</option>\
                            <option value="E.wheel">E.wheel</option>\
                          </select>\
                          <select class="co_fans_hp" name="co_fans_hp[]" id="co_fans_hp'+x2+'" required>\
                            <option value="--">--</option>\
                            <option value="2HP">2HP</option>\
                            <option value="3HP">3HP</option>\
                            <option value="5HP">5HP</option>\
                            <option value="7.5HP">7.5HP</option>\
                            <option value="15HP">15HP</option>\
                          </select>\
                          <select class="co_ew_model" name="co_ew_model[]" id="co_ew_model'+x2+'" required>\
                            <option value="--">--</option>\
                            <option value="PAC1100">PAC1100</option>\
                            <option value="PAC1700">PAC1700</option>\
                            <option value="PAC1900">PAC1900</option>\
                          </select>\
                          <input type="number" step="any" id="co_fans_qty" name="co_fans_qty[]" placeholder="QTY" required>\
                          <select class="co_fansvfd" name="co_fansvfd[]" id="co_fansvfd'+x2+'" required>\
                            <option value="--">--</option>\
                            <option value="ACH580‐01‐047A-208V[RECN3013022]">ACH580‐01‐047A-208V[RECN3013022]</option>\
                            <option value="ACH580-01-03A4-4-460V[RECN3005010]">ACH580-01-03A4-4-460V[RECN3005010]</option>\
                            <option value="ACH580-01-05A7-4-460V[RECN3007016]">ACH580-01-05A7-4-460V[RECN3007016]</option>\
                            <option value="ACH580-01-09A5-4-460V[RECN3009019]">ACH580-01-09A5-4-460V[RECN3009019]</option>\
                            <option value="ACH580-01-12A7-4-460V[RECN3010016]">ACH580-01-12A7-4-460V[RECN3010016]</option>\
                            <option value="ACH580-01-026A-4-460V[RECN3013021]">ACH580-01-026A-4-460V[RECN3013021]</option>\
                          </select>\
                          <button class="btn btn-outline-danger remove_field" type="button">Remove</button>\
                          <br></div>'
          $(newdiv1).append(input2);
         
        }
                          
      else{
        alert('You can add maximum 3 input fields.');
      }
      
      return false
  });
  //////////////////////////////////
  $(document).on("click",".remove_field", function(e){ //user click on remove text
    e.preventDefault(); 
    $(this).parent('div').remove(); 
    x2--;
    return false
    });
//////////////////////////////////////////////

///////////////////////////////////////////

$(document).on("change",".co_fans_type", function(){ 
  var co_fans_type = $(this).find(":selected").val();
  if (co_fans_type==="E.wheel"){
    $(this).nextAll(".co_fans_hp").hide();
    $(this).nextAll(".co_ew_model").show();
    $(this).nextAll(".co_fansvfd").val('ACH580-01-03A4-4-460V[RECN3005010]');
  }
  else if(co_fans_type==="Supply"){
    $(this).nextAll(".co_ew_model").hide();
    $(this).nextAll(".co_fans_hp").show();
    console.log("fddf")
  }
  else if(co_fans_type==="Exhaust"){
    $(this).nextAll(".co_ew_model").hide();
    $(this).nextAll(".co_fans_hp").show();
   
  }
  else if(co_fans_type==="Return"){
    $(this).nextAll(".co_ew_model").hide();
    $(this).nextAll(".co_fans_hp").show();
   
  }
});
///////////////////////////////////////
 
    

$(document).on("change",".co_fans_hp", function(){ 

  var fans_hp = $(this).find(":selected").val();
  if (fans_hp==="2HP" & co_voltage!=="460V-3-60Hz" & co_voltage!=="480V-3-60Hz"){
    $(this).nextAll(".co_fansvfd").val('ACH580-01-05A7-4-460V[RECN3007016]');
  }
  else if (fans_hp==="3HP" & co_voltage!=="208V-3-60Hz" & co_voltage!=="220V-3-60Hz" & co_voltage!=="230V-3-60Hz"){
    $(this).nextAll(".co_fansvfd").val('ACH580-01-09A5-4-460V[RECN3009019]');
  }
  else if (fans_hp==="7.5HP" & co_voltage!=="208V-3-60Hz" & co_voltage!=="220V-3-60Hz" & co_voltage!=="230V-3-60Hz"){
    $(this).nextAll(".co_fansvfd").val('ACH580-01-12A7-4-460V[RECN3010016]');
  }
  
  else if (fans_hp==="15HP" & co_voltage!=="460V-3-60Hz" & co_voltage!=="480V-3-60Hz"){
    $(this).nextAll(".co_fansvfd").val('ACH580‐01‐047A-208V[RECN3013022]');
  }
  else if (fans_hp==="15HP" & co_voltage!=="208V-3-60Hz" & co_voltage!=="220V-3-60Hz" & co_voltage!=="230V-3-60Hz"){
    $(this).nextAll(".co_fansvfd").val('ACH580-01-026A-4-460V[RECN3013021]');
  }
  });

});

// $('#find_code_form').on("submit", function(){ 
//   $('#open_it_as_excel').show();
// });



 
});



// function myFunction() {
//   document.getElementById("myDropdown").classList.toggle("show");
// }

function filterFunction() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("li");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

// ################### end Components##############

// ###################### find_code ##########
function show_find_code_table(){
  console.log("fddf")
  document.getElementById("find_code_table").style.display='inline';
  document.getElementsByClassName(".hidden_anchor").style.display='inline';
}



///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


/////////////////add suppliers emails/////////////////
var x3=0
var max_fields2      = 6; //maximum input boxes allowed
var add_emails_btn     = $(".add_emails_btn"); //Add emails button ID

var newdiv2=$(".suppliers_emails");


$(add_emails_btn).click(function(e){ //on add input button click
  e.preventDefault();
 
      if(x3 <= max_fields2){ //max input box allowed
          x3++; //text box increment
          var input3 =  '<div>\
                          <input type="text"  id="emails_texts'+x3+'" name="emails_texts[]" placeholder="write email'+x3+'" required>\
                          <button class="btn btn-outline-danger remove_field_emails" type="button">Remove</button>\
                          <br></div>'
          $(newdiv2).append(input3);
         
        }
                          
      else{
        alert('You can add maximum 6 input fields.');
      }
      
      return false
  });

  //////////////////////////////////
  $(document).on("click",".remove_field_emails", function(e){ //user click on remove text
    e.preventDefault(); 
    $(this).parent('div').remove(); 
    x3--;
    return false
    });
  //////////////////////////////////

 


// ###################### END  ##########


