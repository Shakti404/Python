import textwrap


def wrap(s, w):
    l = list()
    for i in range(0, len(s), w):
        l.append(s[i:i + w])
    return "\n".join(l)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
