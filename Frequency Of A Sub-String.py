def count_substring(string, sub_string):
    c = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            c += 1
    return c
    # One Line code for the whole operation #

    # return sum([1 for i in range(len(string) - len(sub_string) + 1) if string[i:i + len(sub_string)] == sub_string])

    # We can compute the sliding count by substracting the length of smaller string from bigger string.
    # For each slide, we compare that part of bigger string with our smaller string and generate 1 in a list
    # if match found. Sum of all of these 1's in a list will give us total number of matches found.


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
