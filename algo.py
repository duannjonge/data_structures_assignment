def is_balanced(expression):
    stack = []  # Initialize an empty stack to keep track of open brackets

    # Define a dictionary to map closing brackets to their corresponding open brackets
    bracket_mapping = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in '([{':
            # If the character is an open bracket, push it onto the stack
            stack.append(char)
        elif char in ')]}':
            # If the character is a closing bracket, check if the stack is empty
            if not stack:
                return False  # Unmatched closing bracket, expression is not balanced

            # Pop the top element from the stack
            top_element = stack.pop()

            # Check if the popped open bracket matches the current closing bracket
            if bracket_mapping[char] != top_element:
                return False  # Mismatched brackets, expression is not balanced

    # After processing all characters, the expression is balanced if the stack is empty
    return len(stack) == 0


expression1 = "([]{})"
expression2 = "([)]"


#Question Two 

def remove_duplicates(sequence):
    pass
    # new_list=[ for item in sequence]
    return list(set(sequence))

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)


