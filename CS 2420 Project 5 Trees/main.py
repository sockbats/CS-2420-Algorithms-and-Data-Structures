"""
Project: Project 5 Trees
Author: Kyler Seely
Course: CS 2420
Date: 2022-06-08

Description:

Lessons Learned:
"""
from string import whitespace, punctuation
from bst import *


class Pair:
    """
    Encapsulate letter,count pair as a single entity.
    Realtional methods make this object comparable
    using built-in operators.
    """

    def __init__(self, letter, count=1):
        self.letter = letter
        self.count = count

    def __eq__(self, other):
        return self.letter == other.letter

    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'

    def __str__(self):
        return f'({self.letter}, {self.count})'


def make_tree():
    """
    A helper function to build the tree.
    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    """
    bst = BST()
    with open("around-the-world-in-80-days-3.txt", "r") as f:
        data = f.read()
    for i in whitespace + punctuation:
        data = data.replace(i, "")
    data = list(data)
    for i in data:
        bst = add(bst, Pair(i))
    return bst


def main():
    """Program kicks off here."""
    bst = make_tree()


if __name__ == "__main__":
    main()
