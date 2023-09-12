#Estimating the OLS model NA TORA

y <- matrix(c(6,11,4,3),4,1)
y

X <- matrix(c(1,1,1,1,4,7,2,1,2,6,9,4),4,3)
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
e <- y - y.hat
e

#Getting the M and P matrices
X.X.prime.X.inv.X.prime<-X %*% X.prime.X.inv.X.prime
X.X.prime.X.inv.X.prime

identity<-diag(4)

M<-identity - X.X.prime.X.inv.X.prime
P<- X.X.prime.X.inv.X.prime

#Compare residuals with the ones obtained before
M %*% y
P %*% y

#Create partition with X1=(1 1 1 1):
X1 <- matrix(c(1,1,1,1),4,1)

X1.prime <- t(X1)
X1.prime

X1.prime.X1 <- X1.prime %*% X1
X1.prime.X1

X1.prime.X1.inv<-solve(X1.prime.X1)
X1.prime.X1.inv

X1.prime.X1.inv.X1.prime<-X1.prime.X1.inv %*% X1.prime
X1.prime.X1.inv.X1.prime

#Getting the M1 and P1 matrices
X1.X1.prime.X1.inv.X1.prime<-X1 %*% X1.prime.X1.inv.X1.prime
X1.X1.prime.X1.inv.X1.prime

identity<-diag(4)

M1<-identity - X1.X1.prime.X1.inv.X1.prime
P1<- X1.X1.prime.X1.inv.X1.prime

y_dev <- M1 %*% y

#Find squared sum of total
y.prime<-t(y)
sst <- y.prime %*% M1 %*% y

#Find sum of squared residuals
e.prime<-t(e)
e.prime.e <- e.prime %*% e
e.prime.e
