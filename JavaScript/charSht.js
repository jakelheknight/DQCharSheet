
function updatePrimary(){
	//Calculate all values.
	//Calculating FT
	var ENtot = EN;
	var FT = 0;	    
	if(ENtot >= 3 && ENtot <= 4){
        	FT = 16;   
    	} 
    	else if( ENtot <= 7){
        	FT = 17;   
    	} 
    	else if( ENtot <= 10){
        	 FT = 18;   
    	} 
    	else if( ENtot <= 13){
        	 FT = 19;   
    	} 
    	else if( ENtot <= 16){
        	 FT = 20;   
    	} 
    	else if( ENtot <= 19){
        	 FT = 21;   
    	} 
    	else if( ENtot <= 22){
        	 FT = 22;   
    	} 
    	else if( ENtot <= 25){
        	 FT = 23;   
    	} 
    	else if(ENtot >= 27){
        	 FT = 24;   
    	}
	//Calculating TMR
	var AGtot = AG;	
	var TMR = 0;
	if(AGtot >= 3 && AGtot <=4 ){
    	    var TMR = 2;   
	}
	else if( AGtot <=8 ){
        	var TMR = 3;   
    	}
    	else if( AGtot <=12 ){
        	var TMR = 4;  
    	}
    	else if( AGtot <=17 ){
        	var TMR = 5;   
    	}
    	else if( AGtot <=21 ){
       		var TMR = 6;   
    	}
    	else if( AGtot <=25 ){
        	var TMR = 7;   
    	}
    	else if( AGtot <=27 ){
        	var TMR =  8;  
    	}
	PC = 8;
	//Place values in table
	document.getElementById("PS").innerHTML = PS;
        document.getElementById("MD").innerHTML = MD
        document.getElementById("AG").innerHTML = AG;
        document.getElementById("MA").innerHTML = MA;
        document.getElementById("WP").innerHTML = WP;
        document.getElementById("EN").innerHTML = EN;
        document.getElementById("FT").innerHTML = FT;
        document.getElementById("TMR").innerHTML = TMR;
	document.getElementById("DEFtot").innerHTML = MD;
	document.getElementById("charName").innerHTML = Name;
	document.getElementById("PC").innerHTML = PC;
	document.getElementById("PB").innerHTML = PB;
	document.getElementById("Race").innerHTML = Race;
	document.getElementById("Aspect").innerHTML = Aspect;
	document.getElementById("Social").innerHTML = Social;
	document.getElementById("Birth").innerHTML = Birth;
	document.getElementById("Hand").innerHTML = Hand;
	document.getElementById("FTtot").innerHTML = FT;
	document.getElementById("ENtot").innerHTML = EN;
	
}
function updateFN(){
	updatePrimary();
}
function damageEN(){
	var ENtmp = document.getElementById("ENtot").innerHTML;
		document.getElementById("ENtot").innerHTML = ENtmp-1;
}
function damage(){
	var FTtmp = document.getElementById("FTtot").innerHTML;
	if(FTtmp > 0){
		document.getElementById("FTtot").innerHTML = FTtmp-1;
	}else{
	damageEN();
	}
}
