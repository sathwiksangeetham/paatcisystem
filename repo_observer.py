import os
import time
import subprocess
import argparse

def poll():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dispatcher-server", help="Dispatcher host:port", default="localhost:8888")
    parser.add_argument("repo", metavar="REPO", type=str, help="Path to the repository to observe")
    args = parser.parse_args()
    dispatcher_host, dispatcher_port = args.dispatcher_server.split(":")

    while True:
        try:
            subprocess.check_output(["git", "-C", args.repo, "pull"])
        except subprocess.CalledProcessError as e:
            print(f"Failed to update repo: {e}")
            continue

        print("Repo checked. Sleeping...")
        time.sleep(5)

if __name__ == "__main__":
    poll()
