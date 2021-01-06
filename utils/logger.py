def inputs(args):
    print('>>> PARAMS')
    for arg in vars(args):
        print(arg, getattr(args, arg))

def log(obj, type):
    if type.upper() == 'ARGS':
        inputs(obj)
    elif type.upper() in ['START NUMBERS','TARGET']:
        print('\n>>> {0} {1}'.format(type.upper(), obj))    
    else:
        False
