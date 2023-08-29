
## ---- chunk:example
set.seed(602)
library(MASS) # to generate multi-var distribution
e <-  as.numeric(mvrnorm(n = 100, mu = 0, Sigma = 1))
plot(e)
##