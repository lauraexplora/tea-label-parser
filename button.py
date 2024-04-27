#!/usr/bin/python3
import sys
import zmq

btn = sys.argv[1]
c = zmq.Context()
s = c.socket(zmq.PAIR)
s.bind('tcp://*:1234')
s.send_string(btn)