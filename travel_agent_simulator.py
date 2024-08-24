import random
from rich.console import Console
from rich.text import Text
import pyfiglet

console = Console()


class TravelAgentGame:
    def __init__(self):
        self.money = 1000
        self.leads = 0
        self.clients = 0
        self.office_level = 1
        self.salespeople = 0
        self.social_media_people = 0
        self.experience = 0
        self.meetings = 0

    def run_campaign(self):
        cost = 50
        if self.money >= cost:
            self.money -= cost
            if self.social_media_people == 0:
                leads = random.randint(1, 10)
            else:
                leads = random.randint(1, 10) * self.social_media_people
            console.print(f"Campaign generated {leads} leads.", style="bold green")
            self.leads += leads
        else:
            console.print("Not enough money to run a campaign.", style="bold red")

    def pitch_client(self):
        if self.clients > 0:
            result = random.choice(["good", "bad", "big"])
            if result == "good":
                earnings = random.randint(100, 500)
                console.print(f"Good pitch! Earned ${earnings}.", style="bold green")
            elif result == "bad":
                earnings = random.randint(0, 100)
                console.print(
                    f"Bad pitch. Earned only ${earnings}.", style="bold yellow"
                )
            else:
                earnings = random.randint(500, 2000)
                console.print(f"Big client! Earned ${earnings}.", style="bold green")
            self.money += earnings
            self.clients -= 1
            self.meetings -= 1
        else:
            console.print("No clients to pitch to.", style="bold red")


    def message_client(self):
        if self.clients > 0:
            result = random.choice(["good", "bad", "big"])
            if result == "good":
                earnings = random.randint(100, 500)
                console.print(f"Good pitch! Earned ${earnings}.", style="bold green")
            elif result == "bad":
                earnings = random.randint(0, 100)
                console.print(
                    f"Bad pitch. Earned only ${earnings}.", style="bold yellow"
                )
            else:
                earnings = random.randint(500, 2000)
                console.print(f"Big client! Earned ${earnings}.", style="bold green")
            self.money += earnings
            self.clients -= 1
        else:
            console.print("No clients to pitch to.", style="bold red")


    def upgrade_office(self):
        cost = 1000 * self.office_level
        if self.money >= cost:
            self.money -= cost
            self.office_level += 1
            console.print(
                f"Upgraded office to level {self.office_level}.", style="bold green"
            )
        else:
            console.print("Not enough money to upgrade office.", style="bold red")

    def hire_salesperson(self):
        cost = 500
        if self.money >= cost:
            self.money -= cost
            self.salespeople += 1
            console.print(
                f"Hired a new salesperson. Total salespeople: {self.salespeople}.",
                style="bold green",
            )
        else:
            console.print("Not enough money to hire a salesperson.", style="bold red")

    def hire_social_media_person(self):
        cost = 500
        if self.money >= cost:
            self.money -= cost
            self.social_media_people += 1
            console.print(
                f"Hired a new social media intern. Total social media interns: {self.social_media_people}.",
                style="bold green",
            )
        else:
            console.print(
                "Not enough money to hire a social media intern.", style="bold red"
            )

    def attend_training(self):
        if self.money >= cost:
            console.print("Made some connections,", style="bold green")
            leads = random.randint(1, 10) * self.social_media_people
            console.print(f"Campaign generated {leads} leads.", style="bold green")
            self.clients += leads
            self.experience += 1
        else:
            console.print(
                "Not enough money to invest in the business.", style="bold red"
            )

    def show_status(self):
        status = (
            f"Money: ${self.money}\n"
            f"XP: {self.experience}\n"
            f"Clients: {self.clients}\n"
            f"Leads: {self.leads}\n"
            f"Office Level: {self.office_level}\n"
            f"Salespeople: {self.salespeople}\n"
            f"Social Media People: {self.social_media_people}"
        )
        console.print(status, style="bold green")


def main():
    game = TravelAgentGame()
    # title = text2art("Travel Agent Simulator", font='block')
    # console.print(title, style="bold green")
    text = "Travel Agent Simulator"
    ascii_art = pyfiglet.figlet_format(text, font="small")
    print(ascii_art)
    while True:
        game.show_status()
        console.print("\n1. Run Campaign", style="bold green")
        console.print("2. Pitch Client", style="bold green")
        console.print("3. Message Client", style="bold green")
        console.print("4. Upgrade Office", style="bold green")
        console.print("5. Hire Salesperson", style="bold green")
        console.print("6. Hire Social Media Intern", style="bold green")
        console.print("7. Attend Training", style="bold green")
        console.print("8. Exit", style="bold green")
        choice = input("\nChoose an action:\n\n")
        if choice == "1":
            game.run_campaign()
        elif choice == "2":
            game.pitch_client()
        elif choice == "3":
            game.upgrade_office()
        elif choice == "4":
            game.upgrade_office()
        elif choice == "5":
            game.hire_salesperson()
        elif choice == "6":
            game.hire_social_media_person()
        elif choice == "7":
            game.attend_training()
        elif choice == "8":
            break
        else:
            console.print("Invalid choice. Please try again.", style="bold red")


if __name__ == "__main__":
    main()
