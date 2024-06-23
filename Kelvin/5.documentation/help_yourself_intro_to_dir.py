"""
Objective:
Python comes with lots of inbuilt functionality.
    How do I find information about them and utilize functionalities?

Here is how:
- use dir() built-in function to list all attributes/attrs(methods and variables) available to any python object.
- this can be used as a quick reminder of the functionalities available to objects you are using. e.g: list, tuple
- Objects can be built-in(list, string e.t.c) or user defined via custom classes.
- dir() return a python list
"""

# Illustrate by calling dir on a list object.
# Similar to how we create our classes and instantiate our own objects from them,
#   it is the same way we utilize built-ins classes and objects
python_expert_lst = list()  # alternatively  -->  python_expert_lst = []

# check type

# print(f'type of python_expert_lst: {type(python_expert_lst)}')

# what can I do with a list? What are some of the functionality does a list object comes with?
print(f'The list object has the following attrs: \n {dir(python_expert_lst)}')
# observe, list returns a list with all attrs for an object, there are dunder/overload/magic/special attrs and
#  object specific attrs to the list object. This what makes a list what it is, so it's a tuple or other objects.
#   Specific methods would be different if it was another object type.

# print(python_expert_lst.append)

# lets inspect a tuple object,
python_expert_tuple = ()  # or python_expert_tuple = tuple()
print(f'The tuple object has the following attrs: \n {dir(python_expert_tuple)}')


#  The dunder methods can help you override common default behavior for built-in operations.
#  Python can have common dunder methods while some object can lack other. Same logic objects have unique functionality.
#  A list is a list, a tuple do what tuples do because it has a unique attrs different from other objects e.t.c.


# create custom class
class PythonExpertsFellow:  # What's wrong with this class name?
    """
    inherits dunder attrs from base object
    """

    def __init__(self, name: str = "", age: int = 0, skill_set=''):
        self.name = name
        self.age = age
        self.skill_set = skill_set

    def introduce_self(self):
        return f"I am {self.name}, {self.age} years old python dev.My skill set: {self.skill_set}"


kelvin = PythonExpertsFellow(
    "Kelvin Macharia",
    25,
    "My python skills"
)

intro = kelvin.introduce_self()
# print(intro)

# let's snoop around in out custom class
print(f'The PythonExpertFellow object has the following attrs: \n {dir(kelvin)}')

# print(kelvin.__doc__)
# print(python_experts_fellow.__doc__)

# call dir with no args on this module
# do it here and explain

# Intro to knowing about your objects?  /// Done and dusted
# Next:
# Know more about your objects with help and other documentation sources.
# go deep into builtins, 3rd party packages
# running dir() in a module without an arg
# documentation
# Scope and Name resolution. Answer: What happens when you name your modules a names similar to an inbuilt?
# Iterables, iterators and generators
