def main():
    nome_do_arquivo = 'wata.txt'

    with open(nome_do_arquivo,'r') as file_:
        print(file_.read())


if __name__ == '__main__':
    main()
