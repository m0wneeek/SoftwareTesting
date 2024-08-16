#No import on calc

from calc import add

try: assert add(2,2) == 4, "Did not get 4 for add(2,2)"
except AssertionError as error: print(f"Fail: {error}")

try: assert add(20,22) == 42, "Did not get 42 for add(20,22)"
except AssertionError as error: print(f"Fail: {error}")

try: assert add(20.0,2.0) == "Error: The calculator can only accept whole numbers", "Did not get error message when adding floats"
except AssertionError as error: print(f"Fail: {error}")

try: assert add(2, "cat") == "Error: The calculator can only accept whole numbers", "Did not get error message when adding int and str"
except AssertionError as error: print(f"Fail: {error}")

print("All addition tests have been run")

expected_result = "Error: The calculator can only accept whole numbers"
actual_result = add(20.0, 4.0)

try: assert actual_result == expected_result, f"Expected: {expected_result}, but got: {actual_result}"
except AssertionError as error: print(f"Fail: {error}")

print("All further addition tests have been run")


from calc import sub 

try: assert sub(4,2) == 2, "Did not get 2 for sub(4,2)"
except AssertionError as error: print(f"Fail: {error}")

try: assert sub(2,"cat") == "Error: The calculator can only accept whole numbers", "Did not get an error message subtracting cat from 2"
except AssertionError as error: print(f"Fail: {error}")

try: assert sub(62,20) == 42, "Did not get 42 for sub(62, 20)"
except AssertionError as error: print(f"Fail: {error}")

try: assert sub(20.0, 2.0) == "Error: The calculator can only accept whole numbers", "Did not get an error message subtracting 2.0 from 20.0"
except AssertionError as error: print(f"Fail: {error}")

print("All subtraction tests have been run")

expected_result = 10
actual_result = sub(12, 2)

try: assert actual_result == expected_result, f"Expected: {expected_result}, but got: {actual_result}"
except AssertionError as error: print(f"Fail: {error}")

print("All further subtraction tests have been run")


from calc import mul

try: assert mul(8,8) == 64, "Did not get 64 for mul(8,8)"
except AssertionError as error: print(f"Fail: {error}")

try: assert mul(2,"cat") == "Error: The calculator can only accept whole numbers", "Did not get an error message multiplying 2 and cat"
except AssertionError as error: print(f"Fail: {error}")

try: assert mul(6,7) == 42, "Did not get 42 for mul(6,7)"
except AssertionError as error: print(f"Fail: {error}")

try: assert mul(20.0, 2.0) == "Error: The calculator can only accept whole numbers", "Did not get an error message multiplying 2.0 from 20.0"
except AssertionError as error: print(f"Fail: {error}")

print("All multiplication tests have been run")

expected_result = "Error: The calculator can only accept whole numbers"
actual_result = mul(2,"cat") 

try: assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"
except AssertionError as error: print(f"Fail: {error}")

print("All further multiplication tests have been run")

#mul function concatenates


from calc import div

try: assert div(10,2) == 5, "Did not get 5 for div(10,2)"
except AssertionError as error: print(f"Fail: {error}")

try: assert div(2,"cat") == "Error: The calculator can only accept whole numbers", "Did not get an error message dividing 2 and cat"
except AssertionError as error: print(f"Fail: {error}")

try: assert div(84,2) == 42, "Did not get 42 for div(84,2)"
except AssertionError as error: print(f"Fail: {error}")

try: assert div(20,0) == "Error: The caculator cannot divide by zero", "Did not get an error message dividing by zero"
except AssertionError as error: print(f"Fail: {error}")

try: assert div(20.0,2.0) == "Error: The calculator can only accept whole numbers", "Did not get an error message dividing with floats"
except AssertionError as error: print(f"Fail: {error}")

print("All division tests have been run")

expected_result = "Error: The calculator can't divide by zero"
actual_result = div(20,0)

try: assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"
except AssertionError as error: print(f"Fail: {error}")

print("All further division tests have been run")
