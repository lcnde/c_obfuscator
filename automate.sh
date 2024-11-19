#!/bin/bash

# Check if one parameter is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <directory_name>"
    exit 1
fi

# Step 1: Set the parameter and create the directory
param="$1"
output_dir="./outputs"
tests_dir="./tests"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir/$param"

# Step 2: Use Python to run a command with the parameter
python3 obfuscator.py "$tests_dir/${param}.c" "$output_dir/$param/${param}_obfuscated.c"
# Check if the command failed
if [ $? -ne 0 ]; then
    echo "Error: The obfuscation command failed for ${param}."
    # You can also exit the script if you want
    exit 1
fi
# Set obfuscated file to read-only
chmod 444 ""$output_dir/$param/${param}_obfuscated.c""


# Step 3: Compile the C programs from the specified directory
# Original code
gcc "$tests_dir/${param}.c" -o "$output_dir/$param/${param}_compiled"
# Obfuscated code
gcc "$output_dir/$param/${param}_obfuscated.c" -o "$output_dir/$param/${param}_obfuscated_compiled"

# # Step 4: Run both programs and capture their outputs
output1=$("$output_dir/$param/${param}_compiled")
output2=$("$output_dir/$param/${param}_obfuscated_compiled")

# echo $output1
# echo $output2

# Compare the outputs
if [ "$output1" == "$output2" ]; then
    echo "Outputs are equal."
else
    echo "Outputs are not equal."
fi

# Clean up the compiled files (optional)
rm -rf "$output_dir/${param}"
