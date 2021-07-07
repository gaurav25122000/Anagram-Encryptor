import binascii
import codecs
import hashlib
from colored import fore,style

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


def encryptor(message):
    key = encryption_hash(message)
    print("------------------------------------------------------------------------------")
    print(fore.BLUE+"Key: "+style.RESET +key)
    joined_message = listToString(message)
    salt = hashlib.sha256(codecs.encode(key, encoding='utf_32', errors='strict')).hexdigest().encode('ascii')
    print(fore.RED+"Salt: "+style.RESET+str(salt))
    pwdhash = hashlib.pbkdf2_hmac('sha512', joined_message.encode('utf_32'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    print(fore.RED+"Hashed Password: "+style.RESET+str(pwdhash))
    return (salt + pwdhash).decode('ascii')


def verify(hashed_message, entered_message):
    key = encryption_hash(entered_message)
    entered_message = listToString(entered_message)
    salt = hashlib.sha256(codecs.encode(key, encoding='utf_32', errors='strict')).hexdigest().encode('ascii')
    stored_password = hashed_message[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', entered_message.encode('utf_32'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


msg = input("Enter the message:  ")
spiltted_msg = msg.split(" ")
encrypted_msg = ""
k = 3
for i in range(0, len(spiltted_msg), k):
    encrypted_msg += encryptor(spiltted_msg[i:i + k])
print("\n\n"+fore.RED+"Final Encrypted Message: "+style.RESET+str(encrypted_msg))
#print(verify(encrypted_msg, "Hello How Are you? I am Doing Fine.".split(" ")))
