import os
import time
import subprocess
import argparse

def poll():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dispatcher-server", help="Dispatcher host:port", default="localhost:8888")
    parser.add_argument("repo", metavar="REPO", type=str, help="Path to the repository to observe")
    args = parser.parse_args()

    last_commit_hash = None

    while True:
        try:
            # Fetch latest changes from the remote
            subprocess.check_output(["git", "-C", args.repo, "fetch", "origin", "master"])
            # Get the latest commit hash
            latest_commit_hash = subprocess.check_output(
                ["git", "-C", args.repo, "rev-parse", "FETCH_HEAD"]
            ).strip().decode()

            # Check if there is a new commit
            if last_commit_hash != latest_commit_hash:
                print("New commit detected. Notifying dispatcher...")
                last_commit_hash = latest_commit_hash

            else:
                # Only output "No new commit. Sleeping..." when no changes are detected
                print("No new commit. Sleeping...")

        except subprocess.CalledProcessError as e:
            print(f"Failed to update repo: {e}")
            continue

        # Poll every 5 seconds
        time.sleep(5)

if __name__ == "__main__":
    poll()
