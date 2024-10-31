import os
import sys
import unittest

def run_tests(repo_path):
    # Define the test folder path
    test_folder = os.path.join(repo_path, "tests")
    
    # Discover and load all tests from the test folder
    suite = unittest.TestLoader().discover(test_folder)
    
    # Run the tests and display the results
    print("Running tests...")
    unittest.TextTestRunner().run(suite)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_runner.py <repo_path>")
        sys.exit(1)

    repo_path = sys.argv[1]
    run_tests(repo_path)
