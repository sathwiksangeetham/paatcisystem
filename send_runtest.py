import socket

# Define the dispatcher host and port
dispatcher_host = "localhost"
dispatcher_port = 8888

# Define a sample commit ID for testing
commit_id = "526f28c"  # Replace with the latest commit ID you want to test

# Create a socket and connect to the dispatcher
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((dispatcher_host, dispatcher_port))
    # Send the runtest command with the commit ID
    s.sendall(f"runtest:{commit_id}".encode())
    # Receive the response from the dispatcher or runner
    response = s.recv(1024).decode()
    print(f"Response from dispatcher/runner: {response}")
