#decorators are used to modify funcitons adding new bahaviours
#it is a function that takes a function as input and modifies the function and outputs the modified version 

def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce #this is adding the decorator to the funtion hello
def hello():
    print("Hello, world")

hello()
