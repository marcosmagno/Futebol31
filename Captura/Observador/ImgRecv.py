'''
Created on 26 de out de 2017

@author: Luis Henrique Cantelli Reis
'''
import socket
import _thread as thread
import cv2

from Commons.comunica import comunica
from Commons.configuracao  import configuracaoObservador


class  MostraTela(comunica):

    def __init__(self, con, cliente):
        self.cliente = cliente
        self.set_client_socket(con)
        self.mostraImagem()
                        
    def mostraImagem(self):    
        print("Conectado com ", self.cliente)
        
        while True:
            frame = self.recebe_processador()
            if (len(frame) > 0):
                try:
                    cv2.imshow('Janela de Recepcao', frame)
                except BaseException as e:
                    print("Observador::", e)
                    
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break            

        print("Finanizando Observador" + self.cliente)

    def recebe_processador(self):
        msg = self.recebe_cliente()
        return self.decodifica(msg)
            

class ImgRec:
    
    def __init__(self):
        conf = configuracaoObservador()
        self.porta = conf.observa_porta
        self.aguardaConexao()
        
    def aguardaConexao(self):
        HOST = ''
        PORT = self.porta
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp .setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        orig = (HOST, PORT)
        self.tcp.bind(orig)
        self.tcp.listen(1)
        print("Observador:: Aguardando conexao na porta: ", PORT)
        while True:             
            con, cliente = self.tcp.accept()
            print("Observador:: cliente  ", cliente, " Conectado.")
            thread.start_new_thread(MostraTela, tuple([con, cliente]))
    
    def __del__(self):
        print("Observador:: Encerrado")
        self.tcp.close()
        

if __name__ == '__main__':
    print("Iniciando Observador")
    obj = ImgRec()
    del obj
    
