def test_login():
    return True

def test_payment():
    return False

def test_signup():
    return True

def test_profile_update():
    return True

tests = {
    "Login Test": test_login,
    "Payment Test": test_payment,
    "Signup Test": test_signup,
    "Profile Update Test": test_profile_update
}

def run_tests():
    passed = 0
    failed = 0

    print("Running Regression Tests...\n")

    for name, test in tests.items():
        result = test()
        if result:
            print(f"{name}: PASS")
            passed += 1
        else:
            print(f"{name}: FAIL")
            failed += 1

    total = passed + failed

    print("\nSummary")
    print("-------")
    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

if __name__ == "__main__":
    run_tests()