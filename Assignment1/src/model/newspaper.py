import random
from typing import List

from flask_restx import Model

from .issue import Issue


class Newspaper(object):
    used_ids = []
    def __init__(self, paper_id: int, name: str, frequency: int, price: float):
        self.paper_id: int = paper_id
        self.name: str = name
        self.frequency: int = frequency  # the issue frequency (in days)
        self.price: float = price  # the monthly price
        self.issues: List[Issue] = []
    @classmethod
    def unique_id(cls):
        id = random.randint(1,1000)
        if id not in Newspaper.used_ids:
            return id
        else:Newspaper.unique_id()
