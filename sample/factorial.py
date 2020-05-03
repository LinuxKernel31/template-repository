# Template Repository for testing
# Copyright 2020  Robert Navas

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
""" Calculates the factorial of a given number"""

import os

import numpy as np
import pandas as pd

__author__ = 'Robert Navas'
__version__ = '0.0.1'

factorials = {}


class Person:
    def __init__(self, **kwargs):
        self.nose = kwargs["nose"]
        self.eyes = kwargs["eyes"]
        self.weight = kwargs["weight"]


def factorial(n):

    if n in factorials:
        return factorials[n]

    if n == 1:
        return 1
    else:
        factors = n * factorial(n - 1)

    factorials[n] = factors

    return factors


def main():

    person = Person(nose="matulis", eyes="brown", weight=74)

    print(person.nose)
    print(person.eyes)


if __name__ == "__main__":
    main()
