(function() {
	dataTransformer = {};

	dataTransformer.getBarChartData = function(dataList,labelAttr,valueAttr,transform){
		transform = typeof transform !== 'undefined' ? transform : "AVERAGE";
		
		var transformedList = [];
		var labelValueMap = {};
		for(var i in dataList){
			//console.log(i, dataList[i], labelAttr, valueAttr);
			var dataItem = dataList[i];
			var labelAttrVal = dataItem[labelAttr];
			var valueAttrVal = dataItem[valueAttr];

			if(Object.keys(labelValueMap).indexOf(labelAttrVal)==-1){ // encountering label for first time
				labelValueMap[labelAttrVal] = {
					"valueSum":parseFloat(valueAttrVal),
					"count":1
				};
			}else{
				labelValueMap[labelAttrVal]["valueSum"]+=parseFloat(valueAttrVal);
				labelValueMap[labelAttrVal]["count"]+=1;
			}
		}

		if(transform=="AVERAGE"){
			for(var labelVal in labelValueMap){
				transformedList.push({
					"label":labelVal,
					"value":parseFloat(labelValueMap[labelVal]['valueSum']/labelValueMap[labelVal]['count'])
				});
			}
		}

		return transformedList;
	}

	
	dataTransformer.getScatterplotData  = function(dataList,xAttr,yAttr,transform){
        
        var transformedList = [];
		var labelValueMap = {};
		for(var i in dataList){
				var dataItem = dataList[i];
	            var xVal = dataItem[xAttr];
	            var yVal = parseInt(dataItem[yAttr]);
	            if(xVal in labelValueMap){
					labelValueMap[xVal]['valueSum'] += yVal;
					labelValueMap[xVal]['count'] += 1;
	            }else{
	            	labelValueMap[xVal] = {
	            		"valueSum":yVal,
	            		"count":1
	            	}
	            }
		}
			for(var xVal in labelValueMap){
				transformedList.push({
					"xVal":xVal,
					"yVal":labelValueMap[xVal]["valueSum"]*1.0/labelValueMap[xVal]["count"]
				});
			}
	


       /*
        if(dataProcessor.getAttributeDetails(xAttr)["isCategorical"]=="1" && dataProcessor.getAttributeDetails(yAttr)["isNumeric"]=="1"){
			
			for(var i in dataList){
				var dataItem = dataList[i];
	            var xVal = dataItem[xAttr];
	            var yVal = parseInt(dataItem[yAttr]);
	            if(xVal in labelValueMap){
					labelValueMap[xVal]['valueSum'] += yVal;
					labelValueMap[xVal]['count'] += 1;
	            }else{
	            	labelValueMap[xVal] = {
	            		"valueSum":yVal,
	            		"count":1
	            	}
	            }
			}
			for(var xVal in labelValueMap){
				transformedList.push({
					"xVal":xVal,
					"yVal":labelValueMap[xVal]["valueSum"]*1.0/labelValueMap[xVal]["count"]
				});
			}
			for(var i in dataList){
				//console.log(i, dataList[i], labelAttr, valueAttr);
				var dataItem = dataList[i];
				var labelAttrVal = dataItem[xAttr];
				var valueAttrVal = dataItem[yAttr];

				if(Object.keys(labelValueMap).indexOf(labelAttrVal)==-1){ // encountering label for first time
					labelValueMap[labelAttrVal] = {
						"valueSum":parseFloat(valueAttrVal),
						"count":1
					};
				}else{
					labelValueMap[labelAttrVal]["valueSum"]+=parseFloat(valueAttrVal);
					labelValueMap[labelAttrVal]["count"]+=1;
				}
			}

			for(var labelVal in labelValueMap){
				transformedList.push({
					"xVal":labelVal,
					"yVal":parseFloat(labelValueMap[labelVal]['valueSum']/labelValueMap[labelVal]['count'])
				});
			}
			
		}
		else{
			for(var i in dataList){
				var dataItem = dataList[i];
	            transformedList.push(
				{	
					"xVal": dataProcessor.getAttributeDetails(xAttr)["isCategorical"] == "1" ? dataItem[xAttr] : parseInt(dataItem[xAttr]),
					"label": dataItem["Name"],
				    "yVal": dataProcessor.getAttributeDetails(yAttr)["isCategorical"] == "1" ? dataItem[yAttr] : parseInt(dataItem[yAttr])
				});
			}
		}
		*/
		
      
        return transformedList;
	}

	dataTransformer.getLineChartData  = function(dataList,xAttr,yAttr,transform){
        
        var transformedList = [];
		var labelValueMap = {};
        
        for(var i in dataList){
				var dataItem = dataList[i];
	            var xVal = dataItem[xAttr];
	            var yVal = parseInt(dataItem[yAttr]);
	            if(xVal in labelValueMap){
					labelValueMap[xVal]['valueSum'] += yVal;
					labelValueMap[xVal]['count'] += 1;
	            }else{
	            	labelValueMap[xVal] = {
	            		"valueSum":yVal,
	            		"count":1
	            	}
	            }
			}
			for(var xVal in labelValueMap){
				transformedList.push({
					"xVal":xVal,
					"yVal":labelValueMap[xVal]["valueSum"]*1.0/labelValueMap[xVal]["count"]
				});
			}



        /*
		if(dataProcessor.getAttributeDetails(xAttr)["isNumeric"]=="1" && dataProcessor.getAttributeDetails(yAttr)["isNumeric"]=="1"){
			for(var i in dataList){
				var dataItem = dataList[i];
	            var xVal = parseInt(dataItem[xAttr]);
	            var yVal = parseInt(dataItem[yAttr]);
	            if(xVal in labelValueMap){
					labelValueMap[xVal]['valueSum'] += yVal;
					labelValueMap[xVal]['count'] += 1;
	            }else{
	            	labelValueMap[xVal] = {
	            		"valueSum":yVal,
	            		"count":1
	            	}
	            }
			}
			for(var xVal in labelValueMap){
				transformedList.push({
					"xVal":xVal,
					"yVal":labelValueMap[xVal]["valueSum"]*1.0/labelValueMap[xVal]["count"]
				});
			}
		}
        else 
        
        if(dataProcessor.getAttributeDetails(xAttr)["isCategorical"]=="1" && dataProcessor.getAttributeDetails(yAttr)["isNumeric"]=="1"){
			for(var i in dataList){
				var dataItem = dataList[i];
	            var xVal = dataItem[xAttr];
	            var yVal = parseInt(dataItem[yAttr]);
	            if(xVal in labelValueMap){
					labelValueMap[xVal]['valueSum'] += yVal;
					labelValueMap[xVal]['count'] += 1;
	            }else{
	            	labelValueMap[xVal] = {
	            		"valueSum":yVal,
	            		"count":1
	            	}
	            }
			}
			for(var xVal in labelValueMap){
				transformedList.push({
					"xVal":xVal,
					"yVal":labelValueMap[xVal]["valueSum"]*1.0/labelValueMap[xVal]["count"]
				});
			}
		}
		else{
			for(var i in dataList){
				var dataItem = dataList[i];
	            transformedList.push(
				{	
					"xVal": dataProcessor.getAttributeDetails(xAttr)["isCategorical"] == "1" ? dataItem[xAttr] : parseInt(dataItem[xAttr]),
					"yVal": dataProcessor.getAttributeDetails(yAttr)["isCategorical"] == "1" ? dataItem[yAttr] : parseInt(dataItem[yAttr])
				});
			}
		}	
		*/
		sortObj(transformedList,'xVal');
        return transformedList;
	}

	function sortObj(list, key,order) {
	    order = typeof order !== 'undefined' ? order : 'a';
	    function compare(a, b) {
	        a = a[key];
	        b = b[key];
	        var type = (typeof(a) === 'string' || typeof(b) === 'string') ? 'string' : 'number';
	        var result;
	        if (type === 'string'){
	            if(key=='startDate' || key=='endDate'){
	                a = new Date(a).getTime();
	                b = new Date(b).getTime();
	                if(order=='a'){
	                    result = a - b;
	                }else if(order=='d'){
	                    result = b - a;
	                }
	                //if(order=='a'){
	                //    result = a < b;
	                //}else if(order=='d'){
	                //    result = a > b;
	                //}
	            }else{
	                if(order=='a'){
	                    result = a.localeCompare(b);
	                }else if(order=='d'){
	                    result = b.localeCompare(a);
	                }
	            }
	        } else {
	            if(order=='a'){
	                result = a - b;
	            }else if(order=='d'){
	                result = b - a;
	            }
	        }
	        return result;
	    }
    	return list.sort(compare);
	}	

})();