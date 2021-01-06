from sympy import sympify,srepr

def output(values,displayname='',output='unique'):
    
    unique_values = list(set(values))

    if output.upper() == 'ALL':
        print('\n>>> ALL {0}'.format(displayname.upper()))        
        for unique_value in unique_values:
            print(unique_value)

    elif output.upper() == 'UNIQUE':
        print('\n>>> UNIQUE {0}'.format(displayname.upper()))
        simplified_expressions = [sympify(unique_value.split(" =", 1)[0],evaluate=False) for unique_value in unique_values]
        tree_expressions = ['{0}'.format(srepr(simplified_expression)) for simplified_expression in simplified_expressions]
        unambiguous_solutions = {}
        for i in range(len(tree_expressions)):
            unambiguous_solutions[tree_expressions[i]] = unique_values[i]
            #print('{0} | {1} | {2}'.format(tree_expressions[i],simplified_expressions[i],unique_values[i]))
        for _ ,value in unambiguous_solutions.items():
            print(value)
        #print("\n".join("{}\t{}".format(value, key) for key, value in unambiguous_solutions.items()))
    
    else:
        False