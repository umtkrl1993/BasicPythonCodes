from collections import deque

bracket_dict = {}

bracket_dict['('] = ')'
bracket_dict[')'] = '('
bracket_dict['['] = ']'
bracket_dict[']'] = '['
bracket_dict['{'] = '}'
bracket_dict['}'] = '{'


def isBalanced(s):

	bracket_list = list(s)
	bracket_stack = []

	for bracket in bracket_list:
		if bracket == '(' or bracket == '[' or bracket == '{':
			bracket_stack.append(bracket)

		elif bracket == ')':
			if len(bracket_stack) == 0:
				return "NO"
			if bracket_stack[-1] != '(':
				return "NO"
			bracket_stack.pop()

		elif  bracket == "]":
			if len(bracket_stack) == 0:
				return "NO"
			if bracket_stack[-1] != '[':
				return "NO"
			bracket_stack.pop()

		elif bracket == "}":
			if len(bracket_stack) == 0:
				return "NO"
			if bracket_stack[-1] != '{':
				return "NO"
			bracket_stack.pop()

	if len(bracket_stack) == 0:
		return "YES"
	else:
		return "NO"




input_ = raw_input()

print isBalanced(input_)



