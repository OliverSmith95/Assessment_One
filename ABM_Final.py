# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:23:30 2018
Version 1.10(10/12/2018)
PLEASE NOTE: In order for this code to function, the logical steps have
been altered despite wanting step 4 to be step 7. 
REQUIREMENTS FOR CODE TO FUNCTION:
    Agent_Framework.py
    in.txt
    Tools>Preferences>IPython console> Graphics>\Inline"
    
@author: gy18os
"""
################## - 1. SET UP FUNCTIONS -  ###################################
#import all functions called to run all applicable code 
import random #inputting the random function
import operator
import csv # import csv function to read lines of code from "in.txt"
import matplotlib #import matplotlib function
import matplotlib.pyplot #inputting code to allow for matplot for code
import matplotlib.animation #import animation function.
import Agent_Framework_2 #inform the agent framework - separate bracket of agents, external to other aspects of code. 
import matplotlib.backends.backend_tkagg
import tkinter #import gui machanism 
import time #enables the ability to time agent processing.
import requests
import bs4
import sys
################# - 2. WEB SCRAPING DATA PLOTS ################################
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs) 
############### - 3. CREATION OF DATA LISTS AND PARAMETERS ####################
environment = [] #creation of environment empty list for agent plots 
num_of_agents = 10 #setting up number of agents to implement into the model
num_of_iterations = 100 #setting up number of times to randomise the agent positions
neighbourhood = 20
agents = [] #creation of a list
distances = [] # creation of a list
start = time.process_time()
#for testing purposes
test = 6
test2 = 4

################## - 4. SET UP GUI CANVAS #####################################

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
root = tkinter.Tk()  
root.wm_title("Model") 
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root) 
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
 
############## - 5. EXTRACT ENVIRONMENT FROM CSV FILE- #######################

#Importation of datalist, reading the list and appending the environment
f = open ("in.txt") 
reader = csv.reader(f)
envrionment = [] #create a new list in which to rows from rowlist
for row in reader:
    rowlist = [] #creation of lists derived from csv file
    environment.append(rowlist)
    for value in row:
        #indented below to combat float error. ensure indention is correct
        rowlist.append(int(value))
f.close()
############### -6. MAKE AGENTS - #############################################

#(1) Make the agents and set up x and y co-rdinates and (2) introduce agent_framework.
#Agent_framework_2 is the file i want to input into the ABM that set ups agent
#movements and data. I call upon an external py. file. 
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(Agent_Framework_2.Agent(environment, agents, y, x)) #introduced environments
    
#################### 6.1 TEST CODE IS FUNCTIONAL ##############################
    print(test)
############# - 7. INPUTTING PARAMETERS AND RULES FOR GUI- ####################
    
carry_on = True #informing the GUI to carry one after each iteration against the criteria.

def update(frame_number):
    sys.stdout.flush()
    # sys.stdout.flush() checks to see which part of the code is problematic
    global carry_on
    fig.clear() 
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        agents[i].move() #move agents
        agents[i].eat() #eat agents for environment to absorb agents
        agents[i].share_with_neighbours(neighbourhood) #communication with agents iterations. 
        
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)  
        
    if random.random()< 0.1:
        carry_on = False
        print("stopping condition") # if agents random value is below 0.1, 
        # I am calling for the model to stop. 
         
def gen_function(b = [0]):
    a = 0
    global carry_on #not needed as were not assigning, but clearer
    while (a<20) & (carry_on) :
        yield a            #returns control and waits next call
        a = a + 1
        
######################7.1 TEST CODE IS FUNCTIONAL #############################
        print (test + test2)       
###################### -8. CREATION OF GUI- #####################################
     
def run(): # this is called by the GUI menu item 'Run'
    global animation# taking the animation outside the local environment
    print('hip8') #testing code is functional  
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False) 
    #plot both datasets together - requirement of eating remaining data first then introduce code below. 
    canvas.show() #to show canvas onto GUI as coded above in part 4 block.

  
menu_bar = tkinter.Menu(root) #root is the configuration display - menu bar. 
root.config(menu=menu_bar) 
model_menu = tkinter.Menu(menu_bar) 
menu_bar.add_cascade(label="Model", menu=model_menu) 
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop() # to  initiate the loops within GUI. 


