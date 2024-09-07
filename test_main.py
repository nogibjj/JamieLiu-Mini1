from main import hello


def test_hello():
    """Test hello function."""
    assert hello("Alice") == "Hello, Alice!"


if __name__ == "__main__":
    test_hello()
