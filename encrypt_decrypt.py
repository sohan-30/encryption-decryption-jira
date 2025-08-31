def encrypt(text: str) -> str:
    even = text[0::2]
    odd = text[1::2]
    return even + odd

def decrypt(cipher: str) -> str:
    # Correct split: even-part is longer when string length is odd
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
    print("CLI will be added in AA-8")
