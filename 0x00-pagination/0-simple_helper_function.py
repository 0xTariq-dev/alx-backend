#!/usr/bin/env python3
"""
This module contains a function named index_range that takes two integer
arguments page and page_size
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start index and end index corresponding to
    the range of indexes

    Args:
        page: the page number
        page_size: the number of elements in the page

    Returns:
        A tuple of two values (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
