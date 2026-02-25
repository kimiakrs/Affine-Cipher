# Implementation of the Affine Cipher in Python

This project presents a complete implementation of the Affine Cipher in Python, including encryption, decryption, and a brute-force attack demonstration.

The Affine Cipher is a classical substitution cipher that combines modular arithmetic with a linear transformation to encrypt text.

The project was developed as part of the Software Optimization course during the first semester of my M.Sc. in Software Engineering.

**Full documentation : ./Report-Task1.pdf**

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Affine Cipher](https://img.shields.io/badge/Cipher-Affine-red.svg)](https://en.wikipedia.org/wiki/Affine_cipher)
[![Modular Arithmetic](https://img.shields.io/badge/Concept-Modular%20Arithmetic-purple.svg)](https://en.wikipedia.org/wiki/Modular_arithmetic)
[![Brute Force Attack](https://img.shields.io/badge/Attack-Brute%20Force-orange.svg)](https://en.wikipedia.org/wiki/Brute-force_attack)
[![Classical Cryptography](https://img.shields.io/badge/Type-Classical%20Cipher-lightgrey.svg)](https://en.wikipedia.org/wiki/Classical_cipher)
[![Cryptanalysis](https://img.shields.io/badge/Focus-Cryptanalysis-darkblue.svg)](https://en.wikipedia.org/wiki/Cryptanalysis)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Table of Contents

- [Project Overview](#project-overview)
- [Affine Cipher Theory](#affine-cipher-theory)
- [Project Structure](#project-structure)
- [Security Disucssion](#security-disucssion)
- [Key Learning Outcomes](#key-learning-outcomes)
- [Disclaimer](#disclaimer)
- [License](#license)

---

## Project Overview

The Affine Cipher is a monoalphabetic substitution cipher that encrypts each letter using a linear transformation over modular arithmetic.

Each letter is converted to a number:

```bash
A → 0
B → 1
...
Z → 25
```

Encryption formula:

```python
E(x) = (a × x + b) mod 26
```

where: 

* x = numeric value of plaintext letter
* a = multiplicative key
* b = additive key
* 26 = alphabet size

As described in your documentation 

Report-Task1

As described in documentation, this project implements encryption, decryption, brute-force attack, and output display.

---

## Affine Cipher Theory

The affine cipher requires that:

```bash
gcd(a, 26) = 1
```

This ensures that a has a modular inverse.
Without this condition, decryption is impossible.

---

### Phase1: Encryption

Encryption follows: 

```python
E(x) = (a × x + b) mod 26
```

#### Step 1 — Generate Valid “a” Value

To ensure that *a* is valid:

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

Random *a*

```bash
gcd(a, 26) == 1
```

#### Step 2 — Apply Encryption Formula

For each character:

* Convert letter → number

* Apply formula

* Convert number → encrypted letter

* Output: ciphertext

---

### Phase2: Decryption

Decryption requires the modular inverse of a.

Decryption formula:

```python
D(x) = a⁻¹ × (x − b) mod 26
```

Where:

* a⁻¹ = modular inverse of a module 26

The program:

* Computes modular inverse
* Applies reverse transformation
* Restores original plaintext

---

### Phase3: Brute-Force Attack
The Affine Cipher has a small key space

Possible keys:

* Valid values for a (coprime with 26)
* Possible values for b (0-25)

The program:

1. Test all possible (a,b) combinations
2. Attempts decryption
3. Uses a customized dictionary to check valid English words
4. Calculates attack time

This demonstrates the vulnerability of classical cipher.


### Mathematical Components

The project implements

* GCD calculation
* Modular arithmetic
* Modular inverse
* Linear transformation
* Dictionary-based validation


---

## Project Structure
```
Affine-Cipher/
│
├── Task1-Affine.py          # Encryption/ Decryption/ Brute-force Attach Logics
├── dictionary.txt           # Dictionary
├── Report-Task1.pdf         # Full documentation
├── README.md
└── LICENSE
```

### Execution Workflow
Run this block:
```python
Task1-Affine.py  
```
For complete theoretical explanation, screenshots, brute-force output examples, and implementation details, see:

[Report-Task1.pdf](./Report-Task1.pdf)

---

## Security Disucssion

The Affine Cipher:

Uses simple linear algebra

Has small key space

Is vulnerable to brute-force attack

Is vulnerable to frequency analysis

Weaknesses:

* Predictable structure

* Limited possible keys (small key space)

* No modern security guarantees

Modern secure alternatives include:

* AES

* ChaCha20

* RSA / ECC

---

## Key Learning Outcomes

* Understanding modular arithmetic in cryptography

* Implementing GCD and modular inverse

* Designing encryption/decryption pipelines

* Understanding key constraints

* Performing brute-force cryptanalysis

* Measuring attack execution time

* Recognizing limitations of classical encryption systems

---
## Disclaimer

The Affine Cipher is cryptographically insecure and should not be used for real-world secure communication and also this project is strictly for educational and academic purposes.
---
## License

This project is licensed under the MIT License — see the LICENSE
 file for details.