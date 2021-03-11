import numpy as np
import time
import matplotlib.pyplot as plt

def function_to_relax(x, c=2):
    return 1-np.exp(-1*c*x)

def relaxation(start_guess=1, func_to_relax=None,
               func_keyword_args=None, tolerance=1e-6):
    """Function that computes the root via the fixed point
    (relaxation) method. inputs are a starting guess,
    a function to use, any function arguments, and a tolerance
    to exit the function when successive approximations are
    less than this value"""
    #FILL THIS IN
    old_guess = 0
    while abs(start_guess - old_guess) > tolerance:
        old_guess = start_guess
        start_guess = func_to_relax(start_guess, func_keyword_args['c'])
        #print(start_guess)
    return start_guess

if __name__ == "__main__":
    print("""a. Write a program to solve this equation
            for x using the relaxation method for the case c = 2.
            Calculate your solution to an accuracy of six decimal places.
            (3 pts)""")
    print("The solution for part a is:")
    print(relaxation(func_to_relax=function_to_relax,
                     func_keyword_args={'c':2}))
        

    print("""b) Modify your program to calculate the solution for values
        of R0 from 0 to 5 in steps of 0.01 and make a plot of P as a
        function of R0. Save this plot as a png file as an output to
        your program, with properly labeled axes and titles and such.
        You should see a clear transition from a regime in which P = 0
        to a regime of nonzero P. This is another example of a phase
        transition. In physics this transition is known as the percolation
        transition; in epidemiology it is the epidemic threshold.  (7 pts)""")

    #loop over r0 values from 0 to 5
    r0_values = np.arange(0, 5.0, 0.001)
    solutions = []
    for r0 in r0_values:
        answer = relaxation(func_to_relax=function_to_relax,
                            func_keyword_args={'c':r0}, start_guess=30)
        solutions.append(answer)
       
    plt.plot(r0_values, solutions)
    #plt.yscale('log')
    #plt.xscale('log')
    plt.title('Probability of Epidemic based on R0 Value')
    plt.xlabel('R0 Value')
    plt.ylabel('Probability of Epidemic')
    plt.savefig('Homework6_1_graph.png')
    #plt.show()
   
    #save the output data
    output_textfile = 'problem6_1_data.txt'
    np.savetxt(output_textfile,
               np.array(np.vstack((r0_values, solutions))).T,
               delimiter = ', ', header='R_0, Probability of epidemic',
               fmt = ('%.2f', '%.3e'))
