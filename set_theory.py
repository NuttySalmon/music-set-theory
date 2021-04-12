#!/usr/bin/env python3
# coding: utf-8

from typing import List, Any
import mingus.core.notes as notes
from mingus.containers.note import Note


def notes_to_pc(note_str_list: List[str]) -> List[int]:
    """Convert note letters to list of pitch class integer notation

    Args:
        note_str_list (str): list of notes

    Returns:
        List[int]: Pitch class integers

    Example:
        >>> notes_to_pc(['C', 'F', 'G#', 'Eb'])
        [0, 3, 5, 8]
    """
    pc_list = []
    for n in note_str_list:
        pc = notes.note_to_int(n)
        pc_list.append(pc)
    pc_list = list(set(pc_list))
    pc_list.sort()
    return pc_list


def note_from_int(pc_list: List[int]) -> List[str]:
    """Inteprete pitch class integers to note names

    Args:
        pc_list (List[int]): pitch class integers

    Returns:
        List[str]: Note names
    """
    interpreted = []
    for pc in pc_list:
        note_interpreted = Note().from_int(pc)
        interpreted.append(note_interpreted.name)
    return interpreted


def format_pc(pc_list: List[int]) -> str:
    """Format pitch class set with note names for printing

    Args:
        pc_list (List[int]): Pitch class integers

    Returns:
        str: Pitch class set with note names
    """
    note_str = ", ".join(note_from_int(pc_list))
    return "{} ({})".format(note_str, pc_list)


def pci_calc(pc_list: List[int]) -> List[int]:
    """Calculate pitch class interval (PCI) for a set. Including from last to\
    first note of set

    Args:
        pc_list (List[int]): pitch class integer set

    Returns:
        List[int]: List of intervals in half step counts
    """
    pci_list = []

    # add first note an octave higher to end of list
    pc_0_oct = pc_list[0] + 12
    pc_list_alt = pc_list + [pc_0_oct]

    # calculate intervals
    for i in range(1, len(pc_list_alt)):
        pci = pc_list_alt[i] - pc_list_alt[i - 1]
        pci_list.append(pci)
    return pci_list


def get_normal_candidate_indices(pci_list: List[int]) -> List[int]:
    """Get the indices in the pitch class set corresponding to the provided\
    PCI list for the candidates to be the starting note of normal, which is\
    the destination of the biggest interval in PCI list.

    Args:
        pci_list (List[int]): List of intervals

    Returns:
        List[int]: Indices for elements to be normal candidate starting note

    Note:
        Result of this function can be feed back to create_normal_candidate
        with the corresponding PC list to create candidate orders.
    """
    max_val = max(pci_list)
    print("Max PCI: {}".format(max_val))
    dest_indices = []
    for i in range(len(pci_list)):
        if pci_list[i] == max_val:
            # loop around
            index = i + 1 if i != len(pci_list) - 1 else 0
            dest_indices.append(index)
    return dest_indices


def create_normal_candidate(pc_list, start_index: int) -> List[int]:
    """Create normal candidate ordering form the pitch class list with element\
    at the given index as the starting note.

    Args:
        pc_list ([type]): [description]
        start_index (int): [description]

    Returns:
        List[int]: [description]
    """
    first_half = pc_list[start_index:]
    second_half = pc_list[:start_index]
    # transpose second half an octave up
    second_half = [pc + 12 for pc in second_half]
    return first_half + second_half


def indices_with_value(iter: List[Any], val: Any) -> List[int]:
    """Get all the indices in list of elements with the given value

    Args:
        iter (List): List to search
        val (Any): value to match

    Returns:
        List[int]: Indices for matching elements

    Example:
        >>> indices_with_value(['a', 'b', 'c', 'b'], 'b')
        [1, 3]
    """
    indices = []
    for index in range(len(iter)):
        if iter[index] == val:
            indices.append(index)
    return indices


def most_compact(candidates: List[List[int]]) -> List[int]:
    """Find most compact among cnadidates by comparing intervals starting from\
    second to last note with first not

    Args:
        candidates (List[List[int]]): Candidates ordering in pitch set integer

    Returns:
        [type]: [description]
    """

    # index to start comparing with 1st note in ordering
    index_compare = len(candidates[0]) - 1

    # comparing pci from the first note starting second to last
    for target_index in reversed(range(1, index_compare)):
        print("Comparing PCI for {}-th note and 1st...".format(target_index + 1))
        pcis = []
        for candidate in candidates:
            pci = candidate[target_index] - candidate[0]
            pcis.append(pci)

        min_pci = min(pcis)  # get minimum pci as ideal
        print("Min PCI: {}".format(min_pci))

        # find all candidates that has the minimum PCI for the comparison
        min_candidiates_indices = indices_with_value(pcis, min_pci)

        # return result if only one with minimum
        if len(min_candidiates_indices) == 1:
            print("Most compact found.")
            return candidates[min_candidiates_indices[0]]
        else:  # tie exists. eliminiation if more than one has minimum
            new_candidates = []
            # keep only candidates with minimum
            for index in min_candidiates_indices:
                new_candidates.append(candidates[index])
            candidates = new_candidates
            print("tie exists, elimination result: {}".format(candidates))

    # NOTE: all tied if function run to this point
    # if all comparisons are equal get one with lowest pitch class
    print("Last comparison tied. Selecting lowest PC.")

    # get candidate starting pitch class
    candidate_starts = [candidate[0] for candidate in candidates]
    min_pc = min(candidate_starts)

    # get candidate with the lowest pitch class
    most_compact_index = candidate_starts.index(min_pc)
    most_compact = candidates[most_compact_index]
    return most_compact


def get_normal(pc_list: List[int]) -> List[int]:
    """Calculate normal form

    Args:
        pc_list (List[int]): pitch class integers for set

    Returns:
        List[int]: Normal form calculated notated in pitch class interger
    """
    pci_list = pci_calc(pc_list)  # get list of intervals between pitch classes
    print("Pitch class interval (PCI) list: {}".format(pci_list))

    # get candidates starting notes for potential normal form
    normal_candidate_indices = get_normal_candidate_indices(pci_list)
    # create candidates
    normal_candidates = [
        create_normal_candidate(pc_list, index) for index in normal_candidate_indices
    ]
    print("candidates: {}".format(normal_candidates))
    # get most compact as normal form
    normal = most_compact(normal_candidates)
    print("Selected normal: {}".format(normal))
    return normal


def make_inversion(normal: List[int]) -> List[int]:
    """Calculate inversion from provided normal form

    Args:
        normal (List[int]): [description]

    Returns:
        List[int]: [description]
    """
    normal_pcis = pci_calc(normal)  # get intervals for normal
    print("PCI of normal: {}".format(normal_pcis))

    # invert the intervals (remove the last one because it is not needed)
    inverted_pcis = list(reversed(normal_pcis[: len(normal) - 1]))
    print("Inverted PCI: {}".format(inverted_pcis))

    # calculate notes in inversion
    normal_inversion = [normal[0]]
    for i in range(len(normal) - 1):
        new_note = normal_inversion[i] + inverted_pcis[i]
        normal_inversion.append(new_note)
    return normal_inversion


def prime_calc(pc_set: List[int]) -> List[int]:
    """Calculate prime form from best normal form

    Args:
        pc_set (List[int]): Best normal order as pitch class integers

    Returns:
        List[int]: Prime form numbers
    """
    pc_sorted = sorted(pc_set)
    prime = [pc - pc_sorted[0] for pc in pc_sorted]
    return prime


def get_interval_classes(prime_form: List[int]) -> List[int]:
    """Get all the interval classes

    Args:
        prime_form (List[int]): Prime form

    Returns:
        List[int]: Interval classses

    Note:
        Interval class outputnumber should be within the range of 1 to 6
    """
    interval_classes = []

    # calculate all PCI combinations
    for i in range(len(prime_form)):
        # set current element as lower note
        low = prime_form[i]
        # calculate PCI with all elements after current element as higher note
        for high in prime_form[i + 1 :]:
            pci = high - low  # calculate half steps
            # get interval class
            interval_class = pci if pci <= 6 else 12 - pci
            interval_classes.append(interval_class)
    return interval_classes


def icv_calc(prime_form: List[int]) -> List[int]:
    """Calculate the interval class vector (ICV) from given prime form

    Args:
        prime_form (List[int]): Prime form

    Returns:
        List[int]: Interval classs vector
    """
    prime_form.sort()  # make sure sorted
    interval_classes = get_interval_classes(prime_form)
    print("Interval classes: {}".format(interval_classes))
    icv = icv_summing(interval_classes)
    print(icv)
    return icv


def icv_summing(interval_classes: List[int]) -> List[int]:
    """Counting the provided interval classes to form ICV

    Args:
        interval_classes (List[int]): Interval classes in 1 to 6

    Returns:
        List[int]: The count of interval class with [0] for class 1\
            [1] for class 2 etc.
    """
    icv = [0, 0, 0, 0, 0, 0]
    for interval_class in interval_classes:
        index = interval_class - 1
        icv[index] = icv[index] + 1

    return icv


def parse_notes_str(input_str: str) -> List[int]:
    """Parse space seprated note names to pitch class integers

    Args:
        input_str (str): Space seprated note names

    Returns:
        List[int]: Pitch class integers
    """
    n_list = input_str.split(" ")
    n_list = list(filter(None, n_list))  # remove empty strings
    pc_list = notes_to_pc(n_list)
    pc_list.sort()
    return pc_list


if __name__ == "__main__":
    user_input = input("Type in notes seprated by space then press enter: ")
    print("\nParse input...")
    pc_list = parse_notes_str(user_input)
    print("\n----- Calculate normal -----")
    normal = get_normal(pc_list)
    print("\n----- Calculate inversion -----")
    inversion = make_inversion(normal)
    print(inversion)
    print("\n----- Calculate inversion normal -----")
    inversion_normal = get_normal(inversion)
    print("\n----- Find best normal order -----")
    best = most_compact([normal, inversion, inversion_normal])
    print(best)
    print("\nCalculate prime form...")
    prime_form = prime_calc(best)
    print("\n----- Calculate ICV -----")
    icv = icv_calc(prime_form)
    print("\n========= RESULTS =========")
    print("Pitch class (PC) list: {}".format(pc_list))
    print("Normal: {}".format(format_pc(normal)))
    print("Inversion: {}".format(format_pc(inversion)))
    print("Inversion normal: {}".format(format_pc(inversion_normal)))
    print("Best normal order: {}".format(format_pc(best)))
    print("Prime: {}".format(prime_calc(best)))
    icv_str = "".join([str(n) for n in icv])
    print("Interval class vector: <{}>".format(icv_str))
