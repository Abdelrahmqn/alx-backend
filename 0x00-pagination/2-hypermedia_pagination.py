#!/usr/bin/env python3
""" Index_range p"""
import math
import csv
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    a functino to return a tuple
    of size two containing a start index and an end index
    corresponding.
    """
    beginning = (page - 1) * page_size
    end = beginning + page_size
    return (beginning, end)


class Server:
    """
    Server Class
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        new ins.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """For caching
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        info = self.dataset()
        if start > len(info):
            return []
        return info[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieves information.
        """
        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_information = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages,
        }
        return page_information
