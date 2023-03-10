# informações dos usuários
# esta informações devem vim de banco de dados de login
users = {
    "user1": {
        "password": "password1",
        "name": "John Smith"
    },
    "user2": {
        "password": "password2",
        "name": "Jane Doe"
    }
}

# função de login
def login():
    # solicita nome de usuário e senha
    username = input("Username: ")
    password = input("Password: ")

    # verifica se o usuário existe e a senha está correta
    if username in users and users[username]['password'] == password:
        print("Welcome, " + users[username]['name'] + "!")
    else:
        print("Incorrect username or password. Please try again.")

# chamada da função de login
login()
