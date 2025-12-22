alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
def caesar(original_text, shift_amount, encode_or_decode):
    # Leere Speicherplätze für das fertige Wort
    decrypted_text = ""
    cipher_text = ""
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
    # Wir vergleichen mit dem String "decode" (in Anführungszeichen!)
    if encode_or_decode == "decode":
        for letter in original_text:
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            decrypted_text += alphabet[shifted_position]
        print(f"Here is the decrypted result: {decrypted_text}")
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
    elif encode_or_decode == "encode":
        for letter in original_text:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {cipher_text}")


encrypt(original_text=text, shift_amount=shift, encode_or_decode=direction)



