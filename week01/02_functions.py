import math


# We can define functionality in line as follows...
death_rate = 0.05
period = 0.25
prob_dying = 1 - math.exp(-death_rate*period)

print("Probability of dying = ", prob_dying)


# Or we can modularise and place this in a function
def probability_death(death_rate, period):
    """Get the probability of dying based on a simple death rate per year and period of time in years"""
    return 1 - math.exp(-death_rate*period)

# can assign output to a variable
prob_dying = probability_death(death_rate, period)

# or use it directly
print("Probability of dying = ", probability_death(death_rate, period))


# How can we write a function to calculate the eprate? [Eq. 2, section 3.2.1 in Model Details]
# (Assuming a sample has already been taken from a Normal distribution N(0,1))
# def calc_eprate(...):

import math

n = 0.4
age_group = 4

def calc_eprate(n, age_group):
    """ the rate of starting to have a long term condomless sex partner (ep=1)"""
    return math.exp(0.25*n) / age_group

eprate = calc_eprate(n, age_group)

print("eprate =", eprate)
