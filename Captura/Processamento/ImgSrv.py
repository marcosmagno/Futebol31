'''
Created on 26 de out de 2017

@author: Luis Henrique Cantelli Reis
'''

import _thread as thread
import socket
from Commons.comunica import comunica
from Processamento.Captura import processaImagem
from Commons.configuracao  import configuracaoProcessamento
import time as time

IMAGE_HEIGHT = 800
IMAGE_WIDTH = 1920
COLOR_PIXEL = 3  # RGB


class  processador(comunica):

    def __init__(self, con, cliente):
        config = configuracaoProcessamento()
        self.IpObservador = config.observa_server
        self.PortaObservador = config.observa_porta
        
        self.set_client_socket(con)                
        self.cliente = cliente
        self.proc = processaImagem()
        self.processo_principal()
            
    def processo_principal(self):
        print("Aguardando imagens para processar")

        if (not self.conecta_observador()):
            print("Error: Observer connection fail")
            return
        print("Observador conectado")
        
        # contador de frames por segundo
        start_time = time.time()
        contador = 0
        while True:
            print("Recebendo imagens")
            msg = self.recebe_captura()

            if len(msg) > 0:
                imagem = self.proc.Frecognition(msg)
                imagem = msg
                if len(imagem) > 0:
                    self.envia_observador(msg)
            else:
                return
        
            nowtime = time.time()
            if nowtime - start_time > 1:
                print(contador, " frames processados em ", (nowtime - start_time) , "Segundos")
                start_time = time.time()
                contador = 0
            else:
                contador += 1 

    def recebe_captura(self):
        msg = self.recebe_cliente()     
        frame = self.decodifica(msg)        
        return frame

    def envia_observador(self, msg):
        self.codifica(msg)
        # Enviar Imagem para Observador
        self.envia_servidor(msg)       

    def conecta_observador(self):
        TCP_IP = self.IpObservador         
        TCP_PORT = self.PortaObservador
        con = self.conecta_servidor(TCP_IP, TCP_PORT)
        if con == None:
            return False
        else:
            return True
            

class Server:
    
    def __init__(self):
        config = configuracaoProcessamento()
        self.porta = config.porta
        
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
            thread.start_new_thread(processador, tuple([con, cliente]))

        
if __name__ == '__main__':
    print("Processador Inicializado")
    im = Server()
    im.aguardaConexao()
    print("Processador Finalizado")
    
