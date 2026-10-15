import time
import sys
import random


class DrinkPreset:

    def __init__ (self, name: str, work_minutes: float, break_minutes: float, description: str):
        self.name = name
        self.work_minutes = work_minutes
        self.break_minutes = break_minutes
        self.description = description


    def get_summary(self) -> str:
        return f"{self.name} ({self.work_minutes} minutes focus / {self.break_minutes} minutes break) - {self.description}"

    #^ returns a description of the preset e.g 25 minutes focus / 5 minutes break - classic study

class PomodoroTimer:

    def __init__(self, duration_seconds: int, session_description: str):
        self.duration_seconds = duration_seconds
        self.session_description = session_description

    def format_time(self, seconds_left: int) -> str:
        minutes = seconds_left // 60
        seconds = seconds_left % 60
        return f"{minutes:02d}:{seconds:02d}"

    def run(self):
        print(f"\n ✨ Starting: {self.session_description} ✨\n")

        for remaining in range(self.duration_seconds, -1, -1):

            time_display = self.format_time(remaining)
            sys.stdout.write(f"\r⏳️ [{self.session_description} ] Time Remaining: {time_display}")

            sys.stdout.flush()
            if remaining > 0:
                time.sleep(1)

        print("\n\n⌛️✨ *Ding!* Time is up! Take a gentle breath. \n")

#test for timer v

#test_clock = PomodoroTimer(duration_seconds=3, session_label="Quick Sip")
#test_clock.run()

class CozyTheme:

    #ANSI COLOR
    #\033 (escape key), [ (start formatting), 38;5; (picking color from 256 color palette), m (end of the code)
    #\033[0m (reset)

    RESET = "\033[0m"
    WARM_BROWN = "\033[38;5;137m"
    AMBER = "\033[38;5;215m"
    SOFT_GREEN = "\033[38;5;151m"
    CREAM = "\033[38;5;223m"
    BOLD = "\033[1m"

    CAFE_BANNER = r"""
       (   (
        )   )                       
      _________   
      |       |         ☕️ COZY CAFE POMODORO 
      |       |    Warm Study sessions & tea breaks
      \_______/

    """

    STEAMING_MUG = r"""

            )  
           (    (      )
            )    )    (
        ._________________.
        |_________________| ____
        |                 |/  _  \
        |    DEEP FOCUS   |  / \  |
        |     BREWING     |  \_/  |
        |                 |\_____/
         \_______________/

    """

    COZY_QUOTES = [

        "Small steps every day add up to big peaceful accomplishments.",
        "Take a slow breath. Your mind is clear and ready.",
        "You are making progress, even when it feels quiet.",
        "Work gently, rest deeply.",
        "Enjoy the warm steam and the quiet focus."
    
    ]

class CozyCafe:

    def __init__(self):
        self.cups_brewed = 0
        self.preset = [
            DrinkPreset("Twenty-Five Mocha Brew", 25, 5, "Classic pomodoro study session"),
            DrinkPreset("Espresso Sprint", 15, 3, "Calm burst of focus"),
            DrinkPreset("Leave the Chai brewing Study", 45, 10, "Cozy long-study with a hint of cardamom"),
            DrinkPreset("Quick Sip(DEMO)", 0.5, 0.5, "Quick 30-Second Test")
        ]

    def print_welcome(self):
        print(f"{CozyTheme.AMBER} {CozyTheme.CAFE_BANNER}{CozyTheme.RESET}")

        print(f"{CozyTheme.CREAM}Settle in, get comfortable, and brew your focus.✨ {CozyTheme.RESET}\n")


    def show_menu(self):
        print(f"{CozyTheme.BOLD}---- Cafe Menu ----{CozyTheme.RESET}")
        for item_num, preset in enumerate(self.preset, start= 1):
            print(f"{item_num}. {preset.get_summary()}")
        print(f"5. Check Study Stats ({self.cups_brewed} cups brewed today)")
        print("6. Leave the cafe (Exit)")
        print()
        print("____________________________________")

    def run_session(self, preset: DrinkPreset):
        print(f"{CozyTheme.WARM_BROWN}{CozyTheme.STEAMING_MUG}{CozyTheme.RESET}")
        print(f"{CozyTheme.CREAM}Order Up: {preset.name}!{CozyTheme.RESET}")
        print(f"☁️ {random.choice(CozyTheme.COZY_QUOTES)}\n")

        input("Please press [Enter] to start your focus session...☕️⏳️")
        



        work_timer = PomodoroTimer(int(preset.work_minutes * 60), f"Focus: {preset.name}")
        work_timer.run()

        self.cups_brewed += 1
        print(f"Woahh! You just finished brewing your {preset.name}")

        input("\nPress [Enter] to start your break...🧁")
        break_timer = PomodoroTimer(int(preset.break_minutes * 60), f"Break: Rest & Sip")
        break_timer.run()

        print(f"{CozyTheme.SOFT_GREEN}🍀Break complete!{CozyTheme.RESET}\n")
        print("____________________________________")

    def run(self):
        self.print_welcome()

        while True:
            self.show_menu()
            choice = input("What can we get you today? (1-6): ").strip()

            if choice in ("1", "2", "3", "4"):
                selected_preset = self.preset[int(choice) - 1]
                self.run_session(selected_preset)

            elif choice == "5":
                print(f"\n You have brewed {CozyTheme.BOLD}{self.cups_brewed}{CozyTheme.RESET} cups of focus today!")

                if self.cups_brewed == 0:
                    print("Pick a drink from the menu whenever you're ready to start!\n")

                else:
                    print("Keep up the momentum!\n")

            elif choice == "6":
                print(f"\n{CozyTheme.AMBER}Thank you for visiting the Cozy Cafe. Have a wonderful day we always a seat open for you! {CozyTheme.RESET}\n")
                break

            else:
                print("\n Please choice a valid option!! (1 to 6)\n")


if __name__ == "__main__":
    app = CozyCafe()
    app.run()