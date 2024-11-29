def rail_fence_decrypt(ciphertext, rails):
    rail_lengths = [0] * rails
    row, direction = 0, 1

    for _ in range(len(ciphertext)):
        rail_lengths[row] += 1
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    index = 0
    rails_content = [''] * rails
    for r in range(rails):
        rails_content[r] = ciphertext[index:index + rail_lengths[r]]
        index += rail_lengths[r]

    plaintext = []
    row, direction = 0, 1
    for _ in range(len(ciphertext)):
        if rails_content[row]:
            plaintext.append(rails_content[row][0])
            rails_content[row] = rails_content[row][1:]
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    return ''.join(plaintext)

def rail_fence_encrypt(plaintext, rails):
    fence = ['' for _ in range(rails)]
    row, direction = 0, 1

    for char in plaintext:
        fence[row] += char
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    return ''.join(fence)

plaintext = "HELLO WORLD"
rails = 3
ciphertext = rail_fence_encrypt(plaintext, rails)
print("Ciphertext:", ciphertext)

decrypted_text = rail_fence_decrypt(ciphertext, rails)
print("Decrypted text:", decrypted_text)