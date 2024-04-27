#!/usr/bin/python3
import sys
import socket


# PiJuice will provide switch name
btn = sys.argv[2]

bytesToSend = str.encode(btn)
serverAddressPort   = ("127.0.0.1", 1234)
bufferSize          = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)