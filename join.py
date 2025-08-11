import socket
import threading
import sys
from discover import Discovery

class Join:
    def __init__(self):

        self.fin = False
        self.nom = input("Quel est votre nom ?\n")

        print(".....Recherche d'hôte en cours.....")

        adress = Discovery()
        ippp = adress.snd_rcv()
        if ippp == None:
            print("Aucun hôte trouvé... Fin du programme....")
            sys.exit()

        print("-----Hôte trouvé !-----")


        host , port = (ippp, 5566)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



        try:
            self.socket.connect((host, port))
            self.socket.sendall(self.nom.encode("utf8"))
            print(".....En attente de l'accepation de l'hôte.....")
            rep = self.socket.recv(1024)
            rep = rep.decode("utf8")
            if rep == "off":
                print("-----Connection refusée par l'hôte-----")
                self.socket.close
            if rep != "off":
                self.hote = self.socket.recv(1024)
                self.hote = self.hote.decode("utf8")
                print(f"-----Connection acceptée par {self.hote} ! Vous pouvez chatter. Envoyez /finish pour terminer la communication-----")
                
                

            
            
                self.send_thread = threading.Thread(target=self.snd)
                self.receive_thread = threading.Thread(target=self.rcv)

                self.send_thread.start()
                self.receive_thread.start()
            
                self.send_thread.join()
                self.receive_thread.join()

        except ConnectionRefusedError:
            print('connecton au serveur échouée')
        finally:
            self.socket.close()


    def snd(self):
            
        while self.fin == False:
            snd = input("{}: ".format(self.nom))
            if snd == "/finish":
                sure = input("Voulez vous vraiment arrêter la telecom ?(y/n)\n")
                if sure == "y":
                    self.socket.sendall(snd.encode("utf8"))
                    print("....Fin de la communication....")
                    self.fin = True
                    sys.exit()
                    break

            self.socket.sendall(snd.encode("utf8"))


    def rcv(self):
    
        while self.fin == False:
                            
            rcv = self.socket.recv(1024)
                    
            if not rcv:
                print(f"-----Connexion terminée par {self.hote}-----")
                self.fin = True                
                break
            rcv = rcv.decode("utf8")

            if rcv == "/finish":
                print(f"-----Connexion terminée par {self.hote}-----") 
                self.fin = True  
                sys.exit()            
                break

            else:                    
                print(f"\n-----{self.hote}-----\n", rcv, "\n---------------")