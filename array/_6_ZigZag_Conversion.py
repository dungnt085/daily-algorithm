def convert(s: str, numRows: int) -> str:
    """
    convert a string input to a output string """

    if numRows == 1: 
        return s
    res = ""
    for r in range(numRows):
        increment = 2*(numRows -1)
        for i in range(r, len(s), increment):
            res += s[i]
            if (r > 0 and r< numRows -1 and i + increment - 2*r < len(s)):
                res += s[i + increment - 2*r]
    return res



s = "PPPAASS"
num_rows = 3
print(convert(s=s, numRows=num_rows))