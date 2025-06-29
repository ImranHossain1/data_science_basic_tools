import  numpy as np
prices = np.array([100, 200, 300, 400, 500])
discount = 10 # scalar value

final_prices = prices - (prices * discount / 100)  # Broadcasting the scalar discount across the array
print("Final prices after discount:", final_prices)