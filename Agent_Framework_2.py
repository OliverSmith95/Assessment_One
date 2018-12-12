# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:14:00 2018
Version 1.2 (10/12/2018)
@author: gy18os
"""
import random

class Agent():
#x and y is different values from the model and class.
#define and initate agents - self is a parameter within python inorder create an object referennce. 
    def __init__ (self, environment,agents, y = None, x = None): 
#Introduced environment with a comma after self to introduce the fucntion 
#I have to provide self inorder to create a definition of the data. 
#an underscore before variables implies the code should not be altered. 
        self.environment = environment 
        self.agents = agents
        self.store = 0
        
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x 
            
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y 
      
        
    #defining the moves within the ABM.
    #change i,0 and o,1 into self. 
    
    def move (self):
         if random.random() < 0.5:
             self._y = (self._y + 1) % 100
         else:
             self._y = (self._y - 1) % 100

         if random.random() < 0.5:
             self._x = (self._x + 1) % 100
         else:
             self._x = (self._x - 1) % 100

#defining property, to inform me what the change would be if once the code is run.
#ensuring the values of x and y are now the same of the model, once imported the class 
#safe guarding agents of anything in the class
    @property
    #protects below aspect of code and to indicate no code should be altered.
    def y(self):
        """ get random numbers for Y."""
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @y.deleter
    def y(self):
        del self._y

    @property
    def x(self):
        """get random numbers for x"""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
        
    def eat(self): 
     if self.environment[self.y][self.x] > 10:
         self.environment[self.y][self.x] -= 10
         self.store += 10 
         
   #sharing commmunication of position of agents withn neighbourhood.  
    def share_with_neighbours(self, neighbourhood):
     for agent in self.agents:
         dist = self.distance_between(agent) 
         if dist <= neighbourhood:
             sum = self.store + agent.store
             ave = sum /2
             self.store = ave
             agent.store = ave
             #print("sharing " + str(dist) + " " + str(ave))
             
    #defining and calculating distance between agents
    def distance_between(self, agent): 
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 



          
        
