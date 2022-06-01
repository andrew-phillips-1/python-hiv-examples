import numpy as np
import matplotlib.pyplot as plt

# You can import any parts of the toy model that you want to re-use directly like so
from infection_toy_model import Person
from infection_toy_model import infect
from infection_toy_model import initialise_population

# You may also want to take some of the code and put it inside a class!

# The goal of this exercise is to create a class which can represent a single simulation
# This will facilitate running an ensemble of simulations with sampled parameters
# Once a Simulation object has been created, it should be possible to run it by calling the run() method
# You can choose how to handle things like inputs and outputs - the point is to think about how code can be
# organised in a way that is logical and easy to use.


# Simulation class
class Simulation:
    # What properties does the simulation need to have?

    # How should the simulation be initialised? What information need to be passed in
    # to create the object, and how should things be set? Should anything be checked?
    def __init__(self):

    # Should this method take any additional arguments, or should everything be member variables of the
    # simulation itself?
    # How do you want to handle the results?
    def run(self):

    # You can add more methods as you see fit!

