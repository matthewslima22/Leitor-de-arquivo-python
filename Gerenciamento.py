import os
import os.path
import shutil
import sys
import PyPDF2 as p2


var1 = 1
var2 = 2
var3 = 0
print('//////////////////////////////////////////////////////////////////////')
print('//////////////////////////////////////////////////////////////////////')
print('selecione o tipo de documento de acordo com o número ao seu lado')
print('//////////////////////////////////////////////////////////////////////')
print('pdf (1)', var1)
print('txt (2)', var2)
print('sair (0)', var3)
print('////////////////////////////////////////////////////////////////////////')
var1var2var3 = input('digite o número: ')

if var1var2var3 == '1':
    print('Abrindo Menu PDF')
    print('')
    source: str = ('D:\Projeto\Documento de Arrecadação do Simples Nacional - Correto.pdf')
    destination = 'D:\Salvar arquivos'

    arquivos_gde = os.listdir('D:\Projeto')
    print(os.listdir('D:\Projeto'))

    print('//////////////////////////////////////////////////////////////////////')
    print('//////////////////////////////////////////////////////////////////////')
    print('selecione o documento de acordo com o número ao seu lado')
    print('//////////////////////////////////////////////////////////////////////')
    print('Documento de Arrecadação da Receita Federal - Outro documento.pdf (1)')
    print('Documento de Arrecadação do Simples Nacional - Com CNPJ errado.pdf (2)')
    print('Documento de Arrecadação do Simples Nacional - Correto.pdf (3)')
    print('////////////////////////////////////////////////////////////////////////')

    arquivos_gde = input('Digite o número: ')
    if arquivos_gde == '3':
        original_dir = 'D:\Projeto'
        files = os.listdir(original_dir) # todos os ficheiros

        print(arquivos_gde.isprintable())

        arquivo = open('D:\Projeto\Documento de Arrecadação do Simples Nacional - Correto.pdf', 'rb')
        pdf_reader = p2.PdfFileReader(arquivo)

        n = pdf_reader.numPages
        for i in range(0, n):
            print('pagina {}'.format(i + 1))
        page = pdf_reader.getPage(i)
        print(page.extractText())


    else:
        print('arquivo errado')
        sys.exit()



    dest = shutil.copy(source, destination)

    print("Arquivo copiado:")
    print('')


    print("Destino:", dest)

    for arquivo in os.walk('D:\Projeto\Documento de Arrecadação do Simples Nacional - Correto.pdf'):
        print(arquivo)


    if os.path.isfile('D:\Salvar arquivos\MAAAA.MM - NNNNN.pdf'):
        print('Ja existe um arquivo com esse nome!')
        sys.exit()

    else:

        arquivo = os.rename('D:\Salvar arquivos\Documento de Arrecadação do Simples Nacional - Correto.pdf', 'D:\Salvar arquivos\MAAAA.MM - NNNNN.pdf')
        print('arquivo renomeado')
        print('//////////////////////////////////////////////')

        print('Deseja listar os arquivos desta pasta?')
        print('Sim (1)')
        print('Não (2)')

        z = input('Digite o numero desejado: ')
        if z == '1':
            print(os.listdir(destination))
            print('')
        else:
            sys.exit()


if var1var2var3 ==  ('2'):
    print("abrindo Menu txt")
    print('')

    source: str = ('D:\Projeto\Documento de Arrecadação do Simples Nacional - Correto.txt')
    destination = 'D:\Salvar arquivos'

    arquivos_gde2 = os.listdir('D:\Projeto')
    print(os.listdir('D:\Projeto'))

    print('//////////////////////////////////////////////////////////////////////')
    print('//////////////////////////////////////////////////////////////////////')
    print('Selecione o documento de acordo com o número ao seu lado')
    print('//////////////////////////////////////////////////////////////////////')
    print('Documento de Arrecadação da Receita Federal - Outro documento.txt (1)')
    print('Documento de Arrecadação do Simples Nacional - Com CNPJ errado.txt (2)')
    print('Documento de Arrecadação do Simples Nacional - Correto.txt (3)')
    print('////////////////////////////////////////////////////////////////////////')

    arquivos_gde2 = input('digite o numero: ')
    if arquivos_gde2 == '3':
        original_dir = 'D:\Projeto'
        files = os.listdir(original_dir)

        print(arquivos_gde2.isprintable())

        arquivo2 = open('D:\Projeto\Documento de Arrecadação do Simples Nacional - Correto.txt', 'r')
        for linha in arquivo2:
            linha = linha.strip()
            print (linha)

        dest = shutil.copy(source, destination)

        print("Arquivo copiado:")
        print('')

        print("Destino:", dest)

        for arquivo2 in os.walk('D:\Projeto\Documento de Arrecadação do Simples Nacional - Correto.txt'):
            print(arquivo2)

        if os.path.isfile('D:\Salvar arquivos\MAAAA.MM - NNNNN.txt'):
                print('Ja existe um arquivo com esse nome!')
                sys.exit()

        else:

            arquivo2 = os.rename('D:\Salvar arquivos\Documento de Arrecadação do Simples Nacional - Correto.txt', 'D:\Salvar arquivos\MAAAA.MM - NNNNN.txt')

            print('arquivo renomeado')

            print('//////////////////////////////////////////////')

            print('Deseja listar os arquivos desta pasta?')

            print('Sim (1)')

            print('Não (2)')

            z = input('Digite o numero desejado: ')

            if z == '1':

                print(os.listdir(destination))

                print('')

            else:

                sys.exit()

if var1var2var3 == '0':
    print('Obrigado por utilizar o gerenciador!')
    print('tchau')
    sys.exit()

else:
    var1var2var3 == '!=1,2,0'
    print ('Opção invalida')
    sys.exit()

#Projeto com erros no PDF
#não podendo renomear para o nome pedido por conta disso
#fiz um menu com a escolha do arquivo, criando uma condição para cada escolha e assim abrindo o arquivo desejado da pasta em questão
#ele copia e renomeia o arquivo(os.rename)
# caso exista o arquivo ele diz que ja existe(condição para isso também)
#algumas bibllitecas também não foram instaladas por sucessivos erros durante a instalação
