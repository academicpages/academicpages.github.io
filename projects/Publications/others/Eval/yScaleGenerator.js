function YScaleGenerator(yAxisType, height, YExtentValue)
{
	var yScale;
	if(yAxisType =="linear")
	{
		yScale = d3.scale.linear().domain(YExtentValue).range([height, 0]);
	}
	else
	{
		yScale = d3.scale.ordinal().domain(YExtentValue).rangeRoundBands([height, 0],1);	
	}
	return yScale;
}