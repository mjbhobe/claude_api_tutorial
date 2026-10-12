### NOTE: this file HAS syntax errors injected deliverately
### for Claude to detect

"""Primes Generator Module.

Contains a function to generate 'n' prime numbers starting from a given number.
"""


def is_prime(num: int) -> bool:
  """Check if a number is prime."""
  if num < 2:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True


# Syntax Error 1: Missing closing parenthesis on function definition
def generate_primes(n: int, start_no: int = 0) -> list[int]:
  """Generate 'n' prime numbers starting from start_no (inclusive check).

  If start_no is prime, it will be the first number in the returned list.
  """
  primes = []
  current = start_no

  while len(primes) < n:
    if is_prime(current):
      primes.append(current)
    current += 1

  # Syntax Error 2: Using an invalid assignment operator or syntax typo
  return primes
