import data

us_state_abbrev = data.us_state_abbrev
states_list     = data.states_list

#  Sort List
states_list.sort()

def main():
    # Print Specific Item:
    print_entry(1)
    print_entry(10)
    print_entry(45)
    print_entry(27)

    return

def print_entry(entry = 1, input_list =  states_list, input_dict = us_state_abbrev):
    print(f'Entry # {entry}  is: {input_list[entry-1]} or {input_dict.get(input_list[entry-1])}')
    print()
    return

if __name__ == "__main__":
    main()