from itertools import combinations
from set_theory import parse_notes_str, calc, note_from_int, NoteFormatError

if __name__ == "__main__":
    prev_input = ""  # save input from previous loop
    pc_list = None
    pick = 0

    # infinite loop
    while True:
        user_input = input("\nNotes (leave empty to use previous): ")

        # check note input
        try:
            # use previous input if empty
            if len(user_input.strip()) == 0:
                user_input = prev_input
                print("Using previous: {}".format(user_input))

            pc_list = parse_notes_str(user_input)

            if len(pc_list) == 0:  # check empty input
                print("!! ERROR: empty list !!")
                continue
        except NoteFormatError:
            print("!! ERROR: Invalid input !!")
            continue

        prev_input = user_input  # save input for next time if valid

        # check pick number input
        try:
            pick = int(input("Pick: "))
            if pick <= 0:
                raise ValueError
            if pick > len(pc_list):  # check pick number too big
                print("!! ERROR: picking more than set size !!")
                continue
        except ValueError:
            print("!! ERROR: Invalid input !!")
            continue

        all_prime = dict()  # to store results

        # get all combinations
        all_combinations = list(combinations(pc_list, pick))
        print(all_combinations)

        # calculate for each combination
        for curr_pc_list in all_combinations:
            curr_pc_list = list(curr_pc_list)
            notes_str = ", ".join(note_from_int(curr_pc_list))
            print("\n********** Calculation: {} ***********".format(notes_str))
            result = calc(curr_pc_list)
            prime_str = "".join([str(num) for num in result["prime"]])
            all_prime[notes_str] = prime_str

        # output results
        print("\n======================\nRESULTS \n======================")
        print("Pick {} from {}:".format(pick, user_input))
        for notes_str, prime in all_prime.items():
            print("{}: [{}]".format(notes_str, prime))
