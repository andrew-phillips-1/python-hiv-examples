import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


# Classes provide an interface for use in other code. You don't need to know exactly how the class works as long as you
# know how to interact with it, i.e. what data and methods are available to you. The implementation of the class can
# then be changed without changing any code that depends on it, as long as the necessary interface is not changed.
# For example, the age distribution class that we use in the hivpy code to generate a population based on a probability
# distribution over ages.


# This example is from the actual hivpy code!
# This class contains all the methods to generate a sample of ages for a population given one of the three age
# distributions, defining the continuous cumulative probability distribution function, normalising, and inverting it
class ContinuousAgeDistribution:
    """
    Class to handle age distributions using a continuous probability density.
    Linear-Exponential function is used for the example distribution.

    P(age) = (m*age + c)*exp(A(age-B))

    This fits all three example cases quite neatly.
    P(age): Probability density at a given age
    m: gradient of linear part, determines decline in population with age
    c: intercept of linear part, determines maximum age
    A: exponent of exponential part, determines the curvature
    B: offset of exponential part, scaling parameter
    """

    def _integrated_linexp(self, x, m, c, A, B):
        """Intregral of linear-exponential function

        Un-normalised cumulative probability distribution for age.
        """
        return np.exp(A*(x-B))*(m*x+c - m/A)/A

    n_inversion_points = 11

    # Example parameters
    modelParams1 = [-7.19e-4, 5.39e-2, -8.10e-3, 2.12e1]
    modelParams2 = [-1.03e-3, 7.45e-2, -1.12e-3, 8.47]
    modelParams3 = [-1.15e-3, 8.47e-2, 2.24e-3, 2.49e1]

    def __init__(self, min_age, max_age, model_params):
        self.min_age = min_age
        model_age_limit = -model_params[1]/model_params[0]
        if(max_age > model_age_limit):
            print(f"Max age exceeds the maximum age limit for "
                  f"this model (negative probability). "
                  f"Adjusting max age to {model_age_limit}")
            self.max_age = model_age_limit
        else:
            self.max_age = max_age
        self.cpd = lambda x: self._integrated_linexp(x, *model_params)

    @classmethod
    def select_model(cls, inc_cat):
        if(inc_cat == 1):
            return cls(-68, 65, cls.modelParams1)
        elif(inc_cat == 2):
            return cls(-68, 65, cls.modelParams2)
        else:
            return cls(-68, 65, cls.modelParams3)

    def gen_ages(self, N):
        """Generate ages using a (non-normalised) continuous cumulative probability distribution

        Given an analytic PD, this should also be analytically defined
        Cumulative probability distribution is defined in _integratedLinexp
        """
        # Normalise distribution over given range
        C = self.cpd(self.min_age)
        M = 1/(self.cpd(self.max_age)-self.cpd(self.min_age))

        def norm_dist(x):
            return M*(self.cpd(x) - C)

        # sample and invert the normalised distribution (in case analytic inverse in impractical)
        NormX = np.linspace(self.min_age, self.max_age, self.n_inversion_points)
        NormY = norm_dist(NormX)

        # fix the start and end values in case of numerical errors
        NormY[0] = 0.0
        NormY[self.n_inversion_points-1] = 1.0
        NormInv = interp1d(NormY, NormX, kind='cubic')

        # generate N random numbers in (0,1) and convert to ages
        R = np.random.uniform(0, 1, N)
        Ages = NormInv(R)
        return Ages


# But all you need to do to generate an age sample is this line!
ages = ContinuousAgeDistribution.select_model(1).gen_ages(10000)

# We can then plot to see if it looks like we expect
plt.hist(ages)
plt.show()

# Or we can create the distribution and generate multiple population ages
age_dist = ContinuousAgeDistribution.select_model(1)
population_ages = [age_dist.gen_ages(1000) for i in range(10)]  # generate 10 random population-wide age samples

# And plot them
for i in range(10):
    ys, bins = np.histogram(population_ages[i])
    xs = (bins[1:] + bins[:-1])/2
    plt.plot(xs, ys, label=f"population {i}")
plt.legend()
plt.show()

