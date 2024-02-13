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
To use NumPy, you first need to install it. If you have Python and PIP already installed on a system, then installation of NumPy is very easy. You can install it using this command: 

    pip install numpy [[4]].

Once NumPy is installed, import it in your applications by adding the import keyword: 

    import numpy as np [[4]] [[5]]. 
    
Shortening the imported name to np is better for the readability of code using NumPy.

After importing, you can create NumPy arrays, perform operations on them, and use various NumPy functions.

## 3. What are the functionalities of the package/library?
Here are some snippets of code demonstrating NumPy functionalities:

    import numpy as np

    # Creating arrays

        arr = np.array([1, 2, 3, 4, 5])
        print(arr)

    # Array operations

        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        print(arr1 + arr2)

    # Indexing and slicing

        print(arr[2])
        print(arr[1:4])

    # Array manipulation

        arr_reshaped = arr.reshape(5, 1)
        print(arr_reshaped)

    # Linear algebra

        matrix = np.array([[1, 2], [3, 4]])
        print(np.dot(matrix, matrix))

    # Statistical functions

        data = np.random.normal(loc=0, scale=1, size=100)
        print(np.mean(data))
        print(np.std(data))

    # Random number generation

        random_numbers = np.random.randint(1, 10, size=(3, 3))
        print(random_numbers)

## 4. When was it created?
NumPy was created in [2005](https://numpy.org/about/#:~:text=NumPy%20is%20an%20open%20source,the%20Numeric%20and%20Numarray%20libraries.).

## 5. Why did you select this package/library?
I selected NumPy because it is a powerful library that facilitates efficient numerical computations in Python. It offers extensive functionality for array manipulation, linear algebra, statistical analysis, and random number generation. NumPy's performance benefits and ease of use make it indispensable for data analysis and scientific computing tasks.

## 6. How did learning the package/library influence your learning of the language?
Learning NumPy significantly enhanced my understanding of Python, particularly in terms of numerical computing and data manipulation. It introduced me to new concepts such as array broadcasting, vectorized operations, and efficient indexing techniques. Understanding NumPy has made me more proficient in Python programming overall.

## 7. How was your overall experience with the package/library?
My overall experience with NumPy has been excellent. It has simplified many complex numerical computations and data manipulation tasks. I would highly recommend NumPy to anyone working with numerical data in Python.

### When would you recommend this package/library to someone?

I would recommend NumPy to anyone involved in scientific computing, data analysis, or machine learning tasks in Python. It is especially useful for handling large datasets efficiently and performing complex numerical operations.

### Would you continue using this package/library? Why or why not?

Absolutely, I would continue using NumPy. It has become an essential part of my Python toolkit for data analysis and numerical computing tasks. Its performance benefits and extensive functionality make it indispensable in my projects.

[1]: https://numpy.org/doc/stable/user/whatisnumpy.html
[2]: https://www.w3schools.com/python/numpy/numpy_intro.asp
[3]: https://www.geeksforgeeks.org/python-numpy/
[4]: https://www.w3schools.com/python/numpy/numpy_getting_started.asp
[5]: https://numpy.org/doc/stable/user/absolute_beginners.html