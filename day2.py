import requests
while True:
    pokemon_name = input("Enter a Pokémon name or type quit: ").lower()
    if pokemon_name == "quit":
        print("Goodbye!")
        break

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)

    def display_pokemon(data):
        print("==============")
        print(" Pokemon Info")
        print("==============")
        print("Name:", data["name"].title())
        print("ID:", data["id"])
        print("Height:", data["height"])
        print("Weight:", data["weight"])

    if response.status_code == 200:
        data = response.json()
        display_pokemon(data)

    else:
        print("Pokémon not found.")