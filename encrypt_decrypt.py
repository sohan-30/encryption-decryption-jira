def encrypt(text: str) -> str:
    even = text[0::2]
    odd = text[1::2]
    return even + odd

def decrypt(cipher: str) -> str:
    raise NotImplementedError("TODO in AA-7 / AA-24")

if __name__ == "__main__":
    print("CLI will be added in AA-8")
