from itertools import combinations
from set_theory import parse_notes_str, calc, note_from_int

if __name__ == "__main__":
    while True:
        user_input = input("Notes: ")
        pick = input("Pick: ")
        pc_list = parse_notes_str(user_input)

        all_prime = dict()
        all_combinations = list(combinations(pc_list, int(pick)))
        print(all_combinations)
        for curr_pc_list in all_combinations:
            curr_pc_list = list(curr_pc_list)
            result = calc(curr_pc_list)
            notes_str = ", ".join(note_from_int(curr_pc_list))
            prime_str = ''.join([str(num) for num in result['prime']])
            all_prime[notes_str] = prime_str
        print("\n====== RESULTS ======")
        for notes_str, prime in all_prime.items():
            print("{}: [{}]".format(notes_str, prime))
