#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging


logging.basicConfig(level=logging.INFO, format="%(message)s")


SITES = [
    {
        'selector': 'div.CodeBody',
        'pages': [
            "http://sthurlow.com/python/lesson01/",
            "http://sthurlow.com/python/lesson02/",
            "http://sthurlow.com/python/lesson03/",
            "http://sthurlow.com/python/lesson04/",
            "http://sthurlow.com/python/lesson05/",
            "http://sthurlow.com/python/lesson06/",
            "http://sthurlow.com/python/lesson07/",
            "http://sthurlow.com/python/lesson08/",
            "http://sthurlow.com/python/lesson09/",
            "http://sthurlow.com/python/lesson10/",
            "http://sthurlow.com/python/lesson11/",
        ]
    },
    {
        'selector': 'div.highlight-python pre',
        'pages': [
            "https://docs.python.org/2/tutorial/appetite.html",
            "https://docs.python.org/2/tutorial/interpreter.html",
            "https://docs.python.org/2/tutorial/introduction.html",
            "https://docs.python.org/2/tutorial/controlflow.html",
            "https://docs.python.org/2/tutorial/datastructures.html",
            "https://docs.python.org/2/tutorial/modules.html",
            "https://docs.python.org/2/tutorial/inputoutput.html",
            "https://docs.python.org/2/tutorial/errors.html",
            "https://docs.python.org/2/tutorial/classes.html",
            "https://docs.python.org/2/tutorial/stdlib.html",
            "https://docs.python.org/2/tutorial/stdlib2.html",
            "https://docs.python.org/2/tutorial/whatnow.html",
            "https://docs.python.org/2/tutorial/interactive.html",
            "https://docs.python.org/2/tutorial/floatingpoint.html",
            "https://docs.python.org/2/tutorial/appendix.html",
        ]
    },
    {
        'selector': '#inner-text code',
        'pages': [
            "http://www.learnpython.org/en/Hello%2C_World%21",
            "http://www.learnpython.org/en/Variables_and_Types",
            "http://www.learnpython.org/en/Lists",
            "http://www.learnpython.org/en/Basic_Operators",
            "http://www.learnpython.org/en/String_Formatting",
            "http://www.learnpython.org/en/Basic_String_Operations",
            "http://www.learnpython.org/en/Conditions",
            "http://www.learnpython.org/en/Loops",
            "http://www.learnpython.org/en/Functions",
            "http://www.learnpython.org/en/Classes_and_Objects",
            "http://www.learnpython.org/en/Dictionaries",
            "http://www.learnpython.org/en/Modules_and_Packages",
            "http://www.learnpython.org/en/Generators",
            "http://www.learnpython.org/en/List_Comprehensions",
            "http://www.learnpython.org/en/Multiple_Function_Arguments",
            "http://www.learnpython.org/en/Regular_Expressions",
            "http://www.learnpython.org/en/Exception_Handling",
            "http://www.learnpython.org/en/Sets",
            "http://www.learnpython.org/en/Serialization",
            "http://www.learnpython.org/en/Partial_functions",
            "http://www.learnpython.org/en/Code_Introspection",
            "http://www.learnpython.org/en/Decorators",
        ]
    },
    {
        'selector': 'pre.prettyprint',
        'pages': [
            "http://www.tutorialspoint.com//python/index.htm",
            "http://www.tutorialspoint.com//python/python_overview.htm",
            "http://www.tutorialspoint.com//python/python_environment.htm",
            "http://www.tutorialspoint.com//python/python_basic_syntax.htm",
            "http://www.tutorialspoint.com//python/python_variable_types.htm",
            "http://www.tutorialspoint.com//python/python_basic_operators.htm",
            "http://www.tutorialspoint.com//python/python_decision_making.htm",
            "http://www.tutorialspoint.com//python/python_loops.htm",
            "http://www.tutorialspoint.com//python/python_numbers.htm",
            "http://www.tutorialspoint.com//python/python_strings.htm",
            "http://www.tutorialspoint.com//python/python_lists.htm",
            "http://www.tutorialspoint.com//python/python_tuples.htm",
            "http://www.tutorialspoint.com//python/python_dictionary.htm",
            "http://www.tutorialspoint.com//python/python_date_time.htm",
            "http://www.tutorialspoint.com//python/python_functions.htm",
            "http://www.tutorialspoint.com//python/python_modules.htm",
            "http://www.tutorialspoint.com//python/python_files_io.htm",
            "http://www.tutorialspoint.com//python/python_exceptions.htm",
        ]
    },
    {
        'selector': 'td.code div.highlight',
        'pages': [
            "http://learnpythonthehardway.org/book/preface.html",
            "http://learnpythonthehardway.org/book/intro.html",
            "http://learnpythonthehardway.org/book/ex0.html",
            "http://learnpythonthehardway.org/book/ex1.html",
            "http://learnpythonthehardway.org/book/ex2.html",
            "http://learnpythonthehardway.org/book/ex3.html",
            "http://learnpythonthehardway.org/book/ex4.html",
            "http://learnpythonthehardway.org/book/ex5.html",
            "http://learnpythonthehardway.org/book/ex6.html",
            "http://learnpythonthehardway.org/book/ex7.html",
            "http://learnpythonthehardway.org/book/ex8.html",
            "http://learnpythonthehardway.org/book/ex9.html",
            "http://learnpythonthehardway.org/book/ex10.html",
            "http://learnpythonthehardway.org/book/ex11.html",
            "http://learnpythonthehardway.org/book/ex12.html",
            "http://learnpythonthehardway.org/book/ex13.html",
            "http://learnpythonthehardway.org/book/ex14.html",
            "http://learnpythonthehardway.org/book/ex15.html",
            "http://learnpythonthehardway.org/book/ex16.html",
            "http://learnpythonthehardway.org/book/ex17.html",
            "http://learnpythonthehardway.org/book/ex18.html",
            "http://learnpythonthehardway.org/book/ex19.html",
            "http://learnpythonthehardway.org/book/ex20.html",
            "http://learnpythonthehardway.org/book/ex21.html",
            "http://learnpythonthehardway.org/book/ex22.html",
            "http://learnpythonthehardway.org/book/ex23.html",
            "http://learnpythonthehardway.org/book/ex24.html",
            "http://learnpythonthehardway.org/book/ex25.html",
            "http://learnpythonthehardway.org/book/ex26.html",
            "http://learnpythonthehardway.org/book/ex27.html",
            "http://learnpythonthehardway.org/book/ex28.html",
            "http://learnpythonthehardway.org/book/ex29.html",
            "http://learnpythonthehardway.org/book/ex30.html",
            "http://learnpythonthehardway.org/book/ex31.html",
            "http://learnpythonthehardway.org/book/ex32.html",
            "http://learnpythonthehardway.org/book/ex33.html",
            "http://learnpythonthehardway.org/book/ex34.html",
            "http://learnpythonthehardway.org/book/ex35.html",
            "http://learnpythonthehardway.org/book/ex36.html",
            "http://learnpythonthehardway.org/book/ex37.html",
            "http://learnpythonthehardway.org/book/ex38.html",
            "http://learnpythonthehardway.org/book/ex39.html",
            "http://learnpythonthehardway.org/book/ex40.html",
            "http://learnpythonthehardway.org/book/ex41.html",
            "http://learnpythonthehardway.org/book/ex42.html",
            "http://learnpythonthehardway.org/book/ex43.html",
            "http://learnpythonthehardway.org/book/ex44.html",
            "http://learnpythonthehardway.org/book/ex45.html",
            "http://learnpythonthehardway.org/book/ex46.html",
            "http://learnpythonthehardway.org/book/ex47.html",
            "http://learnpythonthehardway.org/book/ex48.html",
            "http://learnpythonthehardway.org/book/ex49.html",
            "http://learnpythonthehardway.org/book/ex50.html",
            "http://learnpythonthehardway.org/book/ex51.html",
            "http://learnpythonthehardway.org/book/ex52.html",
            "http://learnpythonthehardway.org/book/advice.html",
            "http://learnpythonthehardway.org/book/next.html",
            "http://learnpythonthehardway.org/book/appendixa.html",
        ]
    },
    {
        'selector': 'dl.list1',
        'pages': [
            "http://anh.cs.luc.edu/python/hands-on/handsonHtml/handson2.6.html",
        ]
    },
    {
        'selector': 'div.source-python pre',
        'pages': [
            "http://www.wikihow.com/Start-Programming-in-Python",
        ]
    },
    {
        'selector': 'div.highlight pre',
        'pages': [
            "http://www.stavros.io/tutorials/python/",
        ]
    },
    {
        'selector': 'pre.python',
        'pages': [
            "http://www.raywenderlich.com/62094/teens-python-tutorial",
        ]
    },
    {
        'selector': 'div.highlight-python pre',
        'pages': [
            "https://opentechschool.github.io/python-beginners/en/getting_started.html",
            "https://opentechschool.github.io/python-beginners/en/simple_drawing.html",
            "https://opentechschool.github.io/python-beginners/en/variables.html",
            "https://opentechschool.github.io/python-beginners/en/loops.html",
            "https://opentechschool.github.io/python-beginners/en/functions.html",
            "https://opentechschool.github.io/python-beginners/en/functions_parameters.html",
            "https://opentechschool.github.io/python-beginners/en/conditionals.html",
            "https://opentechschool.github.io/python-beginners/en/conditional_loops.html",
            "https://opentechschool.github.io/python-beginners/en/logical_operators.html",
            "https://opentechschool.github.io/python-beginners/en/where_to_go.html",
        ]
    }
]
