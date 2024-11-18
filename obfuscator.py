import re
import random
import string
import sys

# Utility function to generate a random string
def generate_random_name(length=4):  # Reduced length for shorter names
    return ''.join(random.choices(string.ascii_letters, k=length))

# Remove all comments from the code
def remove_comments(code):
    # Remove single-line comments
    code = re.sub(r'//.*', '', code)
    # Remove multi-line comments
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    return code

# Extract and preserve preprocessor directives from obfuscation
def extract_preprocessor_directives(code):
    directives = re.findall(r'^(#\s*include\s*<.*?>|#\s*define\s+.*?$)', code, flags=re.MULTILINE)
    for directive in directives:
        code = code.replace(directive, '')
    return code, directives

# Reinsert preserved preprocessor directives at the beginning of the code
def reinsert_preprocessor_directives(code, directives):
    return '\n'.join(directives) + '\n' + code

# Minify the code by removing unnecessary whitespaces and newlines
def minify_code(code):
    # Remove leading and trailing whitespace from each line
    lines = [line.strip() for line in code.splitlines()]
    # Join lines together, keeping important newlines for readability
    minified_code = '\n'.join([line for line in lines if line])
    return minified_code

# Rename local variables to obfuscated names, preserving string literals, directives, and function parameters
# Less aggressive approach to avoid breaking functionality
def rename_identifiers(code):
    # Preserve string literals by temporarily replacing them with markers
    string_literals = re.findall(r'"(.*?)"', code)
    for i, literal in enumerate(string_literals):
        code = code.replace(f'"{literal}"', f'__STRING_LITERAL_{i}__')
    
    # Find all words that could be variable or function names
    identifiers = set(re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code))
    
    # Reserved keywords in C that should not be renamed
    reserved_keywords = {
        'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern',
        'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
        'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while', 'printf', 'strcpy', 'strlen', 'strstr'
    }

    # Identify user-defined functions by looking for their definitions
    user_defined_functions = set(re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\s*\(', code))
    user_defined_functions = {func.strip().rstrip('(') for func in user_defined_functions}
    
    # Identify function parameters and global variables to avoid renaming them
    function_parameters = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\(', code)
    function_parameters = {param.split()[1].strip() for param in function_parameters}
    
    # Identify local variables by looking for definitions inside functions
    local_variables = set(re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\s+[a-zA-Z_][a-zA-Z0-9_]*\s*;', code))
    local_variables = {var.split()[1].strip() for var in local_variables if var.split()[1].strip() not in reserved_keywords}
    
    # Create a mapping of identifiers to obfuscated names, excluding critical identifiers
    obfuscation_map = {}
    for identifier in local_variables:
        if identifier not in reserved_keywords and identifier not in user_defined_functions and identifier not in function_parameters:
            obfuscation_map[identifier] = generate_random_name()

    # Replace identifiers in the code with their obfuscated names
    for identifier, obfuscated_name in obfuscation_map.items():
        code = re.sub(r'\b' + re.escape(identifier) + r'\b', obfuscated_name, code)
    
    # Restore string literals
    for i, literal in enumerate(string_literals):
        code = code.replace(f'__STRING_LITERAL_{i}__', f'"{literal}"')
    
    return code

# Main function to obfuscate the C code
def obfuscate_c_code(code):
    # Step 1: Extract preprocessor directives
    code, directives = extract_preprocessor_directives(code)
    # Step 2: Remove comments
    code = remove_comments(code)
    # Step 3: Minify the code
    code = minify_code(code)
    # Step 4: Rename identifiers (only local variables)
    code = rename_identifiers(code)
    # Step 5: Reinsert preserved preprocessor directives
    code = reinsert_preprocessor_directives(code, directives)
    return code

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python obfuscator.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Read the input file
    with open(input_file, 'r') as file:
        original_code = file.read()

    # Obfuscate the code
    obfuscated_code = obfuscate_c_code(original_code)

    # Write the obfuscated code to the output file
    with open(output_file, 'w') as file:
        file.write(obfuscated_code)

    print(f"Obfuscated code has been written to {output_file}")