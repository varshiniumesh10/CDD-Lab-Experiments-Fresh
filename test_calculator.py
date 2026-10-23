
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add(10, 5) == 15


def test_add_negative():
    assert add(-2, -3) == -5


if __name__ == "__main__":
    test_add()
    test_add_negative()
    print("All tests passed successfully!")
