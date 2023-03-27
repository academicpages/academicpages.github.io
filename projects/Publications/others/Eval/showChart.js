
 	function updateChart(currentQ,set){


        dataProcessor.processFile("data/cars.csv");

 	    d3.csv("data/cars.csv",function(data){
	    d3.select("#vis").selectAll("svg").remove();

	        if(set == "Anomalies"){

	        	if(currentQ == 2){
	        		questionID = "Trial";
	        		dataVisualizer.drawTable(data,"Type","Highway Miles Per Gallon","#vis",400);
		        }
		        if(currentQ == 3){
		        	questionID = "Trial";
		        	dataVisualizer.drawPieChart(data,"Cyl","Retail Price","#vis",1600,600);
		        }
		        if(currentQ == 4){
		        	questionID = "Trial";
		        	dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis",1200,600);
		        }
		        if(currentQ == 5){
		        	questionID = "Trial";
	        		dataVisualizer.drawLineChart(data,"Width","Weight","#vis",1600,600);
		        }
		        if(currentQ == 6){
		        	questionID = "Trial";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Highway Miles Per Gallon","#vis",1600,600);
		        }
	        	if(currentQ == 8){
	        		questionID = "BarChart_Anomalies_Nominal_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Type","City Miles Per Gallon","#vis",1200,600);
		        }
		        if(currentQ == 9){
		        	questionID = "PieChart_Anomalies_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Cyl","Weight","#vis",1600,600);
		        }
	          if(currentQ == 10){
	            questionID = "ScatterPlot_Anomalies_Nominal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 11){
              questionID = "ScatterPlot_Anomalies_Numerical_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Wheel Base","Dealer Cost","#vis",1600,600);
		        }
		        if(currentQ == 12){
		        	questionID = "ScatterPlot_Anomalies_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Engine Size (l)","#vis",1600,600);
		        }
            if(currentQ == 13){
              questionID = "Test";
		        	dataVisualizer.drawScatterplot(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 14){
		        	questionID = "LineChart_Anomalies_Numerical_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Width","Horsepower(HP)","#vis",1600,600);
		        }
		        if(currentQ == 15){
                    questionID = "PieChart_Anomalies_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 16){
		        	questionID = "Table_Anomalies_Nominal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Type","City Miles Per Gallon","#vis",400);
		        }
		        if(currentQ == 17){
		        	 questionID = "Table_Anomalies_Numerical_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Wheel Base","Dealer Cost","#vis",400);
		        }
            if(currentQ == 18){
            		questionID = "BarChart_Anomalies_Ordinal_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Cyl","Dealer Cost","#vis",1200,600);
		        }
		        if(currentQ == 19){
		        	 questionID = "Table_Anomalies_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Cyl","Engine Size (l)","#vis",400);
		        }

            if(currentQ == 20){
            		questionID = "BarChart_Anomalies_Numerical_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Width","Engine Size (l)","#vis",1200,600);
		        }
		        if(currentQ == 21){
		        	questionID = "PieChart_Anomalies_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Retail Price","#vis",1600,600);
		        }
		        if(currentQ ==22){
		         	questionID = "LineChart_Anomalies_Nominal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 23){
		        	questionID = "LineChart_Anomalies_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Cyl","Horsepower(HP)","#vis",1600,600);
		        }
		        if(currentQ == 24){
		        	questionID = "Test";
		        	dataVisualizer.drawBarChart(data,"Width","Horsepower(HP)","#vis",1200,600);
		        }
            if(currentQ == 25){
	        		questionID = "BarChart_Anomalies_Nominal_Numerical_MovieData";
	        		dataVisualizer.drawBarChart(data,"Genre","Gross($M)","#vis",1200,600);
		        }
		        if(currentQ == 26){
		        	questionID = "PieChart_Anomalies_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Rating","Gross($M)","#vis",1600,600);
		        }
	          if(currentQ == 27){
	            questionID = "ScatterPlot_Anomalies_Nominal_Numerical_MovieData";
		        	dataVisualizer.drawScatterplot(data,"Genre","Length","#vis",1600,600);
		        }
		        if(currentQ == 28){
              questionID = "ScatterPlot_Anomalies_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawScatterplot(data,"Rating","Budget","#vis",1600,600);
		        }
		        if(currentQ == 29){
		        	questionID = "ScatterPlot_Anomalies_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawScatterplot(data,"Rating","Budget","#vis",1600,600);
		        }
		        if(currentQ == 30){
		        	questionID = "LineChart_Anomalies_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawLineChart(data,"Rating","Gross($M)","#vis",1600,600);
		        }
		        if(currentQ == 31){
                    questionID = "PieChart_Anomalies_Nominal_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Genre","Gross($M)","#vis",1600,600);
		        }
		        if(currentQ == 32){
		        	questionID = "Table_Anomalies_Nominal_Numerical_MovieData";
		        	dataVisualizer.drawTable(data,"Genre","Length","#vis",400);
		        }
		        if(currentQ ==33){
		        	 questionID = "Table_Anomalies_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawTable(data,"Length","Budget","#vis",400);
		        }
            if(currentQ == 34){
            		questionID = "BarChart_Anomalies_Ordinal_Numerical_MovieData";
	        		dataVisualizer.drawBarChart(data,"Rating","Profit($M)","#vis",1200,600);
		        }
		        if(currentQ == 35){
		        	 questionID = "Table_Anomalies_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawTable(data,"Rating","Gross($M)","#vis",400);
		        }
            if(currentQ == 36){
            		questionID = "BarChart_Anomalies_Numerical_Numerical_MovieData";
	        		dataVisualizer.drawBarChart(data,"Rating","Budget","#vis",1200,600);
		        }
		        if(currentQ == 37){
		        	questionID = "PieChart_Anomalies_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Length","Budget","#vis",1600,600);
		        }
		         if(currentQ ==38){
		         	questionID = "LineChart_Anomalies_Nominal_Numerical_MovieData";
		        	dataVisualizer.drawLineChart(data,"Genre","Rating","#vis",1600,600);
		        }
		        if(currentQ == 39){
		        	questionID = "LineChart_Anomalies_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawLineChart(data,"Rating","Length","#vis",1600,600);
		        }
		        if(currentQ == 40){
		        	questionID = "Ranking_Anomalies_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","Highway Miles Per Gallon","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Type","Highway Miles Per Gallon","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Type","Highway Miles Per Gallon","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Type","Highway Miles Per Gallon","#vis5",300);
		        }
		        if(currentQ == 41){
		        	questionID = "Ranking_Anomalies_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawBarChart(data,"Cyl","Len","#vis1",500,200);
		        	dataVisualizer.drawPieChart(data,"Cyl","Len","#vis2",400,300);
		        	dataVisualizer.drawScatterplot(data,"Cyl","Len","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Cyl","Len","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Cyl","Len","#vis5",300);
		        }
		        if(currentQ == 42){
		        	questionID = "Ranking_Anomalies_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Dealer Cost","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Width","Dealer Cost","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Width","Dealer Cost","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Width","Dealer Cost","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Width","Dealer Cost","#vis5",300);
		        }
            if(currentQ == 43){
		        	questionID = "Ranking_Anomalies_Nominal_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Genre","Length","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Genre","Length","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Genre","Length","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Genre","Length","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Genre","Length","#vis5",300);
		        }
		        if(currentQ == 44){
		        	questionID = "Ranking_Anomalies_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawBarChart(data,"Rating","Gross($M)","#vis1",500,200);
		        	dataVisualizer.drawPieChart(data,"Rating","Gross($M)","#vis2",400,300);
		        	dataVisualizer.drawScatterplot(data,"Rating","Gross($M)","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Rating","Gross($M)","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Rating","Gross($M)","#vis5",300);
		        }
		        if(currentQ == 45){
		        	questionID = "Ranking_Anomalies_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Rating","Budget","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Rating","Budget","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Rating","Budget","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Rating","Budget","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Rating","Budget","#vis5",300);
		        }
	        }
          else if(set == "Cluster"){
            if(currentQ == 2){
            		questionID = "Trial";
		        	dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis",1200,600);
		        }
		        if(currentQ == 3){
		        	questionID = "Trial";
		        	dataVisualizer.drawPieChart(data,"Cyl","Retail Price","#vis",1600,600);
		        }
		        if(currentQ == 4){
		        	questionID = "Trial";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Highway Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 5){
		        	questionID = "Trial";
	        		dataVisualizer.drawLineChart(data,"Width","Weight","#vis",1600,600);
		        }
		        if(currentQ == 6){
                	questionID = "Trial";
	        		dataVisualizer.drawTable(data,"Type","Highway Miles Per Gallon","#vis",400);
		        }



	/*********************/
		        if(currentQ == 8){
		        	questionID = "LineChart_Cluster_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Cyl","Horsepower(HP)","#vis",1600,600);
		        }

		        if(currentQ == 9){
		        	questionID = "PieChart_Cluster_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Cyl","Weight","#vis",1600,600);
		        }
	          if(currentQ == 10){
	            	questionID = "Scatterplot_Cluster_Nominal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 11){
		        	questionID = "Scatterplot_Cluster_Numerical_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Wheel Base","Dealer Cost","#vis",1600,600);
		        }
		        if(currentQ == 12){
		        	questionID = "LineChart_Cluster_Numerical_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Width","Horsepower(HP)","#vis",1600,600);
		        }
            if(currentQ == 13){
                	questionID = "Scatterplot_Cluster_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Engine Size (l)","#vis",1600,600);
		        }
		        if(currentQ == 14){
		        	questionID = "Test";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Engine Size (l)","#vis",1600,600);
		        }

		        if(currentQ == 15){
		        	questionID = "PieChart_Cluster_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 16){
		        	questionID = "Table_Cluster_Nominal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Type","City Miles Per Gallon","#vis",400);
		        }
		        if(currentQ == 17){
		        	questionID = "Table_Cluster_Numerical_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Wheel Base","Dealer Cost","#vis",400);
		        }
            if(currentQ == 18){
            		questionID = "BarChart_Cluster_Ordinal_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Cyl","Dealer Cost","#vis",1200,600);
		        }
		        if(currentQ == 19){
		        	questionID = "Table_Cluster_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Cyl","Engine Size (l)","#vis",400);
		        }

            if(currentQ == 20){
            		questionID = "BarChart_Cluster_Numerical_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Highway Miles Per Gallon","Engine Size (l)","#vis",1200,600);
		        }

		        if(currentQ == 21){
		        	questionID = "PieChart_Cluster_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Horsepower(HP)","#vis",1600,600);
		        }
		         if(currentQ ==22){
		         	questionID = "LineChart_Cluster_Nominal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }

		        if(currentQ == 23){
		        	questionID = "BarChart_Cluster_Nominal_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Type","City Miles Per Gallon","#vis",1200,600);
		        }

		        if(currentQ == 24){
		        	questionID = "Test";
		        	dataVisualizer.drawBarChart(data,"Width","Horsepower(HP)","#vis",1200,600);
		        }
            if(currentQ == 25){
             questionID = "LineChart_Cluster_Ordinal_Numerical_MovieData";
             dataVisualizer.drawLineChart(data,"Rating","Budget","#vis",1600,600);
           }

           if(currentQ == 26){
             questionID = "PieChart_Cluster_Ordinal_Numerical_MovieData";
             dataVisualizer.drawPieChart(data,"Rating","Gross($M)","#vis",1600,600);
           }
           if(currentQ == 27){
               questionID = "Scatterplot_Cluster_Nominal_Numerical_MovieData";
             dataVisualizer.drawScatterplot(data,"Genre","Gross($M)","#vis",1600,600);
           }
           if(currentQ == 28){
             questionID = "Scatterplot_Cluster_Numerical_Numerical_MovieData";
             dataVisualizer.drawScatterplot(data,"Length","Budget","#vis",1600,600);
           }
           if(currentQ == 29){
             questionID = "LineChart_Cluster_Numerical_Numerical_MovieData";
             dataVisualizer.drawLineChart(data,"Length","Profit($M)","#vis",1600,600);
           }
           if(currentQ == 30){
                 questionID = "Scatterplot_Cluster_Ordinal_Numerical_MovieData";
             dataVisualizer.drawScatterplot(data,"Rating","Length","#vis",1600,600);
           }
           if(currentQ == 31){
             questionID = "PieChart_Cluster_Nominal_Numerical_MovieData";
             dataVisualizer.drawPieChart(data,"Genre","Budget","#vis",1600,600);
           }
           if(currentQ == 32){
             questionID = "Table_Cluster_Nominal_Numerical_MovieData";
             dataVisualizer.drawTable(data,"Genre","Length","#vis",400);
           }
           if(currentQ == 33){
             questionID = "Table_Cluster_Numerical_Numerical_MovieData";
             dataVisualizer.drawTable(data,"Length","Rating","#vis",400);
           }
           if(currentQ == 34){
               questionID = "BarChart_Cluster_Ordinal_Numerical_MovieData";
             dataVisualizer.drawBarChart(data,"Rating","Profit($M)","#vis",1200,600);
           }
           if(currentQ == 35){
             questionID = "Table_Cluster_Ordinal_Numerical_MovieData";
             dataVisualizer.drawTable(data,"Rating","Gross($M)","#vis",400);
           }

          if(currentQ == 36){
               questionID = "BarChart_Cluster_Numerical_Numerical_MovieData";
             dataVisualizer.drawBarChart(data,"Length","Budget","#vis",1200,600);
           }

           if(currentQ == 37){
             questionID = "PieChart_Cluster_Numerical_Numerical_MovieData";
             dataVisualizer.drawPieChart(data,"Length","Budget","#vis",1600,600);
           }
            if(currentQ ==38){
             questionID = "LineChart_Cluster_Nominal_Numerical_MovieData";
             dataVisualizer.drawLineChart(data,"Genre","Gross($M)","#vis",1600,600);
           }

           if(currentQ == 39){
             questionID = "BarChart_Cluster_Nominal_Numerical_MovieData";
             dataVisualizer.drawBarChart(data,"Genre","Budget","#vis",1200,600);
           }
		       if(currentQ == 40){
		        	questionID = "Ranking_Cluster_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawBarChart(data,"Cyl","Len","#vis1",500,200);
		        	dataVisualizer.drawPieChart(data,"Cyl","Len","#vis2",400,300);
		        	dataVisualizer.drawScatterplot(data,"Cyl","Len","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Cyl","Len","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Cyl","Len","#vis5",300);

		        }
		        if(currentQ == 41){
		        	questionID = "Ranking_Cluster_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","Highway Miles Per Gallon","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Type","Highway Miles Per Gallon","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Type","Highway Miles Per Gallon","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Type","Highway Miles Per Gallon","#vis5",300);

		        }
		        if(currentQ == 42){
		        	questionID = "Ranking_Cluster_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Dealer Cost","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Width","Dealer Cost","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Width","Dealer Cost","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Width","Dealer Cost","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Width","Dealer Cost","#vis5",300);

		        }
            if(currentQ == 43){
              questionID = "Ranking_Cluster_Ordinal_Numerical_MovieData";
              dataVisualizer.drawBarChart(data,"Rating","Profit($M)","#vis1",500,200);
              dataVisualizer.drawPieChart(data,"Rating","Profit($M)","#vis2",400,300);
              dataVisualizer.drawScatterplot(data,"Rating","Profit($M)","#vis3",500,200);
              dataVisualizer.drawLineChart(data,"Rating","Profit($M)","#vis4",500,200);
              dataVisualizer.drawTable(data,"Rating","Profit($M)","#vis5",300);

            }
            if(currentQ == 44){
              questionID = "Ranking_Cluster_Nominal_Numerical_MovieData";
              dataVisualizer.drawPieChart(data,"Genre","Gross($M)","#vis1",400,300);
              dataVisualizer.drawScatterplot(data,"Genre","Gross($M)","#vis2",500,200);
              dataVisualizer.drawBarChart(data,"Genre","Gross($M)","#vis3",500,200);
              dataVisualizer.drawLineChart(data,"Genre","Gross($M)","#vis4",500,200);
              dataVisualizer.drawTable(data,"Genre","Gross($M)","#vis5",300);

            }

            if(currentQ == 45){
              questionID = "Ranking_Cluster_Numerical_Numerical_MovieData";
              dataVisualizer.drawPieChart(data,"Length","Budget","#vis1",400,300);
              dataVisualizer.drawScatterplot(data,"Length","Budget","#vis2",500,200);
              dataVisualizer.drawBarChart(data,"Length","Budget","#vis3",500,200);
              dataVisualizer.drawLineChart(data,"Length","Budget","#vis4",500,200);
              dataVisualizer.drawTable(data,"Length","Budget","#vis5",300);

            }
	        }

            else if(set == "Correlation"){


		        if(currentQ == 2){
		        	questionID = "Trial";
		        	dataVisualizer.drawBarChart(data,"Width","Retail Price","#vis",1200,600);
		        }
		        if(currentQ == 3){
		        	questionID = "Trial";
		        	dataVisualizer.drawPieChart(data,"Cyl","Retail Price","#vis",1600,600);
		        }
		        if(currentQ == 4){
		        	questionID = "Trial";
		        	dataVisualizer.drawTable(data,"Width","Retail Price","#vis",400);
		        }
		        if(currentQ == 5){
		        	questionID = "Trial";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Highway Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 6){
		        	questionID = "Trial";
	        		dataVisualizer.drawLineChart(data,"Width","Weight","#vis",1600,600);
		        }



	/*********************/
		        if(currentQ == 8){
		        	questionID = "LineChart_Correlation_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Cyl","Horsepower(HP)","#vis",1600,600);
		        }

		        if(currentQ == 9){
		        	questionID = "PieChart_Correlation_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Cyl","Weight","#vis",1600,600);
		        }

		        if(currentQ == 10){
		        	questionID = "Scatterplot_Correlation_Numerical_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Wheel Base","Dealer Cost","#vis",1600,600);
		        }
		        if(currentQ == 11){
		            questionID = "LineChart_Correlation_Numerical_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Width","Horsepower(HP)","#vis",1600,600);
		        }
                if(currentQ == 12){
                	questionID = "Scatterplot_Correlation_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Engine Size (l)","#vis",1600,600);
		        }
		        if(currentQ == 13){
		        	questionID = "Test";
		        	dataVisualizer.drawLineChart(data,"Cyl","Engine Size (l)","#vis",1600,600);
		        }

		        if(currentQ == 14){
		            questionID = "Table_Correlation_Numerical_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Wheel Base","Dealer Cost","#vis",400);
		        }
            	if(currentQ == 15){
            		questionID = "BarChart_Correlation_Ordinal_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Cyl","Dealer Cost","#vis",1200,600);
		        }
		        if(currentQ == 16){
		        	questionID = "Table_Correlation_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Cyl","Engine Size (l)","#vis",400);
		        }

            	if(currentQ == 17){
            		questionID = "BarChart_Correlation_Numerical_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Highway Miles Per Gallon","Engine Size (l)","#vis",1200,600);
		        }

		        if(currentQ == 18){
		        	questionID = "PieChart_Correlation_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Dealer Cost","#vis",1600,600);
		        }
            if(currentQ == 19){
		        	questionID = "LineChart_Correlation_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawLineChart(data,"Rating","Length","#vis",1600,600);
		        }

		        if(currentQ == 20){
		        	questionID = "PieChart_Correlation_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Rating","Budget","#vis",1600,600);
		        }

		        if(currentQ == 21){
		        	questionID = "Scatterplot_Correlation_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawScatterplot(data,"Budget","Profit($M)","#vis",1600,600);
		        }
		        if(currentQ == 22){
		          questionID = "LineChart_Correlation_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawLineChart(data,"Length","Gross($M)","#vis",1600,600);
		        }
            if(currentQ == 23){
              questionID = "Scatterplot_Correlation_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawScatterplot(data,"Rating","Gross($M)","#vis",1600,600);
		        }
		        if(currentQ == 24){
		          questionID = "Table_Correlation_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawTable(data,"Length","Budget","#vis",400);
		        }
            if(currentQ == 25){
            	questionID = "BarChart_Correlation_Ordinal_Numerical_MovieData";
	        		dataVisualizer.drawBarChart(data,"Rating","Profit($M)","#vis",1200,600);
		        }
		        if(currentQ == 26){
		        	questionID = "Table_Correlation_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawTable(data,"Rating","Gross($M)","#vis",400);
		        }
            if(currentQ == 27){
            	questionID = "BarChart_Correlation_Numerical_Numerical_MovieData";
	        		dataVisualizer.drawBarChart(data,"Length","Rating","#vis",1200,600);
		        }
		        if(currentQ == 28){
		        	questionID = "PieChart_Correlation_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Length","Budget","#vis",1600,600);
		        }
		        if(currentQ == 29){
		        	questionID = "Ranking_Correlation_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawBarChart(data,"Cyl","Len","#vis1",500,200);
		        	dataVisualizer.drawPieChart(data,"Cyl","Len","#vis2",500,400);
		        	dataVisualizer.drawScatterplot(data,"Cyl","Len","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Cyl","Len","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Cyl","Len","#vis5",300);

		        }
		        if(currentQ == 30){
		        	questionID = "Ranking_Correlation_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Retail Price","#vis1",500,400);
		        	dataVisualizer.drawScatterplot(data,"Width","Retail Price","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Width","Retail Price","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Width","Retail Price","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Width","Retail Price","#vis5",300);
		        }
		        if(currentQ == 31){
		        	questionID = "Ranking_Correlation_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawBarChart(data,"Rating","Length","#vis1",500,200);
		        	dataVisualizer.drawPieChart(data,"Rating","Length","#vis2",500,400);
		        	dataVisualizer.drawScatterplot(data,"Rating","Length","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Rating","Length","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Rating","Length","#vis5",300);

		        }
		        if(currentQ == 32){
		        	questionID = "Ranking_Correlation_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Length","Gross($M)","#vis1",500,400);
		        	dataVisualizer.drawScatterplot(data,"Length","Gross($M)","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Length","Gross($M)","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Length","Gross($M)","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Length","Gross($M)","#vis5",300);

		        }
	        }

            else if(set == "Derived"){

	        	if(currentQ == 2){
	        		questionID = "Trial";
		        	dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis",1200,600);
		        }
            if(currentQ == 3){
              questionID = "Trial";
	        		dataVisualizer.drawTable(data,"Type","Dealer Cost","#vis",400);
		        }

		        if(currentQ == 4){
		        	questionID = "Trial";
		        	dataVisualizer.drawPieChart(data,"Width","Retail Price","#vis",1600,600);
		        }
		        if(currentQ == 5){
		        	questionID = "Trial";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Retail Price","#vis",1600,600);
		        }

		        if(currentQ == 6){
		        	questionID = "Trial";
	        		dataVisualizer.drawLineChart(data,"Width","Retail Price","#vis",1600,600);
		        }

	          if(currentQ == 8){
	            	questionID = "Scatterplot_Derived_Nominal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 9){
		        	questionID = "Scatterplot_Derived_Numerical_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Wheel Base","Dealer Cost","#vis",1600,600);
		        }

		        if(currentQ == 10){
		        	questionID = "LineChart_Derived_Numerical_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Width","Horsepower(HP)","#vis",1600,600);
		        }
		        if(currentQ == 11){
		        	questionID = "LineChart_Derived_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Cyl","Horsepower(HP)","#vis",1600,600);
		        }
  				if(currentQ == 12){
		        	questionID = "PieChart_Derived_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Cyl","Weight","#vis",1600,600);
		        }
		        if(currentQ == 13){
                	questionID = "Test";
	        		dataVisualizer.drawBarChart(data,"Cyl","Dealer Cost","#vis",1200,600);
		        }

		        if(currentQ == 14){
		        	questionID = "Table_Derived_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Cyl","Engine Size (l)","#vis",400);
		        }
		        if(currentQ == 15){
		        	questionID = "Scatterplot_Derived_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Len","#vis",1600,600);
		        }
		        if(currentQ == 16){
		        	questionID = "BarChart_Derived_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawBarChart(data,"Cyl","Engine Size (l)","#vis",1200,600);
		        }
		        if(currentQ == 17){
 				    	questionID = "PieChart_Derived_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }

		        if(currentQ == 18){
		        	questionID = "Table_Derived_Nominal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Type","City Miles Per Gallon","#vis",400);
		        }
		        if(currentQ == 19){
		        	questionID = "Table_Derived_Numerical_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Wheel Base","Dealer Cost","#vis",400);
		        }
            if(currentQ == 20){
            	questionID = "BarChart_Derived_Numerical_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Highway Miles Per Gallon","Engine Size (l)","#vis",1200,600);
		        }
		        if(currentQ == 21){
		        	questionID = "PieChart_Derived_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Retail Price","#vis",1600,600);
		        }
		        if(currentQ ==22){
		          questionID = "LineChart_Derived_Nominal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 23){
		        	questionID = "BarChart_Derived_Nominal_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Type","Len","#vis",1200,600);
		        }
		        if(currentQ == 24){
		        	questionID = "Test";
		        	dataVisualizer.drawBarChart(data,"Width","Horsepower(HP)","#vis",1200,600);
		        }
            if(currentQ == 25){
              questionID = "Scatterplot_Derived_Nominal_Numerical_MovieData";
            dataVisualizer.drawScatterplot(data,"Genre","Gross($M)","#vis",1600,600);
            }
            if(currentQ == 26){
              questionID = "Scatterplot_Derived_Numerical_Numerical_MovieData";
              dataVisualizer.drawScatterplot(data,"Length","Budget","#vis",1600,600);
            }

            if(currentQ == 27){
              questionID = "LineChart_Derived_Numerical_Numerical_MovieData";
              dataVisualizer.drawLineChart(data,"Length","Rating","#vis",1600,600);
            }
            if(currentQ == 28){
              questionID = "LineChart_Derived_Ordinal_Numerical_MovieData";
              dataVisualizer.drawLineChart(data,"Rating","Length","#vis",1600,600);
            }
            if(currentQ == 29){
              questionID = "PieChart_Derived_Ordinal_Numerical_MovieData";
              dataVisualizer.drawPieChart(data,"Rating","Gross($M)","#vis",1600,600);
            }
            if(currentQ == 30){
              questionID = "Table_Derived_Ordinal_Numerical_MovieData";
              dataVisualizer.drawTable(data,"Rating","Length","#vis",400);
            }
            if(currentQ == 31){
              questionID = "Scatterplot_Derived_Ordinal_Numerical_MovieData";
              dataVisualizer.drawScatterplot(data,"Rating","Budget","#vis",1600,600);
            }
            if(currentQ == 32){
              questionID = "BarChart_Derived_Ordinal_Numerical_MovieData";
              dataVisualizer.drawBarChart(data,"Rating","Profit($M)","#vis",1200,600);
            }
            if(currentQ == 33){
              questionID = "PieChart_Derived_Nominal_Numerical_MovieData";
              dataVisualizer.drawPieChart(data,"Genre","Gross($M)","#vis",1600,600);
            }
            if(currentQ == 34){
              questionID = "Table_Derived_Nominal_Numerical_MovieData";
              dataVisualizer.drawTable(data,"Genre","Rating","#vis",400);
            }
            if(currentQ == 35){
              questionID = "Table_Derived_Numerical_Numerical_MovieData";
              dataVisualizer.drawTable(data,"Length","Gross($M)","#vis",400);
            }
            if(currentQ == 36){
              questionID = "BarChart_Derived_Numerical_Numerical_MovieData";
              dataVisualizer.drawBarChart(data,"Length","Profit($M)","#vis",1200,600);
            }
            if(currentQ == 37){
              questionID = "PieChart_Derived_Numerical_Numerical_MovieData";
              dataVisualizer.drawPieChart(data,"Length","Rating","#vis",1600,600);
            }
            if(currentQ ==38){
                questionID = "LineChart_Derived_Nominal_Numerical_MovieData";
              dataVisualizer.drawLineChart(data,"Genre","Length","#vis",1600,600);
            }
            if(currentQ == 39){
              questionID = "BarChart_Derived_Nominal_Numerical_MovieData";
              dataVisualizer.drawBarChart(data,"Genre","Budget","#vis",1200,600);
            }
		        if(currentQ == 40){
		        	questionID = "Ranking_Derived_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawBarChart(data,"Cyl","Len","#vis1",500,200);
		        	dataVisualizer.drawPieChart(data,"Cyl","Len","#vis2",400,300);
		        	dataVisualizer.drawScatterplot(data,"Cyl","Len","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Cyl","Len","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Cyl","Len","#vis5",300);

		        }
		        if(currentQ == 41){
		        	questionID = "Ranking_Derived_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Dealer Cost","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Width","Dealer Cost","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Width","Dealer Cost","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Width","Dealer Cost","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Width","Dealer Cost","#vis5",300);

		        }
		        if(currentQ == 42){
		        	questionID = "Ranking_Derived_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","Highway Miles Per Gallon","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Type","Highway Miles Per Gallon","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Type","Highway Miles Per Gallon","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Type","Highway Miles Per Gallon","#vis5",300);

		        }
            if(currentQ == 43){
              questionID = "Ranking_Derived_Ordinal_Numerical_MovieData";
              dataVisualizer.drawBarChart(data,"Rating","Length","#vis1",500,200);
              dataVisualizer.drawPieChart(data,"Rating","Length","#vis2",400,300);
              dataVisualizer.drawScatterplot(data,"Rating","Length","#vis3",500,200);
              dataVisualizer.drawLineChart(data,"Rating","Length","#vis4",500,200);
              dataVisualizer.drawTable(data,"Rating","Length","#vis5",300);
            }
            if(currentQ == 44){
              questionID = "Ranking_Derived_Numerical_Numerical_MovieData";
              dataVisualizer.drawPieChart(data,"Length","Budget","#vis1",400,300);
              dataVisualizer.drawScatterplot(data,"Length","Budget","#vis2",500,200);
              dataVisualizer.drawBarChart(data,"Length","Budget","#vis3",500,200);
              dataVisualizer.drawLineChart(data,"Length","Budget","#vis4",500,200);
              dataVisualizer.drawTable(data,"Length","Budget","#vis5",300);
            }
            if(currentQ == 45){
              questionID = "Ranking_Derived_Nominal_Numerical_MovieData";
              dataVisualizer.drawPieChart(data,"Genre","Rating","#vis1",400,300);
              dataVisualizer.drawScatterplot(data,"Genre","Rating","#vis2",500,200);
              dataVisualizer.drawBarChart(data,"Genre","Rating","#vis3",500,200);
              dataVisualizer.drawLineChart(data,"Genre","Rating","#vis4",500,200);
              dataVisualizer.drawTable(data,"Genre","Rating","#vis5",300);

            }

	        }


        else if(set == "Distribution"){
				    if(currentQ == 2){
					    questionID = "Trial";
	        		dataVisualizer.drawTable(data,"Type","Retail Price","#vis",400);
		        }
		        if(currentQ == 3){
		        	questionID = "Trial";
		        	dataVisualizer.drawPieChart(data,"Cyl","Retail Price","#vis",1600,600);
		        }
		        if(currentQ == 4){
		        	questionID = "Trial";
		        	dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis",1200,600);
		        }
		        if(currentQ == 5){
		        	questionID = "Trial";
	        		dataVisualizer.drawLineChart(data,"Width","Weight","#vis",1600,600);
		        }
		        if(currentQ == 6){
		        	questionID = "Trial";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Highway Miles Per Gallon","#vis",1600,600);
		        }


	/*********************/
	        	if(currentQ == 8){
                    questionID = "BarChart_Distribution_Nominal_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis",1200,600);
		        }
		        if(currentQ == 9){
		        	questionID = "PieChart_Distribution_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Cyl","Weight","#vis",1600,600);
		        }
	            if(currentQ == 10){
	            	questionID = "Scatterplot_Distribution_Nominal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 11){
		        	questionID = "Scatterplot_Distribution_Numerical_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Wheel Base","Dealer Cost","#vis",1600,600);
		        }
		        if(currentQ == 12){
		        	questionID = "LineChart_Distribution_Numerical_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Width","Horsepower(HP)","#vis",1600,600);
		        }
                if(currentQ == 13){
                	questionID = "Test";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Engine Size (l)","#vis",1600,600);
		        }
		        if(currentQ == 14){
		            questionID = "Scatterplot_Distribution_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Engine Size (l)","#vis",1600,600);
		        }

		        if(currentQ == 15){
		        	questionID = "PieChart_Distribution_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 16){
		        	questionID = "Table_Distribution_Nominal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Type","City Miles Per Gallon","#vis",400);
		        }
		        if(currentQ == 17){
		        	questionID = "Table_Distribution_Numerical_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Wheel Base","Dealer Cost","#vis",400);
		        }
            	if(currentQ == 18){
            		questionID = "BarChart_Distribution_Ordinal_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Cyl","Dealer Cost","#vis",1200,600);
		        }
		        if(currentQ == 19){
		        	questionID = "Table_Distribution_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Cyl","Engine Size (l)","#vis",400);
		        }

            if(currentQ == 20){
            		questionID = "BarChart_Distribution_Numerical_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Width","Engine Size (l)","#vis",1200,600);
		        }

		        if(currentQ == 21){
		        	questionID = "PieChart_Distribution_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Retail Price","#vis",1600,600);
		        }
		         if(currentQ ==22){
		         	questionID = "LineChart_Distribution_Nominal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 23){
		        	questionID = "LineChart_Distribution_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Cyl","Horsepower(HP)","#vis",1600,600);
		        }

		        if(currentQ == 24){
		        	questionID = "Test";
		        	dataVisualizer.drawBarChart(data,"Width","Horsepower(HP)","#vis",1200,600);
		        }
            if(currentQ == 25){
               questionID = "BarChart_Distribution_Nominal_Numerical_MovieData";
	        		 dataVisualizer.drawBarChart(data,"Genre","Gross($M)","#vis",1200,600);
		        }
		        if(currentQ == 26){
		        	questionID = "PieChart_Distribution_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Rating","Budget","#vis",1600,600);
		        }
	            if(currentQ == 27){
	            	questionID = "Scatterplot_Distribution_Nominal_Numerical_MovieData";
		        	dataVisualizer.drawScatterplot(data,"Genre","Length","#vis",1600,600);
		        }
		        if(currentQ == 28){
		        	questionID = "Scatterplot_Distribution_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawScatterplot(data,"Length","Profit($M)","#vis",1600,600);
		        }
		        if(currentQ == 29){
		        	questionID = "LineChart_Distribution_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawLineChart(data,"Length","Rating","#vis",1600,600);
		        }
		        if(currentQ == 30){
		          questionID = "Scatterplot_Distribution_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawScatterplot(data,"Rating","Profit($M)","#vis",1600,600);
		        }

		        if(currentQ == 31){
		        	questionID = "PieChart_Distribution_Nominal_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Genre","Rating","#vis",1600,600);
		        }
		        if(currentQ == 32){
		        	questionID = "Table_Distribution_Nominal_Numerical_MovieData";
		        	dataVisualizer.drawTable(data,"Genre","Budget","#vis",400);
		        }
		        if(currentQ == 33){
		        	questionID = "Table_Distribution_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawTable(data,"Length","Budget","#vis",400);
		        }
            if(currentQ == 34){
            	questionID = "BarChart_Distribution_Ordinal_Numerical_MovieData";
	        		dataVisualizer.drawBarChart(data,"Rating","Budget","#vis",1200,600);
		        }
		        if(currentQ == 35){
		        	questionID = "Table_Distribution_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawTable(data,"Rating","Length","#vis",400);
		        }
            if(currentQ == 36){
            	questionID = "BarChart_Distribution_Numerical_Numerical_MovieData";
	        		dataVisualizer.drawBarChart(data,"Length","Gross($M)","#vis",1200,600);
		        }

		        if(currentQ == 37){
		        	questionID = "PieChart_Distribution_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Length","Rating","#vis",1600,600);
		        }
		         if(currentQ ==38){
		         	questionID = "LineChart_Distribution_Nominal_Numerical_MovieData";
		        	dataVisualizer.drawLineChart(data,"Genre","Gross($M)","#vis",1600,600);
		        }
		        if(currentQ == 39){
		        	questionID = "LineChart_Distribution_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawLineChart(data,"Rating","Gross($M)","#vis",1600,600);
		        }
		        if(currentQ == 40){
		        	questionID = "Ranking_Distribution_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","Highway Miles Per Gallon","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Type","Highway Miles Per Gallon","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Type","Highway Miles Per Gallon","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Type","Highway Miles Per Gallon","#vis5",300);
		        }
		        if(currentQ == 41){
		        	questionID = "Ranking_Distribution_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawBarChart(data,"Cyl","Len","#vis1",500,200);
		        	dataVisualizer.drawPieChart(data,"Cyl","Len","#vis2",400,300);
		        	dataVisualizer.drawScatterplot(data,"Cyl","Len","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Cyl","Len","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Cyl","Len","#vis5",300);
		        }
		        if(currentQ == 42){
		        	questionID = "Ranking_Distribution_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Dealer Cost","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Width","Dealer Cost","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Width","Dealer Cost","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Width","Dealer Cost","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Width","Dealer Cost","#vis5",300);
		        }
            if(currentQ == 43){
              questionID = "Ranking_Distribution_Nominal_Numerical_MovieData";
              dataVisualizer.drawPieChart(data,"Genre","Budget","#vis1",400,300);
              dataVisualizer.drawScatterplot(data,"Genre","Budget","#vis2",500,200);
              dataVisualizer.drawBarChart(data,"Genre","Budget","#vis3",500,200);
              dataVisualizer.drawLineChart(data,"Genre","Budget","#vis4",500,200);
              dataVisualizer.drawTable(data,"Genre","Budget","#vis5",300);
            }
            if(currentQ == 44){
              questionID = "Ranking_Distribution_Ordinal_Numerical_MovieData";
              dataVisualizer.drawBarChart(data,"Rating","Length","#vis1",500,200);
              dataVisualizer.drawPieChart(data,"Rating","Length","#vis2",400,300);
              dataVisualizer.drawScatterplot(data,"Rating","Length","#vis3",500,200);
              dataVisualizer.drawLineChart(data,"Rating","Length","#vis4",500,200);
              dataVisualizer.drawTable(data,"Rating","Length","#vis5",300);
            }
            if(currentQ == 45){
              questionID = "Ranking_Distribution_Numerical_Numerical_MovieData";
              dataVisualizer.drawPieChart(data,"Length","Gross($M)","#vis1",400,300);
              dataVisualizer.drawScatterplot(data,"Length","Gross($M)","#vis2",500,200);
              dataVisualizer.drawBarChart(data,"Length","Gross($M)","#vis3",500,200);
              dataVisualizer.drawLineChart(data,"Length","Gross($M)","#vis4",500,200);
              dataVisualizer.drawTable(data,"Length","Gross($M)","#vis5",300);

            }
	        }
          else if(set == "Extremum"){

	        	if(currentQ == 2){
	        		questionID = "Trial";
		        	dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis",1200,600);
		        }
                if(currentQ == 3){
                	questionID = "Trial";
	        		dataVisualizer.drawTable(data,"Type","Dealer Cost","#vis",400);
		        }

		        if(currentQ == 4){
		        	questionID = "Trial";
		        	dataVisualizer.drawPieChart(data,"Width","Retail Price","#vis",1600,600);
		        }
		        if(currentQ == 5){
		        	questionID = "Trial";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Retail Price","#vis",1600,600);
		        }

		        if(currentQ == 6){
		        	questionID = "Trial";
	        		dataVisualizer.drawLineChart(data,"Width","Retail Price","#vis",1600,600);
		        }


	          if(currentQ == 8){
	            	questionID = "Scatterplot_Extremum_Nominal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 9){
		        	questionID = "Scatterplot_Extremum_Numerical_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Wheel Base","Dealer Cost","#vis",1600,600);
		        }
		        if(currentQ == 10){
		        	questionID = "LineChart_Extremum_Numerical_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Width","Horsepower(HP)","#vis",1600,600);
		        }
		        if(currentQ == 11){
		        	questionID = "LineChart_Extremum_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Cyl","Horsepower(HP)","#vis",1600,600);
		        }

		        if(currentQ == 12){
		        	questionID = "PieChart_Extremum_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Cyl","Weight","#vis",1600,600);
		        }

		        if(currentQ == 13){
		        	questionID = "Test";
	        		dataVisualizer.drawBarChart(data,"Cyl","Dealer Cost","#vis",1200,600);
		        }
		        if(currentQ == 14){
		        	questionID = "Table_Extremum_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Cyl","Engine Size (l)","#vis",400);
		        }
            if(currentQ == 15){
                	questionID = "Scatterplot_Extremum_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Len","#vis",1600,600);
		        }
		        if(currentQ == 16){
		        	questionID = "BarChart_Extremum_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawBarChart(data,"Cyl","Engine Size (l)","#vis",1200,600);
		        }

		        if(currentQ == 17){
		        	questionID = "PieChart_Extremum_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 18){
		        	questionID = "Table_Extremum_Nominal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Type","City Miles Per Gallon","#vis",400);
		        }
		        if(currentQ == 19){
		        	questionID = "Table_Extremum_Numerical_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Wheel Base","Dealer Cost","#vis",400);
		        }

            if(currentQ == 20){
            		questionID = "BarChart_Extremum_Numerical_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Highway Miles Per Gallon","Engine Size (l)","#vis",1200,600);
		        }

		        if(currentQ == 21){
		        	questionID = "PieChart_Extremum_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Retail Price","#vis",1600,600);
		        }
		         if(currentQ ==22){
		         	questionID = "LineChart_Extremum_Nominal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }

		        if(currentQ == 23){
		        	questionID = "BarChart_Extremum_Nominal_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Type","Len","#vis",1200,600);
		        }

		        if(currentQ == 24){
		        	questionID = "Test";
		        	dataVisualizer.drawBarChart(data,"Width","Horsepower(HP)","#vis",1200,600);
		        }

            if(currentQ == 25){
              questionID = "Scatterplot_Extremum_Nominal_Numerical_MovieData";
            dataVisualizer.drawScatterplot(data,"Genre","Rating","#vis",1600,600);
           }
            if(currentQ == 26){
              questionID = "Scatterplot_Extremum_Numerical_Numerical_MovieData";
              dataVisualizer.drawScatterplot(data,"Length","Budget","#vis",1600,600);
            }
            if(currentQ == 27){
              questionID = "LineChart_Extremum_Numerical_Numerical_MovieData";
              dataVisualizer.drawLineChart(data,"Length","Gross($M)","#vis",1600,600);
            }
            if(currentQ == 28){
              questionID = "LineChart_Extremum_Ordinal_Numerical_MovieData";
              dataVisualizer.drawLineChart(data,"Rating","Length","#vis",1600,600);
            }

            if(currentQ == 29){
              questionID = "PieChart_Extremum_Ordinal_Numerical_MovieData";
              dataVisualizer.drawPieChart(data,"Rating","Gross($M)","#vis",1600,600);
            }

            if(currentQ == 30){
              questionID = "Table_Extremum_Ordinal_Numerical_MovieData";
              dataVisualizer.drawTable(data,"Rating","Profit($M)","#vis",400);
            }

            if(currentQ == 31){
              questionID = "Scatterplot_Extremum_Ordinal_Numerical_MovieData";
              dataVisualizer.drawScatterplot(data,"Rating","Gross($M)","#vis",1600,600);
            }
            if(currentQ == 32){
              questionID = "BarChart_Extremum_Ordinal_Numerical_MovieData";
              dataVisualizer.drawBarChart(data,"Rating","Budget","#vis",1200,600);
            }

            if(currentQ == 33){
              questionID = "PieChart_Extremum_Nominal_Numerical_MovieData";
              dataVisualizer.drawPieChart(data,"Genre","Budget","#vis",1600,600);
            }
            if(currentQ == 34){
              questionID = "Table_Extremum_Nominal_Numerical_MovieData";
              dataVisualizer.drawTable(data,"Genre","Profit($M)","#vis",400);
            }
            if(currentQ == 35){
              questionID = "Table_Extremum_Numerical_Numerical_MovieData";
              dataVisualizer.drawTable(data,"Length","Rating","#vis",400);
            }

            if(currentQ == 36){
              questionID = "BarChart_Extremum_Numerical_Numerical_MovieData";
              dataVisualizer.drawBarChart(data,"Length","Rating","#vis",1200,600);
            }

            if(currentQ == 37){
              questionID = "PieChart_Extremum_Numerical_Numerical_MovieData";
              dataVisualizer.drawPieChart(data,"Length","Gross($M)","#vis",1600,600);
            }
             if(currentQ ==38){
              questionID = "LineChart_Extremum_Nominal_Numerical_MovieData";
              dataVisualizer.drawLineChart(data,"Genre","Profit($M)","#vis",1600,600);
            }

            if(currentQ == 39){
              questionID = "BarChart_Extremum_Nominal_Numerical_MovieData";
              dataVisualizer.drawBarChart(data,"Genre","Profit($M)","#vis",1200,600);
            }

		        if(currentQ == 40){
		        	questionID = "Ranking_Extremum_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawBarChart(data,"Cyl","Len","#vis1",500,200);
		        	dataVisualizer.drawPieChart(data,"Cyl","Len","#vis2",400,300);
		        	dataVisualizer.drawScatterplot(data,"Cyl","Len","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Cyl","Len","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Cyl","Len","#vis5",300);

		        }
		        if(currentQ == 41){
		        	questionID = "Ranking_Extremum_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Dealer Cost","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Width","Dealer Cost","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Width","Dealer Cost","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Width","Dealer Cost","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Width","Dealer Cost","#vis5",300);

		        }
		        if(currentQ == 42){
		        	questionID = "Ranking_Extremum_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","Highway Miles Per Gallon","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Type","Highway Miles Per Gallon","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Type","Highway Miles Per Gallon","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Type","Highway Miles Per Gallon","#vis5",300);

		        }
            if(currentQ == 43){
             questionID = "Ranking_Extremum_Ordinal_Numerical_MovieData";
             dataVisualizer.drawBarChart(data,"Rating","Gross($M)","#vis1",500,200);
             dataVisualizer.drawPieChart(data,"Rating","Gross($M)","#vis2",400,300);
             dataVisualizer.drawScatterplot(data,"Rating","Gross($M)","#vis3",500,200);
             dataVisualizer.drawLineChart(data,"Rating","Gross($M)","#vis4",500,200);
             dataVisualizer.drawTable(data,"Rating","Gross($M)","#vis5",300);

           }
           if(currentQ == 44){
             questionID = "Ranking_Extremum_Numerical_Numerical_MovieData";
             dataVisualizer.drawPieChart(data,"Length","Budget","#vis1",400,300);
             dataVisualizer.drawScatterplot(data,"Length","Budget","#vis2",500,200);
             dataVisualizer.drawBarChart(data,"Length","Budget","#vis3",500,200);
             dataVisualizer.drawLineChart(data,"Length","Budget","#vis4",500,200);
             dataVisualizer.drawTable(data,"Length","Budget","#vis5",300);

           }
           if(currentQ == 45){
             questionID = "Ranking_Extremum_Nominal_Numerical_MovieData";
             dataVisualizer.drawPieChart(data,"Genre","Gross($M)","#vis1",400,300);
             dataVisualizer.drawScatterplot(data,"Genre","Gross($M)","#vis2",500,200);
             dataVisualizer.drawBarChart(data,"Genre","Gross($M)","#vis3",500,200);
             dataVisualizer.drawLineChart(data,"Genre","Gross($M)","#vis4",500,200);
             dataVisualizer.drawTable(data,"Genre","Gross($M)","#vis5",300);

           }
	        }

          else if(set == "Filter"){

        	  if(currentQ == 2){
        	    questionID = "Trial";
        	    dataVisualizer.drawTable(data,"Type","Highway Miles Per Gallon","#vis",400);
        		}
        		if(currentQ == 3){
        		  questionID = "Trial";
        		  dataVisualizer.drawPieChart(data,"Cyl","Retail Price","#vis",1600,600);
        		}
        	  if(currentQ == 4){
        		  questionID = "Trial";
        		  dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis",1200,600);
        		}
        		if(currentQ == 5){
        		  questionID = "Trial";
        	    dataVisualizer.drawLineChart(data,"Width","Weight","#vis",1600,600);
            }
        		if(currentQ == 6){
        			questionID = "Trial";
        			dataVisualizer.drawScatterplot(data,"Cyl","Highway Miles Per Gallon","#vis",1600,600);
        		}


        	/*********************/
        	  if(currentQ == 8){
        	  	questionID = "BarChart_Filter_Nominal_Numerical_CarData";
        	  	dataVisualizer.drawBarChart(data,"Type","City Miles Per Gallon","#vis",1200,600);
        		}
		        if(currentQ == 9){
		        	questionID = "PieChart_Filter_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Cyl","Weight","#vis",1600,600);
		        }
	            if(currentQ == 10){
	            	questionID = "Scatterplot_Filter_Nominal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 11){
		        	questionID = "Scatterplot_Filter_Numerical_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Wheel Base","Dealer Cost","#vis",1600,600);
		        }
		        if(currentQ == 12){
		        	questionID = "Scatterplot_Filter_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Engine Size (l)","#vis",1600,600);
		        }
                if(currentQ == 13){
                	questionID = "Test";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Engine Size (l)","#vis",1600,600);
		        }
		        if(currentQ == 14){
		        	questionID = "LineChart_Filter_Numerical_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Width","Horsepower(HP)","#vis",1600,600);
		        }

		        if(currentQ == 15){
		        	questionID = "PieChart_Filter_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 16){
		        	questionID = "Table_Filter_Nominal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Type","City Miles Per Gallon","#vis",400);
		        }
		        if(currentQ == 17){
		        	questionID = "Table_Filter_Numerical_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Wheel Base","Dealer Cost","#vis",400);
		        }
            	if(currentQ == 18){
            		questionID = "BarChart_Filter_Ordinal_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Cyl","Dealer Cost","#vis",1200,600);
		        }
		        if(currentQ == 19){
		        	questionID = "Table_Filter_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Cyl","Engine Size (l)","#vis",400);
		        }

            	if(currentQ == 20){
            		questionID = "BarChart_Filter_Numerical_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Width","Engine Size (l)","#vis",1200,600);
		        }

		        if(currentQ == 21){
		        	questionID = "PieChart_Filter_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Retail Price","#vis",1600,600);
		        }
		         if(currentQ ==22){
		         	questionID = "LineChart_Filter_Nominal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 23){
		        	questionID = "LineChart_Filter_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Cyl","Horsepower(HP)","#vis",1600,600);
		        }

		        if(currentQ == 24){
		        	questionID = "Test";
		        	dataVisualizer.drawBarChart(data,"Width","Horsepower(HP)","#vis",1200,600);
		        }
            if(currentQ == 25){
             questionID = "BarChart_Filter_Nominal_Numerical_MovieData";
             dataVisualizer.drawBarChart(data,"Genre","Rating","#vis",1200,600);
            }
            if(currentQ == 26){
               questionID = "PieChart_Filter_Ordinal_Numerical_MovieData";
               dataVisualizer.drawPieChart(data,"Rating","Budget","#vis",1600,600);
            }
            if(currentQ == 27){
               questionID = "Scatterplot_Filter_Nominal_Numerical_MovieData";
               dataVisualizer.drawScatterplot(data,"Genre","Gross($M)","#vis",1600,600);
            }
            if(currentQ == 28){
               questionID = "Scatterplot_Filter_Numerical_Numerical_MovieData";
               dataVisualizer.drawScatterplot(data,"Length","Gross($M)","#vis",1600,600);
             }
             if(currentQ == 29){
               questionID = "Scatterplot_Filter_Ordinal_Numerical_MovieData";
               dataVisualizer.drawScatterplot(data,"Rating","Length","#vis",1600,600);
             }

             if(currentQ == 30){
               questionID = "LineChart_Filter_Numerical_Numerical_MovieData";
               dataVisualizer.drawLineChart(data,"Length","Rating","#vis",1600,600);
             }

             if(currentQ == 31){
               questionID = "PieChart_Filter_Nominal_Numerical_MovieData";
               dataVisualizer.drawPieChart(data,"Genre","Rating","#vis",1600,600);
             }
             if(currentQ == 32){
               questionID = "Table_Filter_Nominal_Numerical_MovieData";
               dataVisualizer.drawTable(data,"Genre","Profit($M)","#vis",400);
             }
             if(currentQ == 33){
               questionID = "Table_Filter_Numerical_Numerical_MovieData";
               dataVisualizer.drawTable(data,"Length","Gross($M)","#vis",400);
             }
             if(currentQ == 34){
                 questionID = "BarChart_Filter_Ordinal_Numerical_MovieData";
               dataVisualizer.drawBarChart(data,"Rating","Budget","#vis",1200,600);
             }
             if(currentQ == 35){
               questionID = "Table_Filter_Ordinal_Numerical_MovieData";
               dataVisualizer.drawTable(data,"Rating","Length","#vis",400);
             }
            if(currentQ == 36){
                 questionID = "BarChart_Filter_Numerical_Numerical_MovieData";
               dataVisualizer.drawBarChart(data,"Length","Gross($M)","#vis",1200,600);
             }
            if(currentQ == 37){
               questionID = "PieChart_Filter_Numerical_Numerical_MovieData";
               dataVisualizer.drawPieChart(data,"Length","Gross($M)","#vis",1600,600);
             }
            if(currentQ ==38){
               questionID = "LineChart_Filter_Nominal_Numerical_MovieData";
               dataVisualizer.drawLineChart(data,"Genre","Length","#vis",1600,600);
             }
             if(currentQ == 39){
               questionID = "LineChart_Filter_Ordinal_Numerical_MovieData";
               dataVisualizer.drawLineChart(data,"Rating","Length","#vis",1600,600);
             }
		        if(currentQ == 40){
		        	questionID = "Ranking_Filter_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","Highway Miles Per Gallon","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Type","Highway Miles Per Gallon","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Type","Highway Miles Per Gallon","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Type","Highway Miles Per Gallon","#vis5",300);
		        }
		        if(currentQ == 41){
		        	questionID = "Ranking_Filter_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawBarChart(data,"Cyl","Len","#vis1",500,200);
		        	dataVisualizer.drawPieChart(data,"Cyl","Len","#vis2",400,300);
		        	dataVisualizer.drawScatterplot(data,"Cyl","Len","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Cyl","Len","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Cyl","Len","#vis5",300);

		        }
		        if(currentQ == 42){
		        	questionID = "Ranking_Filter_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Dealer Cost","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Width","Dealer Cost","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Width","Dealer Cost","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Width","Dealer Cost","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Width","Dealer Cost","#vis5",300);

		        }
            if(currentQ == 43){
              questionID = "Ranking_Filter_Nominal_Numerical_MovieData";
              dataVisualizer.drawPieChart(data,"Genre","Gross($M)","#vis1",400,300);
              dataVisualizer.drawScatterplot(data,"Genre","Gross($M)","#vis2",500,200);
              dataVisualizer.drawBarChart(data,"Genre","Gross($M)","#vis3",500,200);
              dataVisualizer.drawLineChart(data,"Genre","Gross($M)","#vis4",500,200);
              dataVisualizer.drawTable(data,"Genre","Gross($M)","#vis5",300);

            }
            if(currentQ == 44){
              questionID = "Ranking_Filter_Ordinal_Numerical_MovieData";
              dataVisualizer.drawBarChart(data,"Rating","Length","#vis1",500,200);
              dataVisualizer.drawPieChart(data,"Rating","Length","#vis2",400,300);
              dataVisualizer.drawScatterplot(data,"Rating","Length","#vis3",500,200);
              dataVisualizer.drawLineChart(data,"Rating","Length","#vis4",500,200);
              dataVisualizer.drawTable(data,"Rating","Length","#vis5",300);

            }
            if(currentQ == 45){
              questionID = "Ranking_Filter_Numerical_Numerical_MovieData";
              dataVisualizer.drawPieChart(data,"Length","Rating","#vis1",400,300);
              dataVisualizer.drawScatterplot(data,"Length","Rating","#vis2",500,200);
              dataVisualizer.drawBarChart(data,"Length","Rating","#vis3",500,200);
              dataVisualizer.drawLineChart(data,"Length","Rating","#vis4",500,200);
              dataVisualizer.drawTable(data,"Length","Rating","#vis5",300);

            }
          }
         else if(set == "Order"){
            if(currentQ == 2){
            	questionID = "Trial";
		        	dataVisualizer.drawPieChart(data,"Cyl","Retail Price","#vis",1600,600);
		        }
	        	if(currentQ == 3){
	        		questionID = "Trial";
	        		dataVisualizer.drawTable(data,"Type","City Miles Per Gallon","#vis",400);
		        }
		        if(currentQ == 4){
		        	questionID = "Trial";
		        	dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis",1200,600);
		        }
		        if(currentQ == 5){
		        	questionID = "Trial";
	        		dataVisualizer.drawLineChart(data,"Width","Weight","#vis",1600,600);
		        }
		        if(currentQ == 6){
		        	questionID = "Trial";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Highway Miles Per Gallon","#vis",1600,600);
		        }


	/*********************/
	        	if(currentQ == 8){
	        		questionID = "BarChart_Order_Nominal_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Type","City Miles Per Gallon","#vis",1200,600);
		        }
		        if(currentQ == 9){
		        	questionID = "PieChart_Order_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Cyl","Weight","#vis",1600,600);
		        }
	            if(currentQ == 10){
	            	questionID = "Scatterplot_Order_Nominal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 11){
		        	questionID = "Scatterplot_Order_Numerical_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Wheel Base","Dealer Cost","#vis",1600,600);
		        }
		        if(currentQ == 12){
		        	questionID = "Scatterplot_Order_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Engine Size (l)","#vis",1600,600);
		        }
                if(currentQ == 13){
                	questionID = "Test";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Engine Size (l)","#vis",1600,600);
		        }
		        if(currentQ == 14){
		        	questionID = "LineChart_Order_Numerical_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Width","Horsepower(HP)","#vis",1600,600);
		        }

		        if(currentQ == 15){
		        	questionID = "PieChart_Order_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 16){
		        	questionID = "Table_Order_Nominal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Type","City Miles Per Gallon","#vis",400);
		        }
		        if(currentQ == 17){
		        	questionID = "Table_Order_Numerical_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Wheel Base","Dealer Cost","#vis",400);
		        }
            	if(currentQ == 18){
            		questionID = "BarChart_Order_Ordinal_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Cyl","Dealer Cost","#vis",1200,600);
		        }
		        if(currentQ == 19){
		        	questionID = "Table_Order_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Cyl","Engine Size (l)","#vis",400);
		        }

            	if(currentQ == 20){
            		questionID = "BarChart_Order_Numerical_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Wheel Base","Retail Price","#vis",1200,600);
		        }

		        if(currentQ == 21){
		        	questionID = "PieChart_Order_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Engine Size (l)","#vis",1600,600);
		        }
		         if(currentQ ==22){
		         	questionID = "LineChart_Order_Nominal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 23){
		        	questionID = "LineChart_Order_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Cyl","Horsepower(HP)","#vis",1600,600);
		        }

		        if(currentQ == 24){
		        	questionID = "Test";
		        	dataVisualizer.drawBarChart(data,"Width","Horsepower(HP)","#vis",1200,600);
		        }
            if(currentQ == 25){
	        		questionID = "BarChart_Order_Nominal_Numerical_MovieData";
	        		dataVisualizer.drawBarChart(data,"Genre","Budget","#vis",1200,600);
		        }
		        if(currentQ == 26){
		        	questionID = "PieChart_Order_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Rating","Gross($M)","#vis",1600,600);
		        }
	          if(currentQ == 27){
	            questionID = "Scatterplot_Order_Nominal_Numerical_MovieData";
		        	dataVisualizer.drawScatterplot(data,"Genre","Length","#vis",1600,600);
		        }
		        if(currentQ == 28){
		        	questionID = "Scatterplot_Order_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawScatterplot(data,"Length","Gross($M)","#vis",1600,600);
		        }
		        if(currentQ == 29){
		        	questionID = "Scatterplot_Order_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawScatterplot(data,"Rating","Length","#vis",1600,600);
		        }
		        if(currentQ == 30){
		        	questionID = "LineChart_Order_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawLineChart(data,"Length","Budget","#vis",1600,600);
		        }

		        if(currentQ == 31){
		        	questionID = "PieChart_Order_Nominal_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Genre","Rating","#vis",1600,600);
		        }
		        if(currentQ == 32){
		        	questionID = "Table_Order_Nominal_Numerical_MovieData";
		        	dataVisualizer.drawTable(data,"Genre","Profit($M)","#vis",400);
		        }
		        if(currentQ == 33){
		        	questionID = "Table_Order_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawTable(data,"Length","Profit($M)","#vis",400);
		        }
            if(currentQ == 34){
            		questionID = "BarChart_Order_Ordinal_Numerical_MovieData";
	        		dataVisualizer.drawBarChart(data,"Rating","Length","#vis",1200,600);
		        }
		        if(currentQ == 35){
		        	questionID = "Table_Order_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawTable(data,"Rating","Gross($M)","#vis",400);
		        }
            if(currentQ == 36){
            	questionID = "BarChart_Order_Numerical_Numerical_MovieData";
	        		dataVisualizer.drawBarChart(data,"Length","Profit($M)","#vis",1200,600);
		        }
		        if(currentQ == 37){
		        	questionID = "PieChart_Order_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Length","Rating","#vis",1600,600);
		        }
		         if(currentQ ==38){
		         	questionID = "LineChart_Order_Nominal_Numerical_MovieData";
		        	dataVisualizer.drawLineChart(data,"Genre","Budget","#vis",1600,600);
		        }
		        if(currentQ == 39){
		        	questionID = "LineChart_Order_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawLineChart(data,"Rating","Budget","#vis",1600,600);
		        }
		        if(currentQ == 40){
		        	questionID = "Ranking_Order_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","Highway Miles Per Gallon","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Type","Highway Miles Per Gallon","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Type","Highway Miles Per Gallon","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Type","Highway Miles Per Gallon","#vis5",300);
		        }
		        if(currentQ == 41){
		        	questionID = "Ranking_Order_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawBarChart(data,"Cyl","Len","#vis1",500,200);
		        	dataVisualizer.drawPieChart(data,"Cyl","Len","#vis2",400,300);
		        	dataVisualizer.drawScatterplot(data,"Cyl","Len","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Cyl","Len","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Cyl","Len","#vis5",300);
		        }
		        if(currentQ == 42){
		        	questionID = "Ranking_Order_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Dealer Cost","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Width","Dealer Cost","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Width","Dealer Cost","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Width","Dealer Cost","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Width","Dealer Cost","#vis5",300);
		        }
            if(currentQ == 43){
		        	questionID = "Ranking_Order_Nominal_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Genre","Budget","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Genre","Budget","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Genre","Budget","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Genre","Budget","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Genre","Budget","#vis5",300);

		        }
		        if(currentQ == 44){
		        	questionID = "Ranking_Order_Ordinal_Numerical_MovieData";
		        	dataVisualizer.drawBarChart(data,"Rating","Gross($M)","#vis1",500,200);
		        	dataVisualizer.drawPieChart(data,"Rating","Gross($M)","#vis2",400,300);
		        	dataVisualizer.drawScatterplot(data,"Rating","Gross($M)","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Rating","Gross($M)","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Rating","Gross($M)","#vis5",300);

		        }
		        if(currentQ == 45){
		        	questionID = "Ranking_Order_Numerical_Numerical_MovieData";
		        	dataVisualizer.drawPieChart(data,"Length","Rating","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Length","Rating","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Length","Rating","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Length","Rating","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Length","Rating","#vis5",300);
		        }
	        }

        else if(set == "Range"){
	         if(currentQ == 2){
	        		questionID = "Trial";
		        	dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis",1200,600);
		        }
            if(currentQ == 3){
              questionID = "Trial";
	        		dataVisualizer.drawTable(data,"Type","Dealer Cost","#vis",400);
		        }

		        if(currentQ == 4){
		        	questionID = "Trial";
		        	dataVisualizer.drawPieChart(data,"Width","Retail Price","#vis",1600,600);
		        }
		        if(currentQ == 5){
		        	questionID = "Trial";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Retail Price","#vis",1600,600);
		        }

		        if(currentQ == 6){
		        	questionID = "Trial";
	        		dataVisualizer.drawLineChart(data,"Width","Highway Miles Per Gallon","#vis",1600,600);
		        }

	          if(currentQ == 8){
	            questionID = "Scatterplot_Range_Nominal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 9){
		        	questionID = "Scatterplot_Range_Numerical_Numerical_CarData";
		          dataVisualizer.drawScatterplot(data,"Wheel Base","Dealer Cost","#vis",1600,600);
		        }
		        if(currentQ == 10){
		        	questionID = "LineChart_Range_Numerical_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Width","Horsepower(HP)","#vis",1600,600);
		        }
		        if(currentQ == 11){
		        	questionID = "LineChart_Range_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Cyl","Horsepower(HP)","#vis",1600,600);
		        }

		        if(currentQ == 12){
		        	questionID = "PieChart_Range_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Cyl","Weight","#vis",1600,600);
		        }

		        if(currentQ == 13){
		        	questionID = "Test";
	        		dataVisualizer.drawBarChart(data,"Cyl","Dealer Cost","#vis",1200,600);
		        }
		        if(currentQ == 14){
		        	questionID = "Table_Range_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Cyl","Engine Size (l)","#vis",400);
		        }

            if(currentQ == 15){
              questionID = "Scatterplot_Range_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Len","#vis",1600,600);
		        }
		        if(currentQ == 16){
		        	questionID = "BarChart_Range_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawBarChart(data,"Cyl","Engine Size (l)","#vis",1200,600);
		        }

		        if(currentQ == 17){
		        	questionID = "PieChart_Range_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","Wheel Base","#vis",1600,600);
		        }
		        if(currentQ == 18){
		        	questionID = "Table_Range_Nominal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Type","City Miles Per Gallon","#vis",400);
		        }
		        if(currentQ == 19){
		        	questionID = "Table_Range_Numerical_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Wheel Base","Dealer Cost","#vis",400);
		        }

            if(currentQ == 20){
            	questionID = "BarChart_Range_Numerical_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Highway Miles Per Gallon","Engine Size (l)","#vis",1200,600);
		        }

		        if(currentQ == 21){
		        	questionID = "PieChart_Range_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Retail Price","#vis",1600,600);
		        }
		         if(currentQ ==22){
		         	questionID = "LineChart_Range_Nominal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }

		        if(currentQ == 23){
		        	questionID = "BarChart_Range_Nominal_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Type","Len","#vis",1200,600);
		        }

		        if(currentQ == 24){
		        	questionID = "Test";
		        	dataVisualizer.drawBarChart(data,"Width","Horsepower(HP)","#vis",1200,600);
		        }

            if(currentQ == 25){
                 questionID = "Scatterplot_Range_Nominal_Numerical_MovieData";
             dataVisualizer.drawScatterplot(data,"Genre","Gross($M)","#vis",1600,600);
           }
           if(currentQ == 26){
             questionID = "Scatterplot_Range_Numerical_Numerical_MovieData";
               dataVisualizer.drawScatterplot(data,"Length","Rating","#vis",1600,600);
           }
           if(currentQ == 27){
             questionID = "LineChart_Range_Numerical_Numerical_MovieData";
             dataVisualizer.drawLineChart(data,"Length","Budget","#vis",1600,600);
           }
           if(currentQ == 28){
             questionID = "LineChart_Range_Ordinal_Numerical_MovieData";
             dataVisualizer.drawLineChart(data,"Rating","Length","#vis",1600,600);
           }

           if(currentQ == 29){
             questionID = "PieChart_Range_Ordinal_Numerical_MovieData";
             dataVisualizer.drawPieChart(data,"Rating","Gross($M)","#vis",1600,600);
           }
           if(currentQ == 30){
             questionID = "Table_Range_Ordinal_Numerical_MovieData";
             dataVisualizer.drawTable(data,"Rating","Profit($M)","#vis",400);
           }

           if(currentQ == 31){
                  questionID = "Scatterplot_Range_Ordinal_Numerical_MovieData";
             dataVisualizer.drawScatterplot(data,"Rating","Budget","#vis",1600,600);
           }
           if(currentQ == 32){
             questionID = "BarChart_Range_Ordinal_Numerical_MovieData";
             dataVisualizer.drawBarChart(data,"Rating","Profit($M)","#vis",1200,600);
           }

           if(currentQ == 33){
             questionID = "PieChart_Range_Nominal_Numerical_MovieData";
             dataVisualizer.drawPieChart(data,"Genre","Length","#vis",1600,600);
           }
           if(currentQ == 34){
             questionID = "Table_Range_Nominal_Numerical_MovieData";
             dataVisualizer.drawTable(data,"Genre","Rating","#vis",400);
           }
           if(currentQ == 35){
             questionID = "Table_Range_Numerical_Numerical_MovieData";
             dataVisualizer.drawTable(data,"Length","Rating","#vis",400);
           }

           if(currentQ == 36){
                 questionID = "BarChart_Range_Numerical_Numerical_MovieData";
             dataVisualizer.drawBarChart(data,"Length","Gross($M)","#vis",1200,600);
           }

           if(currentQ == 37){
             questionID = "PieChart_Range_Numerical_Numerical_MovieData";
             dataVisualizer.drawPieChart(data,"Length","Budget","#vis",1600,600);
           }
            if(currentQ ==38){
             questionID = "LineChart_Range_Nominal_Numerical_MovieData";
             dataVisualizer.drawLineChart(data,"Genre","Rating","#vis",1600,600);
           }

           if(currentQ == 39){
             questionID = "BarChart_Range_Nominal_Numerical_MovieData";
             dataVisualizer.drawBarChart(data,"Genre","Length","#vis",1200,600);
           }

		       if(currentQ == 40){
		        	questionID = "Ranking_Range_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawBarChart(data,"Cyl","Len","#vis1",500,200);
		        	dataVisualizer.drawPieChart(data,"Cyl","Len","#vis2",400,300);
		        	dataVisualizer.drawScatterplot(data,"Cyl","Len","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Cyl","Len","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Cyl","Len","#vis5",300);

		        }
		        if(currentQ == 41){
		        	questionID = "Ranking_Range_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Dealer Cost","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Width","Dealer Cost","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Width","Dealer Cost","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Width","Dealer Cost","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Width","Dealer Cost","#vis5",300);

		        }
		        if(currentQ == 42){
				     	questionID = "Ranking_Range_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","Horsepower(HP)","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Type","Horsepower(HP)","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Type","Horsepower(HP)","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Type","Horsepower(HP)","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Type","Horsepower(HP)","#vis5",300);

		        }
           if(currentQ == 43){
             questionID = "Ranking_Range_Ordinal_Numerical_MovieData";
             dataVisualizer.drawBarChart(data,"Rating","Gross($M)","#vis1",500,200);
             dataVisualizer.drawPieChart(data,"Rating","Gross($M)","#vis2",400,300);
             dataVisualizer.drawScatterplot(data,"Rating","Gross($M)","#vis3",500,200);
             dataVisualizer.drawLineChart(data,"Rating","Gross($M)","#vis4",500,200);
             dataVisualizer.drawTable(data,"Rating","Gross($M)","#vis5",300);

           }
           if(currentQ == 44){
             questionID = "Ranking_Range_Numerical_Numerical_MovieData";
             dataVisualizer.drawPieChart(data,"Length","Rating","#vis1",400,300);
             dataVisualizer.drawScatterplot(data,"Length","Rating","#vis2",500,200);
             dataVisualizer.drawBarChart(data,"Length","Rating","#vis3",500,200);
             dataVisualizer.drawLineChart(data,"Length","Rating","#vis4",500,200);
             dataVisualizer.drawTable(data,"Length","Rating","#vis5",300);

           }
           if(currentQ == 45){
             questionID = "Ranking_Range_Nominal_Numerical_MovieData";
             dataVisualizer.drawPieChart(data,"Genre","Gross($M)","#vis1",400,300);
             dataVisualizer.drawScatterplot(data,"Genre","Gross($M)","#vis2",500,200);
             dataVisualizer.drawBarChart(data,"Genre","Gross($M)","#vis3",500,200);
             dataVisualizer.drawLineChart(data,"Genre","Gross($M)","#vis4",500,200);
             dataVisualizer.drawTable(data,"Genre","Gross($M)","#vis5",300);
           }
	      }

        else if(set == "Retrieve"){
              if(currentQ == 2){
            			questionID = "Trial";
            	    dataVisualizer.drawTable(data,"Type","Highway Miles Per Gallon","#vis",400);
            	}
            	if(currentQ == 3){
            	    questionID = "Trial";
            		  dataVisualizer.drawPieChart(data,"Cyl","Retail Price","#vis",1600,600);
              }
              if(currentQ == 4){
            		  questionID = "Trial";
            		  dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis",1200,600);
              }
            	if(currentQ == 5){
            		  questionID = "Trial";
            	    dataVisualizer.drawLineChart(data,"Width","Weight","#vis",1600,600);
            	}
              if(currentQ == 6){
            		  questionID = "Trial";
            		  dataVisualizer.drawScatterplot(data,"Cyl","Highway Miles Per Gallon","#vis",1600,600);
            	}

	/*********************/
	        	if(currentQ == 8){
	        		questionID = "BarChart_Retrieve_Nominal_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Type","City Miles Per Gallon","#vis",1200,600);
		        }
		        if(currentQ == 9){
		        	questionID = "PieChart_Retrieve_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Cyl","Weight","#vis",1600,600);
		        }
	          if(currentQ == 10){
	            questionID = "Scatterplot_Retrieve_Nominal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 11){
		        	questionID = "Scatterplot_Retrieve_Numerical_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Wheel Base","Dealer Cost","#vis",1600,600);
		        }
		        if(currentQ == 12){
		        	questionID = "Scatterplot_Retrieve_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Engine Size (l)","#vis",1600,600);
		        }
            if(currentQ == 13){
              questionID = "Test";
		        	dataVisualizer.drawScatterplot(data,"Cyl","Engine Size (l)","#vis",1600,600);
		        }
		        if(currentQ == 14){
		        	questionID = "LineChart_Retrieve_Numerical_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Width","Horsepower(HP)","#vis",1600,600);
		        }

		        if(currentQ == 15){
		        	questionID = "PieChart_Retrieve_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 16){
		        	questionID = "Table_Retrieve_Nominal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Type","City Miles Per Gallon","#vis",400);
		        }
		        if(currentQ == 17){
		        	questionID = "Table_Retrieve_Numerical_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Wheel Base","Dealer Cost","#vis",400);
		        }
            	if(currentQ == 18){
            		questionID = "BarChart_Retrieve_Ordinal_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Cyl","Dealer Cost","#vis",1200,600);
		        }
		        if(currentQ == 19){
		        	questionID = "Table_Retrieve_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawTable(data,"Cyl","Engine Size (l)","#vis",400);
		        }

            if(currentQ == 20){
            		questionID = "BarChart_Retrieve_Numerical_Numerical_CarData";
	        		dataVisualizer.drawBarChart(data,"Width","Engine Size (l)","#vis",1200,600);
		        }

		        if(currentQ == 21){
		        	questionID = "PieChart_Retrieve_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Retail Price","#vis",1600,600);
		        }
		         if(currentQ ==22){
		         	questionID = "LineChart_Retrieve_Nominal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Type","City Miles Per Gallon","#vis",1600,600);
		        }
		        if(currentQ == 23){
		        	questionID = "LineChart_Retrieve_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawLineChart(data,"Cyl","Horsepower(HP)","#vis",1600,600);
		        }

		        if(currentQ == 24){
		        	questionID = "Test";
		        	dataVisualizer.drawBarChart(data,"Width","Horsepower(HP)","#vis",1200,600);
		        }

            if(currentQ == 25){
               questionID = "BarChart_Retrieve_Nominal_Numerical_MovieData";
            	 dataVisualizer.drawBarChart(data,"Genre","Gross($M)","#vis",1200,600);
            }
            if(currentQ == 26){
            	 questionID = "PieChart_Retrieve_Ordinal_Numerical_MovieData";
            	 dataVisualizer.drawPieChart(data,"Rating","Length","#vis",1600,600);
            }
            if(currentQ == 27){
            	 questionID = "Scatterplot_Retrieve_Nominal_Numerical_MovieData";
            	 dataVisualizer.drawScatterplot(data,"Genre","Rating","#vis",1600,600);
            }
            if(currentQ == 28){
            	 questionID = "Scatterplot_Retrieve_Numerical_Numerical_MovieData";
            	 dataVisualizer.drawScatterplot(data,"Length","Rating","#vis",1600,600);
            }
            if(currentQ == 29){
            	 questionID = "Scatterplot_Retrieve_Ordinal_Numerical_MovieData";
            	 dataVisualizer.drawScatterplot(data,"Rating","Gross($M)","#vis",1600,600);
            }
            if(currentQ == 30){
            	 questionID = "LineChart_Retrieve_Numerical_Numerical_MovieData";
            	 dataVisualizer.drawLineChart(data,"Length","Gross($M)","#vis",1600,600);
            }
            if(currentQ == 31){
            	 questionID = "PieChart_Retrieve_Nominal_Numerical_MovieData";
            	 dataVisualizer.drawPieChart(data,"Genre","Length","#vis",1600,600);
            }
            if(currentQ == 32){
            		questionID = "Table_Retrieve_Nominal_Numerical_MovieData";
            		dataVisualizer.drawTable(data,"Genre","Profit($M)","#vis",400);
            }
            if(currentQ == 33){
            		questionID = "Table_Retrieve_Numerical_Numerical_MovieData";
            		dataVisualizer.drawTable(data,"Length","Profit($M)","#vis",400);
            }
          	if(currentQ == 34){
                questionID = "BarChart_Retrieve_Ordinal_Numerical_MovieData";
            		dataVisualizer.drawBarChart(data,"Rating","Gross($M)","#vis",1200,600);
            }
            if(currentQ == 35){
            		questionID = "Table_Retrieve_Ordinal_Numerical_MovieData";
            		dataVisualizer.drawTable(data,"Rating","Length","#vis",400);
            }
            if(currentQ == 36){
            		questionID = "BarChart_Retrieve_Numerical_Numerical_MovieData";
            		dataVisualizer.drawBarChart(data,"Length","Budget","#vis",1200,600);
            }
            if(currentQ == 37){
            		questionID = "PieChart_Retrieve_Numerical_Numerical_MovieData";
            		dataVisualizer.drawPieChart(data,"Length","Budget","#vis",1600,600);
            }
            if(currentQ == 38){
            		questionID = "LineChart_Retrieve_Nominal_Numerical_MovieData";
            		dataVisualizer.drawLineChart(data,"Genre","Gross($M)","#vis",1600,600);
            }
            if(currentQ == 39){
            		questionID = "LineChart_Retrieve_Ordinal_Numerical_MovieData";
            		dataVisualizer.drawLineChart(data,"Rating","Gross($M)","#vis",1600,600);
            }
		        if(currentQ == 40){
		        	questionID = "Ranking_Retrieve_Nominal_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Type","Highway Miles Per Gallon","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Type","Highway Miles Per Gallon","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Type","Highway Miles Per Gallon","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Type","Highway Miles Per Gallon","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Type","Highway Miles Per Gallon","#vis5",300);
		        }
		        if(currentQ == 41){
		        	questionID = "Ranking_Retrieve_Ordinal_Numerical_CarData";
		        	dataVisualizer.drawBarChart(data,"Cyl","Len","#vis1",500,200);
		        	dataVisualizer.drawPieChart(data,"Cyl","Len","#vis2",400,300);
		        	dataVisualizer.drawScatterplot(data,"Cyl","Len","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Cyl","Len","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Cyl","Len","#vis5",300);
		        }
		        if(currentQ == 42){
		        	questionID = "Ranking_Retrieve_Numerical_Numerical_CarData";
		        	dataVisualizer.drawPieChart(data,"Width","Dealer Cost","#vis1",400,300);
		        	dataVisualizer.drawScatterplot(data,"Width","Dealer Cost","#vis2",500,200);
		        	dataVisualizer.drawBarChart(data,"Width","Dealer Cost","#vis3",500,200);
		        	dataVisualizer.drawLineChart(data,"Width","Dealer Cost","#vis4",500,200);
		        	dataVisualizer.drawTable(data,"Width","Dealer Cost","#vis5",300);
		        }
            if(currentQ == 43){
             questionID = "Ranking_Retrieve_Nominal_Numerical_MovieData";
             dataVisualizer.drawPieChart(data,"Genre","Gross($M)","#vis1",400,300);
             dataVisualizer.drawScatterplot(data,"Genre","Gross($M)","#vis2",500,200);
             dataVisualizer.drawBarChart(data,"Genre","Gross($M)","#vis3",500,200);
             dataVisualizer.drawLineChart(data,"Genre","Gross($M)","#vis4",500,200);
             dataVisualizer.drawTable(data,"Genre","Gross($M)","#vis5",300);

           }
           if(currentQ == 44){
             questionID = "Ranking_Retrieve_Ordinal_Numerical_MovieData";
             dataVisualizer.drawBarChart(data,"Rating","Budget","#vis1",500,200);
             dataVisualizer.drawPieChart(data,"Rating","Budget","#vis2",400,300);
             dataVisualizer.drawScatterplot(data,"Rating","Budget","#vis3",500,200);
             dataVisualizer.drawLineChart(data,"Rating","Budget","#vis4",500,200);
             dataVisualizer.drawTable(data,"Rating","Budget","#vis5",300);

           }
           if(currentQ == 45){
             questionID = "Ranking_Retrieve_Numerical_Numerical_MovieData";
             dataVisualizer.drawPieChart(data,"Length","Rating","#vis1",400,300);
             dataVisualizer.drawScatterplot(data,"Length","Rating","#vis2",500,200);
             dataVisualizer.drawBarChart(data,"Length","Rating","#vis3",500,200);
             dataVisualizer.drawLineChart(data,"Length","Rating","#vis4",500,200);
             dataVisualizer.drawTable(data,"Length","Rating","#vis5",300);

           }
	        }

		})

 	}
