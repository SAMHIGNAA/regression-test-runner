import time
import importlib
import os

def discover_tests(test_folder="tests"):
    test_modules = {}

    for file in os.listdir(test_folder):
        if file.startswith("test_") and file.endswith(".py"):
            module_name = file[:-3]  # remove .py
            module = importlib.import_module(f"{test_folder}.{module_name}")

            if hasattr(module, "run"):
                test_modules[module_name] = module.run

    return test_modules


def run_tests(test_modules):
    results = []
    start_total = time.time()

    for name, test_func in test_modules.items():
        start = time.time()

        result = test_func()

        duration = round(time.time() - start, 2)

        results.append({
            "name": name,
            "status": "PASS" if result else "FAIL",
            "time": duration
        })

    total_time = round(time.time() - start_total, 2)

    return results, total_time