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
               (div, '/',   '({0} * {1})'),
               (idiv, '^/', '({1} * {0})')]



def check(numbers,expressions,target,solutions,approximations,tolerance=10,use='some',verbose=False,stage=''):

    # enforce rule on number usage before checking numbers for a potential soluton
    if use.upper() == 'SOME' or (use.upper() == 'ALL' and len(numbers)==1):

        ## look for exact solution
        if target in numbers:
            target_index = numbers.index(target)
            solution = '{0} = {1}'.format(expressions[target_index],numbers[target_index])
            solutions.append(solution)
            print('{0} SOLUTION : {1}'.format(stage,solution)) if verbose else False
        ## look for an approximation
        for number in numbers:
            if number in list(range(target - tolerance,target + tolerance + 1)):
                approx_index = numbers.index(number)
                approximation = '{0} = {1}'.format(expressions[approx_index],numbers[approx_index])
                approximations.append(approximation)
                print('{0} APPROXIMATION : {1}'.format(stage,solution)) if verbose else False



# most of the job is done here
def recurse(numbers,expressions,target,solutions,approximations,tolerance=10,use='some',verbose=False,stage=''):
    new_stage = stage.strip() + '--- '
    n_numbers = len(numbers)

    # first check if we found solutions
    check(numbers,expressions,target,solutions,approximations,tolerance,use,verbose,new_stage)

    # keep on computing while two or more numbers left    
    if n_numbers > 1:
        print('{0} NUMBERS : {1}'.format(new_stage,numbers)) if verbose else False
        for i in range(n_numbers):
            for j in range(i+1,n_numbers):   
                
                print('{0} i: {1} - j: {2}'.format(new_stage,i,j)) if verbose else False
                for op in operations:
                    print('{0} {1}'.format(new_stage,op[1])) if verbose else False
                    operand = op[0]

                    updated_numbers = numbers[:]                  
                    updated_numbers[i]= operand(numbers[i],numbers[j])
                    del updated_numbers[j]                

                    updated_expressions = expressions[:]
                    updated_expressions[i] = op[2].format(updated_expressions[i], updated_expressions[j])
                    del updated_expressions[j]

                    print('{0} {1}'.format(new_stage,updated_numbers)) if verbose else False
                    print('{0} {1}'.format(new_stage,updated_expressions)) if verbose else False

                    # check that newly computed number is valid
                    if None not in updated_numbers:
                        recurse(updated_numbers,updated_expressions,target,solutions,approximations,tolerance,use,verbose,new_stage)
                    else:
                        print('{0} {1}'.format(new_stage,'> unauthorized values')) if verbose else False
    else:
        print('{0} FINAL VALUE : {1}'.format(new_stage,numbers)) if verbose else False


def solve(numbers,target,tolerance=10,use='some',verbose=False):

    expressions = numbers[:]
    solutions = []
    approximations = []
    recurse(numbers,expressions,target,solutions,approximations,tolerance,use,verbose)

    return solutions, approximations