def trace_calls(frame, event, arg):
    if event == 'call':
        print(f'Calling function: {frame.f_code.co_name}')
    
    return trace_calls

sys.settrace(trace_calls)