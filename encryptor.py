import binascii
import codecs
import hashlib

from colored import Fore, Style

from utils import encryption_hash, listToString


def encryptor(message):
    key = encryption_hash(message)
    print("------------------------------------------------------------------------------")
    print(Fore.blue+"Key: "+ Style.reset + key)
    joined_message = listToString(message)
    salt = hashlib.sha256(codecs.encode(key, encoding='utf_32', errors='strict')).hexdigest().encode('ascii')
    print(Fore.red+"Salt: "+Style.reset+str(salt))
    pwdhash = hashlib.pbkdf2_hmac('sha512', joined_message.encode('utf_32'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    print(Fore.red+"Hashed Password: "+Style.reset+str(pwdhash))
    return (salt + pwdhash).decode('ascii')