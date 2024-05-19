#!/usr/bin/env python3
"""
This module contains functions that performs simple pagination on a CSV dataset
"""

import csv
import math
from typing import Tuple, List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Gets The given page content from a CSV dataset

        Args:
            page: the page number
            page_size: the number of elements in the page

        Returns:
            The given page content
        """
        assert isinstance(page, int) and page > 0

        assert isinstance(page_size, int) and page_size > 0

        total_size = len(self.dataset())
        total_pages = (total_size + page_size - 1) // page_size
        page_range = index_range(page, page_size)
        if (page_range[0] > total_size - 1) or (page > total_pages):
            return []
        else:
            return self.__dataset[page_range[0]:page_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Applies Hypermeida pagination to the returned data adding metadata
        to the returned results
        """
        total_size = len(self.dataset())
        total_pages = (total_size + page_size - 1) // page_size

        hypered_data = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
        return hypered_data


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
