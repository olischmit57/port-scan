Basic Python Port Scanner

A lightweight, beginner‑friendly port scanner written in Python.
This project is a great starting point for learning cybersecurity fundamentals such as networking, enumeration, and TCP connections.

Features

• 	Scans the first 1024 TCP ports
• 	Identifies open ports on a target host
• 	Uses only Python’s built‑in  library
• 	Runs instantly with no external dependencies

Requirements

• 	Python 3.x
• 	Any OS that supports Python (Windows, macOS, Linux)

How to Run

1. 	Clone the repository:
2. 	Navigate into the project folder:
3. 	Run the script:
4. 	Enter the target IP when prompted.

 How It Works
 
The script attempts to establish a TCP connection to each port in the range .
If the connection succeeds, the port is considered open.

This teaches:

• 	How sockets work
• 	Basics of network scanning
• 	How services listen on ports


Future Enhancements (Optional Ideas)

• 	Multi‑threaded scanning for speed
• 	Banner grabbing
• 	Service detection
• 	Scan custom port ranges
• 	Export results to a file

License
This project is open‑source and available under the MIT License.
