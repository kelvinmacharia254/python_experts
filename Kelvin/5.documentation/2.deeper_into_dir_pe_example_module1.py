"""
Author: Kelvin Macharia
module: pe_example_module1.py
Purpose: Demo use of dir to list attrs and method on the context scope.
"""
group: str = "Python Experts"  # user/dev define variable


# user/dev defined function
def demo_function(a: int = None, b: int = None) -> str:
    """
    This is a demo function to demo use of dir in different scope type hints and use of docstrings
    :param a:
    :param b:
    :return:
    """
    print(f"a is {a} while b is {b}")
    demo_function_var = "I am string inside the demo_function(). Other variables sharing scope are 'a' and 'b' "
    return


# user/dev defined class
class DemoClass:
    pass


print("\n1. Call dir without arguments. This considers the current scope. Current scope is this module")
#      We are in a module scope or Global scope(LEGB).
#         other scopes include functions, class, builtins.
print(dir())  # list attributes available to the current scope.
print("Lets demo attrs available to this module as listed.")
print("\n1(a) file/module name")
print(__name__)  # returns '__main__' if this running module

print("\n1(b) __doc__ string attribute")
#       returns docstring if available.Use docstring rather than comments to be able to retrieve them later for
#       ... for an automated documentation using inbuilt tools or 3rd party tools.
print(__doc__)  # module docstring
print(demo_function.__doc__)  # demo_function() function docstring

print("\n1(c) annotations - contains various annotations like function and variables.")
#       What are annotations?
#           Annotations provide a way to attach metadata to function parameters and return values.
#           Annotations are not enforced by the Python interpreter; they are merely hints or documentation
#           They can be used by IDEs, linters, type checkers and developers to understand the expected types of
#           variables and function signatures.
print(__annotations__)  # annotation on the module scope.
print(demo_function.__annotations__)  # annotation on the function scope
#       Try running mypy static check
#       Run 'mypy 2.deeper_into dir_pe_example_module1.py' on the command line"

print("\n1(d). Get module name with __file__. This gives the full file path of this module")
print(dir(__file__))  # file name is a string object

print("\n1(e). Checkout __builtins__. This contains functions such as print and the like. This normally don't require "
      "explicit importation into a module. They are free agents available on demand in the module namespace. "
      "They are the common tools in any python code.")
print(__builtins__)  # you won't see much.
print(dir(__builtins__))  # Run dir on __builtins__ to list attrs
print(__builtins__.__doc__)  # Display a help docstring giving a detailed description

print("\n2. Try dir in a function scope. It will just return attrs available to the function which is the context "
      "scope.")
print(dir(demo_function))  # local variables won't display because they only exist during run time.
print("Lets demo attrs available to the the demo_function as listed.")
print("\n2(a) function annotations")
print(demo_function.__annotations__)
print("\n2(b) __doc__ is string attribute")
print(demo_function.__doc__)
print("\n2(c) __name__  is the name of the function.")
print(demo_function.__name__)
print("\n3. learn about dir by calling dir function on itself")
print(dir(dir))  # What attrs are available to the dir function?
print(dir.__doc__)  # try dir's __doc__ attrs to read its docstring

print("\n4. Inspect a 3rd party package with dir.")
import pandas

df = pandas.DataFrame()

print(pandas.DataFrame.__doc__)
