#!/usr/bin/env python3
"""
this is a function that take type annotation 
into consideration

"""
import mypy
def add(a: float, b: float)-> float:
	return a + b

