# You must make and submit your own test file and txt file with this assignment.

def toString(string):
    # This function returns the text from a given file.
    # Any new lines are written as \n
    with open(string, "r") as f:
        return f.read()


def longestLine():
    # Given a file return the longest line from within that file
    longest_line = ""
    longest_len = 0
    with open(longestline, "r") as f:
        for line in f:
            # remove only the newline at the end so length compares nicely
            line_no_nl = line.rstrip("\n")
            if len(line_no_nl) > longest_len:
                # keep the original line (including newline, if any)
                longest_line = line
                longest_len = len(line_no_nl)
    return longest_line


def toBinary(binary):
    # Given a file that is only 0's and 1's return a list of the file broken into bytes.
    # An example return might be ['01101001', '00101010', '1010']
    with open(binary, "r") as f:
        data = f.read()

    # keep only 0/1 characters (ignore newlines/spaces if any)
    bits = "".join(ch for ch in data if ch in "01")

    # break into chunks of 8 bits (last chunk may be shorter)
    return [bits[i:i + 8] for i in range(0, len(bits), 8)]
