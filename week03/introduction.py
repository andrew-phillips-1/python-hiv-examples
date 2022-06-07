# We can often write code for a specific purpose in many different ways.
# These may vary in, for example, how we encode data or implement the logic involved.
# Even when the final outputs they produce is the same, these choices can affect
# how easy it is to understand and modify the code. 
# Below are three examples of modelling the infection status of a population
# and computing some overall statistics for it.

#### Version 1: For each attribute, have a list with all its values across all people
my_population = [
    [True, True, False, False, True],  # infected
    ['02-Mar-2022', '20-Feb-2022', None, None, '05-Mar-2022'],  # infection date
    [True, True, False, False, True],  # ever infected
    [True, False, False, False, True],  # new infection
    [4, 5, 3, 5, 2],  # contacts
    [1, 2, 0, 0, 2]  # contacts infected
]

def prevalence_in_contacts(population):
    contacts_if_infected = 0
    total_contacts = 0
    for i in range(len(population[0])):  # for every person
        total_contacts += population[4][i]
        if population[0][i]:  # if infected
            contacts_if_infected += population[4][i]
    return contacts_if_infected / total_contacts

def infection_probabilities(population):
    prevalence = prevalence_in_contacts(population)
    # Assume we have determined the number of infected contacts already
    return [1 - (1 - prevalence)**n for n in population[5]]


#### Version 2: Collect together the values corresponding to each person
my_population = [
    [True, "02-Mar-2022", True, True, 4, 1],
    [True, "20-Feb-2022", True, False, 5, 2],
    [False, None, False, False, 3, 0],
    [False, None, False, False, 5, 0],
    [True, "05-Mar-2022", True, True, 2, 2],
]

def prevalence_in_contacts(population):
    contacts_if_infected = sum(person[4] for person in population if person[0])
    total_contacts = sum(person[4] for person in population)
    return contacts_if_infected / total_contacts

def infection_probabilities(population):
    prevalence = prevalence_in_contacts(population)
    return [1 - (1 - prevalence)**person[5] for person in population]


#### Version 3: Use names to clarify the meaning and ignore the ordering
# Here we use custom-made objects which can collect exactly the information we want,
# and with which we can interact in predefined ways.
# Each of these objects is made from the same "blueprint" called a class.
# (This code is for illustration and does not work as is.
# For one possible implementation, see the infection_toy_model.py file.)
my_population = [
    # To create an object, we use the class's name and the arguments the class requires
    Person(True, "02-Mar-2022", True, True, 4, 1),
    Person(True, "20-Feb-2022", True, False, 5, 2),
    Person(False, None, False, False, 3, 0),
    Person(False, None, False, False, 5, 0),
    Person(True, "05-Mar-2022", True, True, 2, 2),
]

def prevalence_in_contacts(population):
    # We can access properties of the object using the notation <my_object>.<property>
    contacts_if_infected = sum(person.contacts for person in population if person.infected)
    total_contacts = sum(person.contacts for person in population)
    return contacts_if_infected / total_contacts

def infection_probabilities(population):
    prevalence = prevalence_in_contacts(population)
    return [1 - (1 - prevalence)**person.infected_contacts for person in population]

# We may also want to specify and call custom behaviour, like:
my_population[0].infect("30-Mar-2022")
