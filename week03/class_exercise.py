# The goal of this exercise is to create a class which can represent a single simulation
# This will facilitate running an ensemble of simulations with sampled parameters
# Once a Simulation object has been created, it should be possible to run it by calling the run() method
# You can choose how to handle things like inputs and outputs - the point is to think about how code can be
# organised in a way that is logical and easy to use.

# You can re-use code from the infection_toy_model.py to fill out the logic of your class - this exercise is more
# about how we organise ideas.
# You can import parts directly from the toy model code like so:
from infection_toy_model import Person
from infection_toy_model import initialise_population

# Or you may wish to copy it across so that you can modify it or place it inside a class.

# And these are just standard useful imports
import numpy as np
import matplotlib.pyplot as plt


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

