// Minnesota Model

data {
  int<lower=1> T;
  vector[T] Y;
  int<lower=0> K;
  matrix[T,K] X;

  // data for the R2D2 prior
  real<lower=0> mean_R2;  // mean of the R2 prior
  real<lower=0> prec_R2;  // precision of the R2 prior

  // Variance for intercept
  real<lower=0> alpha_sd;


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
 vector<lower=0>[K] sigma_diff;
 vector<lower=0>[K] sigma_beta;
}


transformed parameters{
  array[T] vector[K] beta;

  // Initial Conditions
  beta[1] = z_beta[1] .* sigma_beta;

  // Loop here for TVP coefficients
  for (t in 2:T){
  //beta[t]  =  phi.*beta[t-1] + z_beta[t] .* sigma_beta;
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

  sigma_beta ~ inv_gamma(0.1,0.1);
  sigma_diff ~ inv_gamma(0.1,0.1);


  // Observation Likelihood
  target += normal_lpdf(alpha | 0, alpha_sd); // Intercept
for (t in 1:T){
  Yc[t] ~ normal(X[t,]*beta[t] + alpha, sigma);
}

}

generated quantities {
  real intercept = alpha + Ymean;
  real marg_r2 = sum(sigma_beta)/(sum(sigma_beta + sigma^2));
  vector[T] R2_t; // R2 over time
  vector[T] log_lik;
  
  // R2 over time + logscores
  for (t in 1:T){
    R2_t[t] =  ((X[t,]*beta[t])^2)/((X[t,]*beta[t])^2 + sigma^2);
    log_lik[t] = normal_lpdf(Yc[t] | X[t,]*beta[t] + alpha,sigma);
  }
  
}


