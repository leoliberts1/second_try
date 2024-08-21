from typing import List, Union, Optional

from .newspaper import Newspaper


class Agency(object):
    singleton_instance = None

    def __init__(self):
        self.newspapers: List[Newspaper] = []

    @staticmethod
    def get_instance():
        if Agency.singleton_instance is None:
            Agency.singleton_instance = Agency()

        return Agency.singleton_instance

    def add_newspaper(self, new_paper: Newspaper):
        #TODO: assert that ID does not exist  yet (or create a new one)
        if new_paper.paper_id not in Newspaper.used_ids:
            Newspaper.used_ids.append(new_paper.paper_id)
            self.newspapers.append(new_paper)
        else:
            print(Newspaper.used_ids)
            raise ValueError(f"A newspaper with ID {new_paper.paper_id} already exists")


    def get_newspaper(self, paper_id: Union[int,str]) -> Optional[Newspaper]:
        for paper in self.newspapers:
            if paper.paper_id == paper_id:
                return paper
        return None

    def all_newspapers(self) -> List[Newspaper]:
        return self.newspapers

    def remove_newspaper(self, paper: Newspaper):
        self.newspapers.remove(paper)

