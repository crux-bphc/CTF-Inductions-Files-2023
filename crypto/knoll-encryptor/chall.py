from secret import flag, n

alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz{}"


def keygen():
    assert len(flag) == n * n
    arr = [alphabet.index(i) for i in flag]
    return [arr[i : i + n] for i in range(0, n * n, n)]


def enc(s, key):
    for c in s:
        if c not in alphabet:
            return "Invalid characters detected!"

    # pad input
    if len(s) % n != 0:
        s = s.ljust(len(s) + n - len(s) % n, "0")

    final_text = ""
    for i in range(0, len(s), n):
        user_chars = [alphabet.index(x) for x in s[i : i + n]]
        enc_chars = [0] * n

        for j in range(0, n):
            for k in range(0, n):
                enc_chars[j] += key[j][k] * user_chars[k]

        enc_chars = [alphabet[enc_chars[i] % len(alphabet)] for i in range(0, n)]
        final_text += "".join(enc_chars)

    return final_text


def main():
    print("Welcome to the Fort Knoll Encryptor!")
    print(
        "We use cutting-edge military-grade encryption software first patented in the Communist Republic of Upper Xyrgia to secure your data against evil hackers."
    )
    print("Surely it is futile to try to break our inccredibly secure cryptosystem :)")
    while True:
        key = keygen()
        print("\n1. Encrypt")
        print("2. Exit")
        choice = input("> ")
        print("")
        if choice == "1":
            s = input("Enter a string: ")
            print(f"Encrypted string: {enc(s, key)}")
        else:
            print("© 2023 Communist Republic of Upper Xyrgia")
            exit()


if __name__ == "__main__":
    main()
