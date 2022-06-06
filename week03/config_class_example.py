# Python classes can be used to organise and encapsulate data which is relevant to a particular part of the code
# For example configurations

import numpy as np


# Running multiple simulations with different configurations can easily get messy
# Let's take as an example the parameters from our epidemiology toy model
class Config:
    population_size: int
    rate_per_infected_contact: float
    infectious_period: int
    contact_number_parameter: int
    initial_prevalence_in_contacts: float
    simulation_time: int

    # We can use the __init__ function to set the configuration parameters
    # We can set some directly by passing them to the function, and others we can sample inside the function itself.
    # This means we can create an ensemble of simulations sampling our randomised parameters simply by creating a
    # number of these config objects.
    def __init__(self, num_people, infectious_period, sim_time):
        self.population_size = num_people
        self.rate_per_infected_contact = np.random.choice([0.1, 0.2, 0.3])
        self.infectious_period = infectious_period
        self.contact_number_parameter = np.random.choice(range(5, 10))
        self.initial_prevalence_in_contacts = np.random.choice([0.001, 0.01, 0.1])
        self.simulation_time = sim_time
        assert self.validate_config()

    # Object creation is a good opportunity to check the validity of parameters; if this happens whenever an object is
    # created then we don't have to keep track of all the points in our code where this might need to happen, it will
    # happen automatically. Here we check that probabilities are between 0 and 1, and other parameters are greater than
    # 0 in order for the configuration parameters to be acceptable.
    def validate_config(self):
        print("Validating configuration")
        config_valid = True
        config_valid &= (0 <= self.initial_prevalence_in_contacts <= 1)
        config_valid &= self.simulation_time > 0
        config_valid &= self.population_size > 0
        config_valid &= self.infectious_period > 0
        config_valid &= (0 <= self.rate_per_infected_contact <= 1)
        config_valid &= self.contact_number_parameter > 0
        print("Config okay?", config_valid)
        return config_valid

    # Other methods could be useful, for example saving the config to a file so
    # that randomly generated configs can be retained for future reference.


# Let's create an ensemble of configurations, and the population size and the initial prevalence
cfg_list = [Config(num_people=1000, infectious_period=3, sim_time=100) for i in range(5)]
for cfg in cfg_list:
    print(f"Population = {cfg.population_size}, Initial Prevalence = {cfg.initial_prevalence_in_contacts}")

# We can see from the print-out that:
# 1. Validation is run on all the configurations automatically as part of the init
# 2. Each config has the same population size (because we passed it as input)
# 3. The configs vary in initial prevalence because it is independently sampled as part of the init of each config

# Configurations can be created very concisely, and  configurations can now easily be run in separate simulations,
# either sequentially by iterating over the list or in parallel!
# (This is particularly useful for parallel code because all of the config parameters are generated
# early on and kept separate and can be passed around as a complete unit.)
# e.g.
# for cfg in cfg_list:
#    run_simulation(cfg)
