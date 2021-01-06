from sympy import sympify,srepr

def output(values,displayname='',output='unique',debug=False):
    
    # solver may find the same solution many times
    # we filter all duplicates before deep dive
    values = list(set(values))

    # output all solutions when required > EASY!
    if output.upper() == 'ALL':
        print('\n>>> ALL {0}'.format(displayname.upper()))        
        for value in values:
            print(value)

    # output needs to be unique values > ROUGH! 
    ## values might be different but still refering to the same set of operations
    ## SPOILER : we heavily rely on sympy librairies!
    elif output.upper() == 'UNIQUE':
        print('\n>>> UNIQUE {0}'.format(displayname.upper()))
        # more info when debug mode is enabled
        if debug:
            print('---------DEBUG---------')
            print('{0} | {1} | {2}'.format('SOLUTION','SIMPLIFIED EXPRESSION','EXPRESSION TREE'))
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
            # more info when debug mode is enabled
            if debug:
                print('{0} | {1} | {2}'.format(values[i],simplified_expressions[i],tree_expressions[i]))
        # more info when debug mode is enabled
        if debug:
            print('--------/DEBUG---------')

        # done < print unique solutions now
        for _ ,value in unambiguous_solutions.items():
            print(value)    
    else:
        False