import functools
from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class TestCase:
    title: str
    input_data: dict
    expected: any
    description: str = ""

    def to_md(self, root_level: int = 3):
        description = f"\n\n{self.description}" if len(self.description) > 0 else ""
        return (
            f"{'#' * root_level} {self.title}{description}\n\n"
            f"{'#' * (root_level + 1)} input\n\n```\n{self.input_data}\n```\n\n"
            f"{'#' * (root_level + 1)} expected\n\n```\n{self.expected}\n```"
        )


@dataclass
class TestDocs:
    title: str
    cases: list[TestCase]
    description: str = ""

    def to_md(self, root_level: int = 2):
        str_cases = "\n\n".join([c.to_md(root_level + 1) for c in self.cases])
        description = f"\n\n{self.description}" if len(self.description) > 0 else ""
        return f"{'#' * root_level} {self.title}{description}\n\n{str_cases}"


def testdocs(docs: TestDocs):
    def _testdocs(f: Callable):
        @functools.wraps(f)
        def _docs(*args, **kwargs):
            print(f"args: {args}\nkwargs: {kwargs}")
            print(docs.to_md())

        return _docs

    return _testdocs
