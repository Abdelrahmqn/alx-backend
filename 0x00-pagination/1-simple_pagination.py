#!/usr/bin/env python3
""" Index_range """
import csv
from typing import List, Tuple


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
