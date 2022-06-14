*Corporate Finance Theory I Replication Assignment;
proc means data=school.assign;
run;
data assign1; *Subsetting data according to Frank and Goyal (2003);
	set school.assign;
	if substr(SIC,1,2) = '49' then delete; *utilities;
	if substr(SIC,1,1) = '6' then delete; *financials;
	if at =. then delete; *missing book value of assets;
	if scf in (4, 5, 6) then delete; *inappropriate cash flow format;
	if scf=. then delete; *cash flow format not available;
	if seq <0 then delete; *firms with negative net worth or capital impariment;
	if sale_fn = 'AB' then delete; *major mergers;
run;
proc means data=assign1;
run;
data assign2; *Recoding missing data as 0 where appropriate and creating relevant variables;
	set assign1;
	if aco=. then aco=0;
	if ao=. then ao=0;
	if aoloch=. then aoloch=0;
	if apalch=. then apalch=0;
	if aqc=. then aqc=0;
	if capx=. then capx=0;
	if chech=. then chech=0;
	if dlcch=. then dlcch=0;
	if dpc=. then dpc=0;
	if exre=. then exre=0;
	if fiao=. then fiao=0;
	if fopo=. then fopo=0;
	if fsrco=. then fsrco=0;
	if fuset=. then fuset=0;
	if invch=. then invch=0;
	if ivaco=. then ivaco=0;
	if ivaeq=. then ivaeq=0;
	if ivao=. then ivao=0;
	if ivch=. then ivch=0;
	if ivstch=. then ivstch=0;
	if lco=. then lco=0;
	if mib=. then mib=0;
	if ppent=. then ppent=0;
	if recch=. then recch=0;
	if sppiv=. then sppiv=0;
	if txach=. then txach=0;
	if wcapc=. then wcapc=0;
	if txdc=. then txdc=0;
	if xidoc=. then xidoc=0;
	if txditc=. then txditc=0;
	if dv=. then dv=0;
	if ch=. then ch=0;
	if esubc=. then esubc=0;
	if ibc=. then ibc=0;
	if intan=. then intan=0;
	if ivst=. then ivst=0;
	meq = prcc_f*csho;
	mat = at+(meq - seq);
	fd = dlc+dltt;
	blev = fd/at;
	mlev = fd/mat;
	blev_w1 = lt/at;
	mlev_w1=lt/mat;
	blev_w2 = fd/(seq+fd);
	mlev_w2 = fd/(meq+fd);
	mtob = mat/at;
	tang = ppent/at;
	lsale = log(Sale+1);
	profit = oibdp/at;
	keep gvkey sic _numeric_;
	drop mkvalt prcc_c prcc_f csho scf;	
run;
proc means data=assign2;
run;

*Winsorizing;
proc sql noprint;
	select name into :var_list separated by " "
	from sashelp.vcolumn
	where upper(libname)='WORK' and upper(memname)='ASSIGN2'
	and varnum between 5 and 68;
quit;
%winsor(dsetin=assign2, dsetout=assign3, byvar=none, vars=&var_list, type=delete, pctl=0.5 99.5);

*Descriptive data after data treatment and trimming;
proc means data=assign3 n mean median min q1 q3 max;
run;

*Running regressions with time fixed effects;
proc glm data=assign3;
	class fyear;
	model blev = mtob tang lsale profit fyear/solution noint;
run;
proc glm data=assign3;
	class fyear;
	model mlev = mtob tang lsale profit fyear/solution noint;
run;

*Median industry level leverage;
proc sql;
	create table ind as
	select fyear, sic, median(blev) as bmed, median(mlev) as mmed, median(blev_w1) as bmed_w1, median(mlev_w1) as mmed_w1,
	median(blev_w2) as bmed_w2, median(mlev_w2) as mmed_w2
	from assign3
	group by fyear, sic;
quit;
proc sql;
	create table assign4 as
	select a.*, b.*
	from assign3 as a left join ind as b
	on a.fyear=b.fyear and a.sic=b.sic;
quit;
proc means data=assign4 n mean median min q1 q3 max;
run;
proc print data=assign4(obs=100);
	where bmed=0;
run;
data school.q12;
	set assign4;
run;
proc glm data=school.q12;
	class fyear;
	model blev = mtob tang lsale profit fyear bmed/solution noint;
run;
proc glm data=school.q12;
	class fyear;
	model mlev = mtob tang lsale profit fyear mmed/solution noint;
run;
*The results are consistent with Rajan and Zingales (1995);

*Using Welch (2011) measure;
proc glm data=school.q12;
	class fyear;
	model blev_w1 = mtob tang lsale profit fyear bmed_w1/solution noint;
run;
proc glm data=school.q12;
	class fyear;
	model mlev_w1 = mtob tang lsale profit fyear mmed_w1/solution noint;
run;
proc glm data=school.q12;
	class fyear;
	model blev_w2 = mtob tang lsale profit fyear bmed_w2/solution noint;
run;
proc glm data=school.q12;
	class fyear;
	model mlev_w2 = mtob tang lsale profit fyear mmed_w2/solution noint;
run;
*The new dependent variable does not alter the main results;

*Firm fixed effects;
proc sort data=school.q12;
	by gvkey;
run;
proc glm data=school.q12;
	absorb gvkey;
	class fyear;
	model blev_w1 = mtob tang lsale profit fyear bmed_w1/solution noint;
run;
proc glm data=school.q12;
	absorb gvkey;
	class fyear;
	model mlev_w1 = mtob tang lsale profit fyear mmed_w1/solution noint;
run;
*The main results continue to hold even with the inclusion of firm fixed effects;

*Initial leverage;
proc sort data=school.q12;
	by gvkey fyear;
run;
data init;
	set school.q12;
	by gvkey fyear;
	if blev_w1=. then delete;
	if mlev_w1=. then delete;
	if first.gvkey then binit = blev_w1;
	if first.gvkey then minit = mlev_w1;
	if first.gvkey then output;
run;
proc sql;
	create table school.q6 as
	select a.*, b.binit, b.minit
	from school.q12 as a left join init as b
	on a.gvkey=b.gvkey;
quit;
proc glm data=school.q6;
	class fyear;
	model blev = binit mtob tang lsale profit fyear bmed/solution noint;
run;
proc glm data=school.q6;
	class fyear;
	model mlev = minit mtob tang lsale profit fyear mmed/solution noint;
run;
proc glm data=school.q6;
	class fyear;
	model blev_w1 = binit mtob tang lsale profit fyear bmed_w1/solution noint;
run;
proc glm data=school.q6;
	class fyear;
	model mlev_w1 = minit mtob tang lsale profit fyear mmed_w1/solution noint;
run;
proc glm data=school.q6;
	class fyear;
	model blev_w2 = binit mtob tang lsale profit fyear bmed_w2/solution noint;
run;
proc glm data=school.q6;
	class fyear;
	model mlev_w2 = minit mtob tang lsale profit fyear mmed_w2/solution noint;
run;
*As in Lemmon et al. (2008), initial leverage has a large explanatory power;
