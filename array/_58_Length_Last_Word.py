def lengthOfLastWord(s: str) -> int:
    a = s.split()
    return len(a[-1])


s = " jejejlalsd sdasd sa "
print(lengthOfLastWord(s))
