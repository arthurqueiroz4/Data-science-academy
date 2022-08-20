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
            print('Email não alterado.')
            
        if novacidade!='':
            self.cidade = novacidade
            print('Cidade alterada.')
        else:
            print('Email não alterado.')
            
        if novotelefone!='':
            self.telefone = novotelefone
            print('Telefone alterado.')
        else:
            print('Email não alterado.')
            
        if novoemail!='':
            self.email = novoemail
            print('Email alterado.')
        else:
            print('Email não alterado.')
        print('-'*20)
        print(self,'\n')
        
pessoa1 = pessoa("Arthur","Fotaleza","1234","artarroba")
print(pessoa1)
pessoa1.alterardados('Arthur Silva','Fortaleza - Ceará', '123456')

nome = input('Digite seu nome: ')
cidade = input('Digite sua Cidade: ')
telefone = input('Digite seu telefone: ')
email = input('Digite seu email: ')
pessoa2 = pessoa(nome,cidade,telefone,email)
decisao1 = input('Quer visualizar seu cadastro? [S/N]').upper()
if decisao1 == 'S':
    print(pessoa2)
