import socket

def scan_port(ip, port):
    """Attempt to connect to a specific port."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        sock.connect((ip, port))
        return True
    except:
        return False
    finally:
        sock.close()

def basic_port_scanner():
    print("=== Basic Python Port Scanner ===")
    target = input("Enter target IP address: ")

    print(f"\nScanning {target}...\n")

    for port in range(1, 1025):  # Scan first 1024 ports
        if scan_port(target, port):
            print(f"[OPEN] Port {port}")
    
    print("\nScan complete.")

if __name__ == "__main__":
    basic_port_scanner()

