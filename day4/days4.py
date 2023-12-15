import tools
import re

scratchies = tools.split_by_line(tools.fetch_input('https://adventofcode.com/2023/day/4/input'))
winning_tally = 0
multiple_tally = []
for scratchie in scratchies:
    scratchie_parts = re.split(": | \\| ", scratchie)
    mynumbers = scratchie_parts[2].split()
    winning_numbers = scratchie_parts[1].split()
    print(mynumbers)
    print(winning_numbers)
    this_card_number = int(scratchie_parts[0].split()[1])
    print(this_card_number)
    try:
        multiple_tally[this_card_number-1] += 1
    except IndexError:
        multiple_tally.append(1)
    this_win = 0
    win_count = 0
    for number in mynumbers:
        if number in winning_numbers:
            win_count += 1
            try:
                multiple_tally[this_card_number - 1 + win_count] += multiple_tally[this_card_number - 1]
            except IndexError:
                multiple_tally.append(multiple_tally[this_card_number - 1])
            if this_win == 0:
                this_win = 1
            else:
                this_win = this_win*2
    winning_tally += this_win

print(winning_tally)
print(multiple_tally)
print(sum(multiple_tally))

