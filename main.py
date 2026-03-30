import logging
import argparse

from src.runner import run_tests, discover_tests
from src.reporter import print_report
from src.utils import save_log


def main():
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    parser = argparse.ArgumentParser()
    parser.add_argument("--filter", help="Run specific test (e.g. login)")
    args = parser.parse_args()

    logging.info("Test execution started")

    tests = discover_tests()

    # 🔹 Apply filter if given
    if args.filter:
        tests = {name: func for name, func in tests.items() if args.filter in name}

    results, total_time = run_tests(tests)

    print_report(results)
    print(f"\nExecution Time: {total_time}s")

    save_log(results)

    logging.info("Test execution completed")

    print("\nLog saved as test_log.txt")


if __name__ == "__main__":
    main()