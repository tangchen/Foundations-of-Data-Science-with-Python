## Getting Started in Python

Python is an interpreted language, which means that when any Code cell in a Jupyter notebook is evaluated, the Python code will be executed, and any output or error messages will appear in a new output portion of the cell that will appear just after input portion of the cell (that contains the Python code). 

At the bottom of the `Intro.ipynb` notebook, there is a blank cell where you can start entering Python code. If there is not already a blank cell there, click on the last cell and press `alt-Enter`.

### Hello World!

We start with the canonical example that appears in almost every programming book, which is to create a function that writes "Hello World!" to the screen/output. 

To print output in Python, use the `print` function, which is a built-in function in Python 3. Here a *function* is used to denote a *named* set of Python instructions that can be called on demand. Python functions are called by using the function name with parentheses after it. Functions can accept *arguments*, which are variables and values that the function can act on. The arguments for a function are put inside the parentheses, with commas separating different items. 

To output text using `print`, put it as an argument inside single or double quotation marks:

print("Hello World!")

The `print()` function in Python knows how to deal with most standard data types. Unlike `printf` in C, explicit formatting instructions do not have to be given -- just pass the thing to be printed as an argument to `print`:

print(32)

print([1, 4, 9, 16])

To print multiple items, just concatenate them commas inside the `print()` function:

print("Hello", 'world!', 10+5, [1, 4, 9, 16])

Code cells may contain multiple Python statements. All statements in a cell will be run sequentially when the cell is run. The results of every `print` statement will be shown after the *input* part of the cell:

print("Hello ")
print("World!")

Some Python statement return results, and these will appear in a special *output* part of the cell:

5 + 10

However, if a cell contains multiple statments, the output will be the result of the **last** statement:

5+10
5*10

The last statement in a cell may produce not output. Then there is not output from the cell. Note that printed items are not outputs:

5+10
print("hello")

There are several different ways to get the output of multiple statements. One easy way is to just print all the results you want to see:

print(5+10)
print(5*10)

### Comments

Comments are text in your Python code that are ignored by the Python interpreter.
Documentation is usually used to convey what you intend
for your code to be doing -- which is not always what it is actually doing! 
Documentation is both for others who may need to read your code and for your future self, who
may not remember what you meant for a block of code to do. 

Anything that follows a # (hash) symbol is a comment:

#It is important to use comments to document your thinking on big assignments

There is not really a multi-line comment in Python (like /* */ in C). One way to make a multiline comment is to just make a multi-line string that is not assigned to any variable.  Multi-line strings are delimited by triple-ticks ('''):

''' This is a
multi-line comment,
okay?'''

When making custom functions, a multi-line string right after the function definition serves as the documentation string  (docstring) for that function.

### Python Variables and Types

Variables are named entities that store values for future reference. In Python, variable names consists of alphanumeric characters (a-z, A-Z, 0-9) and underscores, but they cannot start with a number. Variable names are case sensitive.  Detailed descriptions of naming conventions for Python are given in [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/]). Generally, we will follow these conventions:
* names should be descriptive, except when using as a simple index
* variable and function names should be lower case, with underscores separating different words
* variables should not duplicate names of modules or Python functions/methods

Variables are created by assigning a value to a valid variable name:

x=10

Python uses implicit typing, which means that you do not have to define a variable's type (i.e., what type of data it holds). The type is determined by the interpreter at the time of assignment. You can determine a variable's type by passing the variable as the argument of the `type()` function:

type(x)

The type of a variable can change whenever new data is assigned to it:

x=10.5

type(x)

x="Hello World!"

type(x)

When a variable is passed as an argument to the `print()` function, the value of the variable is printed:

print(x)

Python knows how to perform many different operations on different data types and will usually do the *right thing* based on the type of the variable:

a=3
b=4
a+b

print(a*b)

```{warning}
Exponentiation is done using two asterices between the number to be operated on and the exponent. The carat operator (^) is reserved for bitwise exclusive or.
```

2**3

We will often have the need to add to an existing value, and Python provides a shortcut notation for this (similar to C). For instance, here is the usualy way we write incrementing a counter:

counter=0
counter+=1
print(counter)

a="Hello "
b="World"
print(a+b)

a=3
b=4.1
print(a+b, type(a+b))

However, Python cannot read minds, and its rules may create unexpected results:

a="3"
b="4"
print(a+b)
print(int(a)+int(b))

c=5
print(a*c)
print(int(a)*c)

#### Basic Data Types

Python has many data types built-in, and we have already seen a few of these: *int*, *float*, and *str* (string). In this book, we will also use a few other of Python's built-in types. 

Boolean values are stored in *bool* variables that take on either `True` or `False`. Note that exact capitalization is required for these values.

a=True
print(a)

b= (2==3)
print(b)

type(b)


Python has a variety of different types of *sequence* types for containing an ordered  collection of values. Values can be retrieved by index from a sequence-type variable by putting the index number in square brackets after the variable name.

```
{warning}
Like C, C++, and JavaScript, indexing in Python starts at 0. This means that in a sequence of $n$ items, the first item is at index 0, and the last item is at index $n-1$. MATLAB and many textbooks use indexing starting at 1.
```

The *list* type is a **mutable** container of values. *Mutable* means the values in the list can be changed. Lists are delimited by square brackets, and items in lists are separated by commas. 

my_list = ['dogs', 'cats', 3, 7.0]
print(my_list)

print(my_list[1])

Because lists are mutable, values can be updated:

my_list[0]='puppies'
print(my_list)

Lists also can be sorted in place:

A *tuple* is an **immutable** sequence type. The values in a tuple cannot be changed. Tuples are often used to contain multiple values returned from a function. Tuples are delimited by parentheses: (). To create a tuple with only one value in it, include a comma after the value. As with lists, tuples can contain a variety of values. Trying to change a value in an immutable type results in an error:

tuple1=(1, 4, 'nine')
tuple2=(16,)

print(tuple1[2])

Trying to change a value in an immutable type results in an error:

tuple1[0]='one'

The *range* type is an **immutable** sequence of numbers that is usually used in looping (especially `for` loops). A range object can be created using the `range` keyword in the following ways:
* `range(stop)` creates a sequence of *stop* values starting at 0. Thus the values are 0, 1, 2, $\ldots,$ *stop*-1. Note that the Python convention is that the *stop* value is not included in the range. 
* `range(start, stop)` creates a sequence of values that starts at *start* and ends at *stop*-1. 
* `range(start, stop, step)` creates a sequence of values that starts at *start*, increments by *step* and ends at *stop*-1.

You can iterate over ranges using a `for`...`in` statement as shown below. More detais on loops are in Section XXX

for i in range(4):
    print(i)

for j in range(2,4):
    print(j)

for k in range(2,10,2):
    print(k)

Python also contains one *mapping* type:
* *dict* is a dictionary object that provides a map between key-value pairs. 
As with lists and tuples, keys and values can be any data types, but the keys must be unique.
Dictionaries are delimited by curly braces: { }. Each entry in a dictionary is written the form `key:value`, and different key-value pairs are separated by commas. The value for a particular key can be retrieved by putting the key in square brackets after the dictionary variable's name.

squares={1:1, 2:4, 3:9, 4:16}
print(squares[3])

misc={'cats':0, 'dogs':1, 3:'test'}
print(misc['cats'])
print(misc[3])

Python variables are actually much more powerful than variables in many languages because they are actually *objects*. Python is an object-oriented programming (OOP) language. To make the content of this book more accessible to people with a wide range of programming experience, this book does not generally use an object-oriented approach. However, we do not to know some fundamentals about **objects* and **classes**:
* *Objects* are special data types that have *methods* associated with them to work on those objects. Methods are similar to functions, except they are specialized to the *objects* to which they belong. Methods are called by giving the variable/object name, adding a period, specifying the method name, and then adding parentheses, with any aguments provided in parentheses. 
* A *class* is a template for an object that defines how an object stores information and defines its methods.

For instance, since *list* is a mutable type, a list can be sorted in place. The *list* object defines a sorting method to achieve this:

new_list=[5,7,1,3,13]
new_list.sort()
print(new_list)

For dictionaries, we often need to retrieve the keys or values. We can do this using methods provided by the dictionary type:

misc={'cats':0, 'dogs':1, 3:'test'}
print(misc.keys())

print(misc.values())

The `keys` and `values` methods return special objects of type `dict_keys` and `dict_values`, respectively, but for our purposes, we can treat these like lists. An example is shown in the Section {ref}`python-intro:loops`.

(python-intro:indentation)=
### Indentation in Python

Programming languages usually have some convention to indicate which statements belong together. For instance, if a statement starts a loop (such as `for` or `while`), there must be a way to indicate which of the following statements should be executed in each iteration of the loop and which should be executed after loop iteration. In many languages, such as C, C++, Java, and Javascript, code blocks are surrounded by curly braces: { }.

In Python, indentation is used to deliminate code blocks. The languages mentioned above used indentation as a *convention* that indicates meaning to humans working on code. Python uses indentation to *define* code blocks and convey meaning to the Python interpreter.

Either tabs or spaces can be used to denote code blocks, but the PEP-8 standard is to use 4 spaces per indent level. Jupyter inserts 4 spaces when `Tab` is pressed in a code block. **Change to footnote: Some editors can be set up to insert a prescribed number of spaces when tab is used or convert tabs to spaces upon saving.**

Note how indentation changes meaning in the following two examples, which differ only by one Tab:

a=2
b=3
if a==2:
    print("a=2")
if b==2:
    print("b=3")
    print(a,b)


a=2
b=3
if a==2:
    print("a=2")
if b==2:
    print("b=3")
print(a,b)



(python-intro:loops)=
### Loops in Python

Python provides `for` and `while` loops. While loops work much as in other languages:


i=1
while i<10:
    if i%2==0: 
        print(i)
    i=i+1

The `for` loops work a bit different in other languages, so it is worth deliving into them a bit more. In Python, `for` loops iterate over a sequence-type object. A `for` loop specifies a loop variable, which will hold the current value in the sequence being iterated over. The general syntax of the `for` statement is:

**`for` \<loop variable\> `in` \<sequence variable\>**

Examples are below:

for x in range(10):
    if x%2==0:
        print(x)

my_list = ['dogs', 'cats', 3, 7.0]
for item in my_list:
    print(item)

squares={1:1, 2:4, 3:9, 4:16}

for key in squares.keys():
    print(key,"^2 = ", squares[key])

(python-intro:functions)=
#### Functions

We have already used built-in functions, like `print()` and `type()`. 
In this book, we will also often create new functions. As with the built-in functions, 
user-defined functions can take arguments and can return values. Functions are declared 
using the Python keyword ```def``` followed by the function name and then parentheses. 
Any variables to received arguments are listed inside the parentheses.  Here is a simple
example:

def say_hello(name):
    print("Hello,", name, "!")

The function name and parameter list are called the *function signature*. User-defined functions are called in the same way as built-in functions:

say_hello("Amelia")

Functions can also return values by placing them after the Python `return` keyword. If multiple values are to be returned, they should be separated by commas. If more than one value is returned, it will be returned as a tuple:

def square_and_cube(x):
    return x**2, x**3

square_and_cube(4)

When storing returned values from a function into multiple variables, you do not have to explicitly use the parentheses around the tupe of variables. You can just separate the variables by commas, as shown below:

four2, four3 = square_and_cube(4)

print(four2, four3)

As mentioned when we introduced strings, you can provide a docstring for a function as 
a string that directly follows the function definition. For example, let's define a function
that returns the squared error between its inputs:

def diff_squared(x,y):
    '''
    Returns the difference between the squares of the arguments
    '''
    
    return x**2 - y**2 

diff_squared(3,2)

diff_squared(2,3)

Python also you to specify default values for function arguments that will be used if the user does not pass a value for the argument. When defining a function, specify the default value for an argument by writing the parameter name, followed by an equal sign, followed by the default value in the function signature.

Let's make a new version of `squared_error` function that sets the default value of `y` to 0:

def diff_squared2(x,y=0):
    '''
    Returns the magnitude of the squared error between the two arguments
    '''
    
    return x**2 - y**2 

diff_squared2(2)

If the user passes a value, the default value is not used:

diff_squared2(2,3)

Note that we can use the names of the parameters (instead of parameter order) to pass values to those parameters. This is very commonly used in functions that have lots of parameters that are optional.

diff_squared2(y=2,x=3)

Parameters can be passed using a mix of order and parameter name. However, any parameters passed by order must come before those passed by name.

We will see in the next section how to get help on a function.

#### Getting Help and Completion

Python has built-in help for almost every function and object. This help can be retrieved in several ways. For instance, consider the built-in `sum` command. Here are several ways to get help in Jupyter:

help(sum)

?sum

For user-defined functions, 'help' will display the docstring you wrote. The following assumes that you have defined the function `squared_errors` from Section {ref}`python-intro:functions`

?squared_errors

If a function's Python source code is available, it can be retrieved in Jupyter using `??`:

??squared_errors

Now, let's look at the help for a variable. 

squares={1:1, 2:4, 3:9, 4:16}

?squares

You should also try `help(x)`, but I have omitted that because it provides help for every method that a dictionary object has available, which results in a lot of output.

You can also try `help()` with no argument to get an interactive help session.

Jupyter also provides many features to help you during programming. Assuming you have run the command defining `squares` above, try the following in a new Jupyter notebook cell:
1. Type `sum(`. When you type the open parenthesis, Jupyter should automatically insert a pair of parentheses. 
2. Press `shift-Tab`. You should see the call signature and doc string for the `sum` function in a pop-over box. You can press the `Esc` key to close the pop-over box. 
3. Type `sq` and press `Tab`. You should see a list of variables and functions that begin with `sq`. Use the cursor keys to scroll to `squares` and press `Enter` to insert it without having to type the full name of the squares dictionary.
4. Let's sum the values in the `squares` dictionary. Type a period and then press `Tab` again to see a list of methods for a `dict` object. Select `values` using the keyboard or mouse
5. Don't forget that we need parentheses to call the `values` method. Press `(` and a pair of parentheses should appear.
6. Press `shift-Enter` to run the cell

sum(squares.values())

#### Python Modules and Namespaces

Python has many useful modules that extend Python's basic functionality. Some of these are included with the base Python distributin and many others are included in the Anaconda distribution. Many more can be installed over the Internet. 

To use a module, you must import it into your Python working environment. The most basic way to do this is to type `import` followed by the name of the module to be imported:

import numpy

Here we have imported NumPy, which is one of the most important Python modules for working with numerical functions and arrays. When a library is imported, the functions and classes from the library will be available in Python, but they are imported into their own *namespace*. To access something that exists in a different namespace, type the name of the namespace, followed by a period, followed by the name of the thing you are trying to access.

For instance, the value of $\pi$ is a constant object named `pi` in numpy. Now that we have imported numpy, we can access that value:

print(numpy.pi)

Numpy has many typical mathematical functions, which we can call using the `numpy` namespace:

numpy.sin(numpy.pi/4)

numpy.sqrt(2)/2

We can control the namespace into which the contents of a module is imported. Because many modules, like numpy, are commonly used, the community often uses community-standardized namespaces that are shorter than the full module name. To do this, type `import`, followed by the module name, followed by the `as` keyword, followed by the desired namespace. 

For NumPy, the user community typically uses `np`, so the import statement is as follows:

import numpy as np

print(np.pi)

```{warning}
It is possible to import the contents of a module into the *global* namespace, which means that the namespace does not have to be specified before each function, class, or object. However, this practice is strongly discouraged because it will often result in conflicts. For instance, both Matplotlib (a plotting module) and SymPy (a symbolic algebra module) have a `plot` function. If you were to import both `matplotlib` and `sympy` into the global namespace, you could not be sure which `plot` you were calling, unless you kept track of which module was imported last.
```


Importing into namespaces is such good practice that we will not give an example of how to import an entire module into the global namespace. However, on occasion, it may be helpful to import just a single function from a module, and in this case, it is reasonable to import into the global namespace if we can be confident that there will not be any collisions. An example follows:

from scipy.special import factorial

factorial(10)

Why is factorial returning a float? Let's check the docstring:

?factorial

By inspecting the docstring, we can see that if we want the exact value, we need to set the parameter `exact` to True. This is typically done using the parameter name because anyone reading the function call will understand what the value of `True` is being used for:

factorial(10, exact=True)

#### Writing Big Numbers in Python

We will be building simulations in Python that require looping thousands or millions of times. Thus, we will often be writing a `range` that has an argument with many zeros. The `range` function will not take a `float` value, and numbers written in scientific notation (like `1e6`) will be treated as floats. This results in using integers that are very hard to read, like 10000000. We can't use commas in the numbers because that would create a tuple:


10,000,000

Fortunately, Python provides a simple way to make large numbers like these more readable. Instead of using commas as a delimiter between every third digit, use underscores (\_). Doing this makes it much easier to interpret large numbers, like ten million:

10_000_000

#### Summary and Other Resources

Do not worry too much about absorbing all these details about Python now. This book contains many examples to get you started, and you can refer back to this section for reference. Some additional features of the Python programming language will be introduced as needed.

For users who want to learn more about Python, the following resources are recommended:
* [*A Whirlwind Tour of Python* (https://jakevdp.github.io/WhirlwindTourOfPython/)](https://jakevdp.github.io/WhirlwindTourOfPython/), by Jake VanderPlas, is a free eBook that covers all the major syntax and features of Python
* [Learn Python for free (https://scrimba.com/learn/python)](https://scrimba.com/learn/python) is a free 5-hour online introduction to Python (signup required)
* The Python documentation includes a [Python Tutorial (https://docs.python.org/3/tutorial/)](https://docs.python.org/3/tutorial/)

#### Jupyter Magics

Code cells can also contain special instructions intended for JupyterLab itself, rather than the
Python kernel. These are called *magics*. For instance, to output your current directory, you can use the 
`%pwd` magic

%pwd

You can use the "%cd" magic to change your directory (recall that~ is a shortcut for your home user directory):

cd ~

Changing directories is often useful to switch to a directory where data is stored.

You can get a list of magics and other information about Jupyter using the `%quickref` magic.