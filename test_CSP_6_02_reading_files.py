from CSP_6_02_reading_files import toString, longestLine, toBinary


def make_temp_file(name, contents):
    with open(name, "w") as f:
        f.write(contents)
    return name


def test_toString():
    fname = make_temp_file(
        "sample_test.txt",
        "This is a short line.\n"
        "This is a much, much longer line of sample text.\n"
        "Mid.\n"
    )
    result = toString(fname)
    assert result == (
        "This is a short line.\n"
        "This is a much, much longer line of sample text.\n"
        "Mid.\n"
    )


def test_longestLine():
    fname = make_temp_file(
        "sample_longest.txt",
        "short\n"
        "this is definitely the longest line here\n"
        "mid\n"
    )
    result = longestLine(fname)
    # longestLine should return the line exactly as in the file (including newline)
    assert result == "this is definitely the longest line here\n"


def test_toBinary():
    fname = make_temp_file(
        "sample_binary.txt",
        "011010010010101010100110\n"
        "10101010\n"
    )
    result = toBinary(fname)
    # Combined bits: 01101001001010101010011010101010
    # Grouped into bytes: 01101001 00101010 10100110 10101010
    assert result == ["01101001", "00101010", "10100110", "10101010"]
