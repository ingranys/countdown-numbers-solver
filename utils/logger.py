def log(obj, msg):
    print('\n>>> {0} {1}'.format(msg.upper(), obj))



def parameters(args,debug=False):
    print('\n>>> PARAMETERS')
    
    # numbers info and size info
    if args.numbers:
        print('Input number(s) : {0}.'.format(args.numbers))
        print('The first {0} number(s) will be considered.'.format(args.size))
    else:
        print('Input number(s) :'\
            ' None given (numbers will be picked randomly).')
    
    # target and use info
    print('The goal is to reach {0} using {1} numbers.'.format(args.target,args.use))

    # solutions
    if args.solutions.upper() == 'EXACT':
        print('We are looking for exact solutions only.')
    elif  args.solutions.upper() == 'APPROXIMATE':
        print('We are looking for exact and approximate solutions' \
                ' (tolerance is {0}).'.format(args.tolerance))
    else :
        raise ValueError('Unexpected value for the argument <solutions> : {0}'.format(args.solutions))

    # output
    if args.output.upper() == 'UNIQUE':
        print('We will filter duplicates and display unique solutions.')    
    elif args.output.upper() == 'ALL':
        print('We will display all solutions, even duplicates' \
                ' (operations order will differ).')
    else:
        raise ValueError('Unexpected value for the argument <output> : {0}'.format(args.output))

    # verbose info    
    if args.verbose == 0:
        pass    
    elif args.verbose == 1:
        print('DEBUG mode has been enabled.')    
    elif args.verbose == 2:
        print('DEBUG mode has been enabled.')
        print('!!!SPAM mode has been enabled!!!')    
    else:
        raise ValueError('Unexpected value for the argument <verbose> : {0}'.format(args.verbose))

    # show technical details if DEBUG mode is enabled
    if debug:
        print('\n---------DEBUG---------')
        print('Technical details about args :')
        for arg in vars(args):
            print(arg, getattr(args, arg))
        print('--------/DEBUG---------')