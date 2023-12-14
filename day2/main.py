import tools

possibles = [['red', 12], ['blue', 13], ['green', 14]]

cubes_shown = tools.fetch_input('https://adventofcode.com/2023/day/2/input')
#print(cubes_shown)
cubes_list = tools.split_by_line(cubes_shown)
valid_game_ids = []
for game in cubes_list:
    print(game)
    game_id = game[game.index(" ")+1: game.index(":")]
    print(game_id)
    turns = game[game.index(":")+2:].split("; ")
    print(turns)
    #is_valid = 1
    max_r = 0
    max_g = 0
    max_b = 0
    for turn in turns:
        handful = turn.split(", ")
        print(handful)

        for blocks in handful:
            print(blocks)
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
    #            #print(game_id)
print(sum(valid_game_ids))
