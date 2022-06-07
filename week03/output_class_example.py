# In this file we'll use a class to achieve a degree of encapsulation. Instead of
# being a recognisable object in the real world (like Person), this class describes a
# unit in our code which achieves a particular purpose. This is a use of classes for
# organisational clarity and convenience.
# This class will handle Outputs from a toy simulation.
# It holds the output data, updates the relevant rows in the table as the simulation
# progresses, and handles all the calculations to calculate the summary statistics from
# the population.

import numpy as np
import matplotlib.pyplot as plt

# we'll need to use the Person class from our toy model in order to get a population going
from infection_toy_model import Person


# The Output class will contain all the methods to calculate output statistics, as well as storing that data.
# The output class can be linked to a population so that we don't have to keep passing a population into it
# when we want to calculate summary statistics.
# This reduces the chance of getting muddled if you are evolving more than one population / simulation!
class Output:
    population: [Person]
    population_size: int

    # When the Output is initialised, we assign a population that it is going to track
    # We also pass in the length of the simulation so that it knows how big to make the output table, which
    # it then creates.
    def __init__(self, population, sim_time):
        self.population = population
        self.population_size = len(population)
        self.results = [{}]*sim_time
        self.total_time = sim_time

    # This calculates the summary statistics (not all of them have been included here!)
    # This uses the population which has already been set and takes a time step, which
    # tells it which row of the output table needs to be updated.
    def update_results(self, time_step):
        current_stats = {
            "infected": sum(person.infected for person in self.population),
        }
        current_stats["overall prevalence"] = current_stats["infected"] / self.population_size
        self.results[time_step] = current_stats

    # Creating a plotting method in the output class which takes a key makes it easy to plot
    # whatever different outputs you need, without repeating lots of boiler-plate code
    def plot(self, output_key):
        time_steps = range(self.total_time)
        output_stats = [row[output_key] for row in self.results]
        plt.plot(time_steps, output_stats)
        plt.xlabel("Time step")
        plt.ylabel(output_key)
        plt.show()


# Let's make a population to start and make an output object to track it
sim_time = 10
population = [Person() for _ in range(1000)]
outputs = Output(population, sim_time)  # defines our Output and assigns the population we just created to it
# run a simulation
for t in range(0, sim_time):
    # toy update for illustration; this could be replaced by the actual update steps if you want
    for person in population:
        if np.random.uniform() < 0.2:
            person.infected = True

    # update results at each step
    # Just needs the time; even though the population data has changed, the Output class has a reference to it
    # so when it calculates the stats, its population data will up to date automatically.
    outputs.update_results(t)

# Once the simulation loop is done, we can now trivially print the data or plot graphs.
# If we wanted to do this somewhere else, we can just pass the Output object around, and everything is there!
outputs.plot("overall prevalence")