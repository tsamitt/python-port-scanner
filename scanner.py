import socket

def scan_port(host: str, port: int) -> bool:
    """Return True if the TCP port is open, otherwise False."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            return result == 0
    except socket.gaierror:
        print("Error: Hostname could not be resolved.")
        return False
    except socket.error:
        print("Error: Could not connect to the server.")
        return False

def main() -> None:
    print("Simple Python Port Scanner")
    host = input("Enter a hostname or IP address: ").strip()

    ports_to_scan = [20, 21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

    print(f"\nScanning host: {host}\n")

    for port in ports_to_scan:
        if scan_port(host, port):
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is closed")

if __name__ == "__main__":
    main()
