from scrapper import Scrapper

class RottenScrapper(Scrapper):

    def __init__(self):
        super().__init__('http://www.rottentomatoes.com')
        self.dom = self.parse_html()
    
    def __str__(self):
        return self.dom.text
    
    def get_essa_semana(self):
        div_em_cartaz = self.dom.find(id = 'Opening')

        dados = []

        for linha in div_em_cartaz.find_all('tr','sidebarInTheaterOpening'):
            print(linha)
            nota = linha.find(class_ = 'left_col').find(class_ = 'tMeterScore').text or 'Sem nota'
            nome = linha.find(class_ = 'middle_col').a.text
            lancamento = linha.find(class_ = 'right_col').a.text

            dados.append((nota,nome,lancamento))

        return dados
