def verify(hashed_message, entered_message):
    key = encryption_hash(entered_message)
    entered_message = listToString(entered_message)
    salt = hashlib.sha256(codecs.encode(key, encoding='utf_32', errors='strict')).hexdigest().encode('ascii')
    stored_password = hashed_message[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', entered_message.encode('utf_32'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
