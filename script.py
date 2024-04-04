import socket

def test_connection(host, port):
    try:
        socket.create_connection((host, port), timeout=5)
        print(f"Connection to {host}:{port} successful")
    except Exception as e:
        print(f"Connection to {host}:{port} failed: {e}")

# Replace 'rabbitmq' and '5672' with the hostname and port you want to test
test_connection('rabbitmq', 5672)