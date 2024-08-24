import random
from rich.console import Console
from rich.text import Text

console = Console()

class TravelAgentGame:
    def __init__(self):
        self.money = 1000
        self.clients = 0
        self.office_level = 1
        self.salespeople = 1
        self.social_media_people = 1

    def run_campaign(self):
        cost = 200 * self.social_media_people
        if self.money >= cost:
            self.money -= cost
            leads = random.randint(1, 10) * self.social_media_people
            console.print(f"Campaign generated {leads} leads.", style="bold green")
            self.clients += leads
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
                console.print(f"Bad pitch. Earned only ${earnings}.", style="bold yellow")
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
            console.print(f"Upgraded office to level {self.office_level}.", style="bold green")
        else:
            console.print("Not enough money to upgrade office.", style="bold red")

    def hire_salesperson(self):
        cost = 500
        if self.money >= cost:
            self.money -= cost
            self.salespeople += 1
            console.print(f"Hired a new salesperson. Total salespeople: {self.salespeople}.", style="bold green")
        else:
            console.print("Not enough money to hire a salesperson.", style="bold red")

    def hire_social_media_person(self):
        cost = 500
        if self.money >= cost:
            self.money -= cost
            self.social_media_people += 1
            console.print(f"Hired a new social media person. Total social media people: {self.social_media_people}.", style="bold green")
        else:
            console.print("Not enough money to hire a social media person.", style="bold red")

    def invest_in_business(self):
        cost = 1000
        if self.money >= cost:
            self.money -= cost
            self.money += random.randint(1000, 5000)
            console.print("Investment paid off!", style="bold green")
        else:
            console.print("Not enough money to invest in the business.", style="bold red")

    def show_status(self):
        status = (f"Money: ${self.money}\n"
                  f"Clients: {self.clients}\n"
                  f"Office Level: {self.office_level}\n"
                  f"Salespeople: {self.salespeople}\n"
                  f"Social Media People: {self.social_media_people}")
        console.print(status, style="bold green")

def main():
    game = TravelAgentGame()
    while True:
        game.show_status()
        console.print("\n1. Run Campaign", style="bold green")
        console.print("2. Pitch Client", style="bold green")
        console.print("3. Upgrade Office", style="bold green")
        console.print("4. Hire Salesperson", style="bold green")
        console.print("5. Hire Social Media Person", style="bold green")
        console.print("6. Invest in Business", style="bold green")
        console.print("7. Show Status", style="bold green")
        console.print("8. Exit", style="bold green")
        choice = input("Choose an action: ")
        if choice == '1':
            game.run_campaign()
        elif choice == '2':
            game.pitch_client()
        elif choice == '3':
            game.upgrade_office()
        elif choice == '4':
            game.hire_salesperson()
        elif choice == '5':
            game.hire_social_media_person()
        elif choice == '6':
            game.invest_in_business()
        elif choice == '7':
            game.show_status()
        elif choice == '8':
            break
        else:
            console.print("Invalid choice. Please try again.", style="bold red")

if __name__ == "__main__":
    main()
