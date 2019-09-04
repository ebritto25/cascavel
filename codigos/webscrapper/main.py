if __name__ == '__main__':
    #scrapper = RottenScrapper()

    def menu():
        opcoes = ['Em cartaz essa semana', 'Top de bilheteria',
                  'Em breve nos cinemas', 'Na TV hoje a noite',
                  'Series populares no RT', 'Top em DVD e Streaming']

        def emcartaz():
            print('TODO: FUNC_EM_CARTAZ')
        def topbox():
            print('TODO: FUNC_TOP_BOX_OFFICE')
        def embreve():
            print('TODO: FUNC_EM_BREVE')
        def tvhoje():
            print('TODO: FUNC_NA_TV_HOJE')
        def series():
            print('TODO: FUNC_SERIES_POP')
        def topdvd():
            print('TODO: FUNC_TOP_DVD')
        def sair():
            exit()
        def opcinvalida():
            print('Opção inválida!')

        def get_acao(escolha):
            acoes = {'1':emcartaz, '2':topbox, '3':embreve,
                     '4':tvhoje, '5':series, '6':topdvd,
                     'sair':sair}

            return acoes.get(escolha,opcinvalida)()


        for opc_num, opcao in enumerate(opcoes,1):
            print(f'{opc_num} - {opcao}')

        get_acao(input('Escolha uma opção ou digite aperte [enter] para sair: ') or 'sair')

    while(True):
        menu()
