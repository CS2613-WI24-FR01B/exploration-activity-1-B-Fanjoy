# NumPy

## 1. Which package/library does the sample program demonstrate?
The sample program demonstrates the usage of the NumPy library, which is a fundamental package for scientific computing with Python. NumPy provides support for arrays, matrices, and mathematical functions, making it essential for data analysis and manipulation.

## 2. How does someone run your program?
To run the program, follow these steps:
1. Ensure you have Python installed on your system.
2. Clone or download the repository containing the sample program.
3. Navigate to the directory containing the program files.
4. Run the program using the following command:
    - py expNumpy.py
5. Follow the on-screen instructions to input the number of samples and features.

## 3. What purpose does your program serve?
The program serves the purpose of demonstrating basic statistical analysis using NumPy. It prompts the user to input the number of samples and features, generates random data based on the input, calculates various statistical measures such as mean, median, and standard deviation for the data, and prints the results. This can be useful for interactive analysis of statistical properties in custom datasets.

## 4. What would be some sample input/output?
Sample input:
    ```
    Enter the number of samples: 1000
    Enter the number of features: 5
    ```

Sample output:
    ```
    Basic Statistics:
    ------------------
    Means:
    [ 0.02980407  0.04552748 -0.01488072 -0.000239   -0.03010215]

    Medians:
    [ 0.02055659  0.02572282  0.02705705  0.02383941 -0.04185027]

    Standard Deviations:
    [0.97809758 0.99381339 0.95701312 0.98362511 0.97042018]

    Skewness:
    [0.09813315 0.01398885 0.04727414 0.0170917  0.14335906]

    Kurtosis:
    [ 0.0150661   0.06691996 -0.05852815  0.17063533  0.07063642]

    Quartiles (25th, 50th, 75th percentiles):
    [[-0.62214477 -0.63851764 -0.69321416 -0.68131706 -0.69054958]
    [ 0.02055659  0.02572282  0.02705705  0.02383941 -0.04185027]
    [ 0.68364096  0.69464042  0.66693796  0.66759475  0.58328591]]

    Covariance Matrix:
    [[ 0.95763252 -0.00460584  0.05737168  0.01773948 -0.02660147]
    [-0.00460584  0.98865372 -0.004763    0.01795159  0.0342366 ]
    [ 0.05737168 -0.004763    0.91679091  0.00273622 -0.01386847]
    [ 0.01773948  0.01795159  0.00273622  0.96848685  0.05090739]
    [-0.02660147  0.0342366  -0.01386847  0.05090739  0.94265799]]

    Correlation Matrix:
    [[ 1.         -0.00473355  0.06122982  0.01842021 -0.02799814]
    [-0.00473355  1.         -0.00500292  0.01834569  0.0354643 ]
    [ 0.06122982 -0.00500292  1.          0.00290382 -0.01491819]
    [ 0.01842021  0.01834569  0.00290382  1.          0.0532791 ]
    [-0.02799814  0.0354643  -0.01491819  0.0532791   1.        ]]
    ```