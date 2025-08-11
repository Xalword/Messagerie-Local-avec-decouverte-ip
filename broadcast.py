import socket

class Attente:
    def __init__(self):
        self.discovery_port = 5567
        self.discovered = []
        
        #self.ip = ip locale

        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.connect(("8.8.8.8", 80))
            self.ip = self.s.getsockname()[0]
            self.s.close()
            
        except:
            self.ip = "127.0.0.1"
        
    def discovery_listener(self):
        self.listen_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_socket.bind(('',self.discovery_port))
        while True:
            try:
                data, adrr = self.listen_socket.recvfrom(1024)
                message = data.decode("utf8")
                if message == "T'es Là ?":
                    print(f"Envoi de réponse '{self.ip}' vers {adrr}")
                    response = self.ip
                    rep_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    rep_socket.sendto(response.encode("utf8"), adrr)
                    rep_socket.close()
                    break
                
            except socket.error:
                print("Erreur de connexion")
                break

