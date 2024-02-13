# Exploring NumPy

## 1. Which package/library did you select?
I selected the NumPy library.

## 2. What is the package/library?
NumPy, short for Numerical Python, is a fundamental package for scientific computing in Python [[1]] [[2]]. It provides a high-performance multidimensional array object, and tools for working with these arrays [[3]].

### Purpose:
- NumPy provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation, and much more [[1]].

- NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences [[1]].

- NumPy aims to provide an array object that is up to 50x faster than traditional Python lists [[2]]. This is because NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently [[2]].

### How do you use it?
To use NumPy, you first need to install it. If you have Python and PIP already installed on a system, then installation of NumPy is very easy. You can install it using this command  [[4]]: 

    pip install numpy

Once NumPy is installed, import it in your applications by adding the import keyword [[4]] [[5]]: 

    import numpy as np 
    
Shortening the imported name to np is better for the readability of code using NumPy.

#### Creating Arrays: 
NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers. You can create a NumPy array using the numpy.array() function [[14]] [[15]].

#### Array Operations: 
You can perform element-wise operations on arrays like addition, subtraction, multiplication, and division [[16]].

#### Indexing and Slicing: 
NumPy arrays can be indexed and sliced, similar to Python lists [[17]] [[18]].

#### Array Manipulation: 
NumPy provides several routines for manipulation of elements in ndarray object [[7]]. They can be classified into the following types [[7]]:

- Changing Shape: reshape, flat, flatten, ravel
- Transpose Operations: transpose, ndarray.T, rollaxis, swapaxes
- Changing Dimensions: broadcast, broadcast_to, expand_dims, squeeze
- Joining Arrays: concatenate, stack, hstack, vstack
- Splitting Arrays: split, hsplit, vsplit
- Adding / Removing Elements: resize, append, insert, delete, unique

#### Linear Algebra: 
NumPy provides us with functions for performing common linear algebra tasks, such as array multiplication, solving linear systems, and more [[8]] [[9]]. Here are some of the linear algebra functions provided by NumPy [[8]]:

- dot(): calculates product of two arrays
- inner(): calculates inner product of arrays
- outer(): calculates outer product of arrays
- det(): calculates determinant of a matrix
- solve(): solves linear matrix equation
- inv(): calculates the multiplicative inverse of the matrix
- trace(): calculates the sum of diagonal elements

#### Statistical Functions: 
NumPy provides various statistical functions for finding minimum, maximum, percentile standard deviation and variance, etc. from the given elements in the array [[10]] [[11]]. Here are some of the statistical functions provided by NumPy [[10]]:

- median(): return the median of an array
- mean(): return the mean of an array
- std(): return the standard deviation of an array
- percentile(): return the nth percentile of elements in an array
- min(): return the minimum element of an array
- max(): return the maximum element of an array

#### Random Number Generation: 
NumPy offers the random module to work with random numbers [[12]] [[13]]. Here are some of the functions provided by NumPy’s random module [[13]]:

- randint(): returns a random integer from a specified range
- rand(): returns a random float between 0 and 1
- choice(): generates a random sample from a given 1-D array

## 3. What are the functionalities of the package/library?
Here are some snippets of code demonstrating NumPy functionalities:

    import numpy as np

    # Creating arrays

        a = np.array([1, 2, 3])  # Creates a 1-dimensional array
        b = np.array([(1, 2, 3), (4, 5, 6)])  # Creates a 2-dimensional array

    # Array operations

        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])

        print(a + b)  # Output: array([5, 7, 9])
        print(a - b)  # Output: array([-3, -3, -3])
        print(a * b)  # Output: array([ 4, 10, 18])
        print(a / b)  # Output: array([0.25, 0.4 , 0.5 ])

    # Indexing and slicing

        a = np.array([1, 2, 3, 4, 5])

        print(a[0])  # Output: 1
        print(a[1:3])  # Output: array([2, 3])

    # Array manipulation

        # Create a 1D array
        a = np.array([1, 2, 3, 4, 5, 6])

        # Reshape the array to a 2D array with 2 rows and 3 columns
        b = a.reshape(2, 3)

        # Transpose the 2D array
        c = b.T

    # Linear algebra

        # Coefficients of the equations
        A = np.array([[1, 2], [3, 4]])

        # Constants on the RHS of the equations
        b = np.array([5, 6])

        # Solve the system of equations
        x = np.linalg.solve(A, b)

    # Statistical functions

        # Create a NumPy array
        a = np.array([1, 2, 3, 4, 5])

        # Calculate the mean
        mean = np.mean(a)

        # Calculate the standard deviation
        std_dev = np.std(a)

    # Random number generation

        # Generate a random integer from 0 to 100
        x = np.random.randint(100)

        # Generate a random float from 0 to 1
        y = np.random.rand()

## 4. When was it created?
NumPy was created in [2005](https://numpy.org/about/#:~:text=NumPy%20is%20an%20open%20source,the%20Numeric%20and%20Numarray%20libraries.).

## 5. Why did you select this package/library?
I selected NumPy because it is a powerful library that provides efficient numerical computations in Python. It offers extensive functionality for array manipulation, linear algebra, statistical analysis, and random number generation. All of which are invaluable tools for a Computer Science student. Especially considering the complex algebraic calculations needed for Linear Algebra and Game Development courses.

## 6. How did learning the package/library influence your learning of the language?
Learning NumPy significantly enhanced my understanding of Python, particularly in terms of efficient data handling and operations. It introduced me to the concept of arrays and the power of vectorized operations, which are more efficient than traditional loops in Python. Additionally, NumPy’s functions and methods provided exposure to a wide range of mathematical and statistical operations which are essential in the field of data science, a field which I am looking into as a career. This helped me understand how Python is a powerful tool for both general-purpose programming and specialized scientific computing tasks.

## 7. How was your overall experience with the package/library?
My overall experience with NumPy has been excellent. It has simplified many complex numerical computations and data manipulation tasks. I would highly recommend NumPy to anyone working with numerical data in Python.

### When would you recommend this package/library to someone?

I would recommend NumPy to anyone involved in scientific computing, data analysis, or machine learning tasks in Python. It is especially useful for handling large datasets efficiently and performing complex numerical operations.

### Would you continue using this package/library? Why or why not?

Absolutely, I would continue using NumPy. It has become an essential part of my Python toolkit for data analysis and numerical computing tasks. I can see it becoming part of my daily usage if I persue data science as a career.

[1]: https://numpy.org/doc/stable/user/whatisnumpy.html
[2]: https://www.w3schools.com/python/numpy/numpy_intro.asp
[3]: https://www.geeksforgeeks.org/python-numpy/
[4]: https://www.w3schools.com/python/numpy/numpy_getting_started.asp
[5]: https://numpy.org/doc/stable/user/absolute_beginners.html
[6]: https://www.devopsschool.com/blog/what-is-numpy-and-how-it-works-an-overview-and-its-use-cases-2/#Use_case_of_Numpy
[7]: https://www.tutorialspoint.com/numpy/numpy_array_manipulation.htm
[8]: https://www.programiz.com/python-programming/numpy/linear-algebra
[9]: https://www.geeksforgeeks.org/numpy-linear-algebra/
[10]: https://www.programiz.com/python-programming/numpy/statistical-functions
[11]: https://www.tutorialspoint.com/numpy/numpy_statistical_functions.htm
[12]: https://realpython.com/numpy-random-number-generator/
[13]: https://www.w3schools.com/python/numpy/numpy_random.asp
[14]: https://numpy.org/doc/stable/user/basics.creation.html
[15]: https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp
[16]: https://www.programiz.com/python-programming/numpy/basic-array-operations
[17]: https://datagy.io/numpy-array-indexing-slicing/
[18]: https://numpy.org/doc/stable/user/basics.indexing.html