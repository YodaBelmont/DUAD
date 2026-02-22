
import csv

csv.excel_tab()

def get_games_info_menu(list1, headers):
    while True:
        games_info = {}
        print("""
----------------------------
Enter videoGame info
VideoGame info must contain:
---------------------------- 
Name
Genre
Developer
ESRB Rating
----------------------------""")
        games_info ["Name"] = input("Name: ")
        games_info ["Genre"] = input("Genre: ")
        games_info ["Developer"] = input("Developer: ")
        games_info ["ESRB Rating"] = input("ESRB Rating: ")
        list1.append(games_info)
        option = 0
        option = int(input(
"""
----------------------------
Do you wish to enter more info?
----------------------------
1- Yes
2- No
-> """))
        while True:
            try:
                if option == 2:
                    write_csv("games.csv",list1,headers)
                    break
            except Exception as err:
                print(f"An exception has occurred: {err}")


def write_csv(path,list1,headers):
    with open(path, "w", newline= "",encoding= "utf-8") as f:
        writer = csv.DictWriter(f,headers)
        writer.writeheader()
        writer.writerows(list1)
    read_csv(path)


def read_csv(path):
    with open(path,"r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
    exit()


def main():
    list1 = []
    games_headers = ("Name", "Genre", "Developer", "ESRB Rating",)
    list1 = get_games_info_menu(list1, games_headers)

main()
