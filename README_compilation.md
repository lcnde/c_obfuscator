# Compilation Process with Hardening

```bash
# Compile source.c into binary
$ gcc -O3 -flto -fomit-frame-pointer -ffunction-sections -fdata-sections -Wl,--gc-sections source.c -o binary
$ strip --strip-all binary
```

## 1. Basic Compilation Flags

### -O3 (Optimization Level 3)

- Enables all optimizations that don't involve a space-speed tradeoff
- Performs:
  - Function inlining
  - Loop unrolling
  - Vector operations
  - Constant propagation
  - Dead code elimination
  - Register allocation optimization

### -flto (Link Time Optimization)

- Enables optimizations across source files
- Stores compiler's internal representation in object files
- During linking:
  - Performs whole-program analysis
  - Can eliminate unused code more effectively
  - Can inline functions across source files

### -fomit-frame-pointer

- Frees up a register by not maintaining frame pointer
- Makes stack traces harder to construct
- Slightly improves performance
- Makes debugging more difficult

### -ffunction-sections -fdata-sections

- Places each function and data item in its own section
- Allows unused sections to be removed during linking
- Works with --gc-sections linker flag

### -Wl,--gc-sections

- Garbage collects unused sections during linking
- Removes unreachable functions and data
- Reduces binary size
- Makes code flow harder to analyze

## 2. Example Compilation Command

```bash
gcc -O3 -flto -fomit-frame-pointer -ffunction-sections -fdata-sections \
    -Wl,--gc-sections source.c -o output_program
```

## 3. Stripping Process

### strip --strip-all

Removes:

- All symbols
- Debug information
- Type information
- Symbol tables
- Relocation information
- String tables
- Line numbers
- Wide-char information

Effect on binary:

- Significantly reduced file size
- Removed function names
- Removed variable names
- Removed source file information
- Removed debugging hooks

### Verification Commands

```bash
# Check binary size before stripping
ls -l output_program

# Apply stripping
strip --strip-all output_program

# Check binary size after stripping
ls -l output_program

# Verify symbols are removed
nm output_program

# Check what information remains
readelf -a output_program
```

## 4. Result

The final binary will have these characteristics:

- Highly optimized machine code
- No debug symbols or metadata
- Minimal size
- Original functionality preserved
- Maximum difficulty for reverse engineering tools
- No source code information
- No function or variable names
- Optimized code paths that may not match source structure

## 5. Important Notes

1. These optimizations are irreversible
2. The binary will be harder to debug
3. Stack traces will be less informative
4. Crash reports will contain less useful information
5. Some security tools may have trouble analyzing the binary
6. Performance will typically be better than unoptimized code
