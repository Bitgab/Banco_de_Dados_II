from services.usuario_services import UsuariosService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session

def main():
    session = Session()
    repository = UsuarioRepository (session)
    service = UsuariosService (repository)

    service.criar_usuario("João", "joao@gmail.com", "1234")

    print("\n Listando todos os usuário.")
    usuarios = service.listar_todos_usuarios()

    for usuario in usuarios:
        print(f"{usuario.nome} - {usuario.email}")

if __name__ == "__main__":
    main()       