# Generating a Random Scatter Plot with Altair 
 
## Objective 
The aim of this function is to create a random scatter plot using Altair, a Python library for declarative visualization. The scatter plot is then displayed in the default web browser. 
 
## Inputs 
This function does not take any inputs. 
 
## Flow 
The following is the flow of operations followed by the function: 
1. Random data points are generated using NumPy library. 
2. The data points are then converted into a Pandas DataFrame. 
3. Altair library is utilized to create a scatter plot with the generated data. 
4. The scatter plot is displayed in the default browser. 
 
## Outputs 
The main output of the function is a scatter plot created using Altair library. 
 
## Additional aspects 
The implementation of this function involves the usage of the following libraries and methods: 
- NumPy and Pandas libraries for generating and manipulating data. 
- A list of two colors from which a random color is chosen for each data point in the scatter plot. 
- Seed is set for NumPy's random number generator to ensure reproducibility. 