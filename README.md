# FunctionFinderGenetic
Genetic program to approximate a function given a set of X and Y values

![Function Finder Learning Curve](plots/learning_curve_02-01-2019_07-28-40-PM.png)

## Overview
This project was an assignment for an algorithms course at Eastern Kentucky University, Spring 2019.

The assignment was to create a genetic program that could approximate a mathematical function given a list of
independent variables and their values and dependent values. The particular values are the following;

Independent variables:
```
X: [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
```

Dependent values:
```
0.0
0.005
0.020
0.045
0.080
0.125
0.180
0.245
0.320
0.405
```

Equations are stored in a tree data structure.

## Running
The program was run multiple times using various population sizes, generations, etc. The parameters used for
submission are included in the `values.json` file. These include a population of `1000` and a max of `100` generations.

For the set of terminal symbols (tree leaves), the set of integers from -5 to 5 inclusive were used. For functions
(internal tree nodes), the set of addition subtraction, multiplication, and division functions was used. The design of
the program allows for new functions (of any number of parameters) to be added easily.

The probability of whether a terminal symbol or function will be selected when growing a tree and the max height a tree
can get can be altered in the `values.json` file.

## Results
After running the program multiple times and getting the best chromosome and error of each, 


