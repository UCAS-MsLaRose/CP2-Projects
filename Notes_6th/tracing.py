# Vienna LaRose, Debugging notes
import trace
import sys

def trace_calls(frame, event, arg):
    if event == 'call': #when the function is called
        print(f'Calling function: {frame.f_code.co_name}')
    elif event == 'line': #when a new line of code happens
        print(f'Executing line {frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'return': #when we return stuff
        print(f'{frame.f_code.co_name} returned {arg}')
    elif event == 'exception': #Tirggered when there is an exception
        print(f'Exception in {frame.f_code.co_name}: {arg}')

    return trace_calls

sys.settrace(trace_calls)
tracer = trace.Trace(count=False, trace=True)
# What is tracing?
def sub(numone, numtwo):
    return numone - numtwo

def add(numone, numtwo):
    print(sub(numone, numtwo))
    return numone + numtwo


print(add(5,2))

#tracer.run('add(8,9)')
#Basic Tracing command
    #python -m trace --trace Notes_6th\tracing.py
"""
    --trace (displays lines as executed)
    --count (displays number of time executed)
    --listfuncs (displays functions used in the program)
    --trackcalls (displays relationships between functions)
"""
# What are some ways we can debug by tracing?
    #Lets you observe what the program is doing without interrupting it
# How do you access the debugger in VS Code?
    #Click the debugger on the left
    #F5 key
    #Dropdown on the play menu
# What is testing?
    #running your code to make sure it works as required, try to break the code

# What are boundary conditions?
    #Check the entries most likely to be wrong
x = 14j
# How do you handle when users give strange inputs?
    #