import Interfaces
import LogicManagement


manager = LogicManagement.Finance_Manager()


def main():
    Interfaces.show_main_menu(manager)

if __name__ == "__main__":
    main()