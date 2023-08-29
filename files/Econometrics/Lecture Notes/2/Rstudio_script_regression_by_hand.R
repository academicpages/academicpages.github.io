#Estimating the OLS model NA TORA

y <- matrix(c(6,11,4,3,5,9,10),7,1)
y

X <- matrix(c(1,1,1,1,1,1,1,4,7,2,1,3,7,8,5,2,6,9,4,3,2,4,3,4,6,5,4,5),7,4)
X

X.prime <- t(X)
X.prime

X.prime.X <- X.prime %*% X
X.prime.X

X.prime.X.inv<-solve(X.prime.X)
X.prime.X.inv

X.prime.X.inv.X.prime<-X.prime.X.inv %*% X.prime
X.prime.X.inv.X.prime

b<-X.prime.X.inv.X.prime %*% y
b

#Confirming our calculations
lm(y~0+X)

#Find the fitted values:
y.hat <- X %*% b 
y.hat

#Find the residuals