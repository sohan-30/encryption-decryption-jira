def encrypt(text: str) -> str:
    even = text[0::2]
    odd = text[1::2]
    return even + odd

def decrypt(cipher: str) -> str:
    half = (len(cipher) + 1) // 2
    even = cipher[:half]
    odd = cipher[half:]
    out = []
    for i in range(len(cipher)):
        if i % 2 == 0:
            out.append(even[i // 2])
        else:
            out.append(odd[i // 2])
    return ''.join(out)

if __name__ == "__main__":
    print("1) Encrypt\n2) Decrypt")
    choice = input("Enter choice (1/2): ").strip()
    if choice == "1":
        text = input("Enter message: ")
        print("Encrypted:", encrypt(text))
    elif choice == "2":
        text = input("Enter encrypted message: ")
        print("Decrypted:", decrypt(text))
    else:
        print("Invalid choice.")
