# RSA Cryptosystem Implementation

A pure Python implementation of the **RSA (Rivest–Shamir–Adleman)** public-key cryptosystem built from scratch without external cryptographic libraries. This project demonstrates the core mathematical principles behind asymmetric encryption, including prime generation, modular arithmetic, and text encoding.

## About RSA

**RSA** is one of the first and most widely used public-key cryptosystems for secure data transmission. Unlike symmetric encryption, which uses a single shared key, RSA relies on an asymmetric key pair:

* **Public Key `(e, n)`:** Shared openly and used to encrypt messages or verify digital signatures.
* **Private Key `(d, n)`:** Kept strictly secret and used to decrypt messages or sign data.

The security of RSA relies on the practical difficulty of factoring the product of two large prime numbers (the factoring problem).

## Features

* **Zero External Crypto Dependencies:** Implemented purely with standard Python arithmetic and modular logic.
* **Custom Prime Validation & Generation:** Primality testing and selection of distinct prime numbers `p` and `q`.
* **Key Pair Generation:** Automated computation of the modulus `n`, Euler's totient `φ(n)`, public exponent `e`, and modular multiplicative inverse `d`.
* **Fast Modular Exponentiation:** Efficient encryption and decryption using square-and-multiply algorithms (`pow(base, exp, mod)`).
* **ASCII Text Encoding/Decoding:** Seamless conversion between plaintext strings, integer blocks, and ciphertext.

## How It Works

1. **Key Generation:**
   * Choose two distinct prime numbers, `p` and `q`.
   * Compute the modulus: `n = p * q`
   * Compute Euler's totient function: `φ(n) = (p - 1) * (q - 1)`
   * Choose a public exponent `e` such that `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`.
   * Compute the private exponent `d` as the modular multiplicative inverse of `e mod φ(n)`:
     `d * e ≡ 1 (mod φ(n))`

2. **Encryption:**
   * Convert each character or block of plaintext into an integer `m` (where `0 <= m < n`).
   * Compute the ciphertext `c`:
     `c = m^e mod n`

3. **Decryption:**
   * Recover the original integer `m` using the private key `d`:
     `m = c^d mod n`
   * Convert the decrypted integers back into readable text.

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/alejadi888/RSA_python_algorithm.git](https://github.com/alejadi888/RSA_python_algorithm.git)
   cd RSA_python_algorithm
