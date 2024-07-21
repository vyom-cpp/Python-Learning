import random
import string


def random_chars(n):
    """Generate a string of n random characters."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))


def encode_word(word):
    """Encode a single word according to the secret code language rules."""
    if len(word) >= 3:
        word = word[1:] + word[0]
        word = random_chars(3) + word + random_chars(3)
    else:
        word = word[::-1]
    return word


def decode_word(word):
    """Decode a single word according to the secret code language rules."""
    if len(word) <= 2:
        word = word[::-1]
    else:
        word = word[3:-3]
        word = word[-1] + word[:-1]
    return word


def encode_message(message):
    """Encode a message by encoding each word individually."""
    words = message.split()
    encoded_words = [encode_word(word) for word in words]
    return " ".join(encoded_words)


def decode_message(message):
    """Decode a message by decoding each word individually."""
    words = message.split()
    decoded_words = [decode_word(word) for word in words]
    return " ".join(decoded_words)


def main():
    action = input("Do you want to 'encode' or 'decode' a message? ").strip().lower()
    if action not in ["encode", "decode"]:
        print("Invalid action. Please choose 'encode' or 'decode'.")
        return

    message = input("Enter the message: ").strip()
    if action == "encode":
        result = encode_message(message)
    else:
        result = decode_message(message)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
