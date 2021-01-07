# countdown-numbers-solver
A Python implementation of a solver for [Countdown Numbers Game, ](https://en.wikipedia.org/wiki/Countdown_(game_show)#Numbers_round) including a wide variety of options.

As a reminder here is a **game demo**
<img src="https://github.com/ingranys/countdown-numbers-solver/blob/master/visuals/countdown.gif">

Want to have fun? [:point_right:Play the game:point_left:](https://incoherency.co.uk/countdown/practice/#numbers)

Want to get a closer look at the rules and approaches to solve? [:point_right:See blog article:point_left:](https://datagenetics.com/blog/august32014/index.html)


<!-- GETTING STARTED -->
## Getting Started

Get a local copy up and run main script.

### Prerequisites
* python3 [:link:](https://www.python.org/downloads/)
* sympy [:link:](https://docs.sympy.org/latest/index.html)
  ```sh
  pip install sympy
  ```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/ingranys/countdown-numbers-solver.git
   ```
2. Make sure python3 is installed
   ```sh
   python3 --version
   ```
3. Make sure sympy is installed (see above)
   ```sh
   python3 -c 'import sympy; print("sympy is installed")'
   ```

### Examples
Run script **with numbers and a target**.
```
$ python3 countdown.py -n 100 25 10 3 2 1 -t 784
```
<details>
  <summary>:heavy_plus_sign: See output</summary>
  
  ```
  
  >>> PARAMETERS
  Input number(s) : [100, 25, 10, 3, 2, 1].
  The first 6 number(s) will be considered.
  The goal is to reach 784 using some numbers.
  We are looking for exact solutions only.
  We will filter duplicates and display unique solutions (the order of the operations is ignored).

  >>> START NUMBERS [100, 25, 10, 3, 2, 1]

  >>> TARGET 784

  >>> UNIQUE EXACT SOLUTIONS
  ((100 - 2) * (((10 + 1) * 3) - 25)) = 784
  ((100 - (3 - 1)) * (10 - 2)) = 784
  ((100 - 2) * ((25 - 1) / 3)) = 784
  ((100 + ((25 - 1) / 2)) * (10 - 3)) = 784
  ((100 - 2) * ((10 - 3) + 1)) = 784
  ((100 - 2) * (10 - (3 - 1))) = 784
  (((100 - 3) + 1) * (10 - 2)) = 784
  ```
</details>

Run script **without providing numbers or a target** (solver will _generate random values instead_).
```
$ python3 countdown.py
```
<details>
  <summary>:heavy_plus_sign: See ouput</summary>
  
  ```
  
  >>> PARAMETERS
  Input number(s) : None given (6 numbers will be picked randomly).
  The goal is to reach 559 using some numbers.
  We are looking for exact solutions only.
  We will filter duplicates and display unique solutions (the order of the operations is ignored).

  >>> START NUMBERS [9, 10, 4, 3, 5, 1]

  >>> TARGET 559

  >>> UNIQUE EXACT SOLUTIONS
  (9 + (10 * (((4 * 3) - 1) * 5))) = 559
  ((((9 + 5) * 4) * 10) - 1) = 559
  (((9 - 1) + 5) * ((10 * 4) + 3)) = 559
  (((((9 + 5) * 10) - 1) * 4) + 3) = 559
  ((9 * (((4 * 3) * 5) + 1)) + 10) = 559
  ((9 + 4) * ((10 * (5 - 1)) + 3)) = 559
  ((9 * ((10 * 5) + (4 * 3))) + 1) = 559
  (((((9 + 3) * 5) - 4) * 10) - 1) = 559
  ```
</details>

Run script and look for **approximate answers as well**.
```
$ python3 countdown.py
```
<details>
  <summary>:heavy_plus_sign: See ouput</summary>
  
  ```
  
  >>> PARAMETERS
  Input number(s) : None given (6 numbers will be picked randomly).
  The goal is to reach 559 using some numbers.
  We are looking for exact solutions only.
  We will filter duplicates and display unique solutions (the order of the operations is ignored).

  >>> START NUMBERS [9, 10, 4, 3, 5, 1]

  >>> TARGET 559

  >>> UNIQUE EXACT SOLUTIONS
  (9 + (10 * (((4 * 3) - 1) * 5))) = 559
  ((((9 + 5) * 4) * 10) - 1) = 559
  (((9 - 1) + 5) * ((10 * 4) + 3)) = 559
  (((((9 + 5) * 10) - 1) * 4) + 3) = 559
  ((9 * (((4 * 3) * 5) + 1)) + 10) = 559
  ((9 + 4) * ((10 * (5 - 1)) + 3)) = 559
  ((9 * ((10 * 5) + (4 * 3))) + 1) = 559
  (((((9 + 3) * 5) - 4) * 10) - 1) = 559
  ```
</details>

<!-- USAGE EXAMPLES -->
## Usage
```
$ python3 countdown.py  [-h] [-n [[...]]] [--size [3..10]] [-u [all|some]]
                        [-t [100..999]] [-s [approximate|exact]]
                        [--tolerance [1..10]] [-o [all|unique]] [-v [0|1|2]]

```
The script is run via the commant-line. Many options are available but the solver can be executed without providing any (will use default values instead).

<details>
  <summary>:heavy_plus_sign: Details</summary>
  
  
**Numbers to be used**
* `-n` (or `--numbers`):  &nbsp;
Numbers to be used to reach target.
  - According to the game rules all values must be in {1,2,3,4,5,6,7,8,9,10,25,50,75,100}.
  - By default, values are generated randomly.
* `--size`:               &emsp;&emsp;&emsp;&emsp;&emsp;
Maximum number or values to be used.
  - Serves as protection to prevent runtime error.
  - Must be an integer value between 1 and 10.
  - By default, we only keep the 6 first values.
* `-u` (or `--use`):      &emsp;&emsp;
Rule for numbers that must used.
  - Muse be `all` or `some`.
  - When set to `all`, solver will ensure that all numbers are used in the solutions (as per official rules). Otherwise, solver will also consider _partial solutions_ that use only some of the numbers.
  - By default, solver will be set to `some`.
  
  
**Target**
* `-t` (or `--target`):   &emsp;
Target value (the goal is to reach that value).
  - According to the game rules this value must be integer between 100 and 999.
  - By default, value is generated randomly.
  
**Constraints on solution**
* `-s` (or `-solutions`): &nbsp;
Type of solutions we are looking for.
  - Must be `approximate` or `exact`.
  - When set to `approximate`, solver will allow approximate answers as well (answers that are a little bit off). Otherwise solution must reach the exact value for target. 
  - By default, solver will be set to `exact`.
* `--tolerance`:          &emsp;&emsp;&emsp;
Tolerance range for approximate solutions.
  - Must be an integer value between 1 and 10.
  - Solutions that reach a value in the range [`target`-`tolerance`:`target`+`tolerance`] will be considered as valid approximate answers.
  - This is useful only in combination with `-s approximate`. Otherwise approximate answers are unathorized and won't be printed anyway.
  - By default, tolerance is set to 10.

**Output results**
* `-o` (or `--output`):   &emsp;
Type of filter to applied to output.
  - Must be `all` or `unique`.
  - When set to `all`, all found solutions will printed, even duplicates. For example : `(((75 * 25) / 5) - ((100 + 1) + 6)) = 268` and `(((75 / 5) * 25) - ((100 + 1) + 6)) = 268`are different solutions but they represent the same set of operations (only the order varies), hence they are duplicates.
  - When set to `unique`, all duplicates are filtered out and only unique solutions are printed.
  - By default, solver will be set to `unique`.

**Verbose**
* `-` (or `--verbose`):   &emsp;
Verbose level for logging
  - Different logging levels are provided for a comprehensive approach. Higher the value, higher the level of logging.
  - Must be an integer value between 0 and 2.
  - `0` is INFO mode, only inputs and outputs are printed.
  - `1` is DEBUG mode, add useful information and technical details for debugging purpose.
  - `2` is SPAM mode, describe every single step of the algorithm and enable DEBUG mode, very useful when trying to visualize how the solver works but not very practical. 
  - Be careful when entering SPAM mode since a huge amount of logs will be generated. Solver won't be able to complete the task within reasonable time unless it has be given a very small set of numbers.
  - By default, the level is 0. Only ouputs are printed, everything else is hidden behind the curtain.
</details>

---
<!-- LICENSE -->
## License :scroll:

Distributed under the GNU General Public License v3.0. See `LICENSE`[:link:](https://github.com/ingranys/countdown-numbers-solver/blob/main/LICENSE) for more information.


<!-- CONTACT -->
## Contact :handshake:

Mustapha Gaies - [@ingranys](https://github.com/ingranys) - ingranys@protonmail.com

Project Link: [https://github.com/ingranys/countdown-numbers-solver](https://github.com/ingranys/countdown-numbers-solver)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements :pray:
* [DataGenetics - Countdown Game Show](https://datagenetics.com/blog/august32014/index.html)
* [James Stanley Practice](https://incoherency.co.uk/countdown/practice/#numbers)
* [James Stanley Sovler](https://incoherency.co.uk/countdown/) 
* [Github - cmdouglas/countdown_numbers](https://github.com/cmdouglas/countdown_numbers)
* [Github - cawhitworth/countdown.py](https://github.com/cawhitworth/countdown.py)
* [Github - othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template/edit/master/README.md)
* [Github - https://github.com/ikatyang/emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet)
* [Github - pierrejoubert73/markdown-details-collapsible.md](https://gist.github.com/pierrejoubert73/902cc94d79424356a8d20be2b382e1ab)
