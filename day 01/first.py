"""
Day 1: 
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
Consider your entire calibration document. What is the sum of all of the calibration values?
"""
sum=0
with open('input_a.txt') as file:
    for l in file.readlines():
        l = l.strip()
        # Inizio ad analizzare le righe una alla volta
        print(l)
        # Come scorrere i caratteri da sx verso dx
        for c in l:
            if c.isdigit():
                print(f"Digit found: {c}")
                first = int(c)
                break

        # Come scorrere i caratteri da dx verso sx
        for c in l[::-1]:
            if c.isdigit():
                print(f"Last digit found: {c}")
                last = int(c)
                break

        value = first * 10 + last
        print(f"Value found: {value}")
        sum += value

print(f"Somma totale: {sum}")