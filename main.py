import socket
import threading
import sys
from create import Create
from join import Join

if __name__ == '__main__':
    
    a = input("create or join ?\n")

    if a == "join":
        Join()

    if a == "create":
        Create()