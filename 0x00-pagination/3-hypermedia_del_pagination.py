#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Applies Hypermeida deletion resilient pagination to the returned data
        adding metadata to the returned results and handling data deletion
        between requests to ensure consistant results
        """
        data = self.indexed_dataset()
        assert index is not None and 0 <= index <= max(data.keys())
        p_data = []
        count, next_index = 0, None
        start_index = index if index else 0
        for k, v in data.items():
            if k >= start_index and count < page_size:
                p_data.append(v)
                count += 1
                continue
            if count == page_size:
                next_index = k
                break
        indexed_page = {
            'index': index,
            'data': p_data,
            'page_size': len(p_data),
            'next_index': next_index
        }
        return indexed_page
