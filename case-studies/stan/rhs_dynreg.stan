// RHS Model

functions {
  /* Efficient computation of the horseshoe prior
   * see Appendix C.1 in https://projecteuclid.org/euclid.ejs/1513306866
   * Args:
   *   z: standardized population-level coefficients
   *   lambda: local shrinkage parameters
   *   tau: global shrinkage parameter
   *   c2: slab regularization parameter
   * Returns:
   *   population-level coefficients following the horseshoe prior
   */
  vector horseshoe(vector z, vector lambda, real tau, real c2) {
    int K = rows(z);
    vector[K] lambda2 = square(lambda);
    vector[K] lambda_tilde = sqrt(c2 * lambda2 ./ (c2 + tau ^ 2 * lambda2));
    return z .* lambda_tilde * tau;
  }
}


data {
  int<lower=1> T;
  vector[T] Y;
  int<lower=0> K;
  matrix[T,K] X;

    // data for the horseshoe prior
  real<lower=0> hs_df; // local degrees of freedom
  real<lower=0> hs_df_global; // global degrees of freedom
  real<lower=0> hs_df_slab; // slab degrees of freedom
  real<lower=0> hs_scale_slab; // slab prior scale
  real<lower=0> p0;

  // Variance for intercept
  real<lower=0> alpha_sd;

  vector<lower=0>[K] var_x;
  
  // concentrations
  vector<lower=0>[K] cons;
  
  // For Predictions
  vector[K] Xf;
  real yf;
  
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
  
  // local parameters for the horseshoe prior
  vector<lower=0>[K] hs_local;
  // horseshoe shrinkage parameters
  real<lower=0> hs_global; // global shrinkage parameter
  real<lower=0> hs_slab; // slab regularization parameter
  
    vector<lower=0>[K] lam_diff;

  
  // Intercept parameters
  real alpha;
}


transformed parameters{
  vector[K] lambda2 = square(hs_local);
  vector[K] lambda_tilde = sqrt(hs_scale_slab ^ 2 * hs_slab * lambda2 ./ (hs_scale_slab ^ 2 * hs_slab + hs_global ^ 2 * lambda2));
  vector<lower=0>[K] sigma_beta = lambda_tilde*hs_global;
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


  hs_global ~ student_t(hs_df_global, 0, p0 / (K - p0) * sigma / sqrt(T));
  hs_slab ~ inv_gamma(0.5 * hs_df_slab, 0.5 * hs_df_slab);
  hs_local ~ student_t(hs_df, 0, 1);
  
  sigma_diff ~ student_t(1,0,1);

  // Observation Likelihood
  target += normal_lpdf(alpha | 0, alpha_sd); // Intercept
  
  if (pp==0){
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


