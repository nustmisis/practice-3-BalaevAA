import re
import task_1


_TestCase = tuple[str, list[str]]

tests: list[tuple[str, list[_TestCase]]] = [
    (
        task_1.REGEXP_1,
        [
            ("1 a 1 2 b", ["a", "b"]),
            ("z 2 y", ["z", "y"]),
        ],
    ),
    (
        task_1.REGEXP_2,
        [
            ("aaa bbb ccc", ["aaa", "bbb", "ccc"]),
            ("ddd eee fgh", ["ddd", "eee", "fgh"]),
            ("a1b c2d e3f", ["a1b", "c2d", "e3f"]),
        ],
    ),
    (
        task_1.REGEXP_3,
        [
            ("a aa aaa", ["aa", "aaa"]),
            ("b bb bbb", ["bb", "bbb"]),
            ("a bb aaa", ["bb", "aaa"]),
        ],
    ),
    (
        task_1.REGEXP_4,
        [
            ("1.1.1.1 aaaa bbbbb", ["1.1.1.1"]),
            ("a.a.a.a bbbb 2.2.2.2", ["2.2.2.2"]),
            ("3.3.3.3 cccc 4.4.4.4", ["3.3.3.3", "4.4.4.4"]),
            ("255.23.0.1 cccc 4.4.4.4", ["255.23.0.1", "4.4.4.4"]),
            ("255.0.23.1 cccc 4.4.4.4", ["255.0.23.1", "4.4.4.4"]),
        ],
    ),
    (
        task_1.REGEXP_5,
        [
            ("aaa Abbb ccc", ["Abbb"]),
            ("Aaa Abbb ccc", ["Aaa", "Abbb"]),
            ("Caa Cbb Accc", ["Accc"]),
        ],
    ),
    (
        task_1.REGEXP_6,
        [
            ("a b c d e f", ["a", "b", "e", "f"]),
            ("abcdef", ["a", "b", "e", "f"]),
            ("adf", ["a", "f"]),
            ("acf", ["a", "f"]),
        ],
    ),
    (
        task_1.REGEXP_7,
        [
            ("aaa +1.0 bb", ["+1.0"]),
            ("aaa -1.0 bb", ["-1.0"]),
            ("aaa -123.234 bb +111.999", ["-123.234", "+111.999"]),
        ],
    ),
    (
        task_1.REGEXP_8,
        [
            ("aaa 18-04-2016 bbb", ["18-04-2016"]),
            ("aaa 18.04.2016 bbb", ["18.04.2016"]),
            ("aaa 18-04-ABCD bbb 18.04.2016", ["18.04.2016"]),
            ("aaa 18/04/ABCD bbb 18/04/2016", ["18/04/2016"]),
            ("aaa 18/04/ABCD bbb 18/4/2016", ["18/4/2016"]),
        ],
    ),
]


def test_task_1():
    for pattern, cases in tests:
        regexp = re.compile(pattern)

        for string, expected in cases:
            actual = regexp.findall(string)
            assert actual == expected
