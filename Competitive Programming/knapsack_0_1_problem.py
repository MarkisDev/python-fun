# A naive recursive implementation of 0-1 Knapsack Problem 

# Returns the maximum value that can be put in a knapsack of 
# capacity W 

def knapSack(W, wt, val, n): 

	if n == 0 or W == 0 : 
		return 0

	if (wt[n-1] > W): 
		return knapSack(W, wt, val, n-1) 
	else: 
		return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), 
				knapSack(W, wt, val, n-1)) 


# Testing
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print knapSack(W, wt, val, n) 
