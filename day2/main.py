import tools

cubes_shown = tools.fetch_input('https://adventofcode.com/2023/day/2/input')

cubes_list = tools.split_by_line(cubes_shown)
valid_game_ids = []

for game in cubes_list:

    game_id = game[game.index(" ")+1: game.index(":")]

    turns = game[game.index(":")+2:].split("; ")

    #is_valid = 1
    max_r = 0
    max_g = 0
    max_b = 0
    for turn in turns:

        handful = turn.split(", ")

        for blocks in handful:

            num_in_hand = ''
            for letter in blocks:
                if letter.isnumeric():
                    num_in_hand += letter
                if letter.isalpha():
                    if letter == 'r':
                        if int(num_in_hand) > max_r:
                            max_r = int(num_in_hand)
                        #if int(num_in_hand) > 12:
                        #    is_valid = 0
                        #    print('game '+game_id+' is invalid')
                    elif letter == 'g':
                        if int(num_in_hand) > max_g:
                            max_g = int(num_in_hand)
                        #if int(num_in_hand) > 13:
                        #    is_valid = 0
                        #    print('game ' + game_id + ' is invalid')
                    elif letter == 'b':
                        if int(num_in_hand) > max_b:
                            max_b = int(num_in_hand)
                        #if int(num_in_hand) > 14:
                        #    is_valid = 0
                        #    print('game ' + game_id + ' is invalid')
                    break
    valid_game_ids.append(max_b * max_g * max_r)
    #if is_valid == 1:
    #    valid_game_ids.append(int(game_id))

print(sum(valid_game_ids))
