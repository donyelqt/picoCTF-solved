# Tab, Tab, Attack

## Challenge Information

- **Category**: General Skills
- **Difficulty**: Easy
- **Author**: syreal

## Description

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames.

## Approach

### Step 1: Extract the archive

```bash
unzip Addadshashanammu.zip
```

The challenge hints that the solution involves tab completion through a long, nested directory structure.

### Step 2: Navigate to the final file

After unzipping, the path to the binary/executable file was extremely long and deeply nested. The hint mentioned this can be solved with **11 button-presses (mostly Tab)**, meaning using tab completion in the terminal to auto-complete the long directory and filename.

Rather than typing the full path, use tab completion to quickly navigate to:

```
Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet
```

### Step 3: Read the flag

The file `fang-of-haynekhtnamet` (with no extension) is an executable binary. Running it directly or reading its contents reveals the flag:

```
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}
```

## Key Takeaway

This challenge emphasizes the power of **tab completion** in Unix-like terminals — it's especially useful when dealing with Cthulhu-inspired, ridiculously long filenames and directory structures.

## Flag

```
picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}
```
