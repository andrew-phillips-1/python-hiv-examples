import numpy as np
import matplotlib.pyplot as plt

# Classes can be used to describe a unit which achieves a particular purpose,
# for example producing output statistics!
# we'll need to use the Person class from our toy model in order to get a population going
from infection_toy_model import Person


# The Output class will contain all the methods to calculate output statistics, as well as storing that data.
# The output class can be linked to a population so that we don't have to keep passing a population into it
# This reduces the chance of getting muddled if you are evolving more than one population / simulation!
class Output:
    population: [Person]
    population_size: int

    def __init__(self, population, sim_time):
        self.population = population
        self.population_size = len(population)
        self.results = [{}]*sim_time
        self.total_time = sim_time

    def update_results(self, time_step):
        current_stats = {
            "infected": sum(person.infected for person in self.population),
        }
        current_stats["overall prevalence"] = current_stats["infected"] / self.population_size
        self.results[time_step] = current_stats

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
outputs = Output(population, sim_time)
# run a simulation
for t in range(0, sim_time):
    # toy update
    for person in population:
        if np.random.uniform() < 0.2:
            person.infected = True

    # update results at each step
    outputs.update_results(t)

outputs.plot("overall prevalence")