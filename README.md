# Python Port Scanner

## Overview

This project is a simple Python-based TCP port scanner that checks a list of common ports on a target host to determine whether they are open or closed.

The purpose of this project is to strengthen understanding of networking concepts such as TCP communication, port numbers, and basic service discovery.

## Skills Demonstrated

- Python scripting
- Socket programming
- TCP/IP fundamentals
- Basic network troubleshooting
- Introductory security concepts

## How It Works

The script prompts the user to enter a hostname or IP address.

It then attempts to connect to a list of common TCP ports using Python's `socket` module.

If the connection succeeds, the port is reported as open. Otherwise, it is reported as closed.

## Common Ports Scanned

- 20 / 21 – FTP
- 22 – SSH
- 23 – Telnet
- 25 – SMTP
- 53 – DNS
- 80 – HTTP
- 110 – POP3
- 139 – NetBIOS
- 143 – IMAP
- 443 – HTTPS
- 445 – SMB
- 3389 – RDP

## Files

- `scanner.py` – Main Python script
- `common-ports.md` – Notes on common ports and services
- `sample-output.txt` – Example output from a scan


## What I Learned

Through this project, I learned how TCP port scanning works at a basic level and how Python sockets can be used to interact with network services.
