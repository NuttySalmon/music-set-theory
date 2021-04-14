# Music set theory calculations (post-tonal analysis)

Calculation tool to assist music theory analysis that uses [musical set theory](https://en.wikipedia.org/wiki/Set_theory_(music)), especially for post-tonal music. Able to calculate:
* [Normal order](https://musictheory.pugetsound.edu/mt21c/PrimeForm.html)
* [Prime form](https://musictheory.pugetsound.edu/mt21c/PrimeForm.html)  (from inversion normal and normal)
* [Interval class vector](https://en.wikipedia.org/wiki/Interval_vector)
* All prime forms for all subset combinations of a given subset size

with steps output for better understanding the calculation processes and for debugging.

__This script is by no means the most effecient way of calculation. Feel free to collaborate and give suggestions for more features.__

## Dependency

* Python version >= 3.6
* mingus


## Usage
#### Setup
1. Before running any scripts, make sure correct Python 3 and Pip are installed on computer
2. clone repo and install dependencies:

        git clone https://github.com/NuttySalmon/music-set-theory.git
        cd music-set-theory
        pip3 install -r requirements.txt


#### Calculating for single set:

1. In the project directory, run script: 

        python3 ./set_theory.py 

2. Following on screen prompt, input notes seprated by space. E.g. `B Eb C# D G`.
3. Once result is displayed, users can enter new set of notes for another calculation.


#### Calculating all prime form values for subsets of given size:

1. In project directory, run script: 

        python3 ./subsets_prime.py 

2. Following on screen prompt, input notes and the number of notes to pick from set for combinations.
3. Once result is displayed, users can enter new set of parameters for calculation.

`Ctrl + C` to quit Python.


## Sample outputs

#### For single set calculation: 

    > python3 set_theory.py
    *****Set Theory Calculator*****
    Type in notes in set (seprated by space Eg: C Eb G F#), then press enter. Type "exit" to quit.

    Note set: B Eb C# D G
    Parsing input...

    ----- Calculate normal -----
    Pitch class interval (PCI) list: [1, 1, 4, 4, 2]
    Max PCI: 4
    candidates: [[7, 11, 13, 14, 15], [11, 13, 14, 15, 19]]
    Comparing PCI for 4-th note and 1st...
    Min PCI: 4
    Most compact found.
    Selected normal: [11, 13, 14, 15, 19]

    ----- Calculate inversion -----
    PCI of normal: [2, 1, 1, 4, 4]
    Inverted PCI: [4, 1, 1, 2]
    [11, 15, 16, 17, 19]

    ----- Calculate inversion normal -----
    Pitch class interval (PCI) list: [4, 1, 1, 2, 4]
    Max PCI: 4
    candidates: [[15, 16, 17, 19, 23], [11, 15, 16, 17, 19]]
    Comparing PCI for 4-th note and 1st...
    Min PCI: 4
    Most compact found.
    Selected normal: [15, 16, 17, 19, 23]

    ----- Find best normal order -----
    Comparing PCI for 4-th note and 1st...
    Min PCI: 4
    tie exists, elimination result: [[11, 13, 14, 15, 19], [15, 16, 17, 19, 23]]
    Comparing PCI for 3-th note and 1st...
    Min PCI: 2
    Most compact found.
    [15, 16, 17, 19, 23]

    Calculate prime form...

    ----- Calculate ICV -----
    Interval classes: [1, 2, 4, 4, 1, 3, 5, 2, 6, 4]
    [2, 2, 1, 3, 1, 1]

    ========= RESULTS =========
    Original input: B Eb C# D G
    Pitch class (PC) list: [1, 2, 3, 7, 11]
    Normal: B, C#, D, D#, G ([11, 13, 14, 15, 19])
    Inversion: B, D#, E, F, G ([11, 15, 16, 17, 19])
    Inversion normal: D#, E, F, G, B ([15, 16, 17, 19, 23])
    Best normal order: D#, E, F, G, B ([15, 16, 17, 19, 23])
    Prime: [01248]
    Interval class vector: <221311>

    Note set: 


#### Calculating for subsets:

    > python3 subsets_prime.py
    Notes (leave empty to use previous): C E G F#
    Pick: 3
    [(0, 4, 6), (0, 4, 7), (0, 6, 7), (4, 6, 7)]

    ...

and finally:

    ======================
    RESULTS
    ======================
    Pick 3 from C E G F#:
    C, E, F#: [026]
    C, E, G: [037]
    C, F#, G: [016]
    E, F#, G: [013]