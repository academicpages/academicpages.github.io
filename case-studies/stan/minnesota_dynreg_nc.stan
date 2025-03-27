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
  array[T-1] vector[K] z_beta;
  vector[K] z_beta_level;
  
  // Variance Parameters
  real<lower=0> sigma;
  // State AR Weights
  vector<lower=0,upper=1>[K] phi;
  // Minnesota scale parameter
  real<lower=0> kappa2_k;
  // Intercept parameters
  real alpha;
  vector[K] sigma_diff;
  //vector<lower = 0>[K] sig_diff;
  vector<lower = 0>[K] lam_diff;
  real<lower = 0> nu_diff;
}


transformed parameters{
  vector<lower=0>[K] sigma_beta = sqrt(var_y_minn)* sqrt(1./var_x_minn) * sqrt(kappa2_k);
  vector[K] beta;
  array[T] vector[K] beta_tilde;

  // Initial Conditions
  beta = z_beta_level .* sigma_beta;
  
  beta_tilde[1] = rep_vector(0,K);

  // Loop here for TVP coefficients
  for (t in 2:T){
  //beta[t]  =  phi.*beta[t-1] + z_beta[t] .* sigma_beta;
  beta_tilde[t]  =  phi.*beta_tilde[t-1] + z_beta[t-1];
  }
  
}

model {
  // Priors
  sigma ~ student_t(3,0, sd_Yc);
  
    for (t in 1:(T-1)) {
  z_beta[t] ~ std_normal();
  }
  
  z_beta_level ~ std_normal();

  (phi +1)./2 ~ beta(10,2); // prior ensures stationarity of the AR coefficients


  kappa2_k ~ gamma(1,1/(0.04^2));
  sigma_diff ~ normal(0,lam_diff*nu_diff);
  lam_diff ~ student_t(1,0,1);
  nu_diff ~ student_t(1,0,1);

  // Observation Likelihood
  target += normal_lpdf(alpha | 0, alpha_sd); // Intercept
for (t in 1:T){
  Yc[t] ~ normal(X[t,]*beta + X[t,] * (beta_tilde[t].*sigma_diff) + alpha, sigma);
}

}

generated quantities {
  real intercept = alpha + Ymean;
  real marg_r2 = sum(sigma_beta + ((sigma_diff^2)./(1-phi)^2))/(sum(((sigma_diff^2)./(1-phi)^2) + sigma_beta + sigma^2));
  vector[T] R2_t; // R2 over time
  vector[T] log_lik;
  vector[K] beta_T = phi.*beta_tilde[T];
  vector[K] bf;
  real muf;
  real yf_pred;
  real yf_lpdf;
  vector[T] ypred;
  
  // R2 over time + logscores
  for (t in 1:T){
    R2_t[t] =  ((X[t,]*beta + X[t,] * (beta_tilde[t].*sigma_diff))^2)/((X[t,]*beta + X[t,] * (beta_tilde[t].*sigma_diff))^2 + sigma^2);
    log_lik[t] = normal_lpdf(Yc[t] | X[t,]*beta + X[t,] * (beta_tilde[t].*sigma_diff) + intercept,sigma);
  }
  
    // Oos prediction
  for (i in 1:K){
  bf[i] = normal_rng(beta_T[i],1);
  }
  muf = intercept + Xf'*beta + (Xf.*sigma_diff)'*bf;
  yf_pred = normal_rng(muf,sigma);
  yf_lpdf = normal_lpdf(yf|muf,sigma);    

  
}

