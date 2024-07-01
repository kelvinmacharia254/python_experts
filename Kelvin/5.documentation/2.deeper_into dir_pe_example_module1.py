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
    demo_function_var = f"I am string inside the demo_function(). Other variables sharing scope are 'a' and 'b' "
    return dir()



# user/dev defined class
class DemoClass:
    pass


# 1. Call dir without arguments. This considers the current scope.
#      We are in a module scope or Global scope.
#         other scopes include functions, class, builtins.
print(dir())  # list attributes available to the current scope. Uncomment user define variables
#   demo attrs available in the current scope
#     a) file/module name
print(__name__)  # returns __main__ if running module

#     b) __doc__ string attribute
#       returns docstring if available.Use docstring rather than comments to be able to retrieve them later for
#       ... for an automated documentation using inbuilt tools or 3rd party tools.
print(__doc__)
print(demo_function.__doc__)

#     c) annotations - contains various annotations like function and variables.
#       What are annotations?
#           Annotations provide a way to attach metadata to function parameters and return values.
#           Annotations are not enforced by the Python interpreter; they are merely hints or documentation
#           They can be used by IDEs, linters, type checkers and developers to understand the expected types of
#           variables and function signatures.
print(__annotations__)  # annotation on local scope
print(demo_function.__annotations__)  # annotation on the function scope
#   author/dev attrs

# 2. Call with arguments like current module or inbuilt or user-defined objects
# print(dir(__file__))  # file name is a string object


# 3. Try dir in a function scope. It will just return attrs available to the function which the context scope
print(demo_function())

# 4. learn about dir by calling dir function on itself
print(dir(dir))  # What attrs are available to the dir function?
print(dir.__doc__)  # try dir's __doc__ attrs

# 4.
# import pandas
#
# df = pandas.DataFrame()
#
# print(pandas.DataFrame.__doc__)