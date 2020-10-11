---
title: Mixed models for COVID antibody data
date: 2020-10-10
permalink: /posts/2020/10/mixed-models-for-covid/
tags:
---

This summer, as the COVID-19 pandemic hit the 6-month mark, there was concern
that immunity to SARS-CoV-2 would begin to wane, since immunity to other
coronaviruses appears to wane at around 6 months after infection.

An [article](https://www.nejm.org/doi/full/10.1056/NEJMc2025179) in *NEJM*
tried to address the question of how antibody titers decline using data from 34
patients. Patients had their antibody titers measured at 2 or 3 timepoints. The
authors analyzed this data to determine how quickly antibody titers decline
with time. In other words, they want to know the slope of titers versus time
since infection.

The authors' approach was to compute the slope for each patient, using each patient's 2 or 3 timepoints, and then feed those slopes into a linear model that corrects for:

- The patients' age and sex, because maybe the antibody-versus-time slope is
  different for different ages or sexes
- The time between the onset of symptoms and the first antibody measurement.
  The decline in antibody titer with time can't actually be linear, since then
  it would eventually hit zero and then negative numbers. Instead, it probably
  declines, concave up, so that the instantaneous slope is more negative closer
  to the onset of symptoms.
- The first measured antibody titer, because it could be that a higher initial
  titer declines faster.

This linear model then has an intercept, which is the mean antibody-versus-time
slope across participants, accounting for the above factors. To make this
intercept more interpretable, the authors mean-centered the patients' ages and
antibody titers (so that the linear model's intercept is for a mean age and
titer) and centered the time since symptom onset at 18 days.

Using the raw data published with the paper, I was able to reproduce the model
coefficients (which we would normally call the "slope", or slopes, which is
confusing in this case because the input values themselves are slopes) but not
the intercept.

```r
library(tidyverse)
library(readxl)
library(lme4)

# Download data
url <- "https://www.nejm.org/doi/suppl/10.1056/NEJMc2025179/suppl_file/nejmc2025179_appendix.xlsx"
fn <- tempfile(fileext = "xlsx")
download.file(url, fn)

# Read in data
raw_data <- read_excel(fn, range = "A2:N73")
unlink(fn)

# Clean data
data <- raw_data %>%
  select(
    patient = `...1`, visit = Visit, day = `Sample\r\nDays`,
    age = Age, sex = Gender,
    titer = `ng/ml`
  ) %>%
  # get log10 of antibody titers
  mutate(log_titer = log10(titer)) %>%
  # replace 1, NA, 2, NA, etc. as 1, 1, 2, 2, etc.
  fill(patient)

# Get patients' age, sex, day of first sample, and first antibody titer
patient_chars <- data %>%
  filter(visit == 1) %>%
  select(patient, age, sex, day, log_titer)

# Get patient-specific slopes
patient_slopes <- data %>%
  select(patient, day, log_titer) %>%
  nest(patient_data = c(day, log_titer)) %>%
  mutate(
    model = map(patient_data, ~ lm(log_titer ~ day, data = .)),
    patient_slope = map_dbl(model, ~ coef(.)["day"])
  ) %>%
  select(patient, patient_slope)

# Create the data set that goes into their model
model_data <- patient_chars %>%
  left_join(patient_slopes, by = "patient") %>%
  mutate(
    # Mean-center age and antibody titer
    age = age - mean(age),
    log_titer = log_titer - mean(log_titer),
    # Center time since onset at 18 days
    day = day - 18,
    # Use female as reference (FALSE is base case)
    sex = sex == "M"
  )

lm(patient_slope ~ age + sex + log_titer + day, data = model_data)
```

A colleague of mine asked if you could do something simpler: just look at the
patient slopes and use a *t*-test to ask if they are mostly above zero? This
approach leaves off all the covariates, which mostly doesn't matter, because
they had very small coefficients anyway. In fact, you get almost exactly the
same estimate of the slope as the authors did with the linear model.

```r
t.test(patient_slopes$patient_slope)
```

My approach would have been to use a mixed model. This approach accounts for
the uncertainty in the patient-by-patient slopes. In the authors' approach, the
patients' titer-versus-time slopes are treated as if they were known exactly;
all the uncertainty that comes from estimating a slope from just 2 or 3 data
points is ignored.

```r
lmer(log_titer ~ day + (day || patient), data = data)
```

However, to my surprise, you get almost the same results as reported in the original paper! My guess is that, because most of the patients have approximately the same number of samples (either 2 or 3) and the coefficients are small (i.e., they don't explain very much of the variation in the observed values), it doesn't matter that much which statistical approach you use.

