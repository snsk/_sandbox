
var someObject = (function(){
    var fieldA = "fieldA";
    var fieldB = "fieldB";

    function _init(){
	//initialize
    }

    function _getFieldA(){
	return fieldA;
    }

    function _getFieldB(){
	return fieldB;
    }

    function _makeCatString(){
	return fieldA + fieldB;
    }

    _init();

    return{ //Public API List
	getFieldA : _getFieldA,
	getFieldB : _getFieldB
    };

})();

