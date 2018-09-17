'''
Created on 19 de jun de 2018

@author: Luis Henrique Cantelli Reis
'''

import configparser


class Configuracao:
    n_processadores = 1
    server = '192.168.0.65'
    porta = 4301
    
    def __init__(self):
        self.abre_arquivo("config.ini")
       
    def abre_arquivo(self , nome_arquivo):
        pass
        
        
class configuracaoCaptura(Configuracao):
    
    def abre_arquivo(self, nome_arquivo):
        
        config = configparser.ConfigParser()        
        n_processadores = 1
        porta = 4301
        server = '192.168.0.65'
        entrada = ""
        try:
            config.read(nome_arquivo)
            n_processadores = config['Processadores']['numero']
            porta = config['PROCESSADOR']['PORT']
            server = config['PROCESSADOR']['IP']
            entrada = config['CAPTURA']['ARQ']
        except FileExistsError as e:
            print("Warning: Configuration File not found. Using default values")
            print("Warning: Default Values: Port ", porta, " Number of Processors: ", n_processadores, e)

        self.n_processadores = int(n_processadores)
        self.porta = int(porta)
        self.server = server
        self.entrada = entrada
        return 


class configuracaoProcessamento(Configuracao):
    observa_server = '192.168.0.65'
    observa_porta = 5005
    
    def abre_arquivo(self, nome_arquivo):
        config = configparser.ConfigParser()        
        n_processadores = 1
        porta = 4301
        server = '192.168.0.65'
        try:
            config.read(nome_arquivo)
            n_processadores = config['Processadores']['numero']
            porta = config['PROCESSADOR']['PORT']
            server = config['PROCESSADOR']['IP']
            observa_server = config['OBSERVADOR']['IP']
            observa_porta = config['OBSERVADOR']['PORT']
            
        except FileExistsError as e:
            print("Warning: Configuration File not found. Using default values")
            print("Warning: Default Values: Port ", porta, " Number of Processors: ", n_processadores, e)

        self.n_processadores = int(n_processadores)
        self.porta = int(porta)
        self.server = server.strip()
        self.observa_porta = int(observa_porta)
        self.observa_server = observa_server.strip()
        return 


class configuracaoObservador(Configuracao):
    observa_server = '192.168.0.65'
    observa_porta = 5005
    
    def abre_arquivo(self, nome_arquivo):
        config = configparser.ConfigParser()        
        n_processadores = 1
        porta = 4301
        server = '192.168.0.65'
        try:
            config.read(nome_arquivo)
            n_processadores = config['Processadores']['numero']
            observa_server = config['OBSERVADOR']['IP']
            observa_porta = config['OBSERVADOR']['PORT']
            
        except FileExistsError as e:
            print("Warning: Configuration File not found. Using default values")
            print("Warning: Default Values: Port ", porta, " Number of Processors: ", n_processadores, e)

        self.n_processadores = int(n_processadores)
        self.porta = int(porta)
        self.server = str(server)
        self.observa_porta = int(observa_porta)
        self.observa_server = str(observa_server)
        return 

