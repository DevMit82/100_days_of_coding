# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    # Richtung umkehren, wenn entschlüsselt (decode) werden soll
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        # Wenn das Zeichen nicht in der Liste alphabet ist, wird es unverändert hinzugefügt
        if letter not in alphabet:
            output_text += letter
        else:
            # Summe von Index aus der Liste alphabet und shift_amount speichern
            shifted_position = alphabet.index(letter) + shift_amount
            # Die Position durch Modulo (%) begrenzen,
            # damit wir im Kreis des Alphabets bleiben (z.B. wird 27 zu 1)
            shifted_position %= len(alphabet)
            # Den Buchstaben an der neuen Position aus der Liste holen und anhängen
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# TODO-3: Can you figure out a way to restart the cipher program?
# Variable new_message für erneute eingabe
new_message = True
# Solange new_message True ist wird die Schleife ausgeführt
while new_message == True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Do you want to start a new message? Type 'yes' or 'no' ")

    if restart == "no":
        # Wenn user "no" eingibt wird new_message auf False geändert und somit die Schleife beendet
        new_message = False






