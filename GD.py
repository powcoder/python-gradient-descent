
import numpy as np
# X          - single array/vector
# y          - single array/vector
# theta      - single array/vector
# alpha      - scalar
# iterations - scarlar

def gradientDescent(X, y, theta, alpha, numIterations):
    '''
    # This function returns a tuple (theta, Cost array)
    '''
    m = len(y)
    arrCost =[];
    transposedX = np.transpose(X) # transpose X into a vector  -> XColCount X m matrix
    for interation in range(0, numIterations):
        ################PLACEHOLDER4 #start##########################
        #: write your codes to update theta, i.e., the parameters to estimate. 
	# Replace the following variables if needed 
        change =  
        theta = np.subtract(theta, change)  # or theta = theta - alpha * gradient
        ################PLACEHOLDER4 #end##########################

        ################PLACEHOLDER5 #start##########################
        # calculate the current cost with the new theta; 
        atmp =    
	print(atmp)
	arrCost.append(atmp)
     
        ################PLACEHOLDER5 #start##########################

    return theta, arrCost
