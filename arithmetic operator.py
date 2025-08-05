
def arithmetic_arranger(problems, show_answers=False):
    first_line=[]
    second_line=[]
    dashes=[]
    answers=[]
    if len(problems)>5:#Error1
        return 'Error: Too many problems.'    
    
    for problem in problems:
        one,op,two=problem.split()
        if op not in ['-','+']:#Error2
            return"Error: Operator must be '+' or '-'."
            
        if not one.isdigit() or not two.isdigit():#Error3
            return'Error: Numbers must only contain digits.'
        
        if len(one)>4 or len(two)>4:#Error4
            return'Error: Numbers cannot be more than four digits.'
            break
        width=max(len(one),len(two))+2
        first_line.append(one.rjust(width))
        second_line.append(op+two.rjust(width-1))
        dashes.append("-"*width)
        answers.append(str(eval(one+op+two)).rjust(width))

    arranger="    ".join(first_line)+'\n'+\
             "    ".join(second_line)+'\n'+\
             "    ".join(dashes)
    if show_answers:
        arranger+="\n"+"    ".join(answers)
    return arranger
    
        


print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')






















