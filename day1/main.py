# This is a sample Python script.
import tools
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

list_of_nums = [['one','1'],['two','2'],['three','3'],['four','4'],['five','5'],['six','6'],['seven','7'],['eight','8'],['nine','9']]
list_of_smun = [['eno','1'],['owt','2'],['eerht','3'],['ruof','4'],['evif','5'],['xis','6'],['neves','7'],['thgie','8'],['enin','9']]

def find_nums(cal_val: str, nums_list: list) -> str:
    lowest_index = len(cal_val)
    num_to_return = ''
    for num in nums_list:
        if num[0] in cal_val:
            if cal_val.index(num[0]) < lowest_index:
                lowest_index = cal_val.index(num[0])
                num_to_return = num[1]

        if num[1] in cal_val:
            if cal_val.index(num[1]) < lowest_index:
                lowest_index = cal_val.index(num[1])
                num_to_return = num[1]
    return num_to_return

todays_input = tools.fetch_input('https://adventofcode.com/2023/day/1/input')

listed_input = tools.split_by_line(todays_input)
all_cals = []
for cal_val in listed_input:
    this_cal = ''
    this_cal += find_nums(cal_val, list_of_nums)
    val_cal = cal_val[::-1]
    this_cal += find_nums(val_cal, list_of_smun)
    if this_cal != '':
        all_cals.append(int(this_cal))
print(sum(all_cals))


#def print_hi(name):
#    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
## Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')
#
## See PyCharm help at https://www.jetbrains.com/help/pycharm/

