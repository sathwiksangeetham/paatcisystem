import os
import subprocess
import sys

def run_tests(repo_path):
    print("Running tests...")
    result = subprocess.run([sys.executable, "-m", "unittest", "discover", repo_path], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_runner.py <repo_path>")
        sys.exit(1)

    run_tests(sys.argv[1])
 
