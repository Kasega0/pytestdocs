import functools
from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class TestCase:
    name: str
    description: Optional[str]
    input_data: dict
    expected: any

    def to_md(self, root_level: int = 3):
        return (
            f"{'#' * root_level} {self.name}\n\n"
            f"{self.description}\n\n"
            f"{'#' * (root_level + 1)} input\n\n"
            f"```\n{self.input_data}\n```\n\n"
            f"{'#' * (root_level + 1)} expected\n\n"
            f"```\n{self.expected}\n```"
        )


@dataclass
class TestDocs:
    name: str
    description: Optional[str]
    cases: list[TestCase]

    def to_md(self, root_level: int = 2):
        str_cases = "\n\n".join([c.to_md(root_level + 1) for c in self.cases])
        return f"{'#' * root_level} {self.name}\n\n{self.description}\n\n{str_cases}"


def testdocs(docs: TestDocs):
    def _testdocs(f: Callable):
        @functools.wraps(f)
        def _docs(*args, **kwargs):
            print(f"args: {args}\nkwargs: {kwargs}")
            print(docs.to_md())

        return _docs

    return _testdocs
