# 9/2 README PATH TEST BEFORE UPLOAD

# Objective Function Suite

## Table of Contents
* [Project Description](#project-description)
* [Requirements](#requirements)
* [Getting Started](#getting-started)
* [Benchmark Functions](#benchmark-functions)
    * [Single-Input, Single-Objective Functions](#single-input-single-objective-functions)
        * [Single Input Ackley Function](#single-input-ackley-function)
        * [Single Input Griewank Function](#single-input-griewank-function)
        * [Single Input Rastrigin Function](#single-input-rastrigin-function)
        * [Single Input Rosenbrock Function](#single-input-rosenbrock-function)
        * [Single Input Schwefel Function](#single-input-schwefel-function)            
        * [Single Input Sphere Function](#single-input-sphere-function)
    * [Single-Objective Functions](#single-objective-functions)
        * [Ackley Function](#ackley-function)
        * [Beale Function](#beale-function)
        * [Booth Function](#booth-function)
        * [Branin Function](#branin-function)
        * [Bukin Function N.6](#bukin-function-n6)
        * [Cross-in-Tray Function](#cross-in-tray-function)
        * [Easom Function](#eason-function)
        * [Eggholder Function](#eggholder-function)
        * [Goldstein–Price Function](#goldstein-price-function)      
        * [Himmelblau's Function](#himmelblaus-function)
        * [Hölder Table Function](#hölder-table-function)
        * [Lévi Function N.13](#lévi-function-n13)
        * [Matyas Function](#matyas-function)
        * [McCormick Function](#mccormick-function)
        * [Michalewicz Function](#michalewicz-function)
        * [Rastrigin Function](#rastrigin-function)
        * [Rosenbrock Function](#rosenbrock-function)
        * [Schaffer Function N.2](#schaffer-function-n2)
        * [Schaffer Function N.4](#schaffer-function-n4)
        * [Sphere Function](#sphere-function)
        * [Styblinski–Tang Function](#styblinskitang-function)    
        * [Three-hump Camel Function](#three-hump-camel-function)    
    * [Multi-Objective Funtions](#multi-objective-functions)
        * [Binh and Korn Function](#binh-and-korn-function)
        * [Chankong and Haimes Function](#chankong-and-haimes-function)
        * [Constr-Ex Problem](#constr-ex-problem)
        * [CTP1 function](#CTP1-function)
        * [Fonseca–Fleming Function](#fonsecafleming-function)
        * [Kursawe Function](#kursawe-function)
        * [Lundquist 3 Variable](#lundquist-3-variable)
        * [Osyczka and Kundu Function](#osyczka-and-kundu-function)
        * [Poloni's Two Objective Function](#polonis-two-objective-function)  
        * [Schaffer Function N.1](#schaffer-function-n1)
        * [Schaffer Function N.2](#schaffer-function-n2-1)
        * [Test Function 4](#test-function-4)  
        * [Viennet Function](#viennet-function)
        * [Zitzler–Deb–Thiele's Function N.1](#zitzlerdebthieles-function-n1)
        * [Zitzler–Deb–Thiele's Function N.2](#zitzlerdebthieles-function-n2)
        * [Zitzler–Deb–Thiele's Function N.3](#zitzlerdebthieles-function-n3)        
        * [Zitzler–Deb–Thiele's Function N.4](#zitzlerdebthieles-function-n4)
        * [Zitzler–Deb–Thiele's Function N.6](#zitzlerdebthieles-function-n6)  
    * [Constrained Objective Funtions](#constrained-objective-functions)
        * [Rosenbrock Function Constrained to Disk](#rosenbrock-function-constrained-to-disk)
        * [Rosenbrock Function Constrained with a Cubic and a Line](#rosenbrock-function-constrained-with-a-cubic-and-a-line)
    * [AntennaCAT Objective Function Set](#antennacat-objective-function-set)
        * [AntennaCAT Function 1](#antennacat-function-1)
        * [AntennaCAT Function 2](#antennacat-function-2)
        * [AntennaCAT Function 3](#antennacat-function-3) (STEP)
        * [AntennaCAT Function 10](#antennacat-function-10)
        * [AntennaCAT Function 11](#antennacat-function-11)
        * [AntennaCAT Function 12](#antennacat-function-12)
        * [AntennaCAT Function 13](#antennacat-function-13)

* [Future Development](#future-development)
* [References](#references)
* [Related Publications](#related-publications)
* [Related Repositories](#related-repositories)
* [To Cite](#to-cite)



## Project Description
This repository is an archive of the benchmarking functions used to collected performance data from the set of optimizers used in the development of AntennaCAT. The repository is under development. Additional information, citations, functions, and variations are continuously added as features are developed, optimizers are tested, and publications are released. 


Objective function references are cited in their individual sections. Supporting literature and other references of interest can be viewed in the [References](#references) section at the end of this README. When possible, multiple references were used for each objective function to provide more resources if they should be of interest.  

## Requirements
It is suggested to run this project in a virtual environment. This was developed using Visual Studio Code, with a Python virtual environment and the following libraries & dependencies. Newer versions of these dependencies may be available, and may work without issue, but have not been tested. 

To install requirements via terminal:
pip install -r requirements.txt

Python version:
3.9.8

Dependencies versions:
```Python
contourpy==1.2.0
cycler==0.12.1
fonttools==4.50.0
importlib_resources==6.4.0
kiwisolver==1.4.5
matplotlib==3.8.3
numpy==1.26.3
packaging==24.0
pandas==2.2.0
pillow==10.2.0
pyarrow==15.0.2
pyparsing==3.1.2
python-dateutil==2.8.2
pytz==2024.1
six==1.16.0
tzdata==2023.4
zipp==3.18.1
```

## Getting Started

Objective functions are organized into the following directories:

* antennacat_set
* constrained_objective
* multi_objective
* single_objective
* single_objective_single_output

Each of the listed directories contains sub-directories of objective functions where each objective function has its own directory containing at least:
   1) configs_F.py - contains imports for the objective function and constraints, CONSTANT assignments for functions and labeling, boundary ranges, the number of input variables, the number of output values, and the target values for the output
   2) constr_F.py - contains a function with the problem constraints, both for the function and for error handling in the case of under/overflow. 
   3) func_F.py - contains a function with the objective function.

When possible, a file for graphing the objective function and select features (e.g., the pareto front, feasible objective space, feasible decision space, relations between input variables, etc.) has been added to the directory as graph.py. Functions with high input and output dimensionality are not graphed.


## Benchmark Functions
### Single-Input, Single-Objective Functions

In usage, all single-dimension input and single-dimenson output functions were constrained from 0 to 1. These are articifial constraints and can be changed in the configs_F.py file.


#### Single Input Ackley Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/one_input_ackley_plots.png" height="300" >
</p>
<p align="center">One Dimensional Ackley Plot, Constrained Input 0 to 1</p>

In mathematical optimization, the Ackley function is a non-convex function used as a performance test problem for optimization algorithms. It was proposed by David Ackley in his 1987 PhD dissertation. [wiki](https://en.wikipedia.org/wiki/Ackley_function "Ackley function page")

```math
f(x) = -20 \exp\left(-0.2 \sqrt(\abs(x)) \right) - \exp\left(\cos(2 \pi x)\right) + 20 + e
```
Where:
- $x$ is the single decision variable input.
- The optimal solution is at $f(x) = 0$, where $x = 0$.

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(0) = 0| $0\leq x,y\leq 1$ (artificial) |   | 




#### Single Input Griewank Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/one_input_griewank_plots.png" height="300" >
</p>
<p align="center">One Dimensional Griewank Plot, Constrained Input 0 to 1</p>


The Griewank function is a popular benchmark function used in optimization problems due to its many widespread local minima, which are regularly distributed. The presence of the cosine term with a frequency that depends on $x$ ensures that the function has a series of local minima and maxima, making it a challenging function to optimize.  [SFU Page](https://www.sfu.ca/~ssurjano/griewank.html "Griewank function page")

```math
f(x) = 1 + \frac{x^2}{4000} - \cos\left(\frac{x}{\sqrt{1}}\right)
```
Where:
- $x$ is the single decision variable input.
- The optimal solution is at $f(x) = 0$, where $x = 0$.

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(0) = 0| $0\leq x,y\leq 1$ (artificial) |   | 



#### Single Input Rastrigin Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/one_input_rastrigin_plots.png" height="300" >
</p>
<p align="center">One Dimensional Rastrigin Plot, Constrained Input 0 to 1</p>



#### Single Input Rosenbrock Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/one_input_rosenbrock_plots.png" height="300" >
</p>
<p align="center">One Dimensional Rosenbrock Plot, Constrained Input 0 to 1</p>




#### Single Input Schwefel Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/one_input_schwefel_plots.png" height="300" >
</p>
<p align="center">One Dimensional Schwefel Plot, Constrained Input 0 to 1</p>


#### Single Input Sphere Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/one_input_sphere_plots.png" height="300" >
</p>
<p align="center">One Dimensional Sphere Plot, Constrained Input 0 to 1</p>







# Future Development

This repository is an archive of objective functions used to test and debug the AntennaCAT software suite, and to train the machine learning models related to the optimization process. It will be updated as functions are added in testing, related repositories, or in related literature.


# References 


# Related Publications
First mention of objective function testing:

L. Linkous, J. Lundquist, M. Suche and E. Topsakal, "Machine Learning Assisted Hyperparameter Tuning for Optimization," 2024 IEEE INC-USNC-URSI Radio Science Meeting (Joint with AP-S Symposium), Florence, Italy, 2024, pp. 107-108, doi: 10.23919/INC-USNC-URSI61303.2024.10632482.


AntennaCAT software:



# Related Repositories



# To Cite

L. Linkous, J. Lundquist, M. Suche and E. Topsakal, "Machine Learning Assisted Hyperparameter Tuning for Optimization," 2024 IEEE INC-USNC-URSI Radio Science Meeting (Joint with AP-S Symposium), Florence, Italy, 2024, pp. 107-108, doi: 10.23919/INC-USNC-URSI61303.2024.10632482.