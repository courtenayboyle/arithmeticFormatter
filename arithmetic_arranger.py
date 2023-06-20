import math

def arithmetic_arranger(problems, calc=False):
		first_row = ''
		sec_row = ''
		lines = ''
		sum_row = ''
		
		#splitting the problem apart
		for problem in problems:
				#["32", "+", "8"]
				item = problem.split(' ')
				first = item[0]
				operator = item[1]
				second = item[2]
				answer = ''

				#Error Handling
				if operator not in "-+" :
						return "Error: Operator must be '+' or '-'."
				if (len(first) > 4) or (len(second) > 4) :
						return "Error: Numbers cannot be more than four digits."
				if not first.isnumeric() or not second.isnumeric() :
						return "Error: Numbers must only contain digits."
				if calc:
						answer = str(int(first) + int(second)) if operator == '+' else str(int(first) - int(second) )
				if len(problems) > 5 :
						return "Error: Too many problems."
				
				#put to R aligned
				length = max(len(first), len(second)) + 2
				top = first.rjust(length)
				bottom = operator + str(second).rjust(length -1)
				line = ''
				total = answer.rjust(length)
				for i in range(length) :
						line = line + '-'

				#insert spaces
				if problem != problems[-1] :
						first_row += top + '    '
						sec_row += bottom + '    '
						lines += line + '    '
						sum_row += total + '    '
				else:
						first_row += top
						sec_row += bottom 
						lines += line 
						sum_row += total 

		if calc:
				arranged_problems = (first_row + '\n') + (sec_row + '\n') + (lines + '\n') + sum_row
		else:
				arranged_problems = (first_row + '\n') + (sec_row + '\n') + lines							
		#print(arranged_problems)
		return arranged_problems


