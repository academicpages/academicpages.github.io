### Bias and Consistency

## Generate function to show the sampling distribution
histfun <- function(what,breaks=44,mainn,xlim=c(1,3)){
  cexx=1.4;lwdd=4
  hist(beta,breaks=44,freq=F,xlim=c(1,3),main=paste(mainn, ", #Obs = ", n,sep=""),
       cex.axis=cexx,cex.main=cexx,cex.lab=cexx-.2,col='lightblue')
  den <- density(what)
  abline(v=2,col=3,lwd=lwdd)
  abline(v=mean(what),col=2,lwd=lwdd)
  lines(den,col=2,lwd=lwdd)
}

### Unbiased and Consistent
repet <- 1000
n <- 20
beta <- NULL
for (i in 1:repet){
  x <- rnorm(n)
  eps <- rnorm(n,0,1)
  y=2+2*x+eps
  beta[i] <- lm(y~x)$coef[2]
}
histfun(beta, mainn= "Unbiased")

n <- 1000
beta <- NULL
for (i in 1:repet){
  x <- rnorm(n)
  eps <- rnorm(n,0,1)
  y=2+2*x+eps
  beta[i] <- lm(y~x)$coef[2]
}
histfun(beta,mainn="Consistent")

###  Biased But Consistent
n <- 20
beta <- NULL
for (i in 1:repet){
  x <- rnorm(n)
  eps <- rnorm(n,0,1)
  y=2+2*x+eps
  beta[i] <- (10/n)+lm(y~x)$coef[2] 
}
histfun(beta,mainn="Biased")

n <- 1000
for (i in 1:repet){
  x <- rnorm(n)
  eps <- rnorm(n,0,1)
  y=2+2*x+eps
  beta[i] <- (10/n)+lm(y~x)$coef[2] 
}
histfun(beta,mainn="Consistent")

### Omitted Variable Bias: Biased and Inconsistent
n <- 20
beta <- NULL
for (i in 1:repet){
  x <- rnorm(n)
  x2 <- rnorm(n)+.2*x # make it correlate with x
  eps <- rnorm(n,0,1)
  y=2+2*x+2*x2+eps
  beta[i] <- lm(y~x)$coef[2] # Do not include x2
}
histfun(beta,mainn="Biased")

n <- 1000
beta <- NULL
for (i in 1:repet){
  x <- rnorm(n)
  x2 <- rnorm(n)+.2*x 
  eps <- rnorm(n,0,1)
  y=2+2*x+2*x2+eps
  beta[i] <- lm(y~x)$coef[2] 
}
histfun(beta,mainn="Inconsistent")

###  Unbiased But Inconsistent
n <- 20
beta <- NULL
for (i in 1:repet){
  x <- 1:n
  z <- 1/x
  eps <- rnorm(n,0,1)
  y=2+2*z+eps
  beta[i] <- lm(y~z)$coef[2] 
}
histfun(beta,mainn="Unbiased")

n <- 1000
beta <- NULL
for (i in 1:repet){
  x <- 1:n
  z <- 1/x
  eps <- rnorm(n,0,1)
  y=2+2*z+eps
  beta[i] <- lm(y~z)$coef[2] 
}
histfun(beta,mainn="Inconsistent")