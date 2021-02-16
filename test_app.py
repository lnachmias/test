#! /usr/bin/python

import pytest

def add():
	a = 2
	b = 2
	return a + b


add()


def test_answer():
    assert add() == 4
