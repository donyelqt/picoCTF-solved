# First Grep

## Challenge Information

- **Category**: General Skills
- **Difficulty**: Easy
- **Author**: Alex Fulton/Danny Tunitis

## Description

Can you find the flag in the file? This would be really tedious to look through manually, something tells me there is a better way.

## Solution

### Step 1: Analyze the file

The file contains a lot of garbled text with ANSI escape codes embedded. Manually scanning it is impractical.

### Step 2: Use grep

```bash
grep -a "picoCTF{" file
```

Or with Python to strip ANSI codes and extract the flag automatically.

### Step 3: Extract the flag

The flag embedded in the file:

```
picoCTF{grep_is_good_to_find_things_cEDf1591}
```

## Flag

```
picoCTF{grep_is_good_to_find_things_cEDf1591}
```
