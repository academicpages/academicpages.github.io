function XScaleGenerator(xAxisType, width, XExtentValue)
{ 
    var xScale;
	if(xAxisType =="linear")
	{
		xScale = d3.scale.linear().domain(XExtentValue).range([0,width]);
	}
	else
	{
		xScale= d3.scale.ordinal().domain(XExtentValue).rangeRoundBands([0,width],1);	
	}
	
	return xScale;
}