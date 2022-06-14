# Required libraries
library(haven)
library(lmtest)
library(sandwich)
library(AER)
library(plm)
library(multiwayvcov)
library(gsynth)
library(xtable)

# Import data
d1 = read_stata("/Users/eelrice/Desktop/School/3. 2022S/41903/Replication/116365-V1/data/AirSea_stage2working.dta")
cols = c("wbcode", "year_t", "ln_trade_p1", "ln_trade_p1pop", "ln_trade_p4",
         "ln_trade_p4pop", "ln_tradei", "ln_gdpc")
d2 = d1[!is.na(d1$landlock), cols] # remove landlocked (main specification)

# Weak Identification Robust Inference
## First Differences
d3 = pdata.frame(d2, index = c("wbcode", "year_t"))
dx = diff(d3$ln_tradei)
dy = diff(d3$ln_gdpc)
dz1 = diff(d3$ln_trade_p1pop)
dz2 = diff(d3$ln_trade_p4pop)

### Column 2 of FD
fd_col2 = ivreg(dy ~ -1 + dx + factor(year_t) | . - dx + dz1, data = d2)
est1 = coeftest(fd_col2, vcov = vcovCL, cluster = ~wbcode, type = "HC1")[1, ]
pt_est1 = est1[1]
conf_int1 = c(est1[1] - 1.96*est1[2], est1[1] + 1.96*est1[2])
fs1 = lm(dx ~ -1 + dz1 + factor(year_t), data = d2)
fstat1 = coeftest(fs1, vcov = vcovCL, cluster = ~wbcode, type = "HC1")[1, 3]**2

### Column 4 of FD
fd_col4 = ivreg(dy ~ -1 + dx + factor(year_t) | . - dx + dz2, data = d2)
est2 = coeftest(fd_col4, vcov = vcovCL, cluster = ~wbcode, type = "HC1")[1, ]
pt_est2 = est2[1]
conf_int2 = c(est2[1] - 1.96*est2[2], est2[1] + 1.96*est2[2])
fs2 = lm(dx ~ -1 + dz2 + factor(year_t), data = d2)
fstat2 = coeftest(fs2, vcov = vcovCL, cluster = ~wbcode, type = "HC1")[1, 3]**2


Mdy = lm(dy ~ factor(year_t), data = d2)$resid
Mdx = lm(dx ~ factor(year_t), data = d2)$resid
Mdz1 = lm(dz1 ~ factor(year_t), data = d2)$resid
Mdz2 = lm(dz2 ~ factor(year_t), data = d2)$resid

### Function to estimate gamma
gamma = function(b){
  temp_mod1 = lm((Mdy - b*Mdx) ~ Mdz1 - 1)
  rej1 = (coeftest(temp_mod1, vcov = sandwich)[4] < 0.05)
  
  temp_mod2 = lm((Mdy - b*Mdx) ~ Mdz2 - 1)
  rej2 = (coeftest(temp_mod2, vcov = sandwich)[4] < 0.05)
  return(c(rej1, rej2))
}

### Try values in [-1, 4]
bs = seq(-1, 4, by = 0.001)
region = data.frame()
for(b in bs){
  temp = gamma(b)
  region = rbind(region, c(b, temp))
}
colnames(region) = c("b", "z1", "z2")

reg_1 = region$b[region$z1 == 0]
reg_2 = region$b[region$z2 == 0]
rob_conf_int1 = c(min(reg_1), max(reg_1))
rob_conf_int2 = c(min(reg_2), max(reg_2))


## Fixed Effects -- Main specification (for comparison)
mod_fe = ivreg(ln_gdpc ~ -1 + ln_tradei + factor(year_t) + factor(wbcode) | . - ln_tradei + ln_trade_p1, data = d2)
est3 = coeftest(mod_fe, vcov = vcovCL, cluster = ~wbcode, type = "HC1")[1, ]
pt_est3 = est3[1]
conf_int3 = c(est3[1] - 1.96*est3[2], est3[1] + 1.96*est3[2])
fs3 = lm(ln_tradei ~ -1 + ln_trade_p1 + factor(wbcode) + factor(year_t), data = d2)
fstat3 = coeftest(fs3, vcov = vcovCL, cluster = ~wbcode, type = "HC1")[1, 3]**2

### Partial out
My = lm(ln_gdpc ~ factor(wbcode) + factor(year_t), data = d2)$resid
Mx = lm(ln_tradei ~ factor(wbcode) + factor(year_t), data = d2)$resid
Mz = lm(ln_trade_p1 ~ factor(wbcode) + factor(year_t), data = d2)$resid

### Function to estimate gamma for FE
gamma1 = function(b){
  temp_mod1 = lm((My - b*Mx) ~ Mz - 1, data = d2)
  rej1 = (coeftest(temp_mod1, vcov = sandwich)[4] < 0.05)
  return(rej1)
}

### Try values in [-1, 1]
bs = seq(-1, 1, by = 0.001)
region1 = data.frame()
for(b in bs){
  temp = gamma1(b)
  region1 = rbind(region1, c(b, temp))
}
reg = region1$X.1[region1$X1 == 0]
rob_conf_int3 = c(min(reg), max(reg))

## Table Output
N = c(774, 774, 774)
fstats = c(fstat1, fstat2, fstat3)
pt_ests = c(pt_est1, pt_est2, pt_est3)

int1 = paste0("(", round(conf_int1[1], 4), ",", round(conf_int1[2], 4), ")")
int2 = paste0("(", round(conf_int2[1], 4), ",", round(conf_int2[2], 4), ")")
int3 = paste0("(", round(conf_int3[1], 4), ",", round(conf_int3[2], 4), ")")
asym_ints = c(int1, int2, int3)

r_int1 = paste0("(", round(rob_conf_int1[1], 4), ",", round(rob_conf_int1[2], 4), ")")
r_int2 = paste0("(", round(rob_conf_int2[1], 4), ",", round(rob_conf_int2[2], 4), ")")
r_int3 = paste0("(", round(rob_conf_int3[1], 4), ",", round(rob_conf_int3[2], 4), ")")
rob_ints = c(r_int1, r_int2, r_int3)

tab1 = rbind(N, round(fstats, 4), round(pt_ests, 4), asym_ints, rob_ints)
tab1 = as.data.frame(tab1, row.names = c("N", "F", "beta", "Asymptotic C.I", "Robust C.I."))
colnames(tab1) = c("(1)", "(2)", "(3)")
cat(print(xtable(tab1, caption = "Weak Identification Robust Inference"),
          include.rownames = T, caption.placement = "top"),
    file = "1 Robust Inference.tex")

# Interactive Fixed Effects
d4 = as.data.frame(d2)
d4$t = d4$year_t - 390
mod_lin_t = ivreg(ln_gdpc ~ -1 + ln_tradei + factor(wbcode):t +
                    factor(year_t) + factor(wbcode) | . - ln_tradei +
                    ln_trade_p1, data = d4)
coeftest(mod_lin_t, vcov = vcovCL, cluster = ~wbcode, type = "HC1")[1:2, ]


gamma_int = function(b, r = 1, nboots = 200){
  tilde_y = d4$ln_gdpc - b*d4$ln_tradei
  z = d4$ln_trade_p1
  country = d4$wbcode
  year = d4$year_t
  temp = data.frame(tilde_y, z, country, year)
  mod = interFE(tilde_y ~ z, data = temp, index = c("country", "year"), 
                r = r, nboots = nboots, normalize = T, seed = 1)
  rej = ifelse(mod$est.table[1, 5] < 0.05, 1, 0)
  return(c(b, rej))
}

bs = seq(-0.1, 0.5, by = 0.01)
region_r2 = data.frame()
for(b in bs){
  rej_ = gamma_int(b, r = 2, nboots = 10)
  region_r2 = rbind(region_r2, rej_)
}
region_r3 = data.frame()
for(b in bs){
  rej_ = gamma_int(b, r = 3, nboots = 10)
  region_r3 = rbind(region_r3, rej_)
}
region_r4 = data.frame()
for(b in bs){
  rej_ = gamma_int(b, r = 4, nboots = 10)
  region_r4 = rbind(region_r4, rej_)
}

bs2 = seq(0.28, 0.31, by = 0.001)
region_r2_r = data.frame()
for(b in bs2){
  rej_ = gamma_int(b, r = 2, nboots = 10)
  region_r2_r = rbind(region_r2_r, rej_)
}
region_r3_r = data.frame()
for(b in bs2){
  rej_ = gamma_int(b, r = 3, nboots = 10)
  region_r3_r = rbind(region_r3_r, rej_)
}
region_r4_r = data.frame()
for(b in bs2){
  rej_ = gamma_int(b, r = 4, nboots = 10)
  region_r4_r = rbind(region_r4_r, rej_)
}

colnames(region_r2_r) = c("b", "rej")
colnames(region_r3_r) = c("b", "rej")
colnames(region_r4_r) = c("b", "rej")

r1 = region_r2_r$b[region_r2_r$rej == 0]
r2 = region_r3_r$b[region_r3_r$rej == 0]
r3 = region_r4_r$b[region_r4_r$rej == 0]

c(min(r1), max(r1))
c(min(r2), max(r2))
c(min(r3), max(r3))

pt_ests2 = c(median(r1), median(r2), median(r3))
ints1 = paste0("(", min(r1), ",", max(r1), ")")
ints2 = paste0("(", min(r2), ",", max(r2), ")")
ints3 = paste0("(", min(r3), ",", max(r3), ")")
conf_ints = c(ints1, ints2, ints3)
factors = c(2, 3, 4)

tab2 = rbind(factors, pt_ests2, conf_ints)
tab2 = as.data.frame(tab2, row.names = c("r", "beta", "Robust C.I."))
colnames(tab2) = c("(1)", "(2)", "(3)")
cat(print(xtable(tab2, caption = "Interactive Fixed Effects Estimation"),
          include.rownames = T, caption.placement = "top"),
    file = "2 Interactive Fixed Effects.tex")
