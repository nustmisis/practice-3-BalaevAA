import task_3


tests: list[tuple[str, str]] = [
    ("+7 123 456-78-90", "+7 123 456-78-90"),
    ("8(123)456-78-90", "+7 123 456-78-90"),
    ("1234567890", "+7 123 456-78-90"),
    ("123456789", "Fail!"),
    ("+9 123 456-78-90", "Fail!"),
    ("+7 123 456+78=90", "Fail!"),
]


def test_task_3():
    for phone, expected in tests:
        actual = task_3.format_phone_number(phone)
        assert actual == expected
