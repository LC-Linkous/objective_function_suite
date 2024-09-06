
# Objective Function Suite

# IN PROGRESS. Last update Sept. 2, 2024
TODO list:


[ ] Add AntennaCAT set functions

[x] Add blurbs for single input, single objective functions

[ ] Update headers to match code migration

[ ] Cosmetic graph fixes for README

[ ] Update summary tables in README



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
        * [Levy Function N.13](#levy-function-n13)
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
* [Function Summary](#function-summary)
* [Future Development](#future-development)
* [References](#references)
* [Related Publications](#related-publications)
* [Related Repositories](#related-repositories)
* [To Cite](#to-cite)



## Project Description
This repository is an archive of the benchmarking functions used to collect performance data from the set of optimizers used in the development of AntennaCAT. The repository is under development. Additional information, citations, functions, and variations are continuously added as features are developed, optimizers are tested, and publications are released. 


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

   1) antennacat_set - objective functions created for testing edge cases or balancing datasets.
   2) constrained_objective - objective functions with enforced  constraints. The unconstrained version may appear in other directories.
   3) multi_objective - multi objective (multiple output) objective functions. The objective functions take one or more input values.
   4) single_objective - single objective (single output) objective functions. The objective functions take one or more input values.
   5) single_objective_single_output - single objective functions that take only one input value. These were created specifically to balance that dataset used for training in the AntennaCAT project. 

Each of the listed directories contains sub-directories of objective functions where each objective function has its own directory containing at least:
   1) configs_F.py - contains imports for the objective function and constraints, CONSTANT assignments for functions and labeling, boundary ranges, the number of input variables, the number of output values, and the target values for the output
   2) constr_F.py - contains a function with the problem constraints, both for the function and for error handling in the case of under/overflow. 
   3) func_F.py - contains a function with the objective function.

When possible, a file for graphing the objective function and select features (e.g., the pareto front, feasible objective space, feasible decision space, relations between input variables, etc.) has been added to the directory as graph.py. Functions with high input and output dimensionality are not graphed.


## Benchmark Functions
### Single-Input, Single-Objective Functions

In usage, all single-dimension input and single-dimension output functions were constrained from 0 to 1. These are artificial constraints and can be changed in the configs_F.py file.


#### Single Input Ackley Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/one_input_ackley_plots.png" height="300" >
</p>
<p align="center">One Dimensional Ackley Plot, Constrained Input 0 to 1</p>

In mathematical optimization, the Ackley function is a non-convex function used as a performance test problem for optimization algorithms. It was proposed by David Ackley in his 1987 PhD dissertation. [wiki](https://en.wikipedia.org/wiki/Ackley_function "Ackley function page")

```math
f(x) = -20 \exp\left(-0.2 \sqrt|x| \right) - \exp\left(\cos(2 \pi x)\right) + 20 + e
```
Where:
- $x$ is the single decision variable input.
- The optimal solution is at $f(x) = 0$, where $x = 0$.

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(0) = 0| $0\leq x\leq 1$ (artificial) |   | 




#### Single Input Griewank Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/one_input_griewank_plots.png" height="300" >
</p>
<p align="center">One Dimensional Griewank Plot, Constrained Input 0 to 1</p>


The Griewank function is a popular benchmark function used in optimization problems. The presence of the cosine term with a frequency that depends on $x$ ensures that the function has a series of local minima and maxima, making it a challenging function to optimize.  [SFU page](https://www.sfu.ca/~ssurjano/griewank.html "Griewank function page")

```math
f(x) = 1 + \frac{x^2}{4000} - \cos\left(\frac{x}{\sqrt{1}}\right)
```
Where:
- $x$ is the single decision variable input.
- The optimal solution is at $f(x) = 0$, where $x = 0$.

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(0) = 0| $0\leq x\leq 1$ (artificial) |   | 



#### Single Input Rastrigin Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/one_input_rastrigin_plots.png" height="300" >
</p>
<p align="center">One Dimensional Rastrigin Plot, Constrained Input 0 to 1</p>


In mathematical optimization, the Rastrigin function is a non-convex function used as a performance test problem for optimization algorithms. It is a typical example of non-linear multimodal function. [wiki](https://en.wikipedia.org/wiki/Rastrigin_function "Rastrigin Function Page") 


```math
f(x) = An + \sum_{i=1}^{n} \left[ x_i^2 - A \cos(2 \pi x_i) \right]

```
Where:
- $x$ is the single decision variable input.
- The optimal solution is at $f(x) = 0$, where $x = 0$.


| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(0) = 0 | $0\leq x\leq 1$ (artificial) |   | 

| Local Minima | Boundary | Constraints |
|----------|----------|----------|
| f(1) = 1 | $0\leq x\leq 1$ (artificial) |   | 



#### Single Input Rosenbrock Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/one_input_rosenbrock_plots.png" height="300" >
</p>
<p align="center">One Dimensional Rosenbrock Plot, Constrained Input 0 to 1</p>


The Rosenbrock function, also known as the Rosenbrock's valley or Rosenbrock's banana function, is a non-convex optimization problem that is widely used as a benchmark problem. [wiki](https://en.wikipedia.org/wiki/Rosenbrock_function "Rosenbrock Function Page") 



```math
f(x) = (1-x)^2 + 100*(x-1)^2

```

Where:
- $x$ is the single decision variable input.
- The optimal solution is at $f(x) = 0$, where $x = 1$.


| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(1) = 0 | $0\leq x\leq 1$ (artificial) |   | 


#### Single Input Schwefel Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/one_input_schwefel_plots.png" height="300" >
</p>
<p align="center">One Dimensional Schwefel Plot, Constrained Input 0 to 1</p>


The Schwefel function is a popular benchmark function used in optimization problems.  [SFU page](https://www.sfu.ca/~ssurjano/schwef.html "Schwefel function page")


```math
f(x) = x * sin(\sqrt|x|)

```
Where:
- $x$ is the single decision variable input.
- The optimal solution is at $f(x) = 0$, where $x = 0$.


| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(0) = 0 | $0\leq x\leq 1$ (artificial) |   | 


#### Single Input Sphere Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/one_input_sphere_plots.png" height="300" >
</p>
<p align="center">One Dimensional Sphere Plot, Constrained Input 0 to 1</p>


The sphere function is one of the simplest optimization test functions. It can be utilized in $n$ dimensions, where it will have $n$ local minima except for the global one. It is continuous, convex and unimodal. [SFU page](https://www.sfu.ca/~ssurjano/spheref.html "Sphere function example") 

```math
f(x) = x^2

```
Where:
- $x$ is the single decision variable input.
- The optimal solution is at $f(x) = 0$, where $x = 0$.


| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(0) = 0 | $0\leq x\leq 1$ (artificial) |   | 




### Single-Objective Functions

#### Ackley Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/ackley_plots.png" height="300" >
</p>
<p align="center">Ackley Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>

In mathematical optimization, the Ackley function is a non-convex function used as a performance test problem for optimization algorithms. It was proposed by David Ackley in his 1987 PhD dissertation. [wiki](https://en.wikipedia.org/wiki/Ackley_function "Ackley function page")

```math
f(x) = -20 \exp\left(-0.2 \sqrt{\frac{1}{n} \sum_{i=1}^{n} x_i^2}\right) - \exp\left(\frac{1}{n} \sum_{i=1}^{n} \cos(2 \pi x_i)\right) + 20 + e
```
Where:
- $x = (x_1, x_2, \ldots, x_n)$ is the vector of decision variables.
- $n$ is the dimensionality of the problem.
- The optimal solution is at $f(x) = 0$, where $x_i = 0$ for all $i$.

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(0,..., 0) = 0| $-5\leq x,y\leq 5$ (artificial) |   | 

It is featured in this repository as a function with 2-dimensional inputs.

```math
f(x, y) = -20 \exp\left(-0.2 \sqrt{\frac{1}{n}*(x^2 + y^2)}\right) - \exp\left(\frac{1}{2} (\cos(2 \pi x) + \cos(2 \pi y)) \right) + 20 + e
```


#### Beale Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/beale_plots.png" height="300" >
</p>
<p align="center">Beale Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>

The Beale function is multimodal, with sharp peaks at the corners of the input domain. It takes two inputs. [SFU page](https://www.sfu.ca/~ssurjano/beale.html "Beale function example")


```math
f(x, y) = (1.5 - x + xy)^2 + (2.25 - x + xy^2)^2 + (2.625 - x + xy^3)^2
```



| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(3, 0.5) = 0| $-4.5\leq x,y\leq 4.5$ |   | 



#### Booth Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/booth_plots.png" height="300" >
</p>
<p align="center">Booth Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>


The Booth function is a 2-dimensional input artificial landscape commonly used for optimization performance evaluation. [SFU page](https://www.sfu.ca/~ssurjano/booth.html "Booth function example") [Medium example](https://silvahansini.medium.com/optimization-of-the-booth-function-with-differential-evaluation-6a60a74a513c "Medium.com example")

```math
 f(x, y) = (x + 2y - 7)^2 + (2x + y - 5)^2
```

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(1,3) = 0| $-10\leq x,y\leq 10$ |   | 



#### Branin Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/branin_plots.png" height="300" >
</p>
<p align="center">Branin Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>


The Branin function, or Branin-Hoo function, is a 2-dimensional input artificial landscape commonly used for optimization performance evaluation. It has three global minimia. [SFU page](https://www.sfu.ca/~ssurjano/branin.html "Branin function example") 

```math
 f(x, y) = a*(y-b*(x**2)+c*x-r)**2 + s*(1-t)*np.cos(x)+1
```

Where the constants are:
* $a = 1$
* $b = \frac{5.1}{4\pi^2}$
* $c = \frac{5}{\pi}$
* $r = 6$
* $s = 10$
* $t = \frac{1}{8\pi}$

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| $f(-\pi,12.275) = 0.397887$| $-5\leq x\leq 10$ <br> $0\leq y\leq 15$ |   | 
| $f(\pi,2.275) = 0.397887$| $-5\leq x\leq 10$ <br> $0\leq y\leq 15$ |   | 
| $f(9.42479,2.475) = 0.397887$| $-5\leq x\leq 10$ <br> $0\leq y\leq 15$ |   | 




#### Bukin Function N.6 

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/bukin_N6_plots.png" height="300" >
</p>
<p align="center">Bukin Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>


The Bukin function is a 2-dimensional input artificial landscape commonly used for optimization performance evaluation. It has many local minima along its primary ridge. [SFU page](https://www.sfu.ca/~ssurjano/bukin6.html "Bukin function example") 

```math
 f(x, y) = 100 \sqrt{|y - 0.01x^2|} + 0.01 |x + 10|
```

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(-10, 1) = 0| $-15\leq x\leq -5$ <br> $-3\leq y\leq 3$ |   | 



#### Cross-in-Tray Function 

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/cross_in_tray_plots.png" height="300" >
</p>
<p align="center">Cross-in-Tray Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>


The Cross-in-Tray function is a 2-dimensional input artificial landscape commonly used for optimization performance evaluation. It has many global minima. [SFU page](https://www.sfu.ca/~ssurjano/crossit.html "Cross-in-Tray function example") 

```math
   f(x, y) = -0.0001 \left|\sin(x) \sin(y) \exp\left(\left|100 - \frac{\sqrt{x^2 + y^2}}{\pi}\right|\right) + 1\right|
```

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(1.3491, -1.34941) = 0| $-10\leq x,y \leq 10$ |   | 
| f(1.3491, 1.34941) = 0| $-10\leq x,y \leq 10$ |   | 
| f(-1.3491, -1.34941) = 0| $-10\leq x,y\leq 10$ |   | 
| f(-1.3491, 1.34941) = 0| $-10\leq x,y\leq 10$ |   | 



#### Easom Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/easom_plots.png" height="300" >
</p>
<p align="center">Easom Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>


The Easom function has several local minima. It is unimodal, and the global minimum has a small area relative to the search space. [SFU page](https://www.sfu.ca/~ssurjano/easom.html "Easom function example") 

```math
f(x, y) = -\cos(x) \cos(y) \exp\left(-(x - \pi)^2 - (y - \pi)^2\right)
```

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| $f(\pi, \pi) = -1$| $-15\leq x,y\leq 15$\* |   | 

\* The [-15, 15] boundary is artificial. The [Wikipedia article](https://en.wikipedia.org/wiki/Test_functions_for_optimization#Test_functions_for_single-objective_optimization) suggests [-100, 100], however many buffer under/overflow issues were encountered experimentally after [-17, 17].

#### Eggholder Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/eggholder_plots.png" height="300" >
</p>
<p align="center">Eggholder Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>


The Eggholder function has a large number local minima, making it difficult to optimize. [SFU page](https://www.sfu.ca/~ssurjano/egg.html "Eggholder function example") 


```math
   f(x, y) = -(y + 47) \sin\left(\sqrt{\left| \frac{x}{2} + (y + 47) \right|}\right) - x \sin\left(\sqrt{\left| x - (y + 47) \right|}\right)
```

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(512, 404.2319) = -959.6407| $-515 \leq x,y \leq 515$ |   | 



#### Goldstein–Price Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/goldstein_price_plots.png" height="300" >
</p>
<p align="center">Goldstein-Price Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>


The Goldstein–Price is a 2-dimensional input artificial landscape with several local minima. [SFU page](https://www.sfu.ca/~ssurjano/goldpr.html "Goldstein–Price function example") 

```math
   g(x,y) = [1 + (x + y + 1)^2 (19 - 14x + 3x^2 - 14y + 6xy + 3y^2)] \\
   h(x,y) =  [30 + (2x - 3y)^2 (18 - 32x + 12x^2 + 48y - 36xy + 27y^2)] \\
   f(g,h) =  g*h
```

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(0, -1) = 3| $-2 \leq x,y \leq 2$ |   | 



#### Himmelblau's Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/himmelblau_plots.png" height="300" >
</p>
<p align="center">Himmelblau's Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>

In mathematical optimization, Himmelblau's function is a multi-modal function, used to test the performance of optimization algorithms. It has 4 identical minima. [wiki](https://en.wikipedia.org/wiki/Himmelblau%27s_function "Himmelblau's function") 

```math
f(x, y) = (x^2 + y - 11)^2 + (x + y^2 - 7)^2
```

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(3, 2) = 0                 | $-5 \leq x,y \leq 5$  |   | 
| f(-2.805118, 3.121212) = 0  | $-5 \leq x,y \leq 5$  |   | 
| f(-3.779310, -3.283186) = 0 | $-5 \leq x,y \leq 5$  |   | 
| f(3.584428, -1.848126) = 0  | $-5 \leq x,y \leq 5$   |   | 



#### Hölder Table Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/holder_table_plots.png" height="300" >
</p>
<p align="center">Hölder Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>


<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/holder_table_plots2.png" height="300" >
</p>
<p align="center">Zoomed in Hölder Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red, to Show the Shallowness of the Center Cups</p>



The Holder Table function has many local minima, with four global minima. [SFU page](https://www.sfu.ca/~ssurjano/holder.html "Hölder Table Function example") 

```math
f(x, y) = -\left| \sin(x) \cos(y) \exp\left| 1 - \frac{\sqrt{x^2 + y^2}}{\pi} \right| \right|

```

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(8.05502, 9.66459) = -19.2085    | $-10 \leq x,y \leq 10$ |   | 
| f(-8.05502, 9.66459) = -19.2085   | $-10 \leq x,y \leq 10$ |   | 
| f(8.05502, -9.66459) = -19.2085   | $-10 \leq x,y \leq 10$ |   | 
| f(-8.05502, -9.66459) = -19.2085  | $-10 \leq x,y \leq 10$ |   | 



#### Levy Function N.13 

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/levy_N13_plots.png" height="300" >
</p>
<p align="center">Levy Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>



The Levy Function N.13 has a complicated and disjoint geometry, making it difficult to optimize. [SFU page](https://www.sfu.ca/~ssurjano/levy13.html "Levy Function N.13 example") [Global Optimization Benchmarks and AMPGO page](https://infinity77.net/global_optimization/test_functions_nd_L.html#go_benchmark.Levy13)


```math
f(\mathbf{x}) = \sin^2(3 \pi x_1) + \sum_{i=1}^{n-1} \left[ (x_i - 1)^2 \left(1 + \sin^2(3 \pi x_{i+1})\right) \right] + (x_n - 1)^2 \left(1 + \sin^2(2 \pi x_n)\right)
```


Where:
* $n$ is the dimensionality of the problem


| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(1,...,1) = 0| $-10 \leq x,y \leq 10$ |   | 


It is used in this repository as a 2-dimensional function:

```math
   f(x, y) = \sin^2(3\pi x) + (x - 1)^2[1 + \sin^2(3\pi y)] + (y - 1)^2[1 + \sin^2(2\pi y)]
```


#### Matyas Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/matyas_plots.png" height="300" >
</p>
<p align="center">Matyas Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>


The Matyas function has no local minima except the global one. [SFU page](https://www.sfu.ca/~ssurjano/matya.html "Matyas function example") 

```math
f(x, y) = 0.26(x^2 + y^2) - 0.48xy
```

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(0, 0) = 0| $-10 \leq x,y \leq 10$ |   | 



#### McCormick Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/mccormick_plots.png" height="300" >
</p>
<p align="center">McCormick Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>


The McCormick function is a 2-dimensional artificial landscape used to evaluate optimizer performance. [SFU page](https://www.sfu.ca/~ssurjano/mccorm.html "McCormick function example") 


```math
f(x, y) = \sin(x + y) + (x - y)^2 - 1.5x + 2.5y + 1
```

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(-0.54719, -1.54719) = -1.9133| $-1.5 \leq x \leq 4$ <br> $-3 \leq y \leq 4$ |   | 



#### Michalewicz Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/michalewicz_plots.png" height="300" >
</p>
<p align="center">Michalewicz Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>


The Michalewicz function is a 2-dimensional artificial landscape used to evaluate optimizer performance. If has $n$ number of local minima, where $n$ is the dimensionality the function is evaluated at. The 2-dimensional case is used here, but literature has used higher dimensionality. [SFU page](https://www.sfu.ca/~ssurjano/michal.html "Michalewicz function example") 


```math
f(x, y) = -\sum_{i=1}^{n} sin(x_i)*sin^{2m}(\frac{i*(x_i)^2}{\pi})

```

Where:
* $n$ is the dimensionality of the problem
* $m$ is a constant, often $10$. This defines the steepness of the valleys and ridges. 

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(2.2, 1.57) = -1.8013| $0 \leq x_i \leq \pi$  |   | 


#### Rastrigin Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/rastrigin_plots.png" height="300" >
</p>
<p align="center">Rastrigin Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>


In mathematical optimization, the Rastrigin function is a non-convex function used as a performance test problem for optimization algorithms. It is a typical example of non-linear multimodal function. Finding the minimum of this function is a fairly difficult problem due to its large search space and its large number of local minima.  [wiki](https://en.wikipedia.org/wiki/Rastrigin_function "Rastrigin Function Page") 


```math
f(x) = An + \sum_{i=1}^{n} \left[ x_i^2 - A \cos(2 \pi x_i) \right]

```
Where:
- $x = (x_1, x_2, \ldots, x_n)$ is the vector of decision variables.
- $n$ is the dimensionality of the problem.
- $A$ is a constant, typically 10.
- The optimal solution is at $f(x) = 0$, where $x_i = 0$ for all $i$.


| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(0,...0) = 0 | $-5.12 \leq x_i \leq 5.12 $|   | 


| Global Maxima | Boundary | Constraints |
|----------|----------|----------|
| f(±4.52299366) = 40.35329019 | $-5.12 \leq x <= 5.12 $|   | 
| f(±4.52299366,±4.52299366) = 80.70658039  | $-5.12 \leq x,y \leq 5.12 $|   | 
| f(±4.52299366, ±4.52299366,±4.52299366) = 121.0598706  | $-5.12 \leq x_i \leq 5.12 $|   | 
| ... | $-5.12 \leq x_i \leq 5.12 $|   | 

It is featured in this repository as a function with 2-dimensional inputs.



#### Rosenbrock Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/rosenbrock_plots.png" height="300" >
</p>
<p align="center">Rosenbrock Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>


The Rosenbrock function, also known as the Rosenbrock's valley or Rosenbrock's banana function, is a non-convex optimization problem that is widely used as a benchmark problem. The global minimum is inside a long, narrow, parabolic shaped flat valley. To find the valley is trivial. To converge to the global minimum, however, is difficult. [wiki](https://en.wikipedia.org/wiki/Rosenbrock_function "Rosenbrock Function Page") 

```math
f(x) = \sum_{i=1}^{n-1} \left[ 100(x_{i+1} - x_i^2)^2 + (1 - x_i)^2 \right]
```

Where:
- $x = (x_1, x_2, \ldots, x_n)$ is the vector of decision variables.
- $n$ is the dimensionality of the problem.
- In the 2-dimensional form it has a global minima at $(x,y)=(a,a^2)$, where $f(x,y)=0$


| $n$ | Global Minima | Boundary | Constraints |
|----------|----------|----------|----------|
| $n=2$ | $f(1,1)= 0$| $-\inf \leq x,y \leq \inf$ <br> $1 \leq i  \leq 2$ | 
| $n=3$ | $f(1,1,1)= 0$| $-\inf \leq x_i \leq \inf$ <br> $1 \leq i \leq 3$ | 
| $n>3$ | $f(1_1,...,1_n)= 0$| $-\inf \leq x_i \leq \inf$ <br> $1 \leq i \leq n$ | 

It is featured in this repository as a function with 2-dimensional inputs. The bounds are limited from $-2 \leq x\leq 2$, $-1 \leq y\leq 3$. 

```math
f(x) =  \left[(a-x)^2 + b(y-x^2)^2 \right]
```
In the 2-dimensional form it has a global minima at $(x,y)=(a,a^2)$, where $f(x,y)=0$. $a=1$ and $b=100$ in the default constraints.



#### Schaffer Function N.2

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/schaffer_N2_plots_1.png" height="300" >
</p>
<p align="center">Single-Objective Schaffer Function N.2 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/schaffer_N2_plots_2.png" height="300" >
</p>
<p align="center">Zoomed in Single-Objective Schaffer Function N.2 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>



There are two versions of the Schaffer Function N.2. The single-objective function has a global minimum at (0,0) with a function value of 0. It is known for its many local minima and is used to test the ability of optimization algorithms to escape local minima and find the global minimum. [SFU page](https://www.sfu.ca/~ssurjano/schaffer2.html "Schaffer N.2 function example") 

```math
f(x, y) = 0.5 + \frac{\sin^2(x^2 - y^2) - 0.5}{[1 + 0.001(x^2 + y^2)]^2}
```


| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(0,0) = 0| $-100 \leq x,y \leq 100$ |   | 



#### Schaffer Function N.4

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/schaffer_N4_plots_1.png" height="300" >
</p
<p align="center">Schaffer Function N.4 3D Projection and 2D Contour Plot, Example Global Minima Candidate in Red</p>

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/schaffer_N4_plots_2.png" height="300" >
</p>
<p align="center">Zoomed in Schaffer Function N.4 3D Projection and 2D Contour Plot, Example Global Minima Candidate in Red</p>

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/schaffer_N4_plots_2.png" height="300" >
</p>
<p align="center">Zoomed in to Center Schaffer Function N.4 3D Projection and 2D Contour Plot, Example Global Minima Candidate in Red</p>


The fourth Schaffer function has a large number local minima, and four equal global minima candidates. [SFU page](https://www.sfu.ca/~ssurjano/schaffer4.html "Schaffer N.4 function example") 

```math
   f(x, y) = 0.5 + \frac{\cos(\sin(|x^2 - y^2|)) - 0.5}{[1 + 0.001(x^2 + y^2)]^2}
```

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(0, 1.25313) = 0.292579| $-100 \leq x,y \leq 100$ |   | 
| f(0, -1.25313) = 0.292579| $-100 \leq x,y \leq 100$ |   | 
| f(1.25313,0) = 0.292579| $-100 \leq x,y \leq 100$ |   | 
| f(-1.25313,0) = 0.292579| $-100 \leq x,y \leq 100$ |   | 



#### Sphere Function 

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/sphere_plots.png" height="300" >
</p>
<p align="center">Sphere Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>


The sphere function is one of the simplest optimization test functions. It can be utilized in $n$ dimensions, where it will have $n$ local minima except for the global one. It is continuous, convex and unimodal. [SFU page](https://www.sfu.ca/~ssurjano/spheref.html "Sphere function example") 

```math
f(x) = \sum_{i=1}^{n} x_i^2
```
Where:
- $x = (x_1, x_2, \ldots, x_n)$ is the vector of decision variables.
- $n$ is the dimensionality of the problem.
- The optimal solution is at $f(x) = 0$, where $x_i = 0$ for all $i$.


| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| $f(x_1,...,x_n)= f(0,..., 0) = 0$| $-\inf\leq x_i\leq \inf$ <br> $1\leq i \leq n$ |   | 

It is featured in this repository as a function with 2-dimensional inputs. The bounds are limited from $-10<=x, y<=10$. 


```math
f(x, y) = x^2 + y^2
```

#### Styblinski–Tang Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/styblinski_tang_plots.png" height="300" >
</p>
<p align="center"> Styblinski–Tang Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>



The Styblinski–Tang function is a multi-dimensional artificial landscape used to test optimizer performance. It can be evaluated in $n$ dimensions. [SFU page](https://www.sfu.ca/~ssurjano/stybtang.html "Styblinski–Tang function example") 

```math
   f(x_1, x_2, \ldots, x_n) = \frac{1}{2} \sum_{i=1}^{n} (x_i^4 - 16x_i^2 + 5x_i)
```
Where:
- $n$ is the dimensionality of the problem.

| $n$ | Global Minima | Boundary | Constraints |
|----------|----------|----------|----------|
| 1 | f(-2.903534) = 0| $-5\leq x \leq 5$ <br> $1 \leq i \leq 1$ | $−39.16617\lt f(x) \lt 39.16617$| 
| 2 | f(-2.903534,-2.903534) = 0| $-5 \leq x,y \leq 5$ <br> $1 \leq i \leq 2$ | $−78.33234 \lt f(x) \lt 78.33234$  |
| ... | f(-2.903534, ...,-2.903534 ) = 0| $-5\leq x_i \leq 5$ <br> $1 \leq i \leq n$ | $−39.16617n \lt f(x)\lt 39.16617n$  |


It is featured in this repository as a function with 2-dimensional inputs.

```math
    f(x, y) = 0.5[(x^4 - 16x^2 + 5x) + (y^4 - 16y^2 + 5y)]
```



#### Three-hump Camel Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/three_hump_camel_plots.png" height="300" >
</p>
<p align="center"> Three-hump Camel Function 3D Projection and 2D Contour Plot, Global Minima Candidate in Red</p>


The Three-hump Camel function is a 2-dimensional artificial landscape with three local minima. [SFU page](https://www.sfu.ca/~ssurjano/camel3.html  "Three-hump Camel function example") 


```math
f(x, y) = 2x^2 - 1.05x^4 + \frac{x^6}{6} + xy + y^2
```

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| f(0,0) = 0| $-5\leq x,y \leq 5$ |   | 



### Multi-Objective Functions

#### Binh and Korn Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/binh_korn_plots.png" height="300" >
</p>
<p align="center">Binh and Korn Function Feasible Decision Space and Objective Space with Pareto Front</p>
 
This is a 2-dimensional input, multi-objective function commonly used for optimization performance evaluation. 

"Test Case 1": (T. T. Binh and U. Korn, “Scalar optimization with linear and nonlinear constraints using Evolution Strategies,” Computational Intelligence Theory and Applications, pp. 381–392, 1997. doi:10.1007/3-540-62868-1_130 ) 


"Test Case 2": (Binh T. and Korn U. (1997) MOBES: A Multiobjective Evolution Strategy for Constrained Optimization Problems)


```math
\text{minimize}: 
\begin{cases}
f(x,y) = 4x^2 + 4y^2 \\
f(x,y) = (x-5)^2 + (y-5)^2
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 2      | $0\leq x\leq 5$ <br>  $0\leq y\leq 3$ | $(x-5)^2 + y^2 \leq 25$ <br> $(x-8)^2+(y+3)^2 \geq 7.7$  | 



#### Chankong and Haimes Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/chankong_haimes_plots.png" height="300" >
</p>
<p align="center">Chankong and Haimes Feasible Decision Space and Objective Space with Pareto Front</p>

The Chankong and Haimes Function is a 2-dimensional input, multi-objective function commonly used for optimization performance evaluation. (Chankong, Vira; Haimes, Yacov Y. (1983). Multiobjective decision making. Theory and methodology. North Holland)

"Test Case 2": (T. T. Binh and U. Korn, “Scalar optimization with linear and nonlinear constraints using Evolution Strategies,” Computational Intelligence Theory and Applications, pp. 381–392, 1997. doi:10.1007/3-540-62868-1_130 ) 

"Chankong and Haimes Function": (https://en.wikipedia.org/wiki/Test_functions_for_optimization)



```math
\text{minimize}: 
\begin{cases}
f(x,y) = 2 + (x-2)^2 + (y-1)^2 \\
f(x,y) = 9x - (y - 1) ^ 2
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 2      | $-20\leq x,y\leq 20$ | $x^2 + y^2 \leq 225$ <br> $x-3y+10\leq 0$ | 




#### Constr-Ex Problem

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/constr_ex_problem_plots.png" height="300" >
</p>
<p align="center">Constr-Ex Problem Feasible Decision Space and Objective Space with Pareto Front</p>


The Constr-Ex (Constrained-Exponential) problem is a 2-dimensional mathematical optimization problem where the objective is to minimize a nonlinear objective function subject to nonlinear constraints. (Deb, Kalyanmoy (2002) Multiobjective optimization using evolutionary algorithms (Repr. ed.). Chichester: Wiley. ISBN 0-471-87339-X.)


```math
\text{minimize}: 
\begin{cases}
f(x,y) = x \\
f(x,y) = \frac{1+y}{x}
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 2      | $0\leq x\leq 1$ <br>  $0\leq y\leq 5$ | $y+9x\geq 6$ <br> $-y+9x\geq 1$  | 



#### CTP1 Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/ctp1_2_vars_plots.png" height="300" >
</p>
<p align="center">CTP1 (2 variable) Feasible Decision Space and Objective Space with Pareto Front</p>

The CTP1 (2 variable) function is a 2-dimensional input, multi-objective function commonly used for optimization performance evaluation. (Deb, Kalyanmoy (2002) Multiobjective optimization using evolutionary algorithms (Repr. ed.)) (Jimenez, F.; Gomez-Skarmeta, A. F.; Sanchez, G.; Deb, K. (May 2002). "An evolutionary algorithm for constrained multi-objective optimization". Proceedings of the 2002 Congress on Evolutionary Computation. CEC'02 (Cat. No.02TH8600). Vol. 2. pp. 1133–1138)


```math
\text{minimize}: 
\begin{cases}
f_{1}(x,y) = x \\
f_{2}(x,y) = (1+y)\exp(\frac{-x}{1+y})
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 2      | $0\leq x,y\leq 1$| $\frac{f_{2}(x,y)}{0.858exp(-0.541f_{1}(x,y))} \geq 1$ <br> $\frac{f_{2}(x,y)}{0.728exp(-0.295f_{1}(x,y))} \geq 1$  | 


**Additional Constraints**

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/ctp1_2_vars_plots_additional_constraints.png" height="300" >
</p>
<p align="center">CTP1 (2 variable) Feasible Decision Space and Objective Space with Pareto Front, with Additional Constraints Applied</p>

Additional error checking and handling were added to this function's constr_F.py script to handle FloatingPointErrors caused by under/overflow. The additions were observed to have some impact on the shape of the pareto front and Feasible Objective Space.



#### Fonseca–Fleming Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/fonseca_fleming_plots_1_var.png" height="300" >
</p>
<p align="center">Fonseca Fleming Feasible Decision Space and Objective Space with Pareto Front for 1 Variable</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/fonseca_fleming_plots_2_var.png" height="300" >
</p>
<p align="center">Fonseca Fleming Feasible Decision Space and Objective Space with Pareto Front for 2 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/fonseca_fleming_plots_3_var.png" height="300" >
</p>
<p align="center">Fonseca Fleming Feasible Decision Space and Objective Space with Pareto Front for 3 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/fonseca_fleming_plots_5_var.png" height="300" >
</p>
<p align="center">Fonseca Fleming Feasible Decision Space and Objective Space with Pareto Front for 5 Variables</p>

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/fonseca_fleming_plots_pareto_1.png.png" height="300" >
</p>
<p align="center">Fonseca Fleming Pareto Front for 1 to 5 Variables with Objective Space</p>


<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/fonseca_fleming_plots_pareto_2.png.png" height="300" >
</p>
<p align="center"> Comparison of Fonseca Fleming Pareto Front for 1 to 5 Variables</p>
 

The Fonseca–Fleming Function is a multi-dimensional input, multi-objective function commonly used for optimization performance evaluation. (Fonseca, C. M.; Fleming, P. J. (1995). "An Overview of Evolutionary Algorithms in Multiobjective Optimization". Evol Comput. 3 (1): 1–16. )


```math
\text{minimize}: 
\begin{cases}
f_{1}\mathbf(x)= 1 - \exp[\sum\limits_{i=1}^{n}(x_i-\frac{1}{\sqrt{n}})^2] \\
f_{2}\mathbf(x)= 1 + \exp[\sum\limits_{i=1}^{n}(x_i-\frac{1}{\sqrt{n}})^2]
\end{cases}
```

Where:
- $\mathbf{x} = (x_1, x_2, \ldots, x_n)$ is the vector of decision variables.
- $n$ is the dimensionality of the problem. 30 is commonly used as a maximum for this problem.
- $x_i$ represents the $i$-th element of the input vector $\mathbf{x}$.


| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 1      | $-4\leq x\leq 4$ <br> $i=1$ | | 
| 2      | $-4\leq x,y\leq 4$ <br> $1\leq i\leq 2$ | | 
| 3      | $-4\leq x,y,z\leq 4$ <br> $1\leq i\leq 3$ | | 
| 1+      | $-4\leq x_i\leq 4$ <br> $1\leq i\leq n$ | | 


In this repository, the Fonseca-Fleming Function is evaluated and shown above with 1 input, 2 input, and 3 input variations. A generalized function is included for completeness, but is not graphed. 


#### Kursawe Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/kursawe_plots_1_var.png" height="300" >
</p>
<p align="center">Kursawe Feasible Decision Space and Objective Space with Pareto Front for 1 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/kursawe_plots_2_var.png" height="300" >
</p>
<p align="center">Kursawe Feasible Decision Space and Objective Space with Pareto Front for 2 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/kursawe_plots_3_var.png" height="300" >
</p>
<p align="center">Kursawe Feasible Decision Space and Objective Space with Pareto Front for 3 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/kursawe_plots_gen.png" height="300" >
</p>
<p align="center">Kursawe Feasible Decision Space and Objective Space with Pareto Front for 1 to 6 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/kursawe_plots_pareto.png" height="300" >
</p>
<p align="center">Kursawe Pareto Front for 1 to 6 Variables</p>

The Kursawe Function is a multi-dimensional input, multi-objective function commonly used for optimization performance evaluation. (F. Kursawe, “A variant of evolution strategies for vector optimization,” in PPSN I, Vol 496 Lect Notes in Comput Sc. Springer-Verlag, 1991, pp. 193–197)

 
```math
\text{minimize}: 
\begin{cases}
f_{1}(\mathbf{x})= \sum\limits_{i=1}^{2}(-10\exp(-0.2\sqrt{x_{i}^2+x_{i+1}^2})) \\
f_{2}(\mathbf{x})= \sum\limits_{i=1}^{3}(|x_{i}|^{0.8}+5\sin{x_{i}^3})
\end{cases}
```

Where:
- $\mathbf{x} = (x_1, x_2, \ldots, x_n)$ is the vector of decision variables.
- $x_i$ represents the $i$-th element of the input vector $\mathbf{x}$.


| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 1 | $-5\leq x\leq 5$ <br> $i = 1$ | | 
| 2 | $-5\leq x\leq 5$ <br> $1\leq i\leq 2$ | | 
| 3 | $-5\leq x\leq 5$ <br> $1\leq i\leq 3$ | | 
|1+ | $-5\leq x\leq 5$ <br> $1\leq i\leq 3$ | | 


In this repository, the Kursawe Function is evaluated and shown above with 1 input, 2 input, and 3 input variations. A generalized function is included for completeness (and to retain name scheme), but the folder does not include the graphing function. 

#### Lundquist 3 Variable

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/lundquist_3var_plots.png" height="300" >
</p>
<p align="center">Lundquist 3 Variable Function Feasible Decision Space and Objective Space with Pareto Front</p>

This function is the example function used in [pso_python](https://github.com/jonathan46000/pso_python), and for consistency the other pso examples included in this project. It was created as a simple 3-variable optimization objective function that would be quick to converge. 


```math
\text{minimize}: 
\begin{cases}
f_{1}(\mathbf{x}) = (x_1-0.5)^2 + (x_2-0.1)^2 \\
f_{2}(\mathbf{x}) = (x_3-0.2)^4
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 3      | $0.21\leq x_1\leq 1$ <br> $0\leq x_2\leq 1$ <br> $0.1 \leq x_3\leq 0.5$  | $x_3\gt \frac{x_1}{2}$ or $x_3\lt 0.1$| 


#### Osyczka and Kundu Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/osyczka_kundu_6_vars_plots.png" height="300" >
</p>
<p align="center">Osyczka and Kundu Function Feasible Decision Space and Objective Space with Pareto Front for 6 Variables</p>


The Osyczka and Kundu Function is a 6-dimensional, multi-objective function commonly used for optimization performance evaluation. It has 6 constraint functions. (Osyczka, A.; Kundu, S. (1 October 1995). "A new method to solve generalized multicriteria optimization problems using the simple genetic algorithm". Structural Optimization)


```math
\text{minimize}: 
\begin{cases}
f_{1}(\mathbf{x}) = −25(x_1−2)^2−(x_2−2)^2−(x_3−1)^2−(x_4−4)^2−(x_5−1)^2−(x_6−1)^2 \\
f_{2}(\mathbf{x}) = \sum\limits_{i=1}^{6}x_{i}^2
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 6      | $0\leq x_1,x_2,x_6\leq 10$ <br> $1\leq x_3,x_5\leq 5$ <br> $0\leq x_4\leq 6$ <br> | $x_{1}+x_{2}-2\geq 0$ <br> $6- x_{1}-x_{2} \geq 0$ <br> $2-x_{2}+x_{1}\geq 0$ <br> $2 - x_{1}+3x_{2}\geq 0$ <br> $4- (x_{3}-3)^2 -x_{4}\geq 0$<br> $(x_{5}-3)^2 + x_{6} -4\geq 0$| 



#### Poloni's Two Objective Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/poloni_2_obj_plots.png" height="300" >
</p>
<p align="center">Poloni's Two Objective Function Feasible Decision Space and Objective Space with Pareto Front</p>


Poloni's Two Objective Function is a 2-dimensional, multi-objective function commonly used for optimization performance evaluation. (Poloni C (1997) Hybrid GA for multiobjective aerodynamic shape optimization. In: Winter G, Periaux J, Galan M, Cuesta P (eds) Genetic algorithms in engineering and computer science. Wiley, New York, pp 397–414)


```math
\text{minimize}: 
\begin{cases}
f(x,y) = [1+(A_{1}-B_{1}(x,y))^2 + (A_{2}-B_{2}(x,y))^2] \\
f(x,y) = (x+3)^2 + (y+1)^2
\end{cases} \\
```
```math
\text{where}: 
\begin{cases}
A_{1} = 0.5\sin(1)-2\cos(1)+\sin(2)-1.5\cos(2) \\
A_{2} = 1.5\sin(1)-\cos(1)+2\sin(2)-0.5\cos(2) \\
B_{1}(x,y) = 0.5\sin(x)-2\cos(x)+\sin(y)-1.5\cos(y)\\
B_{2}(x,y) = 1.5\sin(x)-\cos(x)+2\sin(y)-0.5\cos(y) 
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 2      | $-\pi \leq x,y\leq \pi$ |  | 



#### Schaffer Function N.1

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/schaffer_N1_plots.png" height="300" >
</p>
<p align="center">Schaffer Function N.1 Feasible Decision Space and Objective Space with Pareto Front</p>


Schaffer Function N.1 is a 1-dimensional, multi-objective function commonly used for optimization performance evaluation. (Schaffer, J. David (1984). "Multiple Objective Optimization with Vector Evaluated Genetic Algorithms". In G.J.E Grefensette; J.J. Lawrence Erlbraum (eds.). Proceedings of the First International Conference on Genetic Algorithms)



```math
\text{minimize}: 
\begin{cases}
f_{1}(x) = x^2 \\
f_{2}(x) = (x-2)^2
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 1      | $-A \leq x \leq A*$| |

\* A values of $10^5$ have been used, but higher values increase problem difficulty ([wiki](https://en.wikipedia.org/wiki/Test_functions_for_optimization "Test functions for Optimization")).



#### Schaffer Function N.2

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/multi_schaffer_N2_plots.png" height="300" >
</p>
<p align="center">Multi-Objective Schaffer Function N.2 Feasible Decision Space and Objective Space with Pareto Front</p>

There are two versions of the Schaffer Function N.2. The multi-objective Schaffer Function N.2 is a 1-dimensional function commonly used for optimization performance evaluation. (Schaffer, J. David (1984). "Multiple Objective Optimization with Vector Evaluated Genetic Algorithms". In G.J.E Grefensette; J.J. Lawrence Erlbraum (eds.). Proceedings of the First International Conference on Genetic Algorithms)


```math
\text{minimize}: 
\begin{cases}
f_{1}(x) = \begin{cases} 
-x,   \text{if   } x \leq 1 \\
x-2,  \text{if   } 1 \lt x \leq 3 \\
4-x,  \text{if   } 3 \lt x \leq 4 \\
x-4,  \text{if   } x \gt 4
\end{cases}\\
f_{2}(x) = (x-5)^2
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 1      | $-5\leq x\leq 10$|   | 



#### Test Function 4

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/test_function_4_plots.png" height="300" >
</p>
<p align="center">(ZDB) Test Function 4 Feasible Decision Space and Objective Space with Pareto Front</p>

Test Function 4/Test Case 4 is a 2-dimensional, multi-objective function commonly used for optimization performance evaluation. 

"Test Function 4": (https://en.wikipedia.org/wiki/Test_functions_for_optimization#cite_note-Binh99-6)

"Test Case 4": (Binh T. (1999) A multiobjective evolutionary algorithm. The study cases. Technical report. Institute for Automation and Communication. Barleben, Germany)


```math
\text{minimize}: 
\begin{cases}
f(x,y) = x^2 - y \\
f(x,y) = -0.5x - y - 1
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 2      | $-7 \leq x,y \leq 4$ | $6.5 - \frac{x}{6} - y \geq 0$ <br> $7.5-0.5x-y \geq 0$ <br> $30-5x-y \geq 0$  | 



#### Viennet Function

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/viennet_plots.png" height="300" >
</p>
<p align="center">Viennet Function Feasible Decision Space and Objective Space with Pareto Front for 3 Variables</p>


The Viennet Function is a 2-dimensional, 3-objective function commonly used for optimization performance evaluation. (Viennet R, Fonteix C, Marc I (1996) Multicriteria optimization using a genetic algorithm for determining a Pareto set. Intl J Syst Sci
27(2):255–260)


```math
\text{minimize}: 
\begin{cases}
f_{1}(x,y) = 0.5(x^2+y^2)+\sin(x^2+y^2) \\
f_{2}(x,y) = \frac{(3x-2y+4)^2}{8} + \frac{(x-y+1)^2}{27} + 15\\
f_{3}(x,y) = \frac{1}{x^2+y^2+1} - 1.1\exp(-(x^2+y^2))
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 2      | $-3\leq x,y\leq 3$|    | 


**Additional Constraints**

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/viennet_plots_additional_constraints.png" height="300" >
</p>
<p align="center">Viennet Feasible Decision Space and Objective Space with Pareto Front, with Additional Constraints Applied</p>

Additional error checking and handling were added to this function's constr_F.py script to handle FloatingPointErrors caused by under/overflow. This additions were not observed to change the results of the Decision Space, Objective Space, or Pareto front.



#### Zitzler–Deb–Thiele's Function N.1

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N1_plots_1_var.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.1 Feasible Decision Space and Objective Space with Pareto Front for 1 Variable</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N1_plots_2_var.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.1 Feasible Decision Space and Objective Space with Pareto Front for 2 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N1_plots_3_var.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.1 Feasible Decision Space and Objective Space with Pareto Front for 3 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N1_plots_gen.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.1 Feasible Decision Space and Objective Space with Pareto Front for 1 to 6 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N1_plots_pareto.png" height="300" >
</p>
<p align="center">Zitzler–Deb–Thiele's Function N.1 Pareto Front for 1 to 6 Variables (All Perfectly Overlapped)</p>

Zitzler–Deb–Thiele's Function N.1 is a multi-dimensional, 2-objective function commonly used for optimization performance evaluation. (Viennet R, Fonteix C, Marc I (1996) Multicriteria optimization using a genetic algorithm for determining a Pareto set. Intl J Syst Sci
27(2):255–260)



```math
\text{minimize}: 
\begin{cases}
f_{1}\mathbf(x) = x_1 \\
f_{2}\mathbf(x) = g\mathbf(x)h(f_{1}\mathbf(x), g\mathbf(x))\\
g\mathbf(x) = 1 + \frac{9}{n-1}\sum\limits_{i=2}^{n}x_{i}\\
h(f_{1}\mathbf(x), g\mathbf(x)) = 1- \sqrt{\frac{f_{1}\mathbf(x)}{g\mathbf(x)}}
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 1   | $0\leq x\leq 1$ <br> $1\leq i \leq 30$ |  | 
| 3   | $0\leq x,y\leq 1$ <br>  $1\leq i \leq 30$ |  | 
| 2   | $0\leq x,y,z\leq 1$ <br>  $1\leq i \leq 30$ |  | 
| 1-30| $0\leq x\leq 1$ <br>  $1\leq i \leq 30$ |  | 
 
In this repository, Zitzler–Deb–Thiele's Function N.1 is evaluated and shown above with 1 input, 2 input, and 3 input variations. A generalized function is included for completeness (and to retain name scheme), but the folder does not include the graphing function. 

**Additional Constraints**

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/ZDT_N1_2var_output_additional_constraints.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.1 Feasible Decision Space and Objective Space with Pareto Front for 2 Variables, with Additional Constraints Applied</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/ZDT_N1_3var_output_additional_constraints.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.1 Feasible Decision Space and Objective Space with Pareto Front for 3 Variables, with Additional Constraints Applied</p>

Additional error checking and handling were added to this function's constr_F.py script to handle FloatingPointErrors caused by under/overflow. This additions were not observed to change the results of the Decision Space, Objective Space, or Pareto front. It did not need to be applied to the 1-variable function.


#### Zitzler–Deb–Thiele's Function N.2

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N2_plots_1_var.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.2 Feasible Decision Space and Objective Space with Pareto Front for 1 Variable</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N2_plots_2_var.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.2 Feasible Decision Space and Objective Space with Pareto Front for 2 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N2_plots_3_var.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.2 Feasible Decision Space and Objective Space with Pareto Front for 3 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N2_plots_gen.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.2 Feasible Decision Space and Objective Space with Pareto Front for 1 to 6 Variables</p>

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N2_plots_pareto.png" height="300" >
</p>
<p align="center">Zitzler–Deb–Thiele's Function N.2 Pareto Front for 1 to 6 Variables (All Perfectly Overlapped)</p>


Zitzler–Deb–Thiele's Function N.2 is a multi-dimensional, 2-objective function commonly used for optimization performance evaluation. (Viennet R, Fonteix C, Marc I (1996) Multicriteria optimization using a genetic algorithm for determining a Pareto set. Intl J Syst Sci
27(2):255–260)


```math
\text{minimize}: 
\begin{cases}
f_{1}\mathbf(x) = x_1 \\
f_{2}\mathbf(x) = g\mathbf(x)h(f_{1}\mathbf(x), g\mathbf(x))\\
g\mathbf(x) = 1 + \frac{9}{n-1}\sum\limits_{i=2}^{n}x_{i}\\
h(f_{1}\mathbf(x), g\mathbf(x)) = 1- (\frac{f_{1}\mathbf(x)}{g\mathbf(x)})^2
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 1   | $0\leq x\leq 1$ <br> $1\leq i \leq 30$ |  | 
| 3   | $0\leq x,y\leq 1$ <br>  $1\leq i \leq 30$ |  | 
| 2   | $0\leq x,y,z\leq 1$ <br>  $1\leq i \leq 30$ |  | 
| 1-30| $0\leq x\leq 1$ <br>  $1\leq i \leq 30$ |  | 
 
In this repository, Zitzler–Deb–Thiele's Function N.2 is evaluated and shown above with 1 input, 2 input, and 3 input variations. A generalized function is included for completeness (and to retain name scheme), but the folder does not include the graphing function. 



#### Zitzler–Deb–Thiele's Function N.3

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N3_plots_1_var.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.3 Feasible Decision Space and Objective Space with Pareto Front for 1 Variable</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N3_plots_2_var.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.3 Feasible Decision Space and Objective Space with Pareto Front for 2 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N3_plots_3_var.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.3 Feasible Decision Space and Objective Space with Pareto Front for 3 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N3_plots_gen.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.3 Feasible Decision Space and Objective Space with Pareto Front for 1 to 6 Variables</p>
 <p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N3_plots_pareto.png" height="300" >
</p>
<p align="center">Zitzler–Deb–Thiele's Function N.3 Pareto Front for 1 to 6 Variables (All Perfectly Overlapped)</p>



Zitzler–Deb–Thiele's Function N.3 is a multi-dimensional, 2-objective function commonly used for optimization performance evaluation. (Viennet R, Fonteix C, Marc I (1996) Multicriteria optimization using a genetic algorithm for determining a Pareto set. Intl J Syst Sci
27(2):255–260)


```math
\text{minimize}: 
\begin{cases}
f_{1}\mathbf(x) = x_1 \\
f_{2}\mathbf(x) = g\mathbf(x)h(f_{1}\mathbf(x), g\mathbf(x))\\
g\mathbf(x) = 1 + \frac{9}{n-1}\sum\limits_{i=2}^{n}x_{i}\\
h(f_{1}\mathbf(x), g\mathbf(x)) = 1- \sqrt{\frac{f_{1}\mathbf(x)}{g\mathbf(x)}} - (\frac{f_{1}\mathbf(x)}{g\mathbf(x)})\sin(10\pi f_{1}\mathbf(x))
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 1   | $0\leq x\leq 1$ <br> $1\leq i \leq 30$ |  | 
| 3   | $0\leq x,y\leq 1$ <br>  $1\leq i \leq 30$ |  | 
| 2   | $0\leq x,y,z\leq 1$ <br>  $1\leq i \leq 30$ |  | 
| 1-30| $0\leq x\leq 1$ <br>  $1\leq i \leq 30$ |  | 
 
In this repository, Zitzler–Deb–Thiele's Function N.3 is evaluated and shown above with 1 input, 2 input, and 3 input variations. A generalized function is included for completeness (and to retain name scheme), but the folder does not include the graphing function. 



**Additional Constraints**

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/ZDT_N3_1var_output_additional_constraints.png" height="300" >
</p>
<p align="center">Zitzler–Deb–Thiele's Function N.3 Feasible Decision Space and Objective Space with Pareto Front for 1 Variable, with Additional Constraints Applied</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/ZDT_N3_2var_output_additional_constraints.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.3 Feasible Decision Space and Objective Space with Pareto Front for 2 Variables, with Additional Constraints Applied</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/ZDT_N3_3var_output_additional_constraints.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.3 Feasible Decision Space and Objective Space with Pareto Front for 3 Variables, with Additional Constraints Applied</p>

Additional error checking and handling were added to this function's constr_F.py script to handle FloatingPointErrors caused by under/overflow. This additions were not observed to change the results of the Decision Space, Objective Space, or Pareto front. 



#### Zitzler–Deb–Thiele's Function N.4

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N4_plots_2_var.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.4 Feasible Decision Space and Objective Space with Pareto Front for 2 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N4_plots_3_var.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.4 Feasible Decision Space and Objective Space with Pareto Front for 3 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N4_plots_gen.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.4 Feasible Decision Space and Objective Space with Pareto Front for 2 to 7 Variables</p>

 <p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N4_plots_pareto.png" height="300" >
</p>
<p align="center">Zitzler–Deb–Thiele's Function N.3 Pareto Front for 2 to 7 Variables (All Perfectly Overlapped)</p>




Zitzler–Deb–Thiele's Function N.4 is a multi-dimensional, 2-objective function commonly used for optimization performance evaluation. (Viennet R, Fonteix C, Marc I (1996) Multicriteria optimization using a genetic algorithm for determining a Pareto set. Intl J Syst Sci
27(2):255–260)


```math
\text{minimize}: 
\begin{cases}
f_{1}\mathbf(x) = x_1 \\
f_{2}\mathbf(x) = g\mathbf(x)h(f_{1}\mathbf(x), g\mathbf(x))\\
g\mathbf(x) = 1 + 10*(n-1) + \sum\limits_{i=2}^{n}x_{i}^2-10\cos(4\pi x_{i})\\
h(f_{1}\mathbf(x), g\mathbf(x)) = 1- \sqrt{\frac{f_{1}\mathbf(x)}{g\mathbf(x)}} 
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 2   | $0\leq x_1\leq 1$ <br> $-5\leq x_i\leq 5$ <br> $2\leq i \leq 10$ |  | 
| 3   | $0\leq x_1\leq 1$ <br> $-5\leq x_i\leq 5$ <br> $2\leq i \leq 10$ |  | 
| 2-10| $0\leq x_1\leq 1$ <br> $-5\leq x_i\leq 5$ <br> $2\leq i \leq 10$ |  | 

In this repository, Zitzler–Deb–Thiele's Function N.4 is evaluated and shown above with 2 input and 3 input variations. A generalized function is included for completeness (and to retain name scheme), but the folder does not include the graphing function. 



#### Zitzler–Deb–Thiele's Function N.6

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N6_plots_1_var.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.6 Feasible Decision Space and Objective Space with Pareto Front for 1 Variable</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N6_plots_2_var.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.6 Feasible Decision Space and Objective Space with Pareto Front for 2 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N6_plots_3_var.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.6 Feasible Decision Space and Objective Space with Pareto Front for 3 Variables</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N6_plots_gen.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.6 Feasible Decision Space and Objective Space with Pareto Front for 1 to 6 Variables</p>

  <p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/zitzler_deb_thiele_N6_plots_pareto.png" height="300" >
</p>
<p align="center">Zitzler–Deb–Thiele's Function N.6 Pareto Front for 1 to 6 Variables (All Perfectly Overlapped)</p>



Zitzler–Deb–Thiele's Function N.6 is a 2-dimensional, 2-objective function commonly used for optimization performance evaluation. (Viennet R, Fonteix C, Marc I (1996) Multicriteria optimization using a genetic algorithm for determining a Pareto set. Intl J Syst Sci
27(2):255–260)



```math
\text{minimize}: 
\begin{cases}
f_{1}\mathbf(x) = 1-\exp(-4x_{1})\sin^{6}(6\pi x_1) \\
f_{2}\mathbf(x) = g\mathbf(x)h(f_{1}\mathbf(x), g\mathbf(x))\\
g\mathbf(x) = 1 + 9\frac{\sum\limits_{i=2}^{n}x_{i}}{n-1}\\
h(f_{1}\mathbf(x), g\mathbf(x)) = 1- (\frac{f_{1}\mathbf(x)}{g\mathbf(x)})^2
\end{cases}
```

| Num. Input Variables| Boundary | Constraints |
|----------|----------|----------|
| 1   | $0\leq x\leq 1$ <br> $1\leq i \leq 10$ |  | 
| 3   | $0\leq x,y\leq 1$ <br>  $1\leq i \leq 10$ |  | 
| 2   | $0\leq x,y,z\leq 1$ <br>  $1\leq i \leq 10$ |  | 
| 1-10| $0\leq x\leq 1$ <br>  $1\leq i \leq 10$ |  | 
 
In this repository, Zitzler–Deb–Thiele's Function N.6 is evaluated and shown above with 1 input, 2 input, and 3 input variations. A generalized function is included for completeness (and to retain name scheme), but the folder does not include the graphing function. 


**Additional Constraints**

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/ZDT_N6_2var_output_additional_constraints.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.6 Feasible Decision Space and Objective Space with Pareto Front for 2 Variables, with Additional Constraints Applied</p>
<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/ZDT_N6_3var_output_additional_constraints.png" height="300" >
</p>
 <p align="center">Zitzler–Deb–Thiele's Function N.6 Feasible Decision Space and Objective Space with Pareto Front for 3 Variables, with Additional Constraints Applied</p>

Additional error checking and handling were added to this function's constr_F.py script to handle FloatingPointErrors caused by under/overflow. This additions were not observed to change the results of the Decision Space, Objective Space, or Pareto front. 



### Constrained Objective Funtions

#### Rosenbrock Function Constrained to Disk

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/rosenbrock_disk_plots.png" height="300" >
</p>


This takes the 2-dimensional Rosenbrock function described above, and adds constraints. In this example, a limit is set such that any point $f(x,y) > 2$ is invalid. 

```math
f(x, y) =  \left[(a-x)^2 + b(y-x^2)^2 \right]

```

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| $f(1,1)= 0$| $-1.5\leq x,y\leq 1.5$ | $x^2 + y^2 \leq 2$ | 

#### Rosenbrock Function Constrained with a Cubic and a Line

---

<p align="center">
 <img src="https://github.com/LC-Linkous/objective_function_suite/blob/main/imgs/rosenbrock_cubic_and_line_plots.png" height="300" >
</p>


This takes the 2-dimensional Rosenbrock function described above, and adds constraints. In this example, the valid state space is constrained with a cubic ($(x-1)^3-y \leq 0$), and a line ($x+y-2 \leq 0$). 

```math
f(x, y) =  \left[(a-x)^2 + b(y-x^2)^2 \right]

```

| Global Minima | Boundary | Constraints |
|----------|----------|----------|
| $f(1,1)= 0$| $-1.5\leq x\leq 1.5$ <br> $-0.5\leq y\leq 2.5$ | $(x-1)^3-y \leq 0$ <br> $x+y-2\leq 0$ | 

## AntennaCAT Objective Function Set
This section contains functions created for testing specific edge cases with the optimizers integrated with AntennaCAT. These functions are not attributed to any particular author and do not come from any particular literature. Additional functions will be added as they are included in the benchmarking process.




## Function Summary

CLEANUP IN PROGRESS

### Single-Objective Function Summary

|Function | Directory Name| Num. Objective Functions | Num. Inputs | Example Boundaries | Constraints | Num. Global Minima |
|----------|----------|----------|----------|----------|----------|----------|
| Ackley Function          | ackley            | 1 | 2 | $-5\leq x,y \leq 5$                          |                       | 1 |
| Beale Function           | beale             | 1 | 2 | $-4.5\leq x,y \leq 4.5$                      |                       | 1 |
| Booth Function           | booth             | 1 | 2 | $-10\leq x,y \leq 10$                        |                       | 1 |
| Branin Function          | branin            | 1 | 2 | $-5\leq x\leq 10$ <br> $0\leq y\leq 15$      |                       | 1 |
| Bukin Function N.6       | bukin_N6          | 1 | 2 | $-15\leq x\leq -5$ <br> $-3\leq y \leq 3$    |                       | 1 |
| Cross-in-Tray Function   | cross_in_tray     | 1 | 2 | $-10\leq x,y \leq 10$                        |                       | 4 |
| Easom Function           | easom             | 1 | 2 | $-50\leq x,y \leq 50$                        |                       | 1 |
| Eggholder Function       | eggholder         | 1 | 2 | $-515\leq x,y \leq 515$                      |                       | 1 |
| Goldstein-Price Function | goldstein_price   | 1 | 2 | $-2\leq x,y \leq 2$                          |                       | 1 |
| Himmelblau's Function    | himelblau         | 1 | 2 | $-5\leq x,y \leq 5$                          |                       | 4 |
| Hölder Table Function    | holder_table      | 1 | 2 | $-10\leq x,y \leq 10$                        |                       | 4 |
| Lévi Function N.13       | levi_N13          | 1 | 2 | $-10\leq x,y \leq 10$                        |                       | 1 |
| Matyas Function          | matyas            | 1 | 2 | $-10\leq x,y \leq 10$                        |                       | 1 |
| McCormick Function       | mccormick         | 1 | 2 | $-1.5\leq x \leq 4$ <br> $-3 \leq y \leq 4$  |                       | 1 |
| Michalewicz Function     | michalewicz       | 1 | 2 | $0\leq x_i \leq \pi $                        |                       | 1 |
| Rastrigin Function       | rastrigin         | 1 | 2 | $-5.12\leq x,y \leq 5.12$                    |                       | 4 |
| Rosenbrock Function      | rosenbrock        | 1 | 2 | $-2\leq x \leq 2$ <br> $-1 \leq y \leq 3$    |                       | 1 |
| Schaffer Function N.2    | schaffer_N2       | 1 | 2 | $-100\leq x,y \leq 100$                      |                       | 1 |
| Schaffer Function N.4    | schaffer_N4       | 1 | 2 | $-100\leq x,y \leq 100$                      |                       | 4 |
| Sphere Function          | sphere            | 1 | 2 | $-10\leq x,y \leq 10$                        |                       | 1 |
| Styblinski Tang Function | styblinski_tang   | 1 | 2 | $-5\leq x,y \leq 5$                          |$-78\lt f(x,y)\lt 78$  | 1 |
| Three-hump Camel Function| three_hump_camel  | 1 | 2 | $-5\leq x,y \leq 5$                          |                       | 1 |

### Multi-Objective Function Summary

|Function | Directory Name| Num. Objective Functions | Num. Inputs | Example Boundaries | Constraints |
|----------|----------|----------|----------|----------|----------|
| Binh and Korn Function           | binh_korn                    | 2 | 2   |$0\leq x\leq 5$ <br> $0\leq y\leq 3$      |   yes   |
| Chankong and Haimes Function     | chankong_haimes              | 2 | 2   |$-20\leq x,y\leq 20$                      |   yes   |
| Constr-Ex Problem                | constr_ex_problem            | 2 | 2   |$0.1\leq x\leq 1$ <br> $0\leq y\leq 5$    |   yes   |
| CTP1 Function                    | ctp1_2_vars                  | 2 | 2   |$0\leq x,y\leq 1$                         |   yes   |
| Fonseca–Fleming Function         | fonseca_fleming_1_var        | 2 | 1   |$-4\leq x\leq 4$                          |         |
| Fonseca–Fleming Function         | fonseca_fleming_2_var        | 2 | 2   |$-4\leq x,y\leq 4$                        |         |
| Fonseca–Fleming Function         | fonseca_fleming_3_var        | 2 | 3   |$-4\leq x,y,z\leq 4$                      |         |
| Fonseca–Fleming Function         | fonseca_fleming_gen          | 2 |1-4+ |$-4\leq x, ...\leq 4$                     |         |
| Kursawe Function                 | kursawe_1_var                | 2 | 1   |$-5\leq x\leq 5$                          |         |
| Kursawe Function                 | kursawe_2_var                | 2 | 2   |$-5\leq x,y\leq 5$                        |         |
| Kursawe Function                 | kursawe_3_var                | 2 | 3   |$-5\leq x,y,z\leq 5$                      |         |
| Kursawe Function                 | kursawe_gen                  | 2 |1-3+ |$-5\leq x,...\leq 5$                      |         |
| Osyczka and Kundu Function       | osyczka_kundu_6_vars         | 6 | 2   | $0\leq x_1,x_2,x_6\leq 10$ <br> $1\leq x_3,x_5\leq 5$ <br> $0\leq x_4\leq 6$|   yes   |
| Poloni's Two Objective Function  | poloni_2_obj                 | 2 | 2   | $-\pi\leq x,y \leq \pi$                  |         |
| Schaffer Function N.1            | schaffer_N1                  | 2 | 1   | $-10^5\leq x\leq 10^5$                   |         |
| Schaffer Function N.2            | schaffer_N2                  | 2 | 1   | $-5\leq x \leq 10$                       |         |
| Test Function 4                  | test_function_4              | 2 | 2   | $-7\leq x,y \leq 4$                      |   yes   |
| Viennet Function                 | viennet                      | 3 | 2   | $-3\leq x,y \leq 3$                      |         |
| Zitzler–Deb–Thiele's function N.1| ZDT_N1_1_var  | 2 | 1   | $-0\leq x \leq 1$                        |         |
| Zitzler–Deb–Thiele's function N.1| ZDT_N1_2_var  | 2 | 2   | $-0\leq x,y \leq 1$                      |         |
| Zitzler–Deb–Thiele's function N.1| ZDT_N1_3_var  | 2 | 3   | $-0\leq x,y,z \leq 1$                    |         |
| Zitzler–Deb–Thiele's function N.1| ZDT_N1_gen    | 2 |1-30+| $-0\leq x... \leq 1$                     |         |
| Zitzler–Deb–Thiele's function N.2| ZDT_N2_1_var  | 2 | 1   | $-0\leq x \leq 1$                        |         |
| Zitzler–Deb–Thiele's function N.2| ZDT_N2_2_var  | 2 | 2   | $-0\leq x,y \leq 1$                      |         |
| Zitzler–Deb–Thiele's function N.2| ZDT_N2_3_var  | 2 | 3   | $-0\leq x,y,z \leq 1$                    |         |
| Zitzler–Deb–Thiele's function N.2| ZDT_N2_gen    | 2 |1-30+| $-0\leq x,... \leq 1$                    |         |
| Zitzler–Deb–Thiele's function N.3| ZDT_N3_1_var  | 2 | 1   | $-0\leq x \leq 1$                        |         |
| Zitzler–Deb–Thiele's function N.3| ZDT_N3_2_var  | 2 | 2   | $-0\leq x,y \leq 1$                      |         |
| Zitzler–Deb–Thiele's function N.3| ZDT_N3_3_var  | 2 | 3   | $-0\leq x,y,z \leq 1$                    |         |
| Zitzler–Deb–Thiele's function N.3| ZDT_N3_gen    | 2 |1-30+| $-0\leq x,... \leq 1$                    |         |
| Zitzler–Deb–Thiele's function N.4| ZDT_N4_2_var  | 2 | 2   | $0\leq x_1\leq 1$ <br> $-5\leq x_i\leq 5$|         |
| Zitzler–Deb–Thiele's function N.4| ZDT_N4_3_var  | 2 | 3   | $0\leq x_1\leq 1$ <br> $-5\leq x_i\leq 5$|         |
| Zitzler–Deb–Thiele's function N.4| ZDT_N4_gen    | 2 |2-10+| $0\leq x_1\leq 1$ <br> $-5\leq x_i\leq 5$|         |
| Zitzler–Deb–Thiele's function N.6| ZDT_N6_1_var  | 2 | 1   | $0\leq x \leq 1$                         |         |
| Zitzler–Deb–Thiele's function N.6| ZDT_N6_2_var  | 2 | 2   | $0\leq x \leq 1$                         |         |
| Zitzler–Deb–Thiele's function N.6| ZDT_N6_3_var  | 2 | 3   | $0\leq x \leq 1$                         |         |
| Zitzler–Deb–Thiele's function N.6| ZDT_N6_gen    | 2 |1-10+| $0\leq x \leq 1$                         |         |



# Future Development

This repository is an archive of objective functions used to test and debug the AntennaCAT software suite, and to train the machine learning models related to the optimization process. It will be updated as functions are added in testing, related repositories, or in related literature.


# References 

[1] “Test functions for optimization,” Wikipedia, https://en.wikipedia.org/wiki/Test_functions_for_optimization (accessed Mar. 31, 2024). 

[2] D. Bingham, “Virtual Library of Simulation Experiments,” Optimization Test Functions and Datasets, https://www.sfu.ca/~ssurjano/optimization.html (accessed Mar. 31, 2024). 

[3] C. M. Fonseca and P. J. Fleming, “An overview of evolutionary algorithms in multiobjective optimization,” Evolutionary Computation, vol. 3, no. 1, pp. 1–16, Mar. 1995. doi:10.1162/evco.1995.3.1.1 

[4] B. Y. Qu, J. J. Liang, Z. Y. Wang, Q. Chen, and P. N. Suganthan, “Novel benchmark functions for continuous multimodal optimization with comparative results,” Swarm and Evolutionary Computation, vol. 26, pp. 23–34, 2016. doi:10.1016/j.swevo.2015.07.003 

[5] K. Deb, L. Thiele, M. Laumanns, and Eckart Zitzler, “Scalable Test Problems for Evolutionary Multiobjective Optimization,” Springer eBooks, pp. 105–145, Jan. 2005, doi: https://doi.org/10.1007/1-84628-137-7_6.

[6] D. Bingham, “Virtual Library of Simulation Experiments,” Optimization Test Functions and Datasets, https://www.sfu.ca/~ssurjano/optimization.html (accessed Mar. 31, 2024).

[7] T. T. Binh and U. Korn, “Scalar optimization with linear and Nonlinear Constraints using Evolution Strategies,” Lecture notes in computer science, pp. 381–392, Jan. 1997, doi: https://doi.org/10.1007/3-540-62868-1_130.

[8] E. Zitzler, K. Deb, and L. Thiele, “Comparison of Multiobjective Evolutionary Algorithms: Empirical Results,” Evolutionary Computation, vol. 8, no. 2, pp. 173–195, Jun. 2000, doi: https://doi.org/10.1162/106365600568202.

[9] C. M. Fonseca and P. J. Fleming, “An overview of evolutionary algorithms in multiobjective optimization,” Evolutionary Computation, vol. 3, no. 1, pp. 1–16, Mar. 1995. doi:10.1162/evco.1995.3.1.1

[10] M. Jamil and X. S. Yang, “A literature survey of benchmark functions for global optimisation problems,” International Journal of Mathematical Modelling and Numerical Optimisation, vol. 4, no. 2, p. 150, 2013, doi: https://doi.org/10.1504/ijmmno.2013.055204.



Specific reference links:
* https://infinity77.net/global_optimization/test_functions.html#test-functions-index 


* https://www.sfu.ca/~ssurjano/beale.html 
* https://www.sfu.ca/~ssurjano/booth.html
* https://www.sfu.ca/~ssurjano/branin.html
* https://www.sfu.ca/~ssurjano/bukin6.html
* https://www.sfu.ca/~ssurjano/crossit.html
* https://www.sfu.ca/~ssurjano/easom.html
* https://www.sfu.ca/~ssurjano/egg.html
* https://www.sfu.ca/~ssurjano/goldpr.html
* https://www.sfu.ca/~ssurjano/griewank.html
* https://www.sfu.ca/~ssurjano/holder.html
* https://www.sfu.ca/~ssurjano/levy13.html
* https://www.sfu.ca/~ssurjano/matya.html
* https://www.sfu.ca/~ssurjano/mccorm.html
* https://www.sfu.ca/~ssurjano/michal.html
* https://www.sfu.ca/~ssurjano/schaffer2.html
* https://www.sfu.ca/~ssurjano/schaffer4.html
* https://www.sfu.ca/~ssurjano/schwef.html
* https://www.sfu.ca/~ssurjano/spheref.html
* https://www.sfu.ca/~ssurjano/stybtang.html
* https://www.sfu.ca/~ssurjano/camel3.html
 


* https://en.wikipedia.org/wiki/Test_functions_for_optimization 
* https://en.wikipedia.org/wiki/Ackley_function
* https://en.wikipedia.org/wiki/Himmelblau%27s_function


* https://silvahansini.medium.com/optimization-of-the-booth-function-with-differential-evaluation-6a60a74a513c



# Related Publications
First mention of objective function testing:

L. Linkous, J. Lundquist, M. Suche and E. Topsakal, "Machine Learning Assisted Hyperparameter Tuning for Optimization," 2024 IEEE INC-USNC-URSI Radio Science Meeting (Joint with AP-S Symposium), Florence, Italy, 2024, pp. 107-108, doi: 10.23919/INC-USNC-URSI61303.2024.10632482.


Other Publications:

L. Linkous and E. Topsakal, "Machine Learning Assisted Optimization Methods for Automated Antenna Design," 2024 United States National Committee of URSI National Radio Science Meeting (USNC-URSI NRSM), Boulder, CO, USA, 2024, pp. 377-378, doi: 10.23919/USNC-URSINRSM60317.2024.10464597.

L. Linkous, J. Lundquist and E. Topsakal, "AntennaCAT: Automated Antenna Design and Tuning Tool," 2023 IEEE USNC-URSI Radio Science Meeting (Joint with AP-S Symposium), Portland, OR, USA, 2023, pp. 89-90, doi: 10.23919/USNC-URSI54200.2023.10289238.

L. Linkous, E. Karincic, J. Lundquist and E. Topsakal, "Automated Antenna Calculation, Design and Tuning Tool for HFSS," 2023 United States National Committee of URSI National Radio Science Meeting (USNC-URSI NRSM), Boulder, CO, USA, 2023, pp. 229-230, doi: 10.23919/USNC-URSINRSM57470.2023.10043119.



# Related Repositories



# To Cite

If citing a specific objective function, please site the originating literature (or website) for that objective function. Those sources will have more detailed information on the use, conditions, and limits of those objective functions. 

To cite this repository, or the AntennaCAT function set, please use the following:

L. Linkous, J. Lundquist, M. Suche and E. Topsakal, "Machine Learning Assisted Hyperparameter Tuning for Optimization," 2024 IEEE INC-USNC-URSI Radio Science Meeting (Joint with AP-S Symposium), Florence, Italy, 2024, pp. 107-108, doi: 10.23919/INC-USNC-URSI61303.2024.10632482.