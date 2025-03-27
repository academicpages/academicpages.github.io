// Minnesota Model

data {
  int<lower=1> T;
  vector[T] Y;
  int<lower=0> K;
  matrix[T,K] X;
  vector[K] Xf;
  real yf;

  // Variance for intercept
  real<lower=0> alpha_sd;

  // AR(4) residual variances of y and X
  real<lower=0> var_y_minn;
  vector<lower=0>[K] var_x_minn;
  int<lower=0> pp;
  
}

transformed data{
  real Ymean;
  real sd_Yc;
  vector[T] Yc;
  matrix[K,K] xtx;

  xtx = X' * X;

  Ymean = mean(Y);
  for (i in 1:T){
    Yc[i] = Y[i] - Ymean;
  }

  sd_Yc = sd(Yc);

}

parameters {
  // States
  array[T] vector[K] z_beta;
  
  // Variance Parameters
  real<lower=0> sigma;
  // State AR Weights
  vector<lower=0,upper=1>[K] phi;
  // Minnesota scale parameter
  real<lower=0> kappa2_k;
  // Intercept parameters
  real alpha;
  vector<lower=0>[K] lam_diff;
  //real<lower=0> nu_diff;
}


transformed parameters{
  vector<lower=0>[K] sigma_beta = sqrt(var_y_minn)* sqrt(1./var_x_minn) * sqrt(kappa2_k);
  vector<lower=0>[K] sigma_diff = lam_diff;
  array[T] vector[K] beta;
  // Initial Conditions
  beta[1] = z_beta[1] .* sigma_beta;

  // Loop here for TVP coefficients
  for (t in 2:T){
  beta[t]  =  phi.*beta[t-1] + z_beta[t] .* sigma_diff;
  }
  
}

model {
  // Priors
  sigma ~ student_t(3,0, sd_Yc);
  
    for (t in 1:T) {
  z_beta[t] ~ std_normal();
  }

  (phi +1)./2 ~ beta(10,2); // prior ensures stationarity of the AR coefficients


  kappa2_k ~ gamma(1,1/(0.04^2));
  lam_diff ~ student_t(1,0,1);
  //nu_diff ~ student_t(1,0,1);

  // Observation Likelihood
  target += normal_lpdf(alpha | 0, alpha_sd); // Intercept
  
  if (pp == 0) {
for (t in 1:T){
  Yc[t] ~ normal(X[t,]*beta[t] + alpha, sigma);
}
}
}

generated quantities {
    // Define storage
  real intercept = alpha + Ymean;
  real marg_r2 = sum(sigma_beta)/(sum(sigma_beta + sigma^2));
  vector[K] beta_T = phi.*beta[T];
  vector[K] bf;
  real muf;
  real yf_pred;
  real yf_lpdf;
  vector[T] R2_t; // R2 over time
  vector[T] log_lik;
  vector[T] ypred;
  
  // Define storage for Hadamard product
  matrix[T,K] X_tilde;
  
  // Define storage for row sums
  vector[T] s;
  real<lower=0,upper=1> R2_samp;
  
  // Calculate the Hadamard product and row sums
  for (t in 1:T) {
    s[t] = 0; // Initialize sum for row t
    for (k in 1:K) {
      X_tilde[t,k] = beta[t][k] * X[t,k];
      s[t] += X_tilde[t,k]; // Sum the elements in row t
    }
  }
  
  // R2 over time + logscores
  for (t in 1:T){
    R2_t[t] =  ((X[t,]*beta[t])^2)/((X[t,]*beta[t])^2 + sigma^2);
    log_lik[t] = normal_lpdf(Yc[t] | X[t,]*beta[t] + intercept,sigma);
    ypred[t] = normal_rng(X[t,]*beta[t],sigma);
  }
  
  // Sample R2
  R2_samp = variance(s)/(variance(s)+sigma^2);
  
  // Oos prediction
  for (i in 1:K){
  bf[i] = normal_rng(beta_T[i],sigma_beta[i]);
  }
  muf = intercept + Xf'*bf;
  yf_pred = normal_rng(muf,sigma);
  yf_lpdf = normal_lpdf(yf|muf,sigma);  
  
}


