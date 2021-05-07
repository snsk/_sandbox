//usage:
ocument.onkeydown = konamiCommandChecker;

//body
function konamiCommandChecker(e){
        var commandArray = new Array();
        var correctArray = new Array(38, 38, 40, 40, 37, 39, 37, 39, 66, 65);
        var hitCount = 0;
	commandArray.push(e.keyCode);
	if(commandArray[commandArray.length-1] == correctArray[commandArray.length-1]){
		hitCount++;
	}else{
		hitCount = 0;
		commandArray = new Array();
	}
	if(hitCount > 9){
		alert("fire!");
		hitCount = 0;
		commandArray = new Array();
	}
}
