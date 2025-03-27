
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

  vector<lower=0>[K] var_x;
  
  // concentrations
  vector<lower=0>[K] cons;
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
  matrix[(T-1),K] z_beta;
  vector[K] z_beta1;
  
  // Variance Parameters
  real<lower=0> sigma;
  // State AR Weights
  vector<lower=0,upper=1>[K] phi;
  // Regression Weights
  // R2 Parameters
  simplex[(K)] psi;
  real<lower=0, upper=1> R2;
  // Intercept parameters
  real alpha;
}


transformed parameters{
  real<lower=0> tau2 = R2 / (1 - R2);
  vector<lower=0>[K] sigma_beta = sqrt(tau2) * sqrt(rep_vector(1,K)-phi.^2)  .* sqrt(psi);
  matrix[(T),K] beta;
  //vector<lower=0>[K] beta_sd;
  //vector[K] beta0;

  // Loop here for TVP coefficients
  //for (i in 1:K){
  //for (t in 2:T){
  //beta[t,i]  =  phi[i]*beta[(t-1),i] + z_beta[(t-1),i] * sigma_beta[i];
  //}
  //}
  // Initial condition
  //beta[1,] = z_beta1' .* sigma_beta';
}

model {
  // Priors
  sigma ~ student_t(3,0, sd_Yc);
  
  for (i in 1:K){
  for (t in 1:(T-1)) {
  z_beta[t,i] ~ std_normal();
  }
}
  
  z_beta1 ~ std_normal();

  (phi +1)/2 ~ beta(10,2); // prior ensures stationarity of the AR coefficients


  psi ~ dirichlet(cons);
  R2 ~ beta(mean_R2 * prec_R2, (1 - mean_R2) * prec_R2);

  // Observation Likelihood
  target += normal_lpdf(alpha | 0, alpha_sd); // Intercept
  
//  for (t in 1:T){
//  target += normal_lpdf(Yc[t]|(X[t,]*beta[t,]'+alpha,sigma);
//  }

for (t in 1:T){
  Yc[t] ~ normal(X[t,]*beta[t,]' + alpha, sigma);
}

}

