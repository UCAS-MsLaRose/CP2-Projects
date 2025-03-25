# Vienna larose, Tracing Notes

# What is tracing?
# Debugging method that lets you see what is happening with your functions
# python -m trace --trackcalls C:\Users\Vienna.LaRose\Documents\CP2_Projects\Notes_2nd\tracing.py

"""
--trace
--count
--listfuncs (displays the functions in the project)
--trackcalls (displays relationships between the functions)
"""
import trace
import sys

tracer = trace.Trace(count=False, trace=True)
def trace_calls(frame, event, arg):
    if event == 'call':
        print(f'Calling function: {frame.f_code.co_name}')
    elif event == 'line':
        print(f'Executing line: {frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'return':
        print(f'{frame.f_code.co_name} returned {arg}')
    elif event == 'exception':
        print(f'Exception in {frame.f_code.co_name}: {arg}')
    return trace_calls

sys.settrace(trace_calls)
"""
Event types:
call - When the function is called
line - when a new ine is executed
return - when the function returns a value
exception - when there is an exception raised
"""

# What are some ways we can debug by tracing?
    #Make a function that lets us see how our functions are interacting and running

# How do you access the debugger in VS Code?
    #F5
# What is testing?
    #Going through the code trying to break it, have testers be not the preson who wrote the code

# What are boundary conditions?
    #User conditions that are strange and/or likely to cause issues
age = 18
if age >= 18:
    print("You can vote")
elif age >= 16:
    print("You can drive")
elif age == 15:
    print("You can get learners permit")
elif age >= 5:
    print("You can go to school")
else:
    print("You are too young to do things!")

# How do you handle when users give strange inputs?

def sub(numone, numtwo):
    print( numone-numtwo)

def add(numone, numtwo):
    sub(numone, numtwo)
    return numone+numtwo


print(add(5,4))
sub(8,2)

#tracer.run('sub(8,2)')