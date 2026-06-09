from cryptography.fernet import InvalidToken
from rich.console import Console
from rich.panel import Panel
from getpass import getpass
from password_generator import generate_password
from vault import add_entry, get_entries, search_entries, delete_entry



console = Console()


def show_menu():
    console.print(Panel.fit("Python Password Manager", title="PyVault"))

    console.print("[1] Add password")
    console.print("[2] View saved passwords")
    console.print("[3] Search password")
    console.print("[4] Generate password")
    console.print("[5] Delete password")
    console.print("[6] Exit")


def main():
    master_password = getpass("Enter master password: ")

    while True:
        show_menu()
        choice = input("\nChoose an option: ")

        try:
            if choice == "1":
                site = input("Enter site/app name: ")
                username = input("Enter username/email: ")
                password = getpass("Enter password: ")

                add_entry(site, username, password, master_password)
                console.print("[green]Password saved successfully.[/green]")

            elif choice == "2":
                entries = get_entries(master_password)

                if not entries:
                    console.print("[yellow]No passwords saved yet.[/yellow]")
                else:
                    for index, entry in enumerate(entries, start=1):
                        console.print(f"\n[bold]{index}. {entry['site']}[/bold]")
                        console.print(f"Username: {entry['username']}")
                        console.print("Password: ********")

            elif choice == "3":
                search_term = input("Enter site/app name to search: ")
                results = search_entries(search_term, master_password)

                if not results:
                    console.print("[yellow]No matching passwords found.[/yellow]")
                else:
                    for index, entry in enumerate(results, start=1):
                        console.print(f"\n[bold]{index}. {entry['site']}[/bold]")
                        console.print(f"Username: {entry['username']}")
                        console.print("Password: ********")

            elif choice == "4":
                length = input("Enter password length or press Enter for 16: ")

                if length == "":
                    length = 16
                elif length.isdigit():
                    length = int(length)
                else:
                    console.print("[red]Please enter a valid number.[/red]")
                    continue

                password = generate_password(length)
                console.print(f"\nGenerated password: [green]{password}[/green]")

            elif choice == "5":
                entries = get_entries(master_password)

                if not entries:
                    console.print("[yellow]No passwords saved yet.[/yellow]")
                else:
                    for index, entry in enumerate(entries, start=1):
                        console.print(f"{index}. {entry['site']} - {entry['username']}")

                    delete_choice = input("\nEnter the number to delete: ")

                    if delete_choice.isdigit():
                        delete_index = int(delete_choice) - 1

                        if delete_entry(delete_index, master_password):
                            console.print("[green]Password deleted successfully.[/green]")
                        else:
                            console.print("[red]Invalid entry number.[/red]")
                    else:
                        console.print("[red]Please enter a valid number.[/red]")

            elif choice == "6":
                console.print("Goodbye!")
                break

            else:
                console.print("[red]Invalid option. Please try again.[/red]")

        except InvalidToken:
            console.print("[red]Wrong master password. Cannot unlock vault.[/red]")


if __name__ == "__main__":
    main()