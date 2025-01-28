## Advent of Code 2023 - Day 1: Historian Hysteria 🎅🎄

This repository contains my solutions for Day 1 of the Advent of Code 2023 challenge, "Historian Hysteria".

### Problem Description 🔍

The Chief Historian has gone missing, leaving behind a mess of notes and lists of historically significant locations. Two groups of Elves are trying to create a complete list of these locations, but their lists are not very similar. Your task is to help them reconcile their lists by calculating the total distance between corresponding numbers on the lists.

### Input Format 📝

The input consists of two lists of numbers, one per line. Each number represents a unique location ID.

**Example Input:**

```
3   4
4   3
2   5
1   3
3   9
3   3
```

### Solution Approach 💡

1. **Parse the input:** Read the input file and store the two lists of numbers.
2. **Sort the lists:** Sort the numbers in each list in ascending order.
3. **Calculate distances:** Iterate through both lists simultaneously, pairing up corresponding numbers and calculating the absolute difference between them.
4. **Sum the distances:** Add up all the calculated distances to get the final result.

### Code Structure 💻

The solution is implemented in Python. The main script `day1.py` contains the core logic for parsing the input, calculating the distances, and printing the result.

### Running the Code 🏃‍♀️

To run the code, simply execute the following command in your terminal:

```bash
python day1.py
```

The script will read the input from the `input.txt` file and print the total distance between the lists.

### Notes 📝

- The code assumes that the input file is named `input.txt` and is located in the same directory as the script.
- The solution can be adapted to different programming languages and input formats.

### Further Exploration 🤔

- Can you optimize the code for better performance? 🏎️
- How would you handle cases where the lists have different lengths? 📏
- Can you generalize the solution to handle more than two lists? 🧮

I hope this README page provides a helpful overview of my solution to Day 1 of the Advent of Code 2023. Happy coding! 🎉 
