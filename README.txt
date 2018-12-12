1.0 Agent Based Modelling/Introduction

This readme file outlines the instructions in order to run this Agent Based Model (ABM) which produces a GUI (Graphical User Interface). 
The purpose of this code is to demonstrate the movement of randomised agents within python environments, where the created agents run 
freely within a defined space/environment until the number of iterations have been met. Furthermore, to integrate user interaction 
“Asynchronous programming”, the results will be orchestrated by the use of a GUI; asking the user to call upon the code to show the 
movement of the created agents until the stopping condition is met. This project has been undertaken throughout the past two months 
of learning python throughout academic lead sessions and further research by forking examples of code on GitHub and online tutorials 
to fix any minuscule syntax errors. – would normally be code intending problems or undefined calls or functions. 

2.0 Getting Started/How to source my code

>>>>> Download all files under oliversmith1995.github.io or files found in TurnitIn submission(ONLY for Andy Turner and Nick Gould)
***************************************************************************************************************************************
PLEASE NOTE: Due to problems with my original Github username including upper cases, this will not work. My second account (shown above)
has been flagged and therefore is not public. Until Github unflag my account, my resources will be unavailable. 
***************************************************************************************************************************************


Files should contain

(Essential) ABM_Final.py (Code to create ABM and to use to run GUI)
(Essential Agent_Framework_2.py (Creates a agent class)
In.txt (agent's environment)
README.txt (This document)
README.doc
License.txt
Project Overview.doc 


3.0 Prerequisites/Operating system requirements

(1) In order to run this project, one requires the use of Anaconda 3.7 – Using Spyder (Python 3.7) with the computer system requirements 
as follows (copied from https://docs.anaconda.com/anaconda/install/)

Windows - https://docs.anaconda.com/anaconda/install/windows/
MacOS - https://docs.anaconda.com/anaconda/install/mac-os/

* License: Free use and redistribution under the terms of the End User License Agreement.
* Operating system: Windows 7 or newer, 64-bit macOS 10.10+, or Linux, including Ubuntu, RedHat, CentOS 6+, and others.
* If your operating system is older than what is currently supported, you can find older versions of the Anaconda installers in our archive that might work for you. Check our FAQ for version recommendations.
* System architecture: Windows- 64-bit x86, 32-bit x86; MacOS- 64-bit x86; Linux- 64-bit x86, 32-bit x86, 64-bit Power8/Power9.
* Minimum 5 GB disk space to download and install.


Instructions to run the code

(1) Ensuring all “(Essential)” files are open on Python from 2.0
(2) To ensure the code will create a functional GUI one needs to adjust the IPython graphic functionality.  Tools>Preferences>IPython console> Graphics> Inline. By default, this may be set to Automatic revert this otherwise.
(3) Run the code (press R5) and a pop up will appear “Model”. Click the drop down button and select “Model” (under the feather and “--------“) 
(4) Model RUNS.
(5) On closure of the model (which should run between 2-10 movements depending the agent scores to the stopping criteria) the model output will be displayed in the kernel console showing the number of movements.
Running the tests

There are some evidence of testing the final code provided in the folder. For example, to ensure at the end of project all items of code were being accounted for, I have inserted tests where I ask the code print a value or flush the system/create a forced buffer to execute.

For example sys.stdout.flush()

For 6.1 and 7.1, I have asked python to print a value. This was to ensure the code in the latter end of the script was contributing towards the output. This was because at times the GUI or figure would not display the agent environments. Despite this problem which would not resolve, some parts of the code were placed towards the top of script.  
This is highlighted within the ABM_Final.py script.  

       print(test)
       print(test + test2) 

Versioning

Version 1.10 of ABM_Final.py (14/12/2018) No intention of updating
Version 1.2 of Agent_Framework_2.py (14/12/2018) No intention of updating

Authors

* Oliver Smith - Initial work – Github:OliverSmith95, Wesbite (not functional - oliversmith1995

License

This project is licensed under the Python’s Terms and conditions for accessing or otherwise using Python License - see the LICENSE.txt file for details

Acknowledgments

* I commend Andy Turner, Nick Gould and practical demonstrators for their patience and work throughout these past months
