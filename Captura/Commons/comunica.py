'''
Created on 26 de abr de 2018

@author: luis
'''
import base64
import socket
import numpy as np
import numpy
from _socket import TCP_NODELAY, IPPROTO_TCP


class comunica:
    '''
    classdocs
    
    '''
    IMAGE_HEIGHT = 800
    IMAGE_WIDTH = 1920
    COLOR_PIXEL = 3  # RGB
    servidor_con = None
    client_con = None 
    
    def __init__(self):
        '''
        Constructor

        self.IMAGE_WIDTH = 800
        self.IMAGE_HEIGHT = 1920
        self.COLOR_PIXEL = 3
        self.servidor_con = None
        self.client_con = None 
        '''

    def set_client_socket(self, con):
        self.client_con = con     
    
    def set_definicao(self, largura, altura, cores_pixel=3):
        self.IMAGE_WIDTH = largura
        self.IMAGE_HEIGHT = altura
        self.COLOR_PIXEL = cores_pixel
        
    def conecta_servidor(self, ip, porta):

        self.servidor_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor_con.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)        

        try:
            self.servidor_con.connect((ip, porta))
        except ConnectionRefusedError as e:
            print("Error: Can't connect server : ", ip, "Port: ", porta, " - error", e)
            return None        
        return self.servidor_con            

    def envia_cliente(self, msg):
        self.envia_rede(self.cliente_con, msg)
     
    def envia_rede(self, sock, frame):
        
        data = numpy.array(frame)
        stringData = data.tostring()
        try:
            # Envia a largura da imagem
            msg = str(self.IMAGE_HEIGHT).ljust(16).encode('utf_8')     
            totalsent = 0
            while totalsent < 16:
                sent = sock.send(msg[totalsent:])
                if sent == 0:
                    raise RuntimeError("socket connection broken")
                totalsent = totalsent + sent
                      
            # Envia a altura da imagem                      
            msg = str(int(self.IMAGE_WIDTH)).ljust(16).encode('utf_8')     
            totalsent = 0
            while totalsent < 16:
                sent = sock.send(msg[totalsent:])
                if sent == 0:
                    raise RuntimeError("socket connection broken")
                totalsent = totalsent + sent       
            
            # Envia o tamanho do pacote           
            msg = str(len(stringData)).ljust(16).encode('utf_8')     
            totalsent = 0
            while totalsent < 16:
                sent = sock.send(msg[totalsent:])
                if sent == 0:
                    raise RuntimeError("socket connection broken")
                totalsent = totalsent + sent       
            
            # Enviando imagem
            lenData = len(stringData)
            totalsent = 0
            while totalsent < lenData:
                sent = sock.send(stringData[totalsent:])
                if sent == 0:
                    raise RuntimeError("socket connection broken")
                totalsent = totalsent + sent       
            
        except Exception as e:
            print("Erro ao enviar mensagem::::", str(e))
            raise RuntimeError("socket connection broken")
    
    def recebe_cliente(self):
            return self.recebe_rede(self.client_con)        
   
    def envia_servidor(self, msg):
        self.envia_rede(self.servidor_con, msg)
    
    def recebe_servidor(self):
        self.recebe_rede(self.servidor_con)
        
    def recebe_rede(self, soc):
        # larguda da imagem
        rec = self.recvall(soc, 16)
        if rec == None:
                return ""
        else:
            self.IMAGE_HEIGHT = int(rec)
        
        # altura da umagem
        rec = self.recvall(soc, 16)
        if rec == None:
                return ""
        else:
            self.IMAGE_WIDTH = int(rec)           
        # Tamanho da imagem
        tam = self.recvall(soc, 16)
        if tam == None:
                return ""
        tam = int(tam)
        stringData = self.recvall(soc, int(tam))
        # data = numpy.fromstring(stringData, dtype='uint8')        

        return stringData 

    def recvall(self, soc, count):    
        buf = b''

        while count:            
            newbuf = soc.recv(count)
            print("Recived ", len(newbuf), " of :: ", count)            
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf                

    def codifica(self, frame):
        return frame
        a = b'\r\n'
        f = frame.tostring().encode('utf_8')
        da = base64.b64encode(f)
        return da + a            

    def decodifica(self, msg):
        try:
            # msg = base64.decode(msg)    
            frm = np.fromstring(msg, dtype=np.uint8)
            frame_matrix = np.array(frm)
            frame_matrix = np.reshape(frame_matrix, (self.IMAGE_HEIGHT, self.IMAGE_WIDTH, self.COLOR_PIXEL))
            return frame_matrix
        except Exception as e:
            print("[Erro de decodificacao] ")
            print(e)
            return

    def __del__(self):
        if self.client_con != None:
            self.client_con.close()
        if self.servidor_con != None:
            self.servidor_con.close()
        
