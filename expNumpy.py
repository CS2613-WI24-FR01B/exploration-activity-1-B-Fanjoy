import numpy as np

def generate_random_data(num_samples, num_features):
    # Generate random data for example purposes
    return np.random.normal(loc=0, scale=1, size=(num_samples, num_features))

def calculate_statistics(data):
    # Calculate mean, median, and standard deviation for each feature
    means = np.mean(data, axis=0)
    medians = np.median(data, axis=0)
    std_devs = np.std(data, axis=0)

    # Calculate skewness and kurtosis for each feature
    skewness = np.apply_along_axis(lambda x: ((x - np.mean(x))**3).mean() / (np.std(x)**3), axis=0, arr=data)
    kurtosis = np.apply_along_axis(lambda x: ((x - np.mean(x))**4).mean() / (np.std(x)**4) - 3, axis=0, arr=data)

    # Calculate quartiles for each feature
    quartiles = np.percentile(data, [25, 50, 75], axis=0)

    # Compute the covariance matrix and correlation matrix
    covariance_matrix = np.cov(data, rowvar=False)
    correlation_matrix = np.corrcoef(data, rowvar=False)

    return means, medians, std_devs, skewness, kurtosis, quartiles, covariance_matrix, correlation_matrix

# Main driver
num_samples = int(input("Enter the number of samples: "))
num_features = int(input("Enter the number of features: "))

data = generate_random_data(num_samples, num_features)
means, medians, std_devs, skewness, kurtosis, quartiles, covariance_matrix, correlation_matrix = calculate_statistics(data)

# Print the results
print("Basic Statistics:")
print("------------------")
print("Means:")
print(means)
print("\nMedians:")
print(medians)
print("\nStandard Deviations:")
print(std_devs)
print("\nSkewness:")
print(skewness)
print("\nKurtosis:")
print(kurtosis)
print("\nQuartiles (25th, 50th, 75th percentiles):")
print(quartiles)
print("\nCovariance Matrix:")
print(covariance_matrix)
print("\nCorrelation Matrix:")
print(correlation_matrix)