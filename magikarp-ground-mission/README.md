# Magikarp Ground Mission

## Challenge Information

- **Category**: General Skills
- **Difficulty**: Easy
- **Author**: syreal

## Description

Do you know how to move between directories and read files in the shell? Start the container, ssh to it, and then ls once connected to begin.

Login via ssh as ctf-player with the password, 8c606eb1 on the host wily-courier.picoctf.net and port 53465.

## Solution

### Step 1: Connect via SSH

```bash
ssh ctf-player@wily-courier.picoctf.net -p 53465
# Password: 8c606eb1
```

### Step 2: Explore the home directory

```bash
ls -la
```

Output showed:
- `3of3.flag.txt`
- `drop-in/` directory

### Step 3: Examine the drop-in directory

```bash
ls drop-in/
cat drop-in/1of3.flag.txt
cat drop-in/instructions-to-2of3.txt
```

Found:
- `drop-in/1of3.flag.txt` contained: `picoCTF{xxsh_`
- `drop-in/instructions-to-2of3.txt` contained: `Next, go to the root of all things, more succinctly /`

### Step 4: Follow instructions to find 2of3

```bash
ls /
cat /2of3.flag.txt
```

Found:
- `/2of3.flag.txt` contained: `0ut_0f_//4t3r_`

### Step 5: Find the remaining 3of3

```bash
ls -la
cat 3of3.flag.txt
```

Found:
- `/home/ctf-player/3of3.flag.txt` contained: `0b24fc4f}`

### Step 6: Assemble the complete flag

The three parts combined:
1. `picoCTF{xxsh_`
2. `0ut_0f_//4t3r_`
3. `0b24fc4f}`

**Full flag:** `picoCTF{xxsh_0ut_0f_//4t3r_0b24fc4f}`

## Key Commands Used

- `ssh` - connect to remote server
- `ls` - list directory contents
- `cat` - read file contents
- `find` - search for files

## Flag

```
picoCTF{xxsh_0ut_0f_//4t3r_0b24fc4f}
```
