import requests
from bs4 import BeautifulSoup as bs

'''
Essa classe é responsável por fazer a requisição HTTP a uma url que é
passada para seu construtor (função __init__) e armazenar a resposta no 
atributo resposta
'''
class Scrapper():

    def __init__(self,url):
        self.url = url
        self.resposta = requests.get(url)
        try:
            self.html = self.get_html()
        except Exception as erro:
            print(erro)
    
    def get_html(self):
        '''
        Se o código de resposta HTTP for OK (200) então podemos pegar
        o código html da página para usarmos
        '''

        resposta = self.resposta
        status = resposta.status_code

        if status == 200:
            return resposta.text 
        else:
            raise Exception('Erro ao acessar o site!')

    def parse_html(self):
        '''
        Com o código HTML em mãos podemos transformar ele em um objeto
        da biblioteca BeautifulSoup que se comporta de forma parecida com
        a uma árvore
        '''

        return bs(self.html,'html.parser')
