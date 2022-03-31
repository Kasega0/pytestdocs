import testdocs as td


@td.testdocs(
    docs=td.TestDocs(
        title="足し算",
        cases=[
            td.TestCase(
                title="case 1",
                description="正常時1",
                input_data={"a": 5, "b": 3},
                expected=8,
            ),
            td.TestCase(
                title="case 2",
                description="正常時2",
                input_data={"a": 2, "b": 4},
                expected=6,
            ),
        ],
    )
)
def plus(x: int, y: int):
    return x + y


plus(3, 5)
