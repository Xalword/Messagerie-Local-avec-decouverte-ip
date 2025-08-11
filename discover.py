import socket
import time

class Discovery:
    def __init__(self):
        self.discovery_port = 5567

#self.ip = ip locale

        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.connect(("8.8.8.8", 80))
            self.ip = self.s.getsockname()[0]
            self.s.close()
            
        except:
            self.ip = "127.0.0.1"

    def snd_rcv(self):
        snd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        snd_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        snd_socket.settimeout(10.0)
        #rcv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #rcv_socket.bind(("", self.discovery_port))
        

        snd_socket.sendto("T'es Là ?".encode("utf8"), ('255.255.255.255', self.discovery_port))
        print(f"Message envoyé depuis {snd_socket.getsockname()}")  


        while True:
            try:
                
                data, adrr = snd_socket.recvfrom(1024)
                self.autreip = data.decode('utf8')
                if data:
                    break
                
                
                
            except socket.timeout:
                print("Timeout - aucune réponse")
                return None  
            except socket.error:
                break

        return self.autreip
