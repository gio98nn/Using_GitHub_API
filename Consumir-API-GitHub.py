import requests

def get_github_user_info(username):
    # URL da API do GitHub para obter informações do usuário
    url = f"https://api.github.com/users/{username}"

    # Fazendo a requisão para a API
    response = requests.get(url)

    # Verificando se a resposta foi bem-sucedida
    if response.status_code == 200:
        user_data = response.json()

        # Estraindo informações desejadas
        full_name = user_data.get('name')
        followers = user_data.get('followers')
        following = user_data.get('following')
        location = user_data.get('location')

        # Retornando informações
        return {
            'full_name': full_name,
            'followers': followers,
            'following': following,
            'location': location
        }
    
    else:
        # Em caso de erro, retornar None
        print(f"Erro ao obter informações do usuário: {response.status_code}")
        return None
    
# Exemplo de uso
if __name__ == "__main__":
    username = "gio98nn"  # Substitua pelo nome de usuário desejado
    user_info = get_github_user_info(username)
    if user_info:
        print(f"Nome Completo: {user_info['full_name']}")
        print(f"Seguidores: {user_info['followers']}")
        print(f"Seguindo: {user_info['following']}")
        print(f"Localização: {user_info['location']}")