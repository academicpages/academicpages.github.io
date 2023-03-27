(function() {
	dataProcessor = {};
	var attributeMap = {};

	dataProcessor.processFile = function (dataFile,att) {
		d3.csv(dataFile, function(error, data) {
			for(var attribute in data[0]){
	            attributeMap[attribute] = {
	                'domain':[],
	                'isNumeric':'',
	                'isCategorical':''
	            };
	        }
            for(var i in data){
                var d = data[i];
                for(var attribute in attributeMap){
                    if(isNaN(d[attribute])){
                        attributeMap[attribute]['isCategorical'] = '1';
                        attributeMap[attribute]['isNumeric'] = '0';
                    }else{
                        attributeMap[attribute]['isNumeric'] = '1';
                        attributeMap[attribute]['isCategorical'] = '0';
                    }
                    attributeMap[attribute]['domain'].push(d[attribute]);
                }
            }
            for(var attribute in attributeMap){
                var valueSet = [];
                $.each(attributeMap[attribute]['domain'], function(i, el){
                    if($.inArray(el, valueSet) === -1) valueSet.push(el);
                });
                attributeMap[attribute]['domain'] = valueSet;
                if(valueSet.length<=12 && attributeMap[attribute]['isCategorical']!='1'){
                    attributeMap[attribute]['isCategorical'] = '1';
                }
            }
        });
	}

	dataProcessor.processList = function (data) {	
			for(var attribute in data[0]){
	            attributeMap[attribute] = {
	                'domain':[],
	                'isNumeric':'',
	                'isCategorical':''
	            };
	        }	
            for(var i in data){
                var d = data[i];
                for(var attribute in attributeMap){
                    if(isNaN(d[attribute])){
                        attributeMap[attribute]['isCategorical'] = '1';
                        attributeMap[attribute]['isNumeric'] = '1';
                    }else{
                        attributeMap[attribute]['isNumeric'] = '1';
                        attributeMap[attribute]['isCategorical'] = '0';
                    }
                    attributeMap[attribute]['domain'].push(d[attribute]);
                }
            }
            for(var attribute in attributeMap){
                var valueSet = [];
                $.each(attributeMap[attribute]['domain'], function(i, el){
                    if($.inArray(el, valueSet) === -1) valueSet.push(el);
                });
                attributeMap[attribute]['domain'] = valueSet;
                if(valueSet.length<=12 && attributeMap[attribute]['isCategorical']!='1'){
                    attributeMap[attribute]['isCategorical'] = '1';
                }
            }
            console.log(attributeMap)
	}

	dataProcessor.getAttributeDetails = function(attribute){
		return attributeMap[attribute];
	}
})()