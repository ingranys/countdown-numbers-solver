from sympy import sympify,srepr

def output(values,displayname='',output='unique',debug=False):
    
    # solver may find the same solution many times
    # we filter all duplicates before deep dive
    values = list(set(values))

    ## values might be different but still refering to the same set of operations
    ## SPOILER : we heavily rely on sympy librairies to filter out duplicates!
    # first we simplify mathematical expressions 
    # (remove unnecessary brackets and keep right-hand side only)
    simplified_expressions = [sympify(value.split(" =", 1)[0],evaluate=False) for value in values]
    
    # then we build expression trees that represent the set of operation in a conceptual manner
    # same solutions may have different simplified expressions but always have the same tree
    tree_expressions = ['{0}'.format(srepr(simplified_expression)) for simplified_expression in simplified_expressions]
    
    # now we can filter solutions putting all them in a dictionnary
    # and by using each corresponding expression tree as key
    unambiguous_solutions = {}
    for i in range(len(tree_expressions)):
        unambiguous_solutions[tree_expressions[i]] = values[i]


    # filtering is done > TIME TO PRINT OUTPUT

    ## print header according do displayname and filter
    if output.upper() in ['ALL','UNIQUE']:
        print('\n>>> {0} {1}'.format(output.upper(), displayname.upper()))
    else:
        # unepexted value for output arg
        raise ValueError('Unexpected value for the argument <output> : {0}'.format(output))

    ## more info when debug mode is enabled
    if debug:
        print('---------DEBUG---------')
        print('{0} | {1} | {2}'.format('SOLUTION','SIMPLIFIED EXPRESSION','EXPRESSION TREE'))
        for i in range(len(values)):
            print('{0} | {1} | {2}'.format(values[i],simplified_expressions[i],tree_expressions[i]))
        print('--------/DEBUG---------')

    ## print values depending on what is required
    ### output all solutions when required > VALUES
    if output.upper() == 'ALL':
        # verify if empty        
        if values:   
            for value in values:
                print(value)
        else:
            # print default message whem empty
            print('None found...')  
    ### output needs to be unique values > UNAMBIGUOUS SOLUTIONS
    elif output.upper() == 'UNIQUE':
        # verify if empty 
        if unambiguous_solutions:
            for _ ,value in unambiguous_solutions.items():
                print(value)    
        else :
            # print default message whem empty
            print('None found...')
    ### unepexted value for output arg
    else:
        raise ValueError('Unexpected value for the argument <output> : {0}'.format(output))