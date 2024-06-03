# antennaCAT-objective-func-suite
The objective functions used to collect data for training the AntennaCAT optimizers

This repository will go public close to my PhD defense in August 2024. This is to ensure that the published version is the most up-to-date and accurate. 

It contains single objective, multi objective, and constrained functions used in the dataset for training the built-in AntennaCAT optimizer suite. 
52 common objective functions were pulled from various literature to create the set. 

Each function has its own folder containing:
* the objective function
* configurations (bounds, # input variable, # output variables, etc.)
* constraints
* and a python file for graphing the function, decision space, objective space, etc.


This objective function suite has been tested with the following optimizers:
* [pso_python](https://github.com/jonathan46000/pso_python) by [jonathan46000](https://github.com/jonathan46000)
    1) the main branch with the [adaptive timestep PSO optimizer](https://github.com/jonathan46000/pso_python)
    2) the [pso_basic branch](https://github.com/jonathan46000/pso_python/tree/pso_basic) without the timestep, for a baseline comparison
       
* [sweep](https://github.com/LC-Linkous/sweep) by [LC-Linkous](https://github.com/LC-Linkous), a basic sweep optimization example.
  
* [cat_swarm_python](https://github.com/LC-Linkous/cat_swarm_python)  by [LC-Linkous](https://github.com/LC-Linkous),
    1) the main branch with traditional cat swarm optimizer (LIT REFERENCE TBA!)
    2) the cat_swarm_quantum branch with a quantum inspired approach
  
* [chicken_swarm_python](https://github.com/LC-Linkous/chicken_swarm_python)  by [LC-Linkous](https://github.com/LC-Linkous),
    1) the main branch with traditional chicken swarm optimizer (LIT REFERENCE TBA!)
    2) the chicken_swarm_quantum branch with a quantum inspired approach
  
* [multi_glods_python](https://github.com/jonathan46000/multi_glods_python) by [jonathan46000](https://github.com/jonathan46000)
  1) NOTE: multi_glods_python is currently getting an update to be compatible with AntennaCAT


To cite:

L. Linkous, J. Lundquist, M. Suche, and E. Topsakal, "Machine Learning Assisted Hyperparameter Tuning for Optimization," 2024 IEEE USNC-URSI Radio Science Meeting (Joint with AP-S Symposium), Florence, Italy, 2024 (TO BE PRESENTED JULY 2024)








