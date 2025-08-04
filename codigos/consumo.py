import requests

URL = "http://127.0.0.1:8000"

def cadastrar_usuario():
    usuario = {
        "username": input("Username: "),
        "email": input("Email: "),
        "senha": input("Senha: ")
    }
    resp = requests.post(f"{URL}/cadastro", json=usuario)
    print("Resposta:", resp.json())

def login_usuario():
    login = {
        "email": input("Email: "),
        "senha": input("Senha: ")
    }
    resp = requests.post(f"{URL}/login", json=login)
    print("Resposta:", resp.json())

def criar_questao():
    questao = {
        "disciplina": input("Disciplina: "),
        "assunto": input("Assunto: "),
        "dificuldade": input("Dificuldade (Fácil, Médio, Difícil): "),
        "enunciado": input("Enunciado da questão: "),
        "alternativas": input("Alternativas (separadas por vírgula): ").split(","),
        "correta": input("Alternativa correta: "),
        "ja_respondida": False
    }
    resp = requests.post(f"{URL}/criar_questoes", json=questao)
    print("Resposta:", resp.json())


def listar_questoes():
    resp = requests.get(f"{URL}/listar_questoes")
    print("Questões disponíveis:")
    for q in resp.json():
        print(f"- ID {q['id']}: {q['enunciado']}")

def simular():
    dados = {
        "curso": input("Curso: "),
        "campus": input("Campus: "),
        "nota_usuario": float(input("Sua nota: "))
    }
    resp = requests.post(f"{URL}/simular", json=dados)
    print("Resultado:", resp.json())

def menu():
    while True:
        print("\n=== MENU API ===")
        print("1 - Cadastrar usuário")
        print("2 - Login de usuário")
        print("3 - Criar questão")
        print("4 - Listar questões")
        print("5 - Simular nota")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            login_usuario()
        elif opcao == "3":
            criar_questao()
        elif opcao == "4":
            listar_questoes()
        elif opcao == "5":
            simular()
        elif opcao == "0":
            print("Encerrando.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
