# Data Types & Control Flow
- In this *folder* we wil be covering **data types and control flow** in detail. We might add other topics as we study further to become python experts. We would like Python to be at our finger tips and make a beautiful career out of  it.
- I'm loving the journey and the push it gives me. This adventure contributes to my purpose. I love learning new things every day. God to be with me and the team on this learning journey. 

## Data types
**Tuples**: a tuple is an ordered, immutable collection of elements.

**lists**:a list is an ordered and mutable collection of elements. Lists are a fundamental data structure used to store, access, and manipulate multiple items.

**Sets**: a set is an unordered collection of unique elements. Sets are a fundamental data type that is used to store distinct values. 

**Dictionaries**:A dictionary is an unordered and mutable collection of key-value pairs. Dictionaries are also known as associative arrays or hash maps. 

## List comprehensions
**List comprehension** is a concise way to create lists by applying an expression to each item in an iterable.

**Basic List Comprehension Syntax**

The basic syntax of list comprehension consists of three components:

**Expression**: The expression to be evaluated and included in the new list.

**Iteration**: The loop variable that iterates over an iterable.

**Condition (optional)**: An optional condition that filters items based on a Boolean expression.





# Control Flow
- Else, if-else, if-else-elif
- For loop, while loop


#### resources
- [list comprehension](https://www.geeksforgeeks.org/python-list-comprehension/)

# Github Snippets

#### to get into an existing repository,
- Navigate to the Repository Directory: Open a terminal or command prompt and navigate to the directory of your local repository using the cd command. For example:
""" cd /path/to/your/repository """ and the "git status" to see changes in that repository that needs to be pushed.


**Pull the Latest Changes:**
- Before pushing your changes, it's a good practice to pull the latest changes from the remote repository to make sure you have the most up-to-date version of the branch. 
```
git pull origin main
git status (to check if changes has been pulled from remote repository)
git add <file name>
git add . (adds all files)
git commit -m "Your commit message"
git push origin branch_name

```
**git fetch** and **git pull** are both commands used to update your local repository with changes from a remote repository, but they work in different ways.

**git fetch:**

**Use Case:**

Use git fetch when you want to retrieve the latest changes from a remote repository without automatically merging them into your working branch.

**How it Works:**

*git fetch* downloads new branches or updates existing ones from the remote repository but does not automatically merge the changes into your local working branch. It updates your remote-tracking branches (like origin/main) to reflect the latest changes on the remote.

**Example:**
```
git fetch origin

```
**Benefits:**


Safer: It allows you to review changes before merging, reducing the risk of unexpected conflicts.

**git pull:**

**Use Case:**

- Use *git pull* when you want to fetch the latest changes from a remote repository and automatically merge them into your local working branch.

**How it Works:**

- *git pull* is essentially a combination of git fetch and git merge. It fetches the changes from the remote repository and then merges them into your local branch.

**Example:**
```
git pull origin main
```


**Benefits:**

- Convenient: It's a single command that fetches and merges changes in one step.

- Common Workflow: It's commonly used when you want to quickly update your local branch with the latest changes from the remote.

**Choosing Between *git fetch* and *git pull*:**

If you want to review changes before merging:

- Use *git fetch* to fetch changes, inspect them, and then decide whether to merge.

If you want to quickly update your local branch:

- Use *git pull* for a more streamlined process.

**Note:**

- Both commands require that you have committed or stashed your local changes before updating.

**Example Workflow:**
```
# Use git fetch to get the latest changes from the remote without merging
git fetch origin

# Review the changes if needed
# (use git log or git diff to inspect the changes)

# Merge the changes into your local branch
git merge origin/main
# OR
# Use git pull to fetch and merge in one step
git pull origin main

```

#### Locally Remove and Commit:
**Remove the File Locally:**

- Use the git rm command to remove the file from your local working directory.
```
git rm path/to/file
git rm -r <directory_name> #recursive removal of a directory
```
Replace path/to/file with the actual path to the file you want to delete.

**Commit the Changes:**

- Commit the deletion: 
```
git commit -m "Remove file"
```
##### Unstage the File(s):
- If you want to unstage a specific file, use git reset followed by the file name. For example:
"""
** git reset -- <file>**
"""
- If you want to unstage all files, you can use git reset without specifying a file:
**""git reset""**

#### Deleting untracked files
###### Check Untracked Files:
- First, use the git status command to see which files are untracked: **"Git status"**

###### Preview the Files to be Deleted (Optional):
- You can preview the untracked files that will be deleted by using the -n or --dry-run option with git clean: **"git clean -n"**
###### Delete Untracked Files:
- To permanently delete the untracked files from your repository, use the git clean command with the -f or --force option: **"git clean -f"**
- If you only want to delete untracked directories, you can use the -d option: **"git clean -f -d"**

### File Handling
- Json files
- csv, txt, binary files,
