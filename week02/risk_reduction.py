import numpy as np

pop_size = 100

# initialise risk reduction factors using random numbers
p_rred_p_array = np.random.choice([0.3, 0.5, 0.7], size=pop_size)
newp_factor_array = np.random.choice([0.5, 1, 2], size=pop_size)
rred_a_array = np.random.uniform(0.1, 1.5, size=pop_size)
rred_initial = 1  # since this is a constant we don't need this to be an array


# First, we want a function to generate rred_p from p_rred_p
# For each person we need a random number, r
# (We can get the number of people from the length of p_rred_p)
# if p_rred_p < r then rred_p = 1e-5, otherwise rred_p = 1
# return rred_p
def gen_rred_p(p_rred_p):
    ...


# Calculate the risk reduction
# risk reduction is the product of newp_factor, rred_a, rred_initial, and rred_p
# You can call your gen_rred_p function in the body of this function to get rred_p from p_rred_p
def calc_risk_reduction(p_rred_p, newp_factor, rred_a, rred_initial):
    ...


print(calc_risk_reduction(p_rred_p_array, newp_factor_array, rred_a_array, rred_initial))
