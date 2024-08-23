#!/usr/bin/env python3
""" Pagination Introductino """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    a functino to return a tuple
    of size two containing a start index and an end index
    corresponding.
    """
    beginning = (page - 1) * page_size
    end = beginning + page_size
    return (beginning, end)
