# Function to test

def add(num1, num2):
    return num1 + num2

# Tests

try: assert add(20,24) == 44, "Did not get 44 for add(20,24)"
except AssertionError as error: print(f"Fail: {error}")

print("All tests have been run")

# Function to test

def odd_or_even(num):
    return "Even" if num % 2 == 0 else "Odd"

# Tests

try: assert odd_or_even(10) == "Even", "Did not get Even for odd_or_even(10)"
except AssertionError as error: print(f"Fail {error}")

try: assert odd_or_even(9) == "Odd", "Did not get Odd for odd_or_even(9)"
except AssertionError as error: print(f"Fail {error}")

print("All tests have been run")

# Function to test

def add_to_self(num):
    if isinstance(num, str): return "Error"
    return num + num

# Tests

try: assert add_to_self(5) == 10, "Did not get 10 for add_to_self(5)"
except AssertionError as error: print(f"fail: {error}")

try: assert add_to_self(9) == 18, "Did not get 18 for add_to_self(9)"
except AssertionError as error: print(f"fail:{error}")

try: assert add_to_self(9.0) == 18, "Did not get 18 for add_to_self(9.0)"
except AssertionError as error: print(f"fail:{error}")


try: assert add_to_self("cat") == "Error", "Did not get error for add_to_self('cat')"
except AssertionError as error: print(f"fail:{error}")


expected_result = "Error"
actual_result = add_to_self("cat")

try: assert actual_result == expected_result, f"Expected: {expected_result}, but got: {actual_result}"
except AssertionError as error: print(f"Fail: {error}")

print("All tests have been run")
