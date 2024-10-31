import os
import time
import subprocess
import argparse
import requests  # Add this import if you use HTTP requests to notify the dispatcher

def poll():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dispatcher-server", help="Dispatcher host:port", default="localhost:8888")
    parser.add_argument("repo", metavar="REPO", type=str, help="Path to the repository to observe")
    args = parser.parse_args()
    dispatcher_host, dispatcher_port = args.dispatcher_server.split(":")

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

                # Notify the dispatcher (using a simple print or HTTP call)
                # For example, if your dispatcher listens over HTTP:
                # requests.post(f"http://{dispatcher_host}:{dispatcher_port}/notify", json={"commit": last_commit_hash})

            else:
                print("No new commit. Sleeping...")

        except subprocess.CalledProcessError as e:
            print(f"Failed to update repo: {e}")
            continue

        # Poll every 5 seconds
        time.sleep(5)

if __name__ == "__main__":
    poll()
