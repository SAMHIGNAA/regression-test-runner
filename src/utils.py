def save_log(results):
    with open("test_log.txt", "w") as f:
        f.write("Regression Test Results\n")
        f.write("-----------------------\n")

        for r in results:
            f.write(f"{r['name']}: {r['status']} ({r['time']}s)\n")
