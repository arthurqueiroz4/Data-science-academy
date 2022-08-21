from time import sleep
class pessoa():
    
    def __init__(self, nome='Sem nome',cidade='Sem cidade', telefone='Sem telefone',email='Sem email'):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        print('Pessoa cadastrada!\n')
        
    def __str__(self):
        print('-'*20)
        return f'NOME: {self.nome}\nCIDADE: {self.cidade}\nTELEFONE: {self.telefone}\nEMAIL: {self.email}\n'+'-'*20
        
    def alterardados(self, novonome='', novacidade='', novotelefone='', novoemail=''):
        print('Alteração de dados:')
        if novonome!='':
            self.nome = novonome
            print('Nome alterado.')
        else:
            print('Nome não alterado.')
            
        if novacidade!='':
            self.cidade = novacidade
            print('Cidade alterada.')
        else:
            print('Cidade não alterado.')
            
        if novotelefone!='':
            self.telefone = novotelefone
            print('Telefone alterado.')
        else:
            print('Telefone não alterado.')
            
        if novoemail!='':
            self.email = novoemail
            print('Email alterado.')
        else:
            print('Email não alterado.')
        print('-'*20)
        print(self,'\n')
        
pessoa1 = pessoa("Arthur","Fotaleza","1234","artarroba")
sleep(2.5)
print(pessoa1)
sleep(2.5)

pessoa1.alterardados('Arthur Silva','Fortaleza - Ceará', '123456')
sleep(2.5)

nome = str(input('Digite seu nome: '))
cidade = str(input('Digite sua Cidade: '))
telefone = str(input('Digite seu telefone: '))
email = str(input('Digite seu email: '))
pessoa2 = pessoa(nome,cidade,telefone,email)
sleep(2.5)
decisao1 = input('Quer visualizar seu cadastro? [S/N]').upper()
if decisao1 == 'S':
    print(pessoa2)
