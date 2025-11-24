def get_shifts(cleartext, ciphertext):
    """
    Based on a monoalphabetically shifted cleartext, get the shifts for each letter in the alphabet as an array.
    """
    shifts = [0] * 26
    for i in range(len(cleartext)):
        if cleartext[i] != " ":
            shifts[ord(cleartext[i]) - 65] = ord(ciphertext[i]) - ord(cleartext[i])
        i += 1
    return shifts


def predict_text(cleartext, shifts):
    "Based on a cleartexts and an array of shifts per alphabetic letter (see get_shifts), return an encrypted text"
    ciphertext_pred = []
    for i in range(len(cleartext)):
        if cleartext[i] != " ":
            new_character = chr(ord(cleartext[i]) + shifts[ord(cleartext[i]) - 65])
            ciphertext_pred.append(new_character)

        i += 1
    ciphertext_pred = "".join(ciphertext_pred)
    return ciphertext_pred
