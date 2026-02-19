import json


def main():
    read_json("pkm_info.json")



def read_json(path):
    with open(path, "r") as file:
        pkm_info = json.load(file)
        create_pkm(pkm_info, path)

def create_pkm(pkm_info, path):
    pkm = {}
    types = []
    print(
"""
---------------
POKEMON CENTER
---------------
Enter pokemon´s info:

""")
    while True:
        try:
            pkm["name"] = {"english":input("Name: ")}
            pkm["level"] = int(input("Level: "))
            print("If the pokemon does not have a second type click Enter")
            for index in range(0,2):
                pkm_type = input("Type: ")
                types.append(pkm_type)
            pkm["type"] = types
            pkm["base"] = {
                "HP":int(input("Enter base hp: ")),
                "Attack":int(input("Enter base attack: ")),
                "Defense":int(input("Enter base defense: ")),
                "Sp. Attack":int(input("Enter base Sp.Attack: ")),
                "Sp. Defense":int(input("Enter base Sp.Defense: ")),
                "Speed":int(input("Enter base Speed: "))
                }
            break
        except ValueError as error:
            print(f"An Exception has occurred: {error}")
    pkm_info.append(pkm)
    write_json(pkm_info,path)


def write_json(data, path):
    with open(path,"w") as file:
        json.dump(data, file, indent=4)
    exit()

main()