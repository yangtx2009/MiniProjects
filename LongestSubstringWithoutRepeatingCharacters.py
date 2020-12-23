ss = ["dvdf", "abcabcbb", ""]

for s in ss:
    maxLen = 0
    total = len(s)

    if total > 0:
        buffer = ""
        for i in range(total):
            if s[i] not in buffer:
                buffer += s[i]
            else:
                if len(buffer) > maxLen:
                    maxLen = len(buffer)
                buffer = buffer[buffer.find(s[i])+1:]+s[i]
        if len(buffer) > maxLen:
            maxLen = len(buffer)
    print(maxLen)