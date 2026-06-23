# Substitution Cipher Encryptor

A simple Python-based symmetric encryption tool that uses a **randomized substitution cipher** to encrypt and decrypt text messages.

---

## How It Works

The program builds a character map over the full printable ASCII set — letters, digits, punctuation, and spaces. At startup, it shuffles this set into a random key and constructs two lookup dictionaries:

- `encrypt_dict` — maps each original character → shuffled character
- `decrypt_dict` — maps each shuffled character → original character

Encryption and decryption are both O(n) passes over the input string using these dictionaries. Characters not in the map are passed through unchanged.

```
plain text  →  encrypt()  →  cipher text
cipher text →  decrypt()  →  plain text
```

---

## Project Structure

```
substitution-cipher/
│
├── cipher.py       # Main script (encrypt + decrypt logic)
└── README.md
```

---

## Requirements

- Python 3.x
- No external libraries — uses only the standard library (`random`, `string`)

---

## Usage

Run the script directly:

```bash
python cipher.py
```

You'll be prompted to enter a message:

```
Enter a msg to encrypt : Hello World!
original_msg  : Hello World!
encrypted_msg : xP44t5}t*4Q
decrypted_msg : Hello World!
```

---

## Example

```python
from cipher import encrypt, decrypt, encrypt_dict, decrypt_dict

secret = encrypt("Attack at dawn", encrypt_dict)
print(secret)                          # e.g. "mFF7?< 7F p7/J"

original = decrypt(secret, decrypt_dict)
print(original)                        # "Attack at dawn"
```

---

## Security Notes

> This is an educational project, **not suitable for real-world security use.**

- The key is randomly generated **each run** — there is no key persistence or sharing mechanism.
- Substitution ciphers are vulnerable to **frequency analysis** on long texts.
- For real encryption, use vetted libraries like Python's [`cryptography`](https://cryptography.io/) or `hashlib`.

---

## Character Set

The cipher covers all 94 printable ASCII characters plus space (95 total):

| Category      | Example chars        |
|---------------|----------------------|
| Space         | ` `                  |
| Punctuation   | `! @ # $ % ^ & * …` |
| Digits        | `0–9`                |
| ASCII Letters | `a–z`, `A–Z`         |

---

## License

MIT 
