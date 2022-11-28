# GRB: compactness problem

Notes for a Whiteboard Session on 12th August 2020.

These notes are organised as follows. First I will discuss the origin and generalisation of the compactness problem. I will walk through the maths of the compactness problem and its solution when introducing relativistic motion. Second, I will walk through a couple of the more famous applications of the general compactness problem, in particular for GRB090510 (Ackermann et al. 2010) and GRB170817A (Matsumoto et al. 2018, lots of other paper). A great general review of this and other gamma-ray burst stuff is the book by Bing Zhang, Physics of Gamma-ray bursts. There are also nice review articles led by Pawan Kumar, Tsvi Piran, Ehud Nakar, Peter Meszaros etc.

# General Description

The general compactness problem was first discussed in 1975 by Malvin Ruderman. The problem is basically that we detect photons in gamma-ray bursts that have energy higher than the rest mass energy of electrons, and the spectrum of GRBs is non-thermal. 

The non-thermal spectrum of GRBs implies the source must be optically thin to Thompson scattering of electron positron pairs.

To be able to escape from the source' emitting region the optical depth for two photon pair production  must be less than unity. I.e.,

$$ \text{pair production optical depth:}~\gamma\gamma \rightarrow e^+e^- < 1 \\ \tau_{\gamma\gamma} < 1. $$

For a back-of-the-envelope estimate, the pair production cross section is close to Thompson scattering cross section. Therefore, 

$$ \tau_{\gamma\gamma} \sim \sigma_T n_{ph} R $$

where $\sigma_T$ is the Thompson scattering cross section, $n_{ph}$ is the photon number density, and R is the size of the emission region. The size R can be estimated through a variability timescale i.e., $R = c\delta t$.  Given a typical variability timescale of 10 ms. This corresponds to $R \sim 3\times10^8 \rm{cm}$. 

Now what is $n_{ph}$?

Assume a fraction f of the emitted energy is above pair production threshold ($e_{\gamma} \gtrsim m_{e}c^2$) (more on this in a little bit). Then number density of pair producing photons is.

$$
n_{\mathrm{ph}} \sim \frac{N}{V}\sim\frac{3 E_{\gamma, \mathrm{iso}} f}{4 \pi R^{3} \epsilon_{\gamma}} \sim\left(2.7 \times 10^{30} \mathrm{cm}^{-3}\right) f
$$

Plugging this into in the optical depth expression above, For a typical gamma-ray fluence $E_{\gamma, \text { iso }} \sim 10^{50}$ and a threshold $\epsilon_{\gamma} \sim 1~\rm{MeV}$gives

$$
\tau_{\gamma \gamma} \sim \frac{3 E_{\gamma, \text { iso }} \sigma_{\mathrm{T}} f}{4 \pi R^{2} \epsilon_{\gamma}} \sim 5.4 \times 10^{14} f \gg 1
$$

For typical fractions f, this greatly exceeds 1. So according to this nothing higher than ~1 MeV photons should be observable from a gamma-ray burst. This is the compactness problem, and early on, at least in the early 80s it meant people believed gamma-ray bursts needed to be Galactic. Or, spoiler alert: need to involve relativistic motion.

# Detour: Two photon pair production

The electron rest mass energy is $m_e c^2 = 511~\rm{keV}$. A photon with energy greater than this will be converted into electron-positron pairs and then quickly converted back. 

In order to be converted back and the photon to eventually become visible another object has to be involved in order to conserve energy and momentum. This other object can be another photon, an electric or magnetic field. Now consider a relativistic particle, 

$$
E=m c^{2}=\gamma m_{0}^{2} c^{2} \\
\mathrm{p}=m v=\gamma m_{0} \beta c
\\
E^{2}-\mathrm{p}^{2} c^{2}=\gamma^{2} m_{0}^{2} c^{4}-\gamma^{2} m_{0}^{2} \beta^{2} c^{4}=m_{0}^{2} c^{4} \gamma^{2}\left(1-\beta^{2}\right)=m_{0}^{2} c^{4}=\mathrm{const.} 
$$

For photons E = Hv and p = hv/c, so..

$$
E^2 - p^2c^2 = 0
$$

Now consider the two photon pair production process i.e., $\gamma_{1} \gamma_{2} \rightarrow e^{+} e^{-}$, through conservation arguments this gives, 

$$
\left(E_{\gamma, 1}+E_{\gamma, 2}\right)^{2}-\left(\mathrm{p}_{\gamma, 1}+\mathrm{p}_{\gamma, 2}\right)^{2} c^{2}=\left(E_{e^{+}}+E_{e^{-}}\right)^{2}-\left(\mathrm{p}_{e^{+}}+\mathrm{p}_{e^{-}}\right)^{2} c^{2}
$$

For simplicity, and valid for the threshold of pair production we can assume that the two electron-positron pairs share the incoming energy equally, i.e., 

$$
E_{e^{+}}=E_{e^{-}}=E \text { and } \mathrm{p}_{e^{+}}=\mathrm{p}_{e^{-}}=\mathrm{p}
\\

$$

This means we can simply expression above, in particular the right hand side.

$$
\left(E_{\gamma, 1}+E_{\gamma, 2}\right)^{2}-\left(\mathrm{p}_{\gamma, 1}+\mathrm{p}_{\gamma, 2}\right)^{2} c^{2}= (2 E)^{2}-(2 p)^{2} c^{2}=4 m_{e}^{2} c^{4}
$$

Now consider photons with frequency $f_1$ and $f_2$ hitting each other with an incident angle $\theta$. This means we can rewrite the left hand side. 

$$
2 E_{\gamma, 1} E_{\gamma, 2}-2_{\mathrm{p}_{\gamma}, 1} \cdot \mathrm{p}_{\gamma, 2} c^{2}=2 h f_{1} \cdot h f_{2}(1-\cos \theta) = 4m_e^2 c^4
\\
2h f_{1} \cdot h f_{2}(1-\cos \theta) = 2(m_ec^2)^2
$$

For simplicity just assume $cos\theta = -1.$  This gives the threshold condition for two-photon pair production to work. 

$$
h f_{1} \cdot h f_{2} \geq\left(m_{e} c^{2}\right)^{2}
$$

# Requiring relativistic motion.

As I have now derived, the general threshold for pair production is 

$$
h f_{1} \cdot h f_{2} \geq\left(m_{e} c^{2}\right)^{2}
$$

As derived previously, pair production with this sort of threshold leads to 

$$
\tau_{\gamma \gamma} \sim \frac{3 E_{\gamma, \text { iso }} \sigma_{\mathrm{T}} f}{4 \pi R^{2} \epsilon_{\gamma}} \sim 5.4 \times 10^{15} f \gg 1
$$

But now lets introduce relativistic motion, 

Introducing relativistic motion changes the threshold for pair production, the expression derived above is in the co-moving reference frame.  So introducing relativistic motion means, 

$$
h f_{1}^{\prime} \cdot h f_{2}^{\prime} \geq\left(m_{e} c^{2}\right)^{2} 
$$

with $f'_{1,2} \sim f_{1,2}/\Gamma$. Valid as long as you are on axis to the GRB jet. This means the threshold can actually be written as, 

$$
h f_{1} \cdot h f_{2} \geq \Gamma^{2}\left(m_{e} c^{2}\right)^{2}
$$

Introducing this additional factor of $\Gamma^2$ solves the compactness problem considerably, In the co-moving frame all the photons are deboosted by a factor of $\Gamma$. Now gamma-ray photons above the pair production threshold are x-ray photons in the comoving frame, below the pair production threshold. Furthermore, the size of the emitting region is now also larger, so the variability timescale used to infer R is off by a factor $\Gamma^2$. Let's actually go through the math a little. 
As mentioned, 

$$
\tau_{\gamma \gamma} \sim \frac{3 E_{\gamma, \text { iso }} \sigma_{\mathrm{T}} f}{4 \pi R^{2} \epsilon_{\gamma}} \sim 5.4 \times 10^{15} f \gg 1
$$

Introducing relativistic motion effects the optical depth in two ways, the deboosting of photons i.e changing in the factor f and change in R by a factor of $\Gamma^2$. The latter condition implies,  

$$
R \sim c\delta t \Gamma^2
\\
\frac{R_{relativistic}}{R_{non-relativistic}} = \Gamma^2
$$

The former condition is slightly more involved, but lets start with the assumption that the photons follow a power-law spectrum (this is observationally verified to a certain extent - ask me later). 

This means we can write down the photon number spectrum as 

$$
N(\epsilon) = N_0 \epsilon^\beta
$$

where $\epsilon$  is the energy. Now let us consider the number of photons that can be involved in pair production, i.e are above the pair production threshold, which we label as $\epsilon_{th}$. 

According to the conditions, 

$$
\text{relativistic:}~h v_{1} \cdot h v_{2} \geq \Gamma^{2}\left(m_{e} c^{2}\right)^{2}
$$

$$
\text{non-relativistic:}~h v_{1} \cdot h v_{2} \geq\left(m_{e} c^{2}\right)^{2}
$$

This means the threshold $\epsilon_{th,\rm{R}}, \epsilon_{th, \rm{NR}}$  in relativistic and non-relativistic scenarios is different by a factor of $\Gamma^2$ i.e.,

$$
\epsilon_{\mathrm{th}, \mathrm{R}}=\Gamma^{2} \epsilon_{\mathrm{th}, \mathrm{NR}}
$$

The ratio of the total number of photons above the two thresholds, which is also the fraction f is then, 

$$
\frac{N\left(>\epsilon_{\mathrm{th}, \mathrm{R}}\right)}{N\left(>\epsilon_{\mathrm{th}, \mathrm{NR}}\right)}=\frac{f_{\mathrm{R}}}{f_{\mathrm{NR}}}=\frac{N_{0}\left(\Gamma^{2} \epsilon_{\mathrm{th}, \mathrm{NR}}\right)^{\beta+1}}{N_{0} \epsilon_{\mathrm{th}, \mathrm{NR}}^{\beta+1}}=\Gamma^{2 \beta+2}
$$

Here I am getting the fraction by just integrating the number density. So introducing relativistic motion changes the fraction above the pair production threshold by 

$$
f_R = f_{NR} \Gamma^{2\beta + 2}
$$

Incorporating both these effects, i.e the effect of relativistic motion on the fraction of photons above the pair production threshold and on the radius, we can now write the ratio of the pair production optical depth. 

$$
\frac{\tau_{\gamma \gamma, \mathrm{R}}}{\tau_{\gamma \gamma, \mathrm{NR}}}=\frac{f_{\mathrm{R}} R_{\mathrm{R}}^{-2}}{f_{\mathrm{NR}} R_{\mathrm{NR}}^{-2}}=\Gamma^{2 \beta-2} \rightarrow \tau_{\gamma \gamma,R} = \tau_{\gamma \gamma, NR} \Gamma^{2\beta-2}
$$

So now for a typical $\beta = 2.2$, this is a factor of $\Gamma^{-6.4}$. Assuming a typical fraction f = 0.2, now gamma-ray photons get out as long as $\Gamma \gtrsim 100$. Thus resolving the compactness problem. In reality the assumption of a simple power law photon spectra is probably incorrect, real GRB prompt emission spectra follows the so-called band function. This affect as well as other simplifications made along the way will change the result slightly but not by much. 

# Applications

The compactness problem has a few really cool applications. I'll go through 2, relatively more famous examples. First, estimating the Lorentz factor of jets by observing high energy photons. Second, for GRB170817 specifically, identifying that the prompt emission produced in this GRB was likely not produced by the ultra-relativistic jet, but rather the cocoon-shock breakout etc. Note: Sorry I ran out of time, so only the first application today, I'll write up the other one later. 

## Estimating Lorentz factors

Given the solution to the compactness problem requires relativistic motion, one can turn the solution around to estimate the minimum Lorentz factor given one has observed a photon of a given energy. 

To start this derivation lets begin with generalising the pair production threshold to, 

$$
\epsilon_{\gamma, \mathrm{cut}} \epsilon_{\gamma, \mathrm{th}} \sim\left(\frac{\Gamma}{1+z}\right)^{2}\left(m_{e} c^{2}\right)^{2}
$$

Where I have now introduced the redshift correction. Now $\epsilon_{\gamma, \rm{cut}}$ is the cutoff energy that may be observed in the spectrum, or one simply uses the maximum energy of the photons that are detected. Again using the assumption that the photons follow a power-law spectrum, 

$$
N(\epsilon) = N_0 \epsilon^\beta
$$

If one works with the band-function, then, $N_0$  can be related to measured parameters from the band function. The band function is normally the function that is fitted to GRB prompt spectra. 

$$
N(E)=\left\{\begin{array}{ll}
E^{\alpha} \exp \left(-\frac{E}{E_{0}}\right), & \text { if } E \leq(\alpha-\beta) E_{0} \\
{\left[(\alpha-\beta) E_{0}\right]^{(\alpha-\beta)} E^{\beta} \exp (\beta-\alpha),} & \text { if } E>(\alpha-\beta) E_{0}
\end{array}\right.
\\
N_{0}=A \cdot \Delta T\left[\frac{E_{p}(\alpha-\beta)}{(2+\beta)}\right]^{\alpha-\beta} \exp (\beta-\alpha)(100 \mathrm{keV})^{-\beta}
$$

Where all the parameters can be fitted to the observed GRB spectra using the band-function. Now the fraction of photons emitted above the pair production threshold can be determined by integration. Giving, 

$$
\tau_{\gamma \gamma}\left(E_{\gamma}\right)=\frac{C(\beta) \sigma_{\mathrm{T}} d_{L}^{2} N_{0}}{-1-\beta (1+z)^2}\left(\frac{E_{\gamma}}{m_{e}^{2} c^{4}}\right)^{-1-\beta} \frac{1}{R_{\gamma}^{2}}\left(\frac{\Gamma}{1+z}\right)^{2+2 \beta}
$$

Where, $C(\beta)$ is a fudge factor to account for averaging the spectrum over a range. Note that here I have not substituted $R_{\gamma}\sim\Gamma^{2} c \delta t /(1+z)$. This is because the radius is actually model dependent. If one does not know where prompt emission is produced then one cannot constrain the Lorentz factor, as the optical depth is proportional to R. 

This dependence can be removed by assuming a model for where the prompt emission is produced. If Prompt emission is produced through internal dissipation, we can write $R_{\gamma}\sim\Gamma^{2} c \delta t /(1+z)$. Different prompt emission generation models have different estimations for this radius. So without the assumption one can only constrain the Lorentz factor in a two-dimensional plane of Lorentz factor and radius. Now, people seem to be reasonably certain that prompt emission is in fact generated through internal dissipation but this is important to mention. 

Solving for the Lorentz factor by imposing the constraint that $\tau_{\gamma \gamma} \lesssim 1$ and the prompt emission is produced through internal dissipation such that $R_{\gamma}\sim\Gamma^{2} c \delta t /(1+z)$ approximation is valid, and making a few other simplifications gives, Ackermann et al. 2010.

$$
\Gamma_{\min } \cong\left[\frac{\sigma_{T} d_{L}^{2}(1+z)^{2} f(>\epsilon_{th}) \epsilon_{max}}{4 \delta t m_{e} c^{4}}\right]^{1 / 6},  \ \  \epsilon_{th}=\frac{2 \Gamma^{2}}{(1+z)^{2} \epsilon_{max}}
$$

This type of constraint was used for short GRB090510, (Ackermann et al. 2010). The GRB had a 30.5 GeV photon, implying a lower limit, $\Gamma \gtrsim 1370$ for $f(\epsilon_{th}) \sim 0.5$.

## GW170817 emitting region

Next time.