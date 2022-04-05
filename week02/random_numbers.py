import math

# Numpy also includes methods for sampling random numbers
import numpy as np

rng = np.random.default_rng()

# Draw a single random number from the uniform distribution on [0,1]:
u1 = rng.uniform()
print("A random number:", u1)

# If we call the same code again, we will get a different value:
u2 = rng.uniform()
print("Another random number:", u2)

# This can be used to make decisions with some probability:
if u1 < 0.4:  # option 1 will be chosen 40% of the time
    print("Option 1 taken")
else:
    print("Option 2 taken")


# We can customize the interval over which we sample:
u3 = rng.uniform(5, 7)
print("Random number between 5 and 7:", u3)

# We can also get multiple samples at once. These will be returned in an array:
samples = rng.uniform(size=5)
print("Multiple samples:", samples)


# Other distributions are also available, such as the normal (Gaussian):
normal_samples = rng.normal(size=5)
print("Normal samples:", normal_samples)


# Instead of a continuous distribution, we can sample from a given list of numbers:
# By default, the numbers are chosen uniformly...
options = [0.1, 0.2, 0.3, 0.4, 0.5]
c = rng.choice(options)
print("Choice from a list:", c)
# ...but we can also specify different probabilities/weights:
weights = [0.8, 0.05, 0.05, 0.05, 0.05]
d = rng.choice(options, p=weights)
# This can be combined with the size argument to draw multiple samples:
weighted_samples = rng.choice(options, p=weights, size=10)
print("Weighted samples:", weighted_samples)


# In a previous session, we saw how to compute eprate (Eq. 2, section 3.2.1 in Model Details)
# assuming that we already have a sample from a normal distribution.
# Now we can update that function to also draw the sample, instead of taking it as a parameter:
def calc_eprate(a):
    r = rng.normal()
    eprate = (0.1 * math.exp(r/4)) / a
    return eprate
