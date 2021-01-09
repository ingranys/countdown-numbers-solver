## Countdown Numbers Solver

  
<!-- PROJECT SHIELDS -->
<!-- Shields are generated dynamically using shield.io with static parameters
URL endpoint is https://img.shields.io/badge/<LABEL>-<MESSAGE>-<COLOR>
Emoji characters are also supported as <LABEL> or <MESSAGE>
Go to https://apps.timwhitlock.info/emoji/tables/unicode and find Bytes (UTF-8) for your emoji, replace "\x" by "%" and use as <LABEL> or <MESSAGE>
Example for smiling face : (Bytes UTF-8) \xF0\x9F\x98\x83 > (<MESSAGE>) %F0%9F%98%83 
-->
[![license: GPLv3](https://img.shields.io/badge/licence-GPLv3-orange)](https://www.gnu.org/licenses/gpl-3.0)
[![python: 3.0](https://img.shields.io/badge/python-3.0-blue)](https://www.python.org/)
[![release version](https://img.shields.io/badge/release-v0.3.0-green)](https://github.com/ingranys/countdown-numbers-solver)
[![maintened](https://img.shields.io/badge/maintened-%E2%9C%94-green)](https://github.com/ingranys/countdown-numbers-solver/commits/)

A Python implementation of a solver for [Countdown Numbers Game, ](https://en.wikipedia.org/wiki/Countdown_(game_show)#Numbers_round) including a wide variety of options.

As a reminder here is a **game demo**:

<p align="center">
  <img src="https://github.com/ingranys/countdown-numbers-solver/blob/main/visuals/countdown.gif" height="350">
</p>

Want to have fun? [:point_right:Play the game:point_left:](https://incoherency.co.uk/countdown/practice/#numbers)

Want to get a closer look at the rules and approaches to solve? [:point_right:See blog article:point_left:](https://datagenetics.com/blog/august32014/index.html)


<!-- TABLE OF CONTENTS -->
<!-- Generated automatically (update when saving) using VS Code extension Markdown All in One
-- See https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one 
-->
## Table of Contents
- [Countdown Numbers Solver](#countdown-numbers-solver)
- [Table of Contents](#table-of-contents)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Examples](#examples)
- [Usage](#usage)
- [How It Works](#how-it-works)
  - [The algorithm](#the-algorithm)
  - [Filtering](#filtering)
  - [Complexity](#complexity)
  - [Optimisations](#optimisations)
- [Documentation](#documentation)
  - [Changelog](#changelog)
  - [Docstrings](#docstrings)
  - [Comments](#comments)
- [License :scroll:](#license-scroll)
- [Contact :handshake:](#contact-handshake)
- [Acknowledgements :pray:](#acknowledgements-pray)

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
</details><br />

Run script with numbers and a target and **enforce the use of all number**.
```
$ python3 countdown.py -n 100 25 10 3 2 1 -t 784 -u all
```
<details>
  <summary>:heavy_plus_sign: See output</summary>
  
  ```
  
  >>> PARAMETERS
  Input number(s) : [100, 25, 10, 3, 2, 1].
  The first 6 number(s) will be considered.
  The goal is to reach 784 using all numbers.
  We are looking for exact solutions only.
  We will filter duplicates and display unique solutions.

  >>> START NUMBERS [100, 25, 10, 3, 2, 1]

  >>> TARGET 784

  >>> UNIQUE EXACT SOLUTIONS
  ((100 + ((25 - 1) / 2)) * (10 - 3)) = 784
  ((100 - 2) * (((10 + 1) * 3) - 25)) = 784
  ```
</details><br />

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
</details><br />

Run script and look for **approximate answers as well**.
```
$ python3 countdown.py -n 100 75 50 25 1 3 -t 823 -s approximate --tolerance 1 -o unique
```
<details>
  <summary>:heavy_plus_sign: See ouput</summary>
  
  ```
  
  >>> PARAMETERS
  Input number(s) : [100, 75, 50, 25, 1, 3].
  The first 6 number(s) will be considered.
  The goal is to reach 823 using some numbers.
  We are looking for exact and approximate solutions (tolerance is 1).
  We will filter duplicates and display unique solutions.

  >>> START NUMBERS [100, 75, 50, 25, 1, 3]

  >>> TARGET 823

  >>> UNIQUE EXACT SOLUTIONS
  None found...

  >>> UNIQUE APPROXIMATE SOLUTIONS
  (((((100 / 25) * 50) + 75) - 1) * 3) = 822
  (((((100 / 25) * 50) + 75) * 3) - 1) = 824
  (((75 * (50 * (25 - 3))) / 100) - 1) = 824
  (((75 * (25 - 3)) / (100 / 50)) - 1) = 824
  (((((100 * 25) - 75) + 50) / 3) - 1) = 824
  ((((100 * 25) - (75 - 50)) / 3) - 1) = 824
  ((((100 * (75 - 50)) - 25) / 3) - 1) = 824
  ```
</details><br />

Run script and enable **DEBUG mode**.
```
$ python3 countdown.py -n 25 100 1 7 1 5 -t 563 -v 1
```
<details>
  <summary>:heavy_plus_sign: See ouput</summary>
  
  ```
  
  >>> PARAMETERS
  Input number(s) : [25, 100, 1, 7, 1, 5].
  The first 6 number(s) will be considered.
  The goal is to reach 563 using some numbers.
  We are looking for exact solutions only.
  We will filter duplicates and display unique solutions.
  DEBUG mode has been enabled.

  ---------DEBUG---------
  Technical details about args :
  numbers [25, 100, 1, 7, 1, 5]
  size 6
  use some
  target 563
  solutions exact
  tolerance 10
  output unique
  verbose 1
  --------/DEBUG---------

  >>> START NUMBERS [25, 100, 1, 7, 1, 5]

  >>> TARGET 563

  >>> UNIQUE EXACT SOLUTIONS
  ---------DEBUG---------
  SOLUTION | SIMPLIFIED EXPRESSION | EXPRESSION TREE
  (((100 - 1) * 7) - ((25 + 1) * 5)) = 563 | -5*(1 + 25) + (100 + (-1)*1)*7 | Add(Mul(Integer(-1), Mul(Integer(5), Add(Integer(1), Integer(25)))), Mul(Integer(7), Add(Integer(100), Mul(Integer(-1), Integer(1)))))
  --------/DEBUG---------
  (((100 - 1) * 7) - ((25 + 1) * 5)) = 563

  ```
</details><br />

Run script on a very simple example and **enable SPAM mode to investigate how the solver works**.
```
$ python3 countdown.py -n 100 6 10 -t 104 -s approximate --tolerance 5 -o all -v 2
```
<details>
  <summary>:heavy_plus_sign: See ouput</summary>
  
  ```
  
  >>> PARAMETERS
  Input number(s) : [100, 6, 10].
  The first 6 number(s) will be considered.
  The goal is to reach 104 using some numbers.
  We are looking for exact and approximate solutions (tolerance is 5).
  We will display all solutions, even duplicates (operations order will differ).
  DEBUG mode has been enabled.
  !!!SPAM mode has been enabled!!!

  ---------DEBUG---------
  Technical details about args :
  numbers [100, 6, 10]
  size 6
  use some
  target 104
  solutions approximate
  tolerance 5
  output all
  verbose 2
  --------/DEBUG---------

  >>> START NUMBERS [100, 6, 10]

  >>> TARGET 104
  ---  APPROXIMATE SOLUTION FOUND : 100 = 100
  ---  Current number(s) [100, 6, 10] corresponding to the following expression(s) [100, 6, 10]
  ---  Apply operation (+) to numbers of indexes (i=0,j=1) in [100, 6, 10]
  ---  Number(s) become(s) [106, 10] corresponding to the following expression(s) ['(100 + 6)', 10]
  ------  APPROXIMATE SOLUTION FOUND : (100 + 6) = 106
  ------  Current number(s) [106, 10] corresponding to the following expression(s) ['(100 + 6)', 10]
  ------  Apply operation (+) to numbers of indexes (i=0,j=1) in [106, 10]
  ------  Number(s) become(s) [116] corresponding to the following expression(s) ['((100 + 6) + 10)']
  ---------  FINAL VALUE is [116] corresponding to this expression ['((100 + 6) + 10)']
  ------  Apply operation (-) to numbers of indexes (i=0,j=1) in [106, 10]
  ------  Number(s) become(s) [96] corresponding to the following expression(s) ['((100 + 6) - 10)']
  ---------  FINAL VALUE is [96] corresponding to this expression ['((100 + 6) - 10)']
  ------  Apply operation (^-) to numbers of indexes (i=0,j=1) in [106, 10]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(10 - (100 + 6))']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (*) to numbers of indexes (i=0,j=1) in [106, 10]
  ------  Number(s) become(s) [1060] corresponding to the following expression(s) ['((100 + 6) * 10)']
  ---------  FINAL VALUE is [1060] corresponding to this expression ['((100 + 6) * 10)']
  ------  Apply operation (/) to numbers of indexes (i=0,j=1) in [106, 10]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['((100 + 6) / 10)']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (^/) to numbers of indexes (i=0,j=1) in [106, 10]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(10 / (100 + 6))']
  ------  STOP. Unauthorized expression...
  ---  Apply operation (-) to numbers of indexes (i=0,j=1) in [100, 6, 10]
  ---  Number(s) become(s) [94, 10] corresponding to the following expression(s) ['(100 - 6)', 10]
  ------  Current number(s) [94, 10] corresponding to the following expression(s) ['(100 - 6)', 10]
  ------  Apply operation (+) to numbers of indexes (i=0,j=1) in [94, 10]
  ------  Number(s) become(s) [104] corresponding to the following expression(s) ['((100 - 6) + 10)']
  ---------  EXACT SOLUTION FOUND : ((100 - 6) + 10) = 104
  ---------  FINAL VALUE is [104] corresponding to this expression ['((100 - 6) + 10)']
  ------  Apply operation (-) to numbers of indexes (i=0,j=1) in [94, 10]
  ------  Number(s) become(s) [84] corresponding to the following expression(s) ['((100 - 6) - 10)']
  ---------  FINAL VALUE is [84] corresponding to this expression ['((100 - 6) - 10)']
  ------  Apply operation (^-) to numbers of indexes (i=0,j=1) in [94, 10]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(10 - (100 - 6))']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (*) to numbers of indexes (i=0,j=1) in [94, 10]
  ------  Number(s) become(s) [940] corresponding to the following expression(s) ['((100 - 6) * 10)']
  ---------  FINAL VALUE is [940] corresponding to this expression ['((100 - 6) * 10)']
  ------  Apply operation (/) to numbers of indexes (i=0,j=1) in [94, 10]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['((100 - 6) / 10)']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (^/) to numbers of indexes (i=0,j=1) in [94, 10]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(10 / (100 - 6))']
  ------  STOP. Unauthorized expression...
  ---  Apply operation (^-) to numbers of indexes (i=0,j=1) in [100, 6, 10]
  ---  Number(s) become(s) [None, 10] corresponding to the following expression(s) ['(6 - 100)', 10]
  ---  STOP. Unauthorized expression...
  ---  Apply operation (*) to numbers of indexes (i=0,j=1) in [100, 6, 10]
  ---  Number(s) become(s) [600, 10] corresponding to the following expression(s) ['(100 * 6)', 10]
  ------  Current number(s) [600, 10] corresponding to the following expression(s) ['(100 * 6)', 10]
  ------  Apply operation (+) to numbers of indexes (i=0,j=1) in [600, 10]
  ------  Number(s) become(s) [610] corresponding to the following expression(s) ['((100 * 6) + 10)']
  ---------  FINAL VALUE is [610] corresponding to this expression ['((100 * 6) + 10)']
  ------  Apply operation (-) to numbers of indexes (i=0,j=1) in [600, 10]
  ------  Number(s) become(s) [590] corresponding to the following expression(s) ['((100 * 6) - 10)']
  ---------  FINAL VALUE is [590] corresponding to this expression ['((100 * 6) - 10)']
  ------  Apply operation (^-) to numbers of indexes (i=0,j=1) in [600, 10]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(10 - (100 * 6))']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (*) to numbers of indexes (i=0,j=1) in [600, 10]
  ------  Number(s) become(s) [6000] corresponding to the following expression(s) ['((100 * 6) * 10)']
  ---------  FINAL VALUE is [6000] corresponding to this expression ['((100 * 6) * 10)']
  ------  Apply operation (/) to numbers of indexes (i=0,j=1) in [600, 10]
  ------  Number(s) become(s) [60] corresponding to the following expression(s) ['((100 * 6) / 10)']
  ---------  FINAL VALUE is [60] corresponding to this expression ['((100 * 6) / 10)']
  ------  Apply operation (^/) to numbers of indexes (i=0,j=1) in [600, 10]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(10 / (100 * 6))']
  ------  STOP. Unauthorized expression...
  ---  Apply operation (/) to numbers of indexes (i=0,j=1) in [100, 6, 10]
  ---  Number(s) become(s) [None, 10] corresponding to the following expression(s) ['(100 / 6)', 10]
  ---  STOP. Unauthorized expression...
  ---  Apply operation (^/) to numbers of indexes (i=0,j=1) in [100, 6, 10]
  ---  Number(s) become(s) [None, 10] corresponding to the following expression(s) ['(6 / 100)', 10]
  ---  STOP. Unauthorized expression...
  ---  Apply operation (+) to numbers of indexes (i=0,j=2) in [100, 6, 10]
  ---  Number(s) become(s) [110, 6] corresponding to the following expression(s) ['(100 + 10)', 6]
  ------  Current number(s) [110, 6] corresponding to the following expression(s) ['(100 + 10)', 6]
  ------  Apply operation (+) to numbers of indexes (i=0,j=1) in [110, 6]
  ------  Number(s) become(s) [116] corresponding to the following expression(s) ['((100 + 10) + 6)']
  ---------  FINAL VALUE is [116] corresponding to this expression ['((100 + 10) + 6)']
  ------  Apply operation (-) to numbers of indexes (i=0,j=1) in [110, 6]
  ------  Number(s) become(s) [104] corresponding to the following expression(s) ['((100 + 10) - 6)']
  ---------  EXACT SOLUTION FOUND : ((100 + 10) - 6) = 104
  ---------  FINAL VALUE is [104] corresponding to this expression ['((100 + 10) - 6)']
  ------  Apply operation (^-) to numbers of indexes (i=0,j=1) in [110, 6]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(6 - (100 + 10))']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (*) to numbers of indexes (i=0,j=1) in [110, 6]
  ------  Number(s) become(s) [660] corresponding to the following expression(s) ['((100 + 10) * 6)']
  ---------  FINAL VALUE is [660] corresponding to this expression ['((100 + 10) * 6)']
  ------  Apply operation (/) to numbers of indexes (i=0,j=1) in [110, 6]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['((100 + 10) / 6)']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (^/) to numbers of indexes (i=0,j=1) in [110, 6]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(6 / (100 + 10))']
  ------  STOP. Unauthorized expression...
  ---  Apply operation (-) to numbers of indexes (i=0,j=2) in [100, 6, 10]
  ---  Number(s) become(s) [90, 6] corresponding to the following expression(s) ['(100 - 10)', 6]
  ------  Current number(s) [90, 6] corresponding to the following expression(s) ['(100 - 10)', 6]
  ------  Apply operation (+) to numbers of indexes (i=0,j=1) in [90, 6]
  ------  Number(s) become(s) [96] corresponding to the following expression(s) ['((100 - 10) + 6)']
  ---------  FINAL VALUE is [96] corresponding to this expression ['((100 - 10) + 6)']
  ------  Apply operation (-) to numbers of indexes (i=0,j=1) in [90, 6]
  ------  Number(s) become(s) [84] corresponding to the following expression(s) ['((100 - 10) - 6)']
  ---------  FINAL VALUE is [84] corresponding to this expression ['((100 - 10) - 6)']
  ------  Apply operation (^-) to numbers of indexes (i=0,j=1) in [90, 6]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(6 - (100 - 10))']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (*) to numbers of indexes (i=0,j=1) in [90, 6]
  ------  Number(s) become(s) [540] corresponding to the following expression(s) ['((100 - 10) * 6)']
  ---------  FINAL VALUE is [540] corresponding to this expression ['((100 - 10) * 6)']
  ------  Apply operation (/) to numbers of indexes (i=0,j=1) in [90, 6]
  ------  Number(s) become(s) [15] corresponding to the following expression(s) ['((100 - 10) / 6)']
  ---------  FINAL VALUE is [15] corresponding to this expression ['((100 - 10) / 6)']
  ------  Apply operation (^/) to numbers of indexes (i=0,j=1) in [90, 6]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(6 / (100 - 10))']
  ------  STOP. Unauthorized expression...
  ---  Apply operation (^-) to numbers of indexes (i=0,j=2) in [100, 6, 10]
  ---  Number(s) become(s) [None, 6] corresponding to the following expression(s) ['(10 - 100)', 6]
  ---  STOP. Unauthorized expression...
  ---  Apply operation (*) to numbers of indexes (i=0,j=2) in [100, 6, 10]
  ---  Number(s) become(s) [1000, 6] corresponding to the following expression(s) ['(100 * 10)', 6]
  ------  Current number(s) [1000, 6] corresponding to the following expression(s) ['(100 * 10)', 6]
  ------  Apply operation (+) to numbers of indexes (i=0,j=1) in [1000, 6]
  ------  Number(s) become(s) [1006] corresponding to the following expression(s) ['((100 * 10) + 6)']
  ---------  FINAL VALUE is [1006] corresponding to this expression ['((100 * 10) + 6)']
  ------  Apply operation (-) to numbers of indexes (i=0,j=1) in [1000, 6]
  ------  Number(s) become(s) [994] corresponding to the following expression(s) ['((100 * 10) - 6)']
  ---------  FINAL VALUE is [994] corresponding to this expression ['((100 * 10) - 6)']
  ------  Apply operation (^-) to numbers of indexes (i=0,j=1) in [1000, 6]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(6 - (100 * 10))']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (*) to numbers of indexes (i=0,j=1) in [1000, 6]
  ------  Number(s) become(s) [6000] corresponding to the following expression(s) ['((100 * 10) * 6)']
  ---------  FINAL VALUE is [6000] corresponding to this expression ['((100 * 10) * 6)']
  ------  Apply operation (/) to numbers of indexes (i=0,j=1) in [1000, 6]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['((100 * 10) / 6)']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (^/) to numbers of indexes (i=0,j=1) in [1000, 6]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(6 / (100 * 10))']
  ------  STOP. Unauthorized expression...
  ---  Apply operation (/) to numbers of indexes (i=0,j=2) in [100, 6, 10]
  ---  Number(s) become(s) [10, 6] corresponding to the following expression(s) ['(100 / 10)', 6]
  ------  Current number(s) [10, 6] corresponding to the following expression(s) ['(100 / 10)', 6]
  ------  Apply operation (+) to numbers of indexes (i=0,j=1) in [10, 6]
  ------  Number(s) become(s) [16] corresponding to the following expression(s) ['((100 / 10) + 6)']
  ---------  FINAL VALUE is [16] corresponding to this expression ['((100 / 10) + 6)']
  ------  Apply operation (-) to numbers of indexes (i=0,j=1) in [10, 6]
  ------  Number(s) become(s) [4] corresponding to the following expression(s) ['((100 / 10) - 6)']
  ---------  FINAL VALUE is [4] corresponding to this expression ['((100 / 10) - 6)']
  ------  Apply operation (^-) to numbers of indexes (i=0,j=1) in [10, 6]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(6 - (100 / 10))']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (*) to numbers of indexes (i=0,j=1) in [10, 6]
  ------  Number(s) become(s) [60] corresponding to the following expression(s) ['((100 / 10) * 6)']
  ---------  FINAL VALUE is [60] corresponding to this expression ['((100 / 10) * 6)']
  ------  Apply operation (/) to numbers of indexes (i=0,j=1) in [10, 6]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['((100 / 10) / 6)']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (^/) to numbers of indexes (i=0,j=1) in [10, 6]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(6 / (100 / 10))']
  ------  STOP. Unauthorized expression...
  ---  Apply operation (^/) to numbers of indexes (i=0,j=2) in [100, 6, 10]
  ---  Number(s) become(s) [None, 6] corresponding to the following expression(s) ['(10 / 100)', 6]
  ---  STOP. Unauthorized expression...
  ---  Apply operation (+) to numbers of indexes (i=1,j=2) in [100, 6, 10]
  ---  Number(s) become(s) [100, 16] corresponding to the following expression(s) [100, '(6 + 10)']
  ------  APPROXIMATE SOLUTION FOUND : 100 = 100
  ------  Current number(s) [100, 16] corresponding to the following expression(s) [100, '(6 + 10)']
  ------  Apply operation (+) to numbers of indexes (i=0,j=1) in [100, 16]
  ------  Number(s) become(s) [116] corresponding to the following expression(s) ['(100 + (6 + 10))']
  ---------  FINAL VALUE is [116] corresponding to this expression ['(100 + (6 + 10))']
  ------  Apply operation (-) to numbers of indexes (i=0,j=1) in [100, 16]
  ------  Number(s) become(s) [84] corresponding to the following expression(s) ['(100 - (6 + 10))']
  ---------  FINAL VALUE is [84] corresponding to this expression ['(100 - (6 + 10))']
  ------  Apply operation (^-) to numbers of indexes (i=0,j=1) in [100, 16]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['((6 + 10) - 100)']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (*) to numbers of indexes (i=0,j=1) in [100, 16]
  ------  Number(s) become(s) [1600] corresponding to the following expression(s) ['(100 * (6 + 10))']
  ---------  FINAL VALUE is [1600] corresponding to this expression ['(100 * (6 + 10))']
  ------  Apply operation (/) to numbers of indexes (i=0,j=1) in [100, 16]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(100 / (6 + 10))']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (^/) to numbers of indexes (i=0,j=1) in [100, 16]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['((6 + 10) / 100)']
  ------  STOP. Unauthorized expression...
  ---  Apply operation (-) to numbers of indexes (i=1,j=2) in [100, 6, 10]
  ---  Number(s) become(s) [100, None] corresponding to the following expression(s) [100, '(6 - 10)']
  ---  STOP. Unauthorized expression...
  ---  Apply operation (^-) to numbers of indexes (i=1,j=2) in [100, 6, 10]
  ---  Number(s) become(s) [100, 4] corresponding to the following expression(s) [100, '(10 - 6)']
  ------  APPROXIMATE SOLUTION FOUND : 100 = 100
  ------  Current number(s) [100, 4] corresponding to the following expression(s) [100, '(10 - 6)']
  ------  Apply operation (+) to numbers of indexes (i=0,j=1) in [100, 4]
  ------  Number(s) become(s) [104] corresponding to the following expression(s) ['(100 + (10 - 6))']
  ---------  EXACT SOLUTION FOUND : (100 + (10 - 6)) = 104
  ---------  FINAL VALUE is [104] corresponding to this expression ['(100 + (10 - 6))']
  ------  Apply operation (-) to numbers of indexes (i=0,j=1) in [100, 4]
  ------  Number(s) become(s) [96] corresponding to the following expression(s) ['(100 - (10 - 6))']
  ---------  FINAL VALUE is [96] corresponding to this expression ['(100 - (10 - 6))']
  ------  Apply operation (^-) to numbers of indexes (i=0,j=1) in [100, 4]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['((10 - 6) - 100)']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (*) to numbers of indexes (i=0,j=1) in [100, 4]
  ------  Number(s) become(s) [400] corresponding to the following expression(s) ['(100 * (10 - 6))']
  ---------  FINAL VALUE is [400] corresponding to this expression ['(100 * (10 - 6))']
  ------  Apply operation (/) to numbers of indexes (i=0,j=1) in [100, 4]
  ------  Number(s) become(s) [25] corresponding to the following expression(s) ['(100 / (10 - 6))']
  ---------  FINAL VALUE is [25] corresponding to this expression ['(100 / (10 - 6))']
  ------  Apply operation (^/) to numbers of indexes (i=0,j=1) in [100, 4]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['((10 - 6) / 100)']
  ------  STOP. Unauthorized expression...
  ---  Apply operation (*) to numbers of indexes (i=1,j=2) in [100, 6, 10]
  ---  Number(s) become(s) [100, 60] corresponding to the following expression(s) [100, '(6 * 10)']
  ------  APPROXIMATE SOLUTION FOUND : 100 = 100
  ------  Current number(s) [100, 60] corresponding to the following expression(s) [100, '(6 * 10)']
  ------  Apply operation (+) to numbers of indexes (i=0,j=1) in [100, 60]
  ------  Number(s) become(s) [160] corresponding to the following expression(s) ['(100 + (6 * 10))']
  ---------  FINAL VALUE is [160] corresponding to this expression ['(100 + (6 * 10))']
  ------  Apply operation (-) to numbers of indexes (i=0,j=1) in [100, 60]
  ------  Number(s) become(s) [40] corresponding to the following expression(s) ['(100 - (6 * 10))']
  ---------  FINAL VALUE is [40] corresponding to this expression ['(100 - (6 * 10))']
  ------  Apply operation (^-) to numbers of indexes (i=0,j=1) in [100, 60]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['((6 * 10) - 100)']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (*) to numbers of indexes (i=0,j=1) in [100, 60]
  ------  Number(s) become(s) [6000] corresponding to the following expression(s) ['(100 * (6 * 10))']
  ---------  FINAL VALUE is [6000] corresponding to this expression ['(100 * (6 * 10))']
  ------  Apply operation (/) to numbers of indexes (i=0,j=1) in [100, 60]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['(100 / (6 * 10))']
  ------  STOP. Unauthorized expression...
  ------  Apply operation (^/) to numbers of indexes (i=0,j=1) in [100, 60]
  ------  Number(s) become(s) [None] corresponding to the following expression(s) ['((6 * 10) / 100)']
  ------  STOP. Unauthorized expression...
  ---  Apply operation (/) to numbers of indexes (i=1,j=2) in [100, 6, 10]
  ---  Number(s) become(s) [100, None] corresponding to the following expression(s) [100, '(6 / 10)']
  ---  STOP. Unauthorized expression...
  ---  Apply operation (^/) to numbers of indexes (i=1,j=2) in [100, 6, 10]
  ---  Number(s) become(s) [100, None] corresponding to the following expression(s) [100, '(10 / 6)']
  ---  STOP. Unauthorized expression...

  >>> ALL EXACT SOLUTIONS
  ---------DEBUG---------
  SOLUTION | SIMPLIFIED EXPRESSION | EXPRESSION TREE
  ((100 - 6) + 10) = 104 | (-1)*6 + 10 + 100 | Add(Mul(Integer(-1), Integer(6)), Integer(10), Integer(100))
  (100 + (10 - 6)) = 104 | (-1)*6 + 10 + 100 | Add(Mul(Integer(-1), Integer(6)), Integer(10), Integer(100))
  ((100 + 10) - 6) = 104 | (-1)*6 + 10 + 100 | Add(Mul(Integer(-1), Integer(6)), Integer(10), Integer(100))
  --------/DEBUG---------
  ((100 - 6) + 10) = 104
  (100 + (10 - 6)) = 104
  ((100 + 10) - 6) = 104

  >>> ALL APPROXIMATE SOLUTIONS
  ---------DEBUG---------
  SOLUTION | SIMPLIFIED EXPRESSION | EXPRESSION TREE
  (100 + 6) = 106 | 6 + 100 | Add(Integer(6), Integer(100))
  100 = 100 | 100 | Integer(100)
  --------/DEBUG---------
  (100 + 6) = 106
  100 = 100
  ```
</details><br />


<!-- USAGE EXAMPLES -->
## Usage
```
$ python3 countdown.py  [-h] [-n [[...]]] [--size [3..10]] [-u [all|some]]
                        [-t [100..999]] [-s [approximate|exact]]
                        [--tolerance [1..10]] [-o [all|unique]] [-v [0|1|2]]

```
The script is run via the command-line. Many options are available but the solver can be executed without providing any (will use default values instead).

For more information about options, **see details below**.

<details>
  <summary>:heavy_plus_sign: Details</summary>
  
**Numbers to be used**
* `-n` (or `--numbers`):  &nbsp;
Numbers to be used to reach target.
  - According to the game rules all values must be in {1,2,3,4,5,6,7,8,9,10,25,50,75,100}.
  - By default, values are generated randomly. We first select between zero and four values in the large set {25,50,75,100} and then we select values in the small set {1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10} to make six numbers in total.
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

</details><br />

For a quick reminder, **display help menu**.
```
$ python3 countdown.py  -h
```

<details>
  <summary>:heavy_plus_sign: Help menu</summary>
  
  ```
  usage: countdown.py [-h] [-n [[...]]] [--size [3..10]] [-u [all|some]]
                    [-t [100..999]] [-s [approximate|exact]]
                    [--tolerance [1..10]] [-o [all|unique]] [-v [0|1|2]]

  Countdown numbers solver.

  optional arguments:
    -h, --help            show this help message and exit
    -n [ [ ...]], --numbers [ [ ...]]
                          numbers to be used to reach target, must be in
                          [1|2|3|4|5|6|7|8|9|10|25|50|75|100] (default is
                          random)
    --size [3..10]        maximum number or values to be used (default is 6)
    -u [all|some], --use [all|some]
                          rule for using numbers (default is 'some')
    -t [100..999], --target [100..999]
                          target value (default is random)
    -s [approximate|exact], --solutions [approximate|exact]
                          type of authorized answers (default is 'exact')
    --tolerance [1..10]   tolerance range for approximate solutions (default is
                          10)
    -o [all|unique], --output [all|unique]
                          solutions to output (default is 'unique')
    -v [0|1|2], --verbose [0|1|2]
                          verbose level for logging (default is 0)
  ```
    
</details><br />  


<!-- DESCRIPTION -->
## How It Works

### The algorithm
The main idea is quite simple, we generate every single value we can generate from the input numbers. \
We verify as we go if values we found are close enough to target and store them as solutions (either exact or approximate) when they actually are.

Let's start with the following numbers `n = [100 25 4 7 2]`. \
We generate a list of expressions to track every operation that have been made, initialized as `expr = [100 25 4 7 2]`.

We iterate through every possible pair of elements in the list : `[100 25]`, `[100 4]`, `[25 4]` ... \
<img src="https://github.com/ingranys/countdown-numbers-solver/blob/main/visuals/iterate.gif">

For a given pair of elements (a,b) we perform all possible operations `(a+b)` `(a-b)` `(a*b)` `(a/b)`. \
A new list of numbers and a new list of expressions are generated for each operation, where `a` and `b` are replaced by the operation results.  

</br>

Example :       &emsp;&emsp;
Let's say we start with `a = 100` & `b = 25` from `n = [100 25 4 7 2]`and `expr = [100 25 4 7 2])`.
<p align="left">
  <img src="https://github.com/ingranys/countdown-numbers-solver/blob/main/visuals/operations1.gif">
</p><br/ >

We now start all over and repeat the same steps with every of the newly generated lists : `n+ = [125 4 7 2]`, `n- = [75 4 7 2]`, `n* = [2500 4 7 2]`, `n/ = [4 4 7 2]`.

Example :       &emsp;&emsp;
For next step, we start again with ̀`n* = [2500 4 7 2]`. First pair of elements will be `a = 2500` & `b = 4`.
<p align="left">
  <img src="https://github.com/ingranys/countdown-numbers-solver/blob/main/visuals/operations2.gif">
</p><br/ >

And so on...

</br>

At each step the list of values shrinks (-1 in size) and the list of expressions gets a little more complex (add one operation).

We **stop when there is only one value left**.

> **NOTE** : This recursive approach ensures that all possibles values that could possibly be generated by the inputs numbers are found.  \
> All we have to do is to verify if one of them is solution.

### Filtering
This approach has a major flaw, it generates a large amount of duplicates.

Example :       &emsp;&emsp;
Let's consider `[100 2 3 3]` as input numbers and target `6`. \
Found solutions will be `[(2*3),(2*3),(2*3),(3*2),(3,2)]`. \
We would like the result to be `[(2*3),(3*2)]`.

A simple way to handle duplicates is to filter them out once all the computing is done.

To do so, we use **Expression Trees** as defined in `sympy` library [:link:](https://docs.sympy.org/latest/tutorial/manipulation.html), more about it [here](https://freecontent.manning.com/working-with-symbolic-expressions/) and [here](https://levelup.gitconnected.com/create-and-evaluate-simple-expression-tree-in-python-in-object-oriented-style-5eb27b6376c8).

Exemple :       &emsp;&emsp;
Let's consider the expression `[(3/1)*2+4]`. \
The corresponding Expression Tree is.

<p align="left">
  <img src="https://github.com/ingranys/countdown-numbers-solver/blob/main/visuals/tree.jpeg" height="250">
</p>

> **NOTE** : `sympy` generates Expression Trees in such a way that operations in expression are rearranged alway in the same manner. \
> This is very useful here because expressions that are "equivalent" will have the same Expression Tree regardless og operations order.

<details>
  <summary>:heavy_plus_sign: See example of sympy usage</summary>
  
  Run code in SymPy Live [:link:](https://live.sympy.org/).
  ```python
  from sympy import sympify, srepr

  expr_a = '(((3/1)*2)+4)'
  expr_b = '(4+(2*(3/1)))'
  simp_a = sympify(expr_a, evaluate=False)
  simp_b = sympify(expr_b, evaluate=False)
  tree_a = srepr(simp_a)
  tree_b = srepr(simp_b)

  print('-----------------')
  print('Expressions are :')
  print('A = {0}'.format(expr_a))
  print('B = {0}'.format(expr_b))
  print('-----------------')
  print('After simplication, turn into :')
  print('A = {0}'.format(simp_a))
  print('B = {0}'.format(simp_b))
  print('-----------------')
  print('Corresponding Expression Trees :')
  print('For A, {0}'.format(tree_a))
  print('For B, {0}'.format(tree_b))
  print('-----------------')
  print('Do expressions A & B share the same Expression Tree? ' \
          '{0}'.format(str(tree_a==tree_b).upper()))
  ```
  
  ```
  -----------------
  Expressions are :
  A = (((3/1)*2)+4)
  B = (4+(2*(3/1)))
  C = ((3/1)*(2+4))
  -----------------
  After simplication, turn into :
  A = 4 + 3*1/1*2
  B = 4 + 2*3*1/1
  C = 3*(2 + 4)/1
  -----------------
  Corresponding Expression Trees :
  For A, Add(Integer(4), Mul(Integer(2), Integer(3), Pow(Integer(1), Integer(-1))))
  For B, Add(Integer(4), Mul(Integer(2), Integer(3), Pow(Integer(1), Integer(-1))))
  For C, Mul(Integer(3), Pow(Integer(1), Integer(-1)), Add(Integer(2), Integer(4)))
  -----------------
  Do expressions A & B share the same Expression Tree? TRUE
  Do expressions A & C share the same Expression Tree? FALSE
  ```

</details><br />


### Complexity
Pseudo-code for the solver is.
```python
operations = ['+','-','*','/']
m = len(operations)
def recurse(numbers,target):
  n = len(numbers)
  for i in range(n):
    for j in range(n):
      for k in range(m):
        updated_numbers = ... # len(updated_numbers) = n-1
        recurse(updated_numbers,target)
```

Let's call **T(n) the number of operations** to execute `recurse()` function on a set of size `n`.


<!-- We use http://latex.codecogs.com to generate gif from latex on the fly.
-- Original text :
-- "We have `T(1)=m (1)` and `T(n)=n*n*m*T(n-1) (2)`.
-- Combine `(1)` & `(2)` we get  `T(n)=(n*n*m)*((n-1)*(n-1)*m)*[...]*(2*2*m)*T(1)`. Hence, `T(n)=(m^n)*n!*n!`.
-- For large values of n, time-complexity for this algorithm grows as O((m^n)*n!^2)."
-->
We have `(1)` ![](https://latex.codecogs.com/gif.latex?%7BT%281%29%20%3D%201%20%5Ccdot%201%20%5Ccdot%20m%20%7D) and `(2)` ![](https://latex.codecogs.com/gif.latex?%7BT%28n%29%3Dn%20%5Ccdot%20n%20%5Ccdot%20m%20%5Ccdot%20T%28n-1%29%20%7D). \
Combine `(1)` & `(2)` we get  ![](https://latex.codecogs.com/gif.latex?%7BT%28n%29%3D%28n%20%5Ccdot%20n%20%5Ccdot%20m%29*%28%28n-1%29%20%5Ccdot%20%28n-1%29%20%5Ccdot%20m%29*%5B...%5D*%282%20%5Ccdot%202%20%5Ccdot%20m%29*%281%20%5Ccdot%201%20%5Ccdot%20T%281%29%29%7D). \
Hence, ![](https://latex.codecogs.com/gif.latex?%7B%20T%28n%29%3Dm%5En%20%5Ccdot%20n%21%20%5Ccdot%20n%21%20%7D).

For large values of `n`, time-complexity for this algorithm grows as ![](https://latex.codecogs.com/gif.latex?%7B%5Cmathcal%7BO%7D%28m%5En%20%5Ccdot%20n%21%5E2%29%7D). \
We end up with **factorial complexity**... This is the danger zone :scream:!

Luckily for Countdown Numbers, we are limited to 6 numbers. **This is manageable in practice**.

> **NOTE** : This is a example of brute-force search, very similar to the naive solution for [the travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem#Computing_a_solution).

### Optimisations

**Unique pairs only** \
With naive approach, we consider every pair of elements in a given set and apply the following basic operations `+`, `-`, `*` and `/`. \
We can also iterate through unique pairs only, considering `(a,b)` and ignoring `(b,a)`) for example. \
we then apply the following operations : `(a+b)`, `(a-b)`, `(b-a)`, `(a*b)`, `(a/b)`, `(b/a)`. \
New pseudo code is. 
```python
operations = ['+','-','^-','*','/','^/']
m = len(operations)
def recurse(numbers,target):
  n = len(numbers)
  for i in range(n):
    for j in range(i+1,n):
      for k in range(m):
        updated_numbers = ... # len(updated_numbers) = n-1
        recurse(updated_numbers,target)
```
It goes through twice as less pairs and apply 6 operations instead of 4, it pays off in the end.

**Avoid forbidden values** \
All values must be strictly positive integers. \
We stop recursive calls if a negative or flot value is found.
```python
# custom lamdba functions (output None for forbidenn values)
'-' = lambda a,b: a-b if a>b else None
'^-' = lambda a,b: b-a if b>a else None
'/' = lambda a,b: a//b if a % b == 0 else None
'^/' = lambda a,b: b//a if b % a == 0 else None

def recurse():
  [...]
  updated_numbers = ... # new value based on lambda function

  # check that newly computed number is valid
  if None not in updated_numbers:
      # valid > next recursive call
      recurse()
  else:
      # not valid > stop
      print('STOP. Unauthorized expression...')
```

> **NOTE** : An approach based on [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) provide improved performance, unfortunately this is not an option in Python. \
> The closest we can get is taking advantage of lambda functions. 


<!-- DOCUMENTATION -->
## Documentation

### Changelog
See `CHANGELOG`[:link:](https://github.com/ingranys/countdown-numbers-solver/blob/main/CHANGELOG.md).

### Comments
Single-Line comments are provided for better understanding.
```python
# get numbers and crop to size
if not numbers:
    numbers = pick(n_numbers=SIZE)
else:
    numbers = numbers[:SIZE]
```

### Docstrings
Docstrings are provided for each module and each function.
```python
def pickFromBigNumbers(n_desired=-1):
    """
    Pick as many numbers as required in the set of big numbers {25,50,75,100}.
    Choose randomly between 0 and 4 if nothing is specified.

    Args:
        n_desired (int, optional): Number of desired numbers. Defaults to -1.

    Returns:
        list[int]: Generated list of numbers from the set of big numbers.
    """
```
Example of function **documentation in IDE**.
<details>
  <summary>:heavy_plus_sign: See screenshot</summary>
  <img src="https://github.com/ingranys/countdown-numbers-solver/blob/main/visuals/hover.png">
</details><br />

Example of module **documentation in console**.
```sh
$ python3 -c "import utils.parser;help(utils.parser)"
```

<details>
  <summary>:heavy_plus_sign: See output</summary>
  
  ```
  Help on module utils.parser in utils:

  NAME
      utils.parser - Custom parser for countdown.

  DESCRIPTION
      For more information, see README.

      For usage, use help menu <python3 countdown.py -h>.

      Project can be found here <https://github.com/ingranys/countdown-numbers-solver>.

      This program is free software: you can redistribute it and/or modify it under
      the terms of the GNU General Public License as published by the Free Software
      Foundation, either version 3 of the License, or (at your option) any later
      version.

      This program is distributed in the hope that it will be useful, but WITHOUT
      ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
      FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

      You should have received a copy of the GNU General Public License along with
      this program. If not, see <http://www.gnu.org/licenses/>.

  FUNCTIONS
      parse()
          Parse given arguments according to countdown specifications.
          - Defines arguments names.
          - Verify argument type and limitation on number of values.
          - Verify that values are contained in given choices.
          - Set argument to default when no value is given.
          - Provide usage and help menu.

          Returns:
              argparse.Namespace: Object containing parsed arguments.

  DATA
      __contact__ = 'ingranys@protonmail.com'
      __copyright__ = 'Copyright 2021, Mustapha Gaies, Toulouse (France)'
      __deprecated__ = False
      __email__ = 'ingranys@protonmail.com'
      __license__ = 'GPLv3'
      __maintainer__ = 'developer'
      __status__ = 'Production'

  VERSION
      0.4.0

  DATE
      2021/01/07

  AUTHOR
      ingranys

  FILE
      /user/Downloads/countdown/utils/parser.py
  ``` 
</details><br />


<!-- LICENSE -->
## License :scroll:

Distributed under the GNU General Public License v3.0. 

See `LICENSE`[:link:](https://github.com/ingranys/countdown-numbers-solver/blob/main/LICENSE) for more information.


<!-- CONTACT -->
## Contact :handshake:

**Mustapha Gaies** - [@ingranys](https://github.com/ingranys) - ingranys@protonmail.com

Project Link: [https://github.com/ingranys/countdown-numbers-solver](https://github.com/ingranys/countdown-numbers-solver)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements :pray:
* [DataGenetics - Countdown Game Show](https://datagenetics.com/blog/august32014/index.html)
* [James Stanley - Countdown Practice](https://incoherency.co.uk/countdown/practice/#numbers)
* [James Stanley - Countdown Sovler](https://incoherency.co.uk/countdown/) 
* [Github - cmdouglas/countdown_numbers](https://github.com/cmdouglas/countdown_numbers)
* [Github - cawhitworth/countdown.py](https://github.com/cawhitworth/countdown.py)
* [Github - othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template/edit/master/README.md)
* [Github - https://github.com/ikatyang/emoji-cheat-sheet](https://github.com/ikatyang/emoji-cheat-sheet)
* [Github - pierrejoubert73/markdown-details-collapsible.md](https://gist.github.com/pierrejoubert73/902cc94d79424356a8d20be2b382e1ab)
* [Github - Shields.io](https://github.com/badges/shields)
* [Github - NicolasBizzozzero/comprehensive_header](https://gist.github.com/NicolasBizzozzero/6d4ca63f8482a1af99b0ed022c13b041)
* [StackOverflow - Simple changelog builder](https://stackoverflow.com/questions/40865597/generate-changelog-from-commit-and-tag)
* [StackOverflow - Latex rendering in Github](https://stackoverflow.com/questions/35498525/latex-rendering-in-readme-md-on-github)
