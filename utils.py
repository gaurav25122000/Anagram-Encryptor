def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def encryption_hash(message):
    encryption_key = ""
    for i in message:
        encryption_key += i[0]
    return encryption_key