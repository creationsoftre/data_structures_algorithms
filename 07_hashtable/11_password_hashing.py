# ============================================================
# Password Hashing Demo
# ============================================================
#
# Password hashing is different from hash table hashing.
#
# Hash table hashing:
#
#   Goal:
#       Turn a key into an index.
#
#   Example:
#       index = key % table_size
#
# Password hashing:
#
#   Goal:
#       Protect passwords.
#
#   Instead of storing the real password, we store a hashed version.
#
# ------------------------------------------------------------
# SIMPLE IDEA
# ------------------------------------------------------------
#
# Bad idea:
#
#   username: trevonte
#   password: hello123
#
# Better idea:
#
#   username: trevonte
#   password_hash: long scrambled-looking value
#
# When the user logs in:
#
#   1. Hash the password they entered.
#   2. Compare it to the stored hash.
#   3. If both hashes match, the password is correct.
#
# ------------------------------------------------------------
# BIG O / SPEED
# ------------------------------------------------------------
#
# Hashing a password:
#   Usually O(n)
#
# Why?
#   The algorithm reads the password characters.
#
# n = number of characters in the password.
#
# ------------------------------------------------------------
# SPACE COMPLEXITY
# ------------------------------------------------------------
#
# O(1)
#
# We store one hash result for the password.
#
# ------------------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------------------
#
# This file is only a beginner demo.
#
# In real applications, do not use plain SHA-256 by itself for
# password storage.
#
# Real password systems should use password hashing tools designed
# for security, such as bcrypt, scrypt, or Argon2.
#
# This demo only shows the basic idea:
#
#   Store the hash, not the real password.
# ============================================================


import hashlib


# ------------------------------------------------------------
# Hash a password
# ------------------------------------------------------------
#
# This function takes a plain password and returns a hash.
#
# Plain password:
#   "hello123"
#
# Hashed password:
#   A long fixed-length string.
#
# Important:
#   The same input creates the same hash.
# ------------------------------------------------------------

def hash_password_demo(password):
    # Convert the password string into bytes.
    #
    # Hash functions work with bytes, not normal Python strings.
    password_bytes = password.encode("utf-8")

    # Create a SHA-256 hash object.
    hash_object = hashlib.sha256(password_bytes)

    # Convert the hash result into a readable hexadecimal string.
    password_hash = hash_object.hexdigest()

    return password_hash


# ------------------------------------------------------------
# Verify a password
# ------------------------------------------------------------
#
# This function checks if a password matches a stored hash.
#
# It does not decrypt the hash.
#
# Instead:
#
#   1. Hash the entered password.
#   2. Compare the new hash to the stored hash.
# ------------------------------------------------------------

def verify_password_demo(entered_password, stored_hash):
    # Hash the password the user entered.
    entered_password_hash = hash_password_demo(entered_password)

    # If the new hash matches the stored hash, the password is correct.
    return entered_password_hash == stored_hash


# ------------------------------------------------------------
# Print hash explanation
# ------------------------------------------------------------
#
# This helper explains what is happening during password hashing.
# ------------------------------------------------------------

def explain_password_hashing(password):
    print("Password Hashing Explanation")
    print("=" * 60)

    print("Password entered:")
    print(f'  "{password}"')
    print()

    print("Step 1:")
    print("Convert the password into bytes.")
    print(f'  "{password}".encode("utf-8")')
    print()

    password_bytes = password.encode("utf-8")

    print("Password as bytes:")
    print(f"  {password_bytes}")
    print()

    print("Step 2:")
    print("Run the bytes through SHA-256.")
    print()

    password_hash = hash_password_demo(password)

    print("Step 3:")
    print("Store the hash, not the original password.")
    print()

    print("Hash result:")
    print(f"  {password_hash}")

    return password_hash


# ------------------------------------------------------------
# Real example: Simple login demo
# ------------------------------------------------------------

print("Password Hashing Demo")
print("=" * 60)
print("Goal: Store a hashed password instead of the real password.")
print()

# User creates an account.
username = "trevonte"
password = "hello123"

print("Create Account")
print("-" * 60)
print(f"Username: {username}")
print(f'Plain password: "{password}"')
print()

stored_password_hash = explain_password_hashing(password)

print()
print("Stored Account Record")
print("-" * 60)
print(f"Username: {username}")
print(f"Stored password hash: {stored_password_hash}")
print()
print("Notice:")
print("The real password is not stored.")
print()


# ------------------------------------------------------------
# Login attempt 1: correct password
# ------------------------------------------------------------

print("Login Attempt 1")
print("=" * 60)

entered_password = "hello123"

print(f'Entered password: "{entered_password}"')
print("Hash the entered password and compare it to the stored hash.")

is_valid = verify_password_demo(entered_password, stored_password_hash)

print(f"Password correct: {is_valid}")
print()


# ------------------------------------------------------------
# Login attempt 2: incorrect password
# ------------------------------------------------------------

print("Login Attempt 2")
print("=" * 60)

entered_password = "wrongpassword"

print(f'Entered password: "{entered_password}"')
print("Hash the entered password and compare it to the stored hash.")

is_valid = verify_password_demo(entered_password, stored_password_hash)

print(f"Password correct: {is_valid}")
print()


# ------------------------------------------------------------
# Show why hashes are useful
# ------------------------------------------------------------

print("Why This Helps")
print("=" * 60)

print("A password hash is one-way for normal use.")
print()
print("That means:")
print("  We can hash a password and compare hashes.")
print("  But we do not decrypt the hash to get the password back.")
print()

print("Same password produces the same hash:")
print(f'  "hello123" -> {hash_password_demo("hello123")}')
print(f'  "hello123" -> {hash_password_demo("hello123")}')
print()

print("Different password produces a different hash:")
print(f'  "hello124" -> {hash_password_demo("hello124")}')
print()

print("Important real-world note:")
print("  This demo uses SHA-256 to explain the concept.")
print("  Real password storage should use bcrypt, scrypt, or Argon2.")