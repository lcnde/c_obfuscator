# Readme

## Automated tests

The `automate.sh` shell script is designed to assist in testing the obfuscation of C code. For each
test, the script will:

1. Obfuscate the code.
2. Compile both the original and obfuscated versions.
3. Compare the output of the two.

If the outputs are identical, it indicates that the obfuscation process has successfully preserved
the functionality of the code (at least in theory).

For the script to work properly, please place your test files in the `./tests` directory. Name the
files using the format `test-$`, where `$` is a sequentially increasing number (e.g., `test-1`,
`test-2`, etc.).

## Test files

To ensure the effectiveness of the obfuscator, C test files should use a range of file structures
and features that the obfuscator is expected to handle without compromising the integrity of the
code. By creating more complex test files, we can better identify potential issues within the
obfuscation process, allowing for fixes and improvements.

The output of the obfuscated test file will be compared against the original test file output. If
the outputs match, it confirms that the obfuscation process has successfully preserved the original
functionality of the code. This approach is essential for validating the reliability and robustness
of the obfuscator.

### Test 1

- Includes Standard Libraries: #include <stdio.h> and #include <string.h> are used for console
  logging and string manipulation.
- Array Handling: A sample array of integers is printed element-by-element.
- Switch Case: A switch statement tests branching behavior.
- If-Else: Demonstrates conditional branching logic.
- Loops: A for loop prints the squares of the first 5 numbers.
- String Manipulation: A checkString function checks for the presence of a substring and modifies
  the string.
- Function Calls: The main function calls printArray and checkString to test function handling.
