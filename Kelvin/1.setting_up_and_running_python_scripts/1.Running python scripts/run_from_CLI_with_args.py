# Open CLI and run <python run_from_CLI_with_args.py> or <python -m  run_from_CLI_with_args>

import sys

# 'sys' is one of built-in system libraries(libraries that interact with the underlying operating system.
# Examples of other such libraries includes OS and

# Example 1: Basics of sys.argv
# counts start from 1 because index 0 contains the scripts directory by default
# print(f"You passed {sys.argv[1]} and {sys.argv[2]}")

# Example 2: sys.arv is a list of strings
# whatever you pass is taken as string. Do necessary type casting for use in your project
# print(f"You passed {type(sys.argv[1])} and {type(sys.argv[2])}")

# Example 3: What can go wrong with sys.arg? Use conditionals
# You must pass the args you put in your code otherwise the program fails.
# But you can use branches and len(sys.argv) to make the script robust(cover all cases) and not fail.
# length of sys.argv 1 by default before passing any extra args from the CLI.
print(f"len(sys.argv) = {len(sys.argv)}")
if len(sys.argv) > 1:
    for i, arg in enumerate(sys.argv):  # sys.argv is a list of strings
        print()
        print(i, arg)
else:
    print("No args passed from the CLI")
