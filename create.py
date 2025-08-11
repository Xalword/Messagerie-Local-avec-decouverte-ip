import socket
import threading
import sys
from broadcast import Attente

class Create:
    def __init__(self):


        self.fin = False
        self.nom = input("Quel est votre nom ?\n")
        print("En attente de connexion...")

        a = Attente()
        envoyer = a.discovery_listener()
        host, port = ('', 5566)

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(5)
        self.conn, self.address = self.socket.accept()

        self.interloc = self.conn.recv(1024)
        b = input(f"{self.interloc.decode("utf8")} souhaite discuter avec vous ! Accepter ? (y/n)\n")

        if b == "y":
            g = "good"
            self.conn.sendall(g.encode("utf8"))

            self.conn.sendall(self.nom.encode("utf8"))

            print(f"Connecté ! Vous pouvez désormais envoyer et recevoir des messages avec {self.interloc.decode("utf8")} ! ")


            self.send_thread = threading.Thread(target=self.snd)
            self.receive_thread = threading.Thread(target=self.rcv)

            self.send_thread.start()
            self.receive_thread.start()
            
            self.send_thread.join()
            self.receive_thread.join()


        if b == "n":
            mss = "off"
            self.conn.sendall(mss.encode("utf8"))
            self.conn.close()
            self.socket.close()
            print("connexion avortée.")








    def snd(self):

        while self.fin == False:
            snd = input("{}: ".format(self.nom))
            if snd == "/finish":
                sure = input("Voulez vous vraiment arrêter la telecom ?(y/n)\n")
                if sure == "y":
                    self.conn.sendall(snd.encode("utf8"))
                    print("....Fin de la communication....")
                    self.fin = True
                    sys.exit()
                    break

            self.conn.sendall(snd.encode("utf8"))


    def rcv(self):

        while self.fin == False:
                        
            rcv = self.conn.recv(1024)
                    
            if not rcv:
                print(f"-----Connexion terminée par {self.interloc.decode("utf8")}-----")
                self.fin = True               
                break
            rcv = rcv.decode("utf8")

            if rcv == "/finish":
                print(f"-----Connexion terminée par {self.interloc.decode("utf8")}-----")
                self.fin = True
                sys.exit()           
                break

            else:                    
                print(f"\n-----{self.interloc.decode("utf8")}-----\n", rcv, "\n---------------")
            
       

    
