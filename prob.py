import numpy as np
import pymc3 as pm
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
true_slope = 2
true_intercept = 1
data_x = np.linspace(0, 1, 100)
data_y = true_slope * data_x + true_intercept + np.random.normal(scale=0.2, size=100)

# Define the model
with pm.Model() as linear_model:
    # Priors
    slope = pm.Normal('slope', mu=0, sd=10)
    intercept = pm.Normal('intercept', mu=0, sd=10)
    sigma = pm.HalfNormal('sigma', sd=1)
    
    # Likelihood
    likelihood = pm.Normal('y', mu=slope * data_x + intercept, sd=sigma, observed=data_y)

# Perform MCMC sampling
with linear_model:
    trace = pm.sample(2000, tune=1000)

# Plot the results
pm.traceplot(trace)
plt.show()
