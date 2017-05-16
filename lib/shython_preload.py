
import sys

def line_trace(frame, event, arg):
    print('EVENT:'),
    print(type(event)),
    print(event),
    print(dir(event))

    if event != 'line':
        return

    print('TRACE:shython_line:LINE:\"%s\"' % (arg,))

if __name__ == "__main__":
    print('TRACING')
    sys.settrace(line_trace)
