from colored import Fore, Style
import pyfiglet

from encryptor import encryptor

if __name__ == "__main__":
    f = pyfiglet.figlet_format("Anagram Encryption", font="banner")
    print(f)
    msg = input("Enter the message:  ")
    spiltted_msg = msg.split(" ")
    encrypted_msg = ""
    k = 3
    for i in range(0, len(spiltted_msg), k):
        encrypted_msg += encryptor(spiltted_msg[i:i + k])
    print("\n\n"+Fore.red+"Final Encrypted Message: "+Style.reset+str(encrypted_msg))
