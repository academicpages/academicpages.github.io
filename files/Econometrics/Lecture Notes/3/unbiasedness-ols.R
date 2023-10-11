### Unbiasedness of the OLS estimator

# Simular os dados
N <- 100000
X <- runif(N, min = 0, max = 20)
u <- rnorm(N, sd = 10)

# population regression
Y <- -2 + 3.5 * X + u
population <- data.frame(X, Y)



# set repetitions and sample size
n <- 100
reps <- 10000

# initialize the matrix of outcomes
fit <- matrix(ncol = 2, nrow = reps)

# loop sampling and estimation of the coefficients
for (i in 1:reps){
  
  sample <- population[sample(1:N, n), ]
  fit[i, ] <- lm(Y ~ X, data = sample)$coefficients
  
}


# plot histograms of beta_hat_1 
hist(fit[, 2],
     cex.main = 0.8,
     main = bquote(The ~ Distribution  ~ of ~ 10000 ~ beta[1] ~ Estimates), 
     xlab = bquote(hat(beta)[1]), 
     freq = F)

