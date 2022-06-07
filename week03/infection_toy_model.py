# This file contains the infection toy model developed previously (with a small change to the Person class.)
# This can be run as an independent python script by un-commenting out the last two lines to run the simulation
# and plot the results.

# This file is useful for illustrating the Person class in context, and contains code / methods (such as Update)
# which you may wish to import, re-purpose, or modify for your simulation class (see class_exercise.py)
# to avoid re-doing this logic!

import numpy as np
import matplotlib.pyplot as plt

# Parameters that control the simulation
population_size = 1000
rate_per_infected_contact = 0.2  # 20% chance of becoming infected per infected contact
duration_of_infectivity = 2  #  Assume 2 time periods (this needs to be >1)
contact_number_parameter = 8  # Parameter determining the distribution of number of contacts per person
initial_prevalence_in_contacts = 0.01  # No contacts are infected at time 0 at start of the simulation
simulation_time = 20  # How many steps to simulate the population for


# This is a template for an 'object'; variables and functions are defined inside the class and are accessed using a '.' syntax e.g. x.infected = True
# 'self' is used to refer to each object's individual variables which are independent of other "Person" objects
class Person:
    def __init__(self):  # This assigns values to the variables below for each person at the start of each period
        """Initialise a new person."""
        self.infected = False
        self.time_of_infection = None
        self.ever_infected = False
        self.new_infection = False

        self.contacts = np.random.poisson(contact_number_parameter)
        self.infected_contacts = 0

    def data_string(self):
        return f"Infected: {self.infected}, Time of infection: {self.time_of_infection}, Ever infected: {self.ever_infected}, Infected Contacts: {self.infected_contacts}"

    def infect(self, time):
        self.infected = True
        self.time_of_infection = time
        self.ever_infected = True
        self.new_infection = True


def initialise_population(population_size):
    """Create a population with only one person infected."""
    population = [Person() for _ in range(population_size)]
    population[0].infect(0)  # infect the first person
    return population


def summarise(population):
    stats = {
        "contacts": sum(person.contacts for person in population),
        "contacts_if_infected":  sum(person.contacts for person in population if person.infected),
        "infected": sum(person.infected for person in population),
        "new_infections": sum(person.new_infection for person in population)

    }
    stats["prevalence_in_contacts"] = stats["contacts_if_infected"] / stats["contacts"]
    stats["overall prevalence"] = stats["infected"] / len(population)

    return stats


def update(population, time):
    if time == 0:
        # At the start of the simulation, use a predefined value as we have no data
        prevalence_in_contacts = initial_prevalence_in_contacts
    else:
        prevalence_in_contacts = (
            sum(person.contacts for person in population if person.infected)
            / sum(person.contacts for person in population)
        )

    for person in population:
        person.new_infection = False

        if person.infected:
            person.infected_contacts = None
            if (time - person.time_of_infection) == duration_of_infectivity:
                person.infected = False
                person.time_of_infection = None

        if not person.infected and not person.ever_infected:
            # First calculate number of infected contacts
            person.infected_contacts = 0
            for i in range(person.contacts):
                e = np.random.uniform()
                if e < prevalence_in_contacts:
                    person.infected_contacts = person.infected_contacts + 1
            # Then calculate risk of infection per infected contact
            for i in range(person.infected_contacts):
                e = np.random.uniform()
                if e < rate_per_infected_contact:
                    person.infect(time)
                    break

        # contacts_if_infected is the number of contacts a person with infection has
        person.contacts_if_infected = person.contacts if person.infected else 0


def simulate(population_size):
    results = []  # the outputs we will compute
    population = initialise_population(population_size)
    results.append(summarise(population))
    printing_time = 10
    for t in range(1, simulation_time):
        update(population, t)
        stats = summarise(population)
        results.append(stats)
        if(t < printing_time):
          print("\nTime = ", t, "\tPrevalence in contacts = ", round(stats["prevalence_in_contacts"],3), "\tOverall prevalence", stats["overall prevalence"])
          for i in range (10):
            print("\t", i, population[i].data_string())
    return results


def plot_results(results):
    times = range(0, simulation_time)
    tick = 2

    plt.plot(times, [result["infected"] for result in results], 'x-', label='Total active')
    plt.plot(times, [result["new_infections"] for result in results], 'o-', label='New')
    plt.xticks(range(0, simulation_time, tick))
    plt.xlabel("Time")
    plt.ylabel("Number")
    plt.title("Infections")
    plt.legend()
    plt.show()

    plt.plot(times, [result["prevalence_in_contacts"]*100 for result in results], 'x-', label="Prevalence in Contacts")
    plt.plot(times, [result["overall prevalence"]*100 for result in results], 'o-', label="Overall Prevalence")
    plt.title("Prevalence of Infection")
    plt.ylabel("Prevalence %")
    plt.xlabel("Time")
    plt.xticks(range(0, simulation_time, tick))
    plt.legend()
    plt.show()


# results = simulate(population_size)
# plot_results(results)
