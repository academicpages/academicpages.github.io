In Bayesian machine learning, deep generative models are providing exciting ways to extend our understanding of optimization and flexible parametric forms to more conventional statistical problems while simultaneously lending insight from probabilistic modeling to AI / ML. This is an exciting time to be studying the topic as it is blending results from probability theory, statistical physics, deep learning and information theory in sometimes surprising ways. This post is a short summary of some of the major work on the subject and serves as an annotated bibliography on the most important developments in the subject. It also uses common notation to help smooth over some of the differences in detail between papers.

An initial good resource for a high-level overview of the problem is given in [Variational Inference: A Review for Statisticians](https://arxiv.org/abs/1601.00670) by David Blei et al. (2017). This paper gives a Bayesian statistical perspective on variational methods which are designed around manipulating the *expected lower bound on the evidence* (ELBO). From a statistical physics point of view, this can also be viewed as an upper bound on a system's energy function. 

## The setup:  approximate posterior inference

Blei et al. 2017 starts with a very broad general statement about Bayesian modeling: if we have some known observational data $\boldsymbol{x}=x_1,...,x_N$ and a model with parameters or latent variables $\boldsymbol{z}=z_1,...,z_N$, then our model is specified by a joint probability distribution $p(\boldsymbol{x},\boldsymbol{z})$. The $\boldsymbol{z}$ values could be latent (also described as *local*) parameters such as the factor scores in factor analysis or they could be global parameters like the coefficients in linear regression. After setting up this model, one of the main tasks is usually to conduct inference and obtain a posterior distribution $p(\boldsymbol{z}\vert \boldsymbol{x})=p(\boldsymbol{x},\boldsymbol{z})p(\boldsymbol{z})/p(\boldsymbol{x})$ where the intractable integral $p(\boldsymbol{x})=\int_z p(\boldsymbol{x}\vert \boldsymbol{z})p(\boldsymbol{z})dz$ prevents straightforward computation of $p(\boldsymbol{z}\vert \boldsymbol{x})$. The application of Markov chain Monte Carlo is intended to compute approximate estimates of exactly $p(\boldsymbol{z}\vert \boldsymbol{x})$ while the variational Bayes strategy is to get exact solutions to an approximate distribution $q(\boldsymbol{z}\vert \boldsymbol{x})$ where $q$ is chosen from some class of distributions that have nice properties for optimization. We typically choose $q$ from a family of parametric densities indexed by parameters $\boldsymbol{\phi}$. Then, the variational objective is to solve the following problem in terms of a loss function $f$, true posterior $p$ and approximate posterior $q$.


$$
q_\phi^*(\boldsymbol{z})=\underset{q_{\phi}}{\mathrm{argmin}} \ f
(q_\boldsymbol{\phi}(\boldsymbol{z}),p(\boldsymbol{z}\vert \boldsymbol{x}))
$$



We are free to choose any $f$ that we want, keeping in mind that our choice of $f$ should intuitively encapsulate notions of closeness or fidelity between two distributions $p,q$. Many different methods can be categorized by their choice of $f$ within this framework. For example, using the asymmetric Kullback-Leibler divergence defined as $KL(p\vert \vert q)=E_p [\log p(z)/q(z)]$ yields either variational Bayes or [expectation propagation](https://arxiv.org/abs/1412.4869) depending upon whether $KL(p\vert\vert q)$ or $KL(q\vert\vert p)$ is used

We can also frame variational inference in the context of the evidence $p(\boldsymbol{x})$ also referred to as the *marginal likelihood*. Without loss of generality, we can also assume that the true generative model $p_{\theta}$ of the data has some parameters $\theta$. In this post, I'll be extremely detailed with the derivations so that they are easy to follow.


$$
\begin{align}
\underbrace{\log p_{\boldsymbol{\theta}}(\boldsymbol{x})}_{\text{Log evidence}}&= \log \int_z p_{\boldsymbol{\theta}}(\boldsymbol{z,x}) dz\\
&= \log \int_z q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})\frac{p_{\boldsymbol{\theta}}(\boldsymbol{z,x})}{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})} dz\\
&= \log \int_z q_{\boldsymbol{\phi}}(\boldsymbol{z}\vert \boldsymbol{x})\frac{p_{\boldsymbol{\theta}}(\boldsymbol{z\vert x})p_{\boldsymbol{\theta}}(\boldsymbol{x})}{q(\boldsymbol{z}\vert \boldsymbol{x})} dz\\
&= \log \int_z q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})\frac{p_{\boldsymbol{\theta}}(\boldsymbol{z\vert x})p_{\boldsymbol{\theta}}(\boldsymbol{x})}{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})} dz\\
&\ge  \int_z q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})\log \left[\frac{p_{\boldsymbol{\theta}}(\boldsymbol{z\vert x})p_{\boldsymbol{\theta}}(\boldsymbol{x})}{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})}\right] dz  = ELBO(q_{\boldsymbol{\phi}})\\
\end{align}
$$



We used Bayes' Rule in (3) and Jensen's inequality after (5), leading us to the form of the expected lower bound of the model evidence shown in equation 6. With a few more manipulations we get:

$$
\begin{align}
ELBO(q_\boldsymbol{\phi}) &=  \int_z q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})\log \left[\frac{p_{\boldsymbol{\theta}}(\boldsymbol{z,x})}{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})}\right] dz\\
&=  E_{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})}\left[\log {p_{\boldsymbol{\theta}}(\boldsymbol{z,x})}-\log q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})\right] \\
&=  E_{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})}\left[\log {p_{\boldsymbol{\theta}}(\boldsymbol{z\vert x})}-\log q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})-\log p_{\boldsymbol{\theta}}(\boldsymbol{x})\right] \\
&= -KL(q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})\vert \vert p_{\boldsymbol{\theta}}(\boldsymbol{z}\vert \boldsymbol{x}))+  E_{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})}\left[\log p_{\boldsymbol{\theta}}(\boldsymbol{x})\right] \\
&= -KL(q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})\vert \vert p_{\boldsymbol{\theta}}(\boldsymbol{z}\vert \boldsymbol{x}))+  \log p_{\boldsymbol{\theta}}(\boldsymbol{x})
\end{align}
$$



The form shown in (11) is informative - remember that the marginal likelihood $p(\boldsymbol{x})$ is not a function of $\boldsymbol{z}$. If we think of the log marginal likelihood as fixed, then $$\log p(\boldsymbol{x})= KL(q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})\vert \vert p_{\boldsymbol{\theta}}(\boldsymbol{z}\vert \boldsymbol{x})) +  ELBO(q_\boldsymbol{\phi})$$ so that increasing the KL-divergence must decrease the ELBO and vice versa. 

## Auto-Encoding Variational Bayes: [Kingma and Welling (2013)](https://arxiv.org/abs/1312.6114) 

This paper ignited an enormous amount of interest from the machine learning community in variational methods because it recast approximate inference in a form that has a straightforward interpretation in the context of auto-encoder models. I won't go into depth about how those work and will instead focus on the main contribution. We do need to know that within the conceptual framework of Kingma & Welling, we have a latent variable model that maps hidden or latent codes $z$ to observed data points $\boldsymbol{x}$ via a generator model $$p_{\boldsymbol{\theta}}(\boldsymbol{x}\vert \boldsymbol{z})$$. They make the assumption that this generator is a neural network parameterized by weights contained within $\boldsymbol{\theta}$.

Starting with equation (8) from the previous section, the authors made the following observation:


$$
\begin{align}ELBO(q_\boldsymbol{\phi}) 
&=  E_{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})}[\log p_{\boldsymbol{\theta}}(\boldsymbol{x,z})-\log q_\boldsymbol{\phi}(\boldsymbol{z\vert x})]\\
&=  E_{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})}[\log p_{\boldsymbol{\theta}}(\boldsymbol{x\vert z}) + \log p_{\boldsymbol{\theta}}(\boldsymbol{z})-\log q_\boldsymbol{\phi}(\boldsymbol{z\vert x})]\\
&=  E_{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})}[\log p_{\boldsymbol{\theta}}(\boldsymbol{x\vert z})] + E_{q(\boldsymbol{z}\vert \boldsymbol{x})}\left[ \log p_{\boldsymbol{\theta}}(\boldsymbol{{z}})-\log q_\boldsymbol{\phi}(\boldsymbol{z\vert x})\right]\\
&=  \underbrace{E_{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})}[\log p_{\boldsymbol{\theta}}(\boldsymbol{x\vert z})]}_{\text{Reconstruction}} -\underbrace{KL(q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x}),p_{\boldsymbol{\theta}}(\boldsymbol{z}))}_{\text{Shrinkage}}\\
\end{align}
$$



(16) presents a common interpretation of the ELBO in terms of the variational parameters $\boldsymbol{\phi}$ as a tradeoff between maximizing the model likelihood $E_{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})}\left[\log p_{\boldsymbol{\theta}}(\boldsymbol{x\vert z})\right]$ and keeping the learned posterior over $\boldsymbol{z}$ close to a prior distribution $p_{\boldsymbol{\theta}}$. An arbitrary choice of prior which seems to have caught on is to assume that $\boldsymbol{z} \sim N(\boldsymbol{0},\sigma^2 I)$ where $I$ denotes the identity matrix. From a non-Bayesian machine learning perspective, the first term is analogous to reconstruction or denoising error from a normal auto-encoder while the second term is a Bayesian innovation intended to help keep the learned latent space (governed by $\boldsymbol{\phi}$) relatively close to a spherical Gaussian.

## ELBO surgery: [Hoffman and Johnson (2016)](http://approximateinference.org/accepted/HoffmanJohnson2016.pdf)

This is one of my favorite papers because it's a lucid and compact explanation of an interesting phenomenon in deep generative models. It also has two more rearrangements of the ELBO. The first one is nearly the same expression as (12):


$$
\begin{align}
ELBO(q_\boldsymbol{\phi}) 
&=  E_{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})}\left[\log p_{\boldsymbol{\theta}}(\boldsymbol{x,z})-\log q_\boldsymbol{\phi}(\boldsymbol{z\vert x})\right]\\
&=  \underbrace{E_{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})}\left[\log p_{\boldsymbol{\theta}}(\boldsymbol{x,z})\right]}_{\text{Negative expected energy}} -\underbrace{E_{q_\boldsymbol{\phi}}\left[\log q_\boldsymbol{\phi}(\boldsymbol{z\vert x})\right]}_{\text{Entropy}}\\
\end{align}
$$



The term *energy* here refers to the convention that in statistical mechanics, the Boltzmann distribution is defined by an exponential dependence between energy and probability, i.e. $p(x)\propto e^{-U/kT}$ where $U$ is an energy function and $kT$ is a normalized temperature. This  rewriting of the ELBO highlights how it balances likelihood maximization (equivalent to energy minimization) with keeping most of its probability mass from spreading out and thereby boosting the entropy term.

The second form of the ELBO is the key result of this paper and provides a more detailed breakdown than the previous forms. The setup is a little more involved and requires recasting the ELBO as a function dependent upon not just the variational parameters $\phi$ or the generative model parameters $\theta$ but also the identity of the $n$-th data point being analyzed. The main point of this section is that we should think about information being shared between the identity of the data point (as captured by its index $n$) and the latent code $z_n$. 

$$
\begin{align}
ELBO(q_\boldsymbol{\phi}) &=  \underbrace{E_{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})}[\log p_{\boldsymbol{\theta}}(\boldsymbol{x\vert z})]}_{\text{Reconstruction}} -\underbrace{KL(q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x}),p_{\boldsymbol{\theta}}(\boldsymbol{z}))}_{\text{Shrinkage}}\\

&=E_{q_\phi(z\vert x)}\left[\log p_\theta(\boldsymbol{x}\vert\boldsymbol{z})-\log \frac{q_\phi({\boldsymbol{z} \vert\boldsymbol{x})}}{p_\theta(\boldsymbol{z})}\right]\\

&=E_{q_\phi(z\vert x)}\left[ \log \left( \prod_n p_\theta(x_n\vert z_n)\right)-\log \left(\prod_n \frac{q_\phi({z_n \vert x_n)}}{p_\theta(z_n)}\right)\right]\\

&=E_{q_\phi(z\vert x)}\left[\sum_n \log   p_\theta(x_n\vert z_n)-\sum_n \log \frac{q_\phi({z_n \vert x_n)}}{p_\theta(z_n)}\right]\\
&=E_{q_\phi(z\vert x)}\left[\sum_n \left(\log   p_\theta(x_n\vert z_n)- \log \frac{q_\phi({z_n \vert x_n)}}{p_\theta(z_n)}\right)\right]\\

&=\int_{z_1}\ldots \int_{z_N}\prod_n q_\phi(z_n\vert x_n) \left[\sum_n \left(\log p_\theta(x_n\vert z_n)- \log \frac{q_\phi({z_n \vert x_n)}}{p_\theta(z_n)}\right)\right]dz_1 \ldots dz_n
\end{align}
$$



The latent variables $z_n$ are specific to each data point so $z_i$ is independent of $z_j$ given $x_i$. This allows us to rewrite the above integral as a sum.
$$
\begin{align}
ELBO(q_\phi)&=\sum_n \int_{z_n} q_\phi(z_n\vert  x_n)\left(\log p_\theta( x_n\vert z_n)- \log \frac{q_\phi({ z_n \vert x_n)}}{p_\theta( z_n)}d z_n\right)\\

&=\sum_n E_{q_\phi(z_n\vert  x_n)}\left[\log   p_\theta( x_n\vert z_n)\right]- KL(q_\phi(z_n\vert x_n)\vert\vert p_\theta(z_n))\\
\end{align}
$$



This expression can be seen in several other works as well and usually includes a prefactor of $1/N$, implying that the above equation is the term-by-term average reconstruction error minus a per-data point KL divergence. I am not sure why this is done and it doesn't appear to be consistent with a physical point of view - the ELBO can be viewed as an upper bound on a total system-wide energy and a system's total energy is a sum of energy functions across particles rather than an across-particle average. In practice, this factor of $1/N$ is unimportant because $N$ is known ahead of time and the optimization strategies resulting from the ELBO reparameterization are unaffected by it. However, to make these derivations consistent with the literature, I will include it here too. 

Integrating results across different work in a common notation can be challenging and here we must be very specific in noting that $z_n$ refers to the latent code for a single data point, $\boldsymbol{z}$ refers to the latent codes for all data points and $z$ refers to a latent code which is not indexed by $n$ but which is conceptually linked to a single data point.  This is an important distinction moving forward. We continue by defining priors over $n$ which are the probabilities that a given data point is sampled and fed into the ELBO expression. A natural choice is to simply choose them at random so that $p_{sample} = 1/N$ where $N$ is the number of observations in our dataset. We'll make the same assumption for the accompanying prior under $q$ so that $p(n)=q(n)=1/N$. We also want to express $q_\phi (z_n|x_n)$ in terms of the random variable $n$ and not $x_n$ so we have $q_\phi (z\vert n)\triangleq q_\phi(z\vert x_n)$. This is purely notational - the random variable $n$ should be thought of as synonymous with $x_n$.
$$
ELBO(q_\phi)=\frac{1}{N}\left(\sum_n E_{q_\phi(z_n\vert  x_n)}\left[\log   p_\theta( x_n\vert z_n)\right]- KL(q_\phi(z_n\vert x_n)\vert\vert p_\theta(z_n))\right)\\
\begin{align}
\frac{1}{N}\sum_n KL(q_\phi(z_n\vert x_n)\vert\vert p_\theta(z_n))&=\frac{1}{N}\sum_n KL(q_\phi(z\vert n)\vert\vert p_\theta(z))\\
&=\frac{1}{N}\sum_n E_{q_\phi(z\vert n)} \log \frac{q_\phi(z\vert n)}{p_\theta(z)}\\
&=\frac{1}{N}\sum_n E_{q_\phi(z\vert n)} \log \frac{q_\phi(n\vert z)q_\phi(z)}{p_\theta(z)q_\phi(n)}\\
&=\frac{1}{N}\sum_n E_{q_\phi(z\vert n)} \log \frac{q_\phi(n\vert z)q_\phi(z)}{p_\theta(z)q_\phi(n)}\\
&=\frac{1}{N}\sum_n E_{q_\phi(z\vert n)}\left[ \log \frac{q_\phi(z)}{p_\theta(z)} + \log \frac{q_\phi(n\vert z)}{q_\phi(n)}\right]\\
&=\frac{1}{N}\sum_n E_{q_\phi(z\vert n)}\left[ \log \frac{q_\phi(z)}{p_\theta(z)} + \log \frac{q_\phi(n\vert z)q_\phi(z)}{q_\phi(n)q_\phi(z)}\right]\\
&=\frac{1}{N}\sum_n E_{q_\phi(z\vert n)}\left[ \log \frac{q_\phi(z)}{p_\theta(z)} + \log \frac{q_\phi(n, z)}{q_\phi(n)q_\phi(z)}\right]\\
&=KL(q_\phi(z)\vert\vert p_\theta(z)) + \frac{1}{N}\sum_n E_{q_\phi(z\vert n)}\left[ \log \frac{q_\phi(n, z)}{q_\phi(n)q_\phi(z)}\right]\\
&=KL(q_\phi(z)\vert\vert p_\theta(z)) +\sum_n E_{q_\phi(n,z)}\left[ \log \frac{q_\phi(n, z)}{q_\phi(n)q_\phi(z)}\right]\\
&=KL(q_\phi(z)\vert\vert p_\theta(z)) + \mathbb{I}_{q_\phi}(n,z)\\
\end{align}
$$



This result rearranges the sum of per-data point KL divergences into an averaged KL divergence and the mutual information $\mathbb{I}$ between the random variables $n$ and $z$. Conceptually, this is a very nice result - it represents the original regularizing term as a divergence between averaged (i.e. non data point specific) prior distributions and information shared acros $q_\phi$ between $n$ and $z$. We can start to think about $q_\phi$ as a communication channel which may perfectly communicate the information in the index $n$ to the latent code $z$, i.e. perfect reconstruction, or it may fail to communicate substantial information and thereby the generative model learns to ignore the latent code $z$! We can use these expressions to rewrite the ELBO in a form identical to an equation from the Hoffman and Johnson paper:


$$
ELBO(q) =\underbrace{\left[\frac{1}{N}\sum_n E_{q_\phi(z_n\vert x_n})\left[\log p_\theta(x_n\vert z_n)\right] \right]}_{\text{Expected reconstruction error}} - \underbrace{\mathbb{I}_{q_\phi(n,z)}(n,z)}_\text{Decoded information} - \underbrace{KL(q_\phi(z)\vert\vert p_\theta(z))}_{\text{Marginal regularizer}}
$$


In the above expression, the first term on the right hand side represents how well the generative model can reconstruct the data points $x_n$ using the latent codes. If the values of $\theta$ are chosen poorly and the generative model is insufficient, this term will be relatively low. The next term is the mutual information from before and tells us how well the encoder network $q_\phi$ is transmitting information from the identity of the data point $x_n$ into the latent variable $z_n$. Finally, the last term pushes the *average* distribution of latent codes $z_n$ to be close to the prior $p_\theta(z)$. For many applications, $p_\theta$ is chosen somewhat arbitrarily to be a diagonal or isotropic Gaussian and this form suggests that we may want to choose more carefully in order to obtain more desired behavior from variational methods.

## $\beta$-VAE: [Higgins et al. (2017)](https://openreview.net/pdf?id=Sy2fzU9gl)

As researchers began to catch on that the shrinkage term $KL(q_\phi(z\vert x)\vert\vert p_\theta(z))$ may play an important role in favoring certain classes of representations, they developed new modifications to the ELBO to help push the variational objective in different directions. 

A conceptually straightforward way to do this is to simply up- or down-weight the shrinkage term in conjunction with the right prior. The intuition behind $\beta$-VAE appears to be that in the $\beta$-modified expression for the ELBO:$ELBO(q_\boldsymbol{\phi}) =  E_{q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x})}[\log p_{\boldsymbol{\theta}}(\boldsymbol{x\vert z})] -\ \beta \cdot KL(q_\boldsymbol{\phi}(\boldsymbol{z}\vert \boldsymbol{x}),p_{\boldsymbol{\theta}}(\boldsymbol{z}))$, the second term can be tuned to push $q_\phi(z\vert x)$ closer to a desired prior structure. The default prior that had been chosen in many studies up to this point is a simple isotropic Gaussian which *promotes cross-factor independence* and will naturally push towards a *disentangled* representation in which the different dimensions of $z$ are uncorrelated in the approximate posterior $q_\phi(z\vert x)$. It's straightforward to show that for two approximately isotropic Gaussian distributions $q_\phi, p_\theta$, their KL divergence is proportional to 

$$
\log\frac {\vert\Sigma_{q_\phi}\vert}{\vert\Sigma_{p_\theta}\vert}\propto \log \sigma^2_{q_\phi}-\log \sigma^2_{p_\theta}
$$



where $\Sigma_{q_{\phi}}$ and $\Sigma_{p_\theta}$ are the diagonal covariance matrices of $q_\phi$ and $p_\theta$ respectively. As a consequence, we can also view an adjustment to $\beta$ as equivalent to tweaking our latent space prior variance. In statistical physics, $\beta$ is a function of the system temperature so it is unclear to me why the notion of $\beta$ was introduced despite several other identical conceptual frameworks existing which were appropriate for describing this improvement. Perhaps this was indeed the motivation but this fact was omitted from the text.

Regardless, this led to marked improvements on learning disentangled representations and is such an easy computational tweak that it can be implemented into the vast majority of VI workflows.



