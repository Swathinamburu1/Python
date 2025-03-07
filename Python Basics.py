#1. Write a program to print your name.
    print ("My Name is Swathi") 

#2. Write a program for a Single line comment and multi-line comments.

    # This is a single-line comment in Python
    print("Hello, World!")  # This is another single-line comment
    
    # This is a multi-line comment in Python.
    """
    This is a multi-line comment in Python.
    It spans multiple lines and is enclosed within triple double-quotes.
    Python treats this as a string, but it's often used as a comment.
    """
    
    ''' 
    This is another way to write multi-line comments using triple single-quotes.
    It works the same way as the triple double-quotes.
    '''

#3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.

    a = -25
    print("Type of a: ", type(a))
    b = True
    print("Type of b: ", type(b))
    c = 13.0
    print("Type of c: ", type(c))
    S = 'Swathi'
    print("Type of S: ", type(S))

#4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables.

    k=15
    # Uses global because there is no local 'k'
    def m1():
        print('Inside m1() : ',k)
    # Variable 'k' is redefined as a local
    def m2():
        k = 2
        print('Inside m2() : ', k) 
    # Use global keyword to modify global 'k'
    def m3():
        global k
        k = 4      #Value of 'k' modified
        print('Inside m3() : ', k)  
    # Global scope
    print('global : ', k)
    m1()
    print('global : ', k)
    m2()
    print('global : ', k)
    m3()
    print('global : ', k)
