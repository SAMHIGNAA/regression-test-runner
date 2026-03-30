def print_report(results):
    passed = 0
    failed = 0

    print("\nRunning Regression Tests...\n")

    for r in results:
        print(f"{r['name']}: {r['status']} ({r['time']}s)")
        if r['status'] == "PASS":
            passed += 1
        else:
            failed += 1

    print("\nSummary")
    print("-------")
    print(f"Total Tests: {len(results)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
