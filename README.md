# python-cpp-PoC

Proofs Of Concepts created from **MateFacil** project.

**MateFacil** is a web app to help both professors and students to learn and evaluate the skills gained from the semester's course.
In this particular case, we decided to create a web app that can create or 'generate' mathematical problems.
On this first version (MateFacil 0.1) we focus on arithmethical and inequality problems.

On the initial design stage we look over Python's subprocesses to execute C++ and Java code.
This is because some of the 'generators' are written on those languajes and instead of refactor the existing 'generators' we leverage Python's subprocesses to make use of them.

On this repository we'll see all the proof of concetp that helped us to understand the funcionality of Python and C++ through Python's subprocesses.

---

## Test Case A
Output:
- The first approximation, we're printing a numerical series.

## Test Case Arguments
Output:
- We're executing C++ code with arguments or 'flags' that can be used to do a specific task from C++ and get the results to the Python execution.

## Test Case File
Output:
- This C++ snipet creates a file, writes content to the file and then the content of that fle is shown through the Python execution.

## Test Case Hello
Output:
- This is the mandatory first step on every software project! :)

---
Python Version used for this work: 3.8.3
g++ (GCC) 10.1.0
