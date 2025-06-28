# np.sum(array) add all
# np.mean(array) average
# np.min(array) minimum
# np.max(array) maximum
# np.std(array) standard deviation
# np.var(array) variance
# np.median(array) median
# np.percentile(array, q) qth percentile
# np.quantile(array, q) qth quantile
# np.any(array) check if any element is True
# np.all(array) check if all elements are True
# np.argmin(array) index of minimum
# np.argmax(array) index of maximum
# np.nonzero(array) indices of non-zero elements
# np.where(condition) indices where condition is True
# np.unique(array) unique elements
# np.sort(array) sorted array
# np.argsort(array) indices that would sort the array
# np.searchsorted(array, value) index where value would be inserted to maintain order
# np.diff(array) discrete difference
# np.cumsum(array) cumulative sum
# np.cumprod(array) cumulative product

import numpy as np
arr = np.array([10, 20, 30, 40, 50])

print("Sum:", np.sum(arr))  # Add all elements
print("Mean:", np.mean(arr))  # Average of elements
print("Minimum:", np.min(arr))  # Minimum element
print("Maximum:", np.max(arr))  # Maximum element
print("Standard Deviation:", np.std(arr))  # Standard deviation
print("Variance:", np.var(arr))  # Variance of elements
print("Median:", np.median(arr))  # Median of elements
print("25th Percentile:", np.percentile(arr, 25))  # 25th percentile
print("75th Percentile:", np.percentile(arr, 75))  # 75th percentile
print("Quantile (0.5):", np.quantile(arr, 0.5))  # 50th quantile (median)
print("Any True:", np.any(arr > 25))  # Check if any element is greater than 25
print("All True:", np.all(arr > 5))  # Check if all elements are
