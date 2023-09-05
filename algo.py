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


# test output 

print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False


#Question Two 
def remove_duplicates(sequence):
    """
    This function removes duplicates from a sequence while maintaining the original order of elements.
    Args:
        sequence: A list or tuple.
    Returns:
        A new sequence with duplicates removed.
    """
    # Check if the input sequence is valid.
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("The input sequence must be a list or tuple.")
    
    # Create a new list to store the unique elements while preserving order.
    unique_elements = []
    
    # Iterate through the original sequence, adding elements to the new list if not already present.
    for element in sequence:
        if element not in unique_elements:
            unique_elements.append(element)
    
    return unique_elements


# def remove_duplicates(sequence):
#     # new_list=[ for item in sequence]
#     return list(set(sequence))

# input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
# result = remove_duplicates(input_sequence)



#Question Three


import string

def word_frequency(sentence):
    translator = str.maketrans('', '', string.punctuation)  # Create a translation table to remove punctuation
    words = sentence.lower().translate(translator).split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

sentence = "This is a test sentence. This sentence is just a test."
result = word_frequency(sentence)
print(result)



