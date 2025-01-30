def swap_case(s):
    newString = ""
    for index in range(len(s)):
        if s[index] == s[index].lower():
            newString += s[index].upper()
        else:
            newString += s[index].lower()
    return newString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
