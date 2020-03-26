import unittest

"""
Implementation task.

Implement vector class that should make comparison of vectors by length.

>>> Vector([1, 2])
Vector([1, 2])

>>> Vector(1)
TypeError: expected Any[Tuple[Any[float, int]], List[Tuple[Any[float, int]]].

>>> Vector([[1]])
ValueError: expected Any[Tuple[Any[float, int]], List[Tuple[Any[float, int]]].

>>> Vector(["a"])
ValueError: expected Any[Tuple[Any[float, int]], List[Tuple[Any[float, int]]].

>>> Vector("a")
TypeError: expected Any[Tuple[Any[float, int]], List[Tuple[Any[float, int]]].

>>> Vector([1, 2]) > Vector([0, 1])
True

>>> Vector([1, 2]) >= Vector([2, 1])
True

>>> Vector([1, 2]) <= Vector([2, 1])
True

>>> Vector([1, 2, 3]) >= Vector([2, 1])
ValueError: vectors shape mismatch.

>>> Vector([1, 2]) == Vector([2, 1.00001])
True

    Vectors are considered equal if the difference between their lengths <= EPSILON.

    Additional points will be given for docstrings and if style checker returns nothing
    >> pycodestyle task.py --max-line-length=120
"""
import math
from typing import List, Sequence, Any, Tuple, Union

EPSILON = 0.001


class Vector:
    def __init__(self, v):
        self.check_input(v)
        self.v = v

    def check_input(self, v):
        """
        Check input.
        If input type is not tuple or list - raise TypeError.
        If input tuple/list contains some elements that are not float/int - raise ValueError.
        :param v: input argument during class initialization.
        :return: None.
        """
        if not (isinstance(v, list)) and not (isinstance(v, tuple)):
            try:
                raise TypeError("Any[Tuple[Any[float, int]], List[Tuple[Any[float, int]]]")
            except TypeError as e:
                print("TypeError : " + str(e))
        else:
            for i in v:
                if not (isinstance(i, int)) and not (isinstance(i, float)):
                    try:
                        raise TypeError("Any[Tuple[Any[float, int]], List[Tuple[Any[float, int]]]")
                    except TypeError as e:
                        print("TypeError : " + str(e))
                    break


    def __eq__(self, other):
        "="
        if len(self.v) != len(other.v):
            try:
                raise ValueError("vectors shape mismatch.")
            except ValueError as e:
                print("ValueError : " + str(e))
            return
        l1 = 0
        for i in self.v:
            l1 += i ** 2
        l1 = math.sqrt(l1)
        l2 = 0
        for i in other.v:
            l2 += i ** 2
        l2 = math.sqrt(l2)
        print(math.fabs(l1 - l2) < EPSILON)
        return math.fabs(l1 - l2) < EPSILON

    def __lt__(self, other):
        "<"
        if len(self.v) != len(other.v):
            try:
                raise ValueError("vectors shape mismatch.")
            except ValueError as e:
                print("ValueError : " + str(e))
            return
        l1 = 0
        for i in self.v:
            l1 += i ** 2
        l1 = math.sqrt(l1)
        l2 = 0
        for i in other.v:
            l2 += i ** 2
        l2 = math.sqrt(l2)
        tr1 = (math.fabs(l1 - l2) < EPSILON)

        if tr1:
            print(False)
            return False
        else:
            print(l1 < l2)
            return l1 < l2

    def __le__(self, other):
        "<="
        if len(self.v) != len(other.v):
            try:
                raise ValueError("vectors shape mismatch.")
            except ValueError as e:
                print("ValueError : " + str(e))
            return
        l1 = 0
        for i in self.v:
            l1 += i ** 2
        l1 = math.sqrt(l1)

        l2 = 0
        for i in other.v:
            l2 += i ** 2
        l2 = math.sqrt(l2)
        tr1 = (math.fabs(l1 - l2) < EPSILON)
        if tr1 or (l1 < l2 or l1 <= l2):
            print("True")
            return True
        else:
            print("False")
            return False

    def __ne__(self, other):
        if len(self.v) != len(other.v):
            try:
                raise ValueError("vectors shape mismatch.")
            except ValueError as e:
                print("ValueError : " + str(e))
            return
        l1 = 0
        for i in self.v:
            l1 += i ** 2
        l1 = math.sqrt(l1)
        l2 = 0
        for i in other.v:
            l2 += i ** 2
        l2 = math.sqrt(l2)
        tr1 = (math.fabs(l1 - l2) < EPSILON)

        if tr1:
            print("Fasle")
            return False
        elif l1 != l2:
            print("True")
            return True

    def __gt__(self, other):
        if len(self.v) != len(other.v):
            try:
                raise ValueError("vectors shape mismatch.")
            except ValueError as e:
                print("ValueError : " + str(e))
            return
        l1 = 0
        for i in self.v:
            l1 += i ** 2
        l1 = math.sqrt(l1)
        l2 = 0
        for i in other.v:
            l2 += i ** 2
        l2 = math.sqrt(l2)
        tr1 = (math.fabs(l1 - l2) < EPSILON)

        if tr1:
            print(False)
            return False
        else:
            print(l1 > l2)
            return l1 > l2

    def __ge__(self, other):
        if len(self.v) != len(other.v):
            try:
                raise ValueError("vectors shape mismatch.")
            except ValueError as e:
                print("ValueError : " + str(e))
            return
        l1 = 0
        for i in self.v:
            l1 += i ** 2

        l2 = 0
        for i in other.v:
            l2 += i ** 2
        l1 = math.sqrt(l1)
        l2 = math.sqrt(l2)
        tr1 = (math.fabs(l1 - l2) < EPSILON)
        if tr1 or (l1 > l2 or l1 >= l2):
            print("True")
            return True
        else:
            print("False")
            return (False)


Vector((1,))

