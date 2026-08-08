from app import *
from logger import *

# add
def test_add(a, b, r):
    log("starting testing add function")
    result = add(a, b)
    if result == r:
        log("test successful")
        success_message(f"adding {a} + {b} is equal to {r}")
    else:
        error("test failed")
        failed_message(f"adding {a} + {b} is not equal to {r}")
    log("test ended.")

test_add(7, 4, 11)

print("-------------------------------------------")

# subtract
def test_subtract(a, b, r):
    log("starting testing subtract function")
    result = subtract(a, b)
    if result == r:
        log("test successful")
        success_message(f"subtracting {a} - {b} is equal to {r}")
    else:
        error("test failed")
        failed_message(f"subtracting {a} - {b} is not equal to {r}")
    log("test ended.")

test_subtract(50, 15, 35)

print("-------------------------------------------")

# multiply
def test_multiply(a, b, r):
    log("starting testing multiply function")
    result = multiply(a, b)
    if result == r:
        log("test successful")
        success_message(f"multipling {a} * {b} is equal to {r}")
    else:
        error("test failed")
        failed_message(f"multipling {a} * {b} is not equal to {r}")
    log("test ended.")

test_multiply(5, 5, 25)

print("-------------------------------------------")

# division
def test_division(a, b, r):
    log("starting testing division function")
    result = division(a, b)
    if result == r:
        log("test successful")
        success_message(f"dividing {a} / {b} is equal to {r}")
    else:
        error("test failed")
        failed_message(f"dividing {a} / {b} is not equal to {r}")
    log("test ended.")

test_division(100, 5, 20)
