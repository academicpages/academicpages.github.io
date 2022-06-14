xtivdfreg ln_gdpc ln_tradei, absorb(wbnum year_t) iv(ln_trade_p1) factmax(2)
eststo int_fe
esttab int_fe using ./tables/int_fe.tex
