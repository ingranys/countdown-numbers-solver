add = lambda a,b: a+b
sub = lambda a,b: a-b if a>b else None
osub = lambda a,b: b-a if b>a else None
mul = lambda a,b: a*b
div = lambda a,b: a//b if a % b == 0 else None
idiv = lambda a,b: b//a if b % a == 0 else None


operations = [ (add, '+',   '({0} + {1})'),
               (sub, '-',   '({0} - {1})'),
               (osub,'^-', '({1} - {0})'),
               (mul, '*',   '({0} * {1})'),
               (div, '/',   '({0} / {1})'),
               (idiv, '^/', '({1} / {0})')]


# check if numbers contain a solution (either exact or approximate)
def check(numbers,expressions,target,solutions,approximations,tolerance=10,use='some',verbose=False,stage=''):

    # enforce rule on number usage before checking numbers for a potential solution
    ## use='some' > we can look for a solution no matter how many numbers are remaining
    ## use='all' > make sure there is no remaining numbers before looking for a solution
    if use.upper() == 'SOME' or (use.upper() == 'ALL' and len(numbers)==1):

        # we always look for both exact and approximate solutions
        # if we find one, we store the mathematical expression used to find the solution (set of operations)

        ## look for an exact solution
        if target in numbers:
            target_index = numbers.index(target)
            solution = '{0} = {1}'.format(expressions[target_index],numbers[target_index])
            solutions.append(solution)
            print('{0} EXACT SOLUTION FOUND : {1}'.format(stage,solution)) if verbose else False

        ## look for an approximate solution
        for number in numbers:
            ## consider approximate solution that are not exact solution (number must be different from target)
            if (number in list(range(target - tolerance,target + tolerance + 1))) and (number!=target):
                approx_index = numbers.index(number)
                approximation = '{0} = {1}'.format(expressions[approx_index],numbers[approx_index])
                approximations.append(approximation)
                print('{0} APPROXIMATE SOLUTION FOUND : {1}'.format(stage,approximation)) if verbose else False
    
    else:
        # unexpected value for use argument (should be 'some' or 'all')
        raise ValueError('Unexpected value for the argument <use> : {0}'.format(use))



# most of the job is done here
def recurse(numbers,expressions,target,solutions,approximations,tolerance=10,use='some',verbose=False,stage=''):
    
    n_numbers = len(numbers)            # will be useful to implement loops over number
    new_stage = stage.strip() + '--- '  # crank up log level at each recursive call

    # first check if numbers cocntains solutions
    check(numbers=numbers,
            expressions=expressions,
            target=target,
            solutions=solutions,
            approximations=approximations,
            tolerance=tolerance,
            use=use,
            verbose=verbose,
            stage=new_stage)

    # keep on computing while two or more numbers left    
    if n_numbers > 1:
        print('{0} Current number(s) {1} corresponding to the following expression(s) {2}'.format(new_stage,numbers,expressions)) if verbose else False
        # go through all unique pairs in the list (order is ignored)
        for i in range(n_numbers):
            for j in range(i+1,n_numbers):
                # apply each possible operations to these two numbers
                # (+) > add, (-) > substract, (^-)> switch order then substract ,(x) > multiply, (/) > divide, (/) > switch order then divide 
                # applying (^-) and (^/) allow us to ignore order when picking pair of number which saves time   
                for op in operations:
                    print('{0} Apply operation ({1}) to numbers of indexes (i={2},j={3}) in {4}'.format(new_stage,op[1],i,j,numbers)) if verbose else False
                    operand = op[0]

                    updated_numbers = numbers[:]                  
                    updated_numbers[i]= operand(numbers[i],numbers[j])
                    del updated_numbers[j]                

                    updated_expressions = expressions[:]
                    updated_expressions[i] = op[2].format(updated_expressions[i], updated_expressions[j])
                    del updated_expressions[j]

                    print('{0} Number(s) become(s) {1} corresponding to the following expression(s) {2}'.format(new_stage,updated_numbers,updated_expressions)) if verbose else False

                    # check that newly computed number is valid
                    if None not in updated_numbers:
                        # valid > next recursive call
                        recurse(numbers=updated_numbers,
                                expressions=updated_expressions,
                                target=target,
                                solutions=solutions,
                                approximations=approximations,
                                tolerance=tolerance,
                                use=use,
                                verbose=verbose,
                                stage=new_stage)
                    else:
                        # not valid > stop because of the rules (all values must be postive integers at any given time)
                        print('{0} STOP. Unauthorized expression...'.format(new_stage)) if verbose else False
    
    # no more numbers to crunch > time to stop
    else:
        print('{0} FINAL VALUE is {1} corresponding to this expression {2}'.format(new_stage,numbers,expressions)) if verbose else False



# start solver
def solve(numbers,target,tolerance=10,use='some',verbose=False):

    # initialize lists for results
    expressions = numbers[:]
    solutions = []
    approximations = []

    # launch recursive call
    recurse(numbers=numbers,
            expressions=expressions,
            target=target,
            solutions=solutions,
            approximations=approximations,
            tolerance=tolerance,
            use=use,
            verbose=verbose)

    return solutions, approximations