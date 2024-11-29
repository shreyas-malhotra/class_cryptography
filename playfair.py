def create_matrix(key):
    matrix = []
    alphabets = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upper().replace("J", "I").replace(" ", "")

    for char in key:
        if char not in matrix and char in alphabets:
            matrix.append(char)

    for char in alphabets:
        if char not in matrix:
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j
    return None


def final_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    final = []

    i = 0
    while i < len(text):
        char1 = text[i]
        char2 = text[i + 1] if i + 1 < len(text) else 'X'
        if char1 == char2:
            final.append(char1 + 'X')
            i += 1
        else:
            final.append(char1 + char2)
            i += 2

    return final


def encrypt(plaintext, key):
    matrix = create_matrix(key)
    text = final_text(plaintext)
    ciphertext = ""

    for letter in text:
        row1, col1 = find_position(matrix, letter[0])
        row2, col2 = find_position(matrix, letter[1])

        if row1 == row2:  # same row
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # same column
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext


def decrypt(ciphertext, key):
    matrix = create_matrix(key)
    text = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    plaintext = ""

    for letter in text:
        row1, col1 = find_position(matrix, letter[0])
        row2, col2 = find_position(matrix, letter[1])

        if row1 == row2:  # same row
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # same column
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    return plaintext


key = "FAIRPLAY EXAMPLE"
plaintext = "HIDE THE GOLD"
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text", decrypted_text)