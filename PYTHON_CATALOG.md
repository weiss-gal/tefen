# Python Teaching Materials – Catalog

Everything Python in the [tefen repo](https://github.com/weiss-gal/tefen), in a sensible teaching order (setup → values → conditions → loops → functions → recursion → files → dictionaries → data → OOP/trees → graphics/games → projects). Materials are mostly in Hebrew; code and some exercises are in English. Where the same material exists in several years, only the latest/best version is listed (older copies are noted at the bottom).

Year folders are Israeli school years (e.g. `2025_2026` = תשפ"ו). Grades: 8th = ח, 9th = ט, 10th = י, 11th = יא.

## 0. Setup & general reference
- [Install Python 3.10 (step-by-step)](https://github.com/weiss-gal/tefen/blob/main/manuals/install_python_310.md) – Windows installer walkthrough
- [Quick install script](https://github.com/weiss-gal/tefen/blob/main/manuals/quick_install.bat) – `.bat` helper
- [Python cheat sheet (PDF)](https://github.com/weiss-gal/tefen/blob/main/manuals/python_cheat_sheet.pdf) – one-page command summary
- [Code quality: functions and variable names](https://github.com/weiss-gal/tefen/blob/main/manuals/code_quality-functions-and-names.md) – naming and function-design guidelines
- [Python course home page (9th grade, 2025-26)](https://github.com/weiss-gal/tefen/blob/main/docs/python/index.html) – syllabus overview and "why programming / why Python"
- Recommended external courses are linked from the class readmes, e.g. [2025-26 9th grade readme](https://github.com/weiss-gal/tefen/blob/main/2025_2026/9th_grade/readme.md) (python.org, Arcade docs, Hebrew tutorial, campus.il course, IBM Python for Data Science)

## 1. Values, expressions and variables
- [Slides: Python expressions and variables (PPTX)](https://github.com/weiss-gal/tefen/blob/main/2026_2027/9th_grade/lessons/01_expressions_and_vars/Python%20expressions%20and%20variables.pptx) – latest deck (2026-27)
- [Lesson: expressions and variables](https://github.com/weiss-gal/tefen/blob/main/2026_2027/9th_grade/lessons/01_expressions_and_vars/readme.md) – "what does this expression print?" warm-up (incl. `"1" + 1` error) + link to the memory game
- [Memory game – Python expressions deck](https://github.com/weiss-gal/tefen/blob/main/docs/games/memory_game/index.html) – matching game for expressions ↔ results ([deck data](https://github.com/weiss-gal/tefen/blob/main/docs/games/memory_game/python_expressions.json))
- [Lesson: values and variables](https://github.com/weiss-gal/tefen/blob/main/2024_2025/10th_grade/lessons/00_values_and_variables/readme.md) – types, evaluation, `input()` and conversion · [solution](https://github.com/weiss-gal/tefen/blob/main/2024_2025/10th_grade/lessons/00_values_and_variables/solution.py)
- [Lesson: variables and operators](https://github.com/weiss-gal/tefen/blob/main/2023_2024/8th_grade/lessons/00_vars_and_expresssions/readme.md) – evaluation, value vs. type · [practice: predict the output](https://github.com/weiss-gal/tefen/blob/main/2023_2024/8th_grade/lessons/00_vars_and_expresssions/test_exp.py)

## 2. Boolean expressions and conditions (`if`)
- [Slides: Boolean expressions and conditions (PPTX)](https://github.com/weiss-gal/tefen/blob/main/2024_2025/10th_grade/lessons/00_values_and_variables/Boolean_expressions_and_Conditions.pptx)
- [Lesson: conditions](https://github.com/weiss-gal/tefen/blob/main/2024_2025/10th_grade/lessons/01_conditions/readme.md) – `if / elif / else`, calculator exercise · [solution](https://github.com/weiss-gal/tefen/blob/main/2024_2025/10th_grade/lessons/01_conditions/solution.py)
- [Lesson: Boolean expressions and conditions](https://github.com/weiss-gal/tefen/blob/main/2023_2024/8th_grade/lessons/01_boolean_expressions_and_conditions/readme.md) · [rock-paper-scissors example](https://github.com/weiss-gal/tefen/blob/main/2023_2024/8th_grade/lessons/01_boolean_expressions_and_conditions/rock_paper_scissors.py)
- [Exercise: rock, paper, scissors (simple version)](https://github.com/weiss-gal/tefen/blob/main/2023_2024/8th_grade/lessons/02_conditions/readme.md)

## 3. Loops
- [Lesson: conditional loop (`while`) – guessing game](https://github.com/weiss-gal/tefen/blob/main/2023_2024/8th_grade/lessons/03_conditional_loop/readme.md)

## 4. Functions
- [Lesson: functions (self-study, `print_nice`)](https://github.com/weiss-gal/tefen/blob/main/2023_2024/8th_grade/lessons/04_functions/readme.md)

## 5. Recursion
- [Slides: recursion (PPTX)](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/02_recursion/recursion.pptx)
- [Recursion demo](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/02_recursion/recursion_demo.py) · [call stack](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/02_recursion/call_stack.py) · [rabbits, Australia and more](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/02_recursion/rabbits_australia_and_more.py)

## 6. Files
- [Files in Python (intro)](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/03_files/Readme.md) – sample files: [English](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/03_files/english.txt), [Hebrew](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/03_files/hebrew.txt)
- [Files – classroom practice](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/04_more_files/readme.md) – [read_full_file.py](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/04_more_files/read_full_file.py), [yesterday.txt](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/04_more_files/yesterday.txt), [netflix_movies.csv](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/04_more_files/netflix_movies.csv)

## 7. Dictionaries
- [Dictionaries](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/05_dictionaries/readme.md)

## 8. Data analysis (notebooks, statistics, pandas)
- [Intro to Google Colab notebooks](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/06_notebooks/readme.md)
- [Descriptive statistics](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/07_descriptive_statistics/readme.md) – [salary_data.csv](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/07_descriptive_statistics/salary_data.csv)
- [The pandas library](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/08_pandas_library/readme.md)
- [Data intro course – chapter 2 (Jupyter notebook)](https://github.com/weiss-gal/tefen/blob/main/data_intro_course/notebooks/chapter2.ipynb)
- [Data analysis exercise (PDF)](https://github.com/weiss-gal/tefen/blob/main/2023_2024/11th_grade/lessons/01_data_analysis/data_analysis_excercise.pdf) – datasets: [S&P 500 history](https://github.com/weiss-gal/tefen/blob/main/2023_2024/11th_grade/lessons/01_data_analysis/historical_data_spx.csv), [Netflix movies](https://github.com/weiss-gal/tefen/blob/main/2023_2024/11th_grade/lessons/01_data_analysis/netflix_movies.csv), [resources](https://github.com/weiss-gal/tefen/blob/main/2023_2024/11th_grade/lessons/01_data_analysis/resources.md)
- [Plotting with matplotlib – dice results](https://github.com/weiss-gal/tefen/blob/main/2022_2023/lessons/matplotlib/dice_results.py)
- [Real-life data: Steam client example](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/09_real_life_data/user_test.py)
- [Suggested research topics](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/materials/research_subject.md) · [Research methods (PPTX)](https://github.com/weiss-gal/tefen/blob/main/2022_2023/lessons/research_methods/research_methods.pptx)

## 9. Trees, classes and data structures
- [Trees – skeleton with a `Node` class](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/01_trees/pretty_print_tree.py) · [`Node` implementation](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/01_trees/node.py)
- [Trees – dictionary-based version (9th grade)](https://github.com/weiss-gal/tefen/blob/main/2023_2024/9th_grade/lessons/00_trees/pretty_print_tree.py)

## 10. Graphics: Turtle
- [Turtle graphics lesson](https://github.com/weiss-gal/tefen/blob/main/2024_2025/10th_grade/lessons/02_turtle_graphics/readme.md) – install, shapes, loops, functions (identical copy also in the [9th grade folder](https://github.com/weiss-gal/tefen/blob/main/2024_2025/9th_grade/lessons/01_turtle_graphics/readme.md))

## 11. Game development with Arcade
- [Collect coins – sprites, moving and bouncing coins](https://github.com/weiss-gal/tefen/blob/main/2025_2026/9th_grade/lessons/00_intro/collect_coins.py)
- [Random shapes – animation with classes](https://github.com/weiss-gal/tefen/blob/main/2025_2026/9th_grade/lessons/00_intro/random_shapes.py)

## 12. 2D lists – mazes
- [Maze examples (2D lists)](https://github.com/weiss-gal/tefen/blob/main/2024_2025/10th_grade/lessons/03_maze/examples.py) · [display_maze.py](https://github.com/weiss-gal/tefen/blob/main/2024_2025/10th_grade/lessons/03_maze/display_maze.py) · [check_solution.py](https://github.com/weiss-gal/tefen/blob/main/2024_2025/10th_grade/lessons/03_maze/check_solution.py)

## 13. Exercises and projects
- [FizzBuzz (Kattis)](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/excercises/00_fizzbuzz.md) · [screenshot](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/excercises/fizzbuzz_screenshot.png)
- Password-cracking challenge, two variants: [10th grade](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/excercises/password_crack.md) · [code](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/excercises/password_crack.py) — [8th grade](https://github.com/weiss-gal/tefen/blob/main/2023_2024/8th_grade/excercises/password_crack.md) · [code](https://github.com/weiss-gal/tefen/blob/main/2023_2024/8th_grade/excercises/password_crack.py)
- [Akinator-style game (v1)](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/excercises/akinator_v1.md) – builds on trees/dictionaries
- [City vote – guided reading of a data site](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/excercises/city_vote.md)
- [Last lesson: practice games and Kattis "hipphipp"](https://github.com/weiss-gal/tefen/blob/main/2023_2024/8th_grade/lessons/05_final/readme.md)
- [Tic-tac-toe: unbeatable 3×3](https://github.com/weiss-gal/tefen/blob/main/2022_2023/lessons/tic-tac-toe/unbeatable_3x3/tictactoe.py) · [board-clone tester](https://github.com/weiss-gal/tefen/blob/main/2022_2023/lessons/tic-tac-toe/components/clone_tester.py)
- [Text-matching project ("nikky")](https://github.com/weiss-gal/tefen/blob/main/2022_2023/lessons/nikky/nikky.py) – regex-based text cleanup ([band.txt](https://github.com/weiss-gal/tefen/blob/main/2022_2023/lessons/nikky/band.txt), [test.txt](https://github.com/weiss-gal/tefen/blob/main/2022_2023/lessons/nikky/test.txt))

## 14. Extras
- [Fun with Python: writing a Discord bot](https://github.com/weiss-gal/tefen/blob/main/2023_2024/10th_grade/lessons/09_fun_stuff/readme.md)
- [Git/GitHub exercise (fix a function, resolve a merge conflict)](https://github.com/weiss-gal/tefen/blob/main/2022_2023/lessons/github/avia/targil1.py) · [conflict demo](https://github.com/weiss-gal/tefen/blob/main/2022_2023/lessons/github/conflict/print_nums.py)

---

## Notes on duplicates (older copies not listed above)
- *Python expressions and variables* deck: same file in `2023_2024/8th_grade` and `2024_2025/10th_grade`; `2026_2027/9th_grade` is the newest (different, smaller) version.
- Turtle lesson: `2024_2025/9th_grade` and `2024_2025/10th_grade` are byte-identical.
- `netflix_movies.csv`: identical in `2023_2024/10th_grade/04_more_files` and `2023_2024/11th_grade/01_data_analysis`.
- FizzBuzz: `2023_2024/11th_grade/00_refresh/homework.md` is an earlier-dated copy of the 10th-grade one without the "problems and tips" section.
- Git exercise `targil1.py`: one identical copy per student folder (avia, geva, naya, noga).
