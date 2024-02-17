def names(lst):
    for name in lst:
        print(name)
    return None


if __name__ == "__main__": # self test code
    print(__name__)
    lst_ = ['Rogers', 'Kelvin', 'Caroline']
    names(lst_)
else:
    print("Running your script else where.")
