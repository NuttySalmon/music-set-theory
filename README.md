# Music set theory calculations (post-tonal analysis)

This is a script to assist musical analysis through musical [set theory](https://en.wikipedia.org/wiki/Set_theory_(music)), especially for post-tonal music. Able to calculate:
* [Normal order](https://musictheory.pugetsound.edu/mt21c/PrimeForm.html)
* [Prime form](https://musictheory.pugetsound.edu/mt21c/PrimeForm.html)  (from inversion normal and normal)
* [Interval class vector](https://en.wikipedia.org/wiki/Interval_vector)

with steps output for better understanding the calculation processes and for debugging.

__This script is by no means the most effecient way of calculation. Feel free to collaborate and give suggestions for more features.__

## Dependency:

* Python version >= 3.6
* mingus

## Usage:

Just run the script after installing dependencies and type in notes seprated by space:

E.g. `B Eb C# D G`

Sample output:

    >python set_theory.py
    Type in notes seprated by space then press enter: B Eb C# D G   

    Parse input...

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
    Pitch class (PC) list: [1, 2, 3, 7, 11]
    Normal: B, C#, D, D#, G ([11, 13, 14, 15, 19])
    Inversion: B, D#, E, F, G ([11, 15, 16, 17, 19])
    Inversion normal: D#, E, F, G, B ([15, 16, 17, 19, 23])
    Best normal order: D#, E, F, G, B ([15, 16, 17, 19, 23])
    Prime: [0, 1, 2, 4, 8]
    Interval class vector: <221311> 

