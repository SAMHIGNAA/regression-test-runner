import time

def test_login():
    time.sleep(1)
    return True

def test_payment():
    time.sleep(1)
    return False

def test_signup():
    time.sleep(1)
    return True

def test_profile_update():
    time.sleep(1)
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

    start_time = time.time()

    results = []

    for name, test in tests.items():
        test_start = time.time()
        result = test()
        duration = round(time.time() - test_start, 2)

        status = "PASS" if result else "FAIL"
        results.append((name, status, duration))

        if result:
            print(f"  {name}: PASS ({duration}s)")
            passed += 1
        else:
            print(f"  {name}: FAIL ({duration}s)")
            failed += 1

    total_time = round(time.time() - start_time, 2)

    print("\n--- Summary ---")
    print(f"  Total Tests   : {passed + failed}")
    print(f"  Passed        : {passed}")
    print(f"  Failed        : {failed}")
    print(f"  Execution Time: {total_time}s")

    # Save log
    with open("test_log.txt", "w") as log_file:
        log_file.write("Regression Test Execution\n")
        log_file.write("-" * 30 + "\n")
        for name, status, duration in results:
            log_file.write(f"{name}: {status} ({duration}s)\n")
        log_file.write("\n--- Summary ---\n")
        log_file.write(f"Total  : {passed + failed}\n")
        log_file.write(f"Passed : {passed}\n")
        log_file.write(f"Failed : {failed}\n")
        log_file.write(f"Time   : {total_time}s\n")

    print("\nLog saved as test_log.txt")

if __name__ == "__main__":
    run_tests()