from abc import ABCMeta
import functools
from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class Base(metaclass=ABCMeta):
    heading: str
    description: str = ""

    def __new__(cls, *args, **kwargs):
        dataclass(cls)
        return super().__new__(cls)

    def to_md(self, root_level: int = 1):
        description = f"\n\n{self.description}" if len(self.description) > 0 else ""
        return f"{'#' * root_level} {self.heading}{description}"


class Case(Base):
    input_data: any
    expected: any
    head_input: str = "input"
    head_expected: str = "expected"

    def to_md(self, root_level: int = 3):
        str_base = super().to_md(root_level)
        return (
            f"{str_base}\n\n"
            f"{'#' * (root_level + 1)} {self.head_input}\n\n```\n{self.input_data}\n```\n\n"
            f"{'#' * (root_level + 1)} {self.head_expected}\n\n```\n{self.expected}\n```"
        )


class Unit(Base):
    cases: list[Case]

    def to_md(self, root_level: int = 2):
        str_base = super().to_md(root_level)
        str_cases = "\n\n".join([c.to_md(root_level + 1) for c in self.cases])
        return f"{str_base}\n\n{str_cases}"


class Section(Base):
    children: list["Section"]

    def to_md(self, root_level: int = 1):
        str_base = super().to_md(root_level)
        str_children = "\n\n".join([c.to_md(root_level + 1) for c in self.children])
        return f"{str_base}\n\n{str_children}"


def testdocs(docs: Unit):
    def _testdocs(f: Callable):
        @functools.wraps(f)
        def _docs(*args, **kwargs):
            print(docs.to_md())

        return _docs

    return _testdocs
