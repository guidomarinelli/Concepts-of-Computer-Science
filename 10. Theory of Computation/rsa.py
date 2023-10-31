"""
Title: RSA encryption and decryption
Author: [Guido Marinelli](https://github.com/GuidoMarinelli/)
Date created: 2023/10/31
Last modified: 2023/10/31
Description: Implementing the RSA Public Key Encryption Algorithm.
"""

import sympy
import random
import math

START_RANGE = 800
STOP_RANGE = 1500


def random_prime_number():
    """Returns a prime number from a given range."""

    while True:
        n = random.randrange(START_RANGE, STOP_RANGE)

        if sympy.isprime(n):
            return n


def generate_key_e(z):
    """Determines the exponent e of the public key."""
    e = 0

    # find the first uncommon and smaller factor than z
    for i in range(2, z):

        if math.gcd(z, i) == 1:
            e = i
            break

    return e


def generate_key_d(z, e):
    """Determines the exponent d of the private key."""
    d = 0

    for i in range(z):

        if ((e * i) % z) == 1:
            d = i
            break

    return d


def int_to_binary(int_char):
    """Converts integer to binary by applying a padding."""
    unicode32_length = 32
    pad = '0'

    bin_char = str(bin(int_char))[2:]
    bin_char_length = len(bin_char)

    return pad * (unicode32_length - bin_char_length) + bin_char


class RSASystem:
    """
    Class that implements the RSA Public Key Encryption Algorithm.
    """

    def __init__(self, pub_key=(0, 0), pri_key=(0, 0)):
        self.public_key = pub_key
        self.private_key = pri_key
        self._n = pub_key[0]
        self._e = pub_key[1]
        self._npri = pri_key[0]
        self._d = pri_key[1]

    def generate_keys(self):
        """Generate the public and private key."""
        # randomly select two prime numbers
        p = random_prime_number()
        q = random_prime_number()
        # calculate the modulus
        self._n = p * q
        self._npri = self._n
        # calculate the tozient function
        z = (p - 1) * (q - 1)
        # determines the exponent e of the public key
        self._e = generate_key_e(z)
        self.public_key = (self._n, self._e)
        # determines the exponent d of the private key
        self._d = generate_key_d(z, self._e)
        self.private_key = (self._npri, self._d)
        return self.private_key, self.public_key

    def encode(self, message):
        """Performs the encryption process."""
        message_list = [ord(char) for char in list(message)]
        code = [(m ** self._e) % self._n for m in message_list]
        return ''.join([int_to_binary(c) for c in code])

    def decode(self, encrypted_message):
        """Performs the decryption process."""
        unicode32_length = 32
        base = 2
        k = int(len(encrypted_message) / unicode32_length)
        split_code = [encrypted_message[unicode32_length * i: unicode32_length * (i + 1)] for i in range(k)]
        code_int = [int(c, base) for c in split_code]
        return ''.join([chr((c ** self._d) % self._npri) for c in code_int])


def main():
    # Bob generate the public and private key and distributes the public key to Alice and Rose.
    Bob = RSASystem()
    bob_private_key, bob_public_key = Bob.generate_keys()
    print(f'Bob - Private key: {bob_private_key}')
    print(f'Bob - Public key: {bob_public_key}')

    # Alice with Bob's public key encrypts a message and sends it to Bob.
    message_from_Alice_to_Bob = "Hi Bob! 😆"
    Alice = RSASystem(pub_key=bob_public_key)
    alice_encrypted_message = Alice.encode(message_from_Alice_to_Bob)

    # Rose does the same thing.
    message_from_Rose_to_Bob = "Ciao Bob! 👋"
    Rose = RSASystem(pub_key=bob_public_key)
    rose_encrypted_message = Rose.encode(message_from_Rose_to_Bob)

    # Bob received messages from Alice and Rose deciphers them with her private key.
    Bob = RSASystem(pri_key=bob_private_key)
    alice_decrypted_message = Bob.decode(alice_encrypted_message)
    rose_decrypted_message = Bob.decode(rose_encrypted_message)

    print("\nMESSAGE FROM ALICE TO BOB")
    print(f'Message: {message_from_Alice_to_Bob}')
    print('ENCRYPTED MESSAGE:')
    print(alice_encrypted_message)
    print('DECRYPTED MESSAGE:')
    print(alice_decrypted_message)

    print("\nMESSAGE FROM ROSE TO BOB")
    print(f'Message: {message_from_Rose_to_Bob}')
    print('ENCRYPTED MESSAGE:')
    print(rose_encrypted_message)
    print('DECRYPTED MESSAGE:')
    print(rose_decrypted_message)


main()
