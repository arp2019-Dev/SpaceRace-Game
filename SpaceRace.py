from tkinter import messagebox
import random


class RuleMessage:
    def __init__(self, parent):
        self.parent = parent
        self.rule_message()

    def rule_message(self):
        rules = (
            "Welcome to the space race game thingy!\n\nRules:\n"
            "1. To successfully launch a mission, ensure the Government Anger Level is below 10 and Tech Level is at least 3.\n"
            "2. To upgrade technology, you need at least 300 funds for each upgrade.\n"
            "3. Make good decisions to manage the Government Anger Level.\n\n"
            "Click OK to start the game."
        )
        messagebox.showinfo("Rules", rules)


class DecisionDialog(tk.Toplevel):
    def __init__(self, parent, options, callback):
        super().__init__(parent)
        self.title("Make Decision")
        self.geometry("600x300")
        self.resizable(False, False)

        self.selected_option = tk.IntVar(self)

        label = tk.Label(self, text="Choose the best course of action:")
        label.pack(pady=10)

        self.random_options = random.sample(options, min(len(options), 4))

        for i, option in enumerate(self.random_options):
            radio_button = tk.Radiobutton(self, text=option["text"], variable=self.selected_option, value=i)
            radio_button.pack(anchor="w", padx=20)

        self.callback = callback

        ok_button = ttk.Button(self, text="OK", command=self.ok)
        ok_button.pack(pady=10)

    def ok(self):
        selected_option_index = self.selected_option.get()
        print("Selected Option Index:", selected_option_index)
        if selected_option_index is not None:
            selected_option_text = self.random_options[selected_option_index]["text"]
            print("Selected Option Text:", selected_option_text)
            selected_option = next((option for option in DECISIONS if option["text"] == selected_option_text), None)
            if selected_option:
                print("Selected Option:", selected_option)
                self.callback(selected_option)
                self.destroy()
            else:
                messagebox.showerror("Invalid Option", "Please select a valid option.")
        else:
            messagebox.showerror("No Option Selected", "Please select an option.")


DECISIONS = [
    {"text": "Increase funding for research", "success_chance": 90},
    {"text": "Send additional cosmonauts for training", "success_chance": 70},
    {"text": "Delay mission to perform additional tests", "success_chance": 55},
    {"text": "Recruit renowned scientist to advise on mission", "success_chance": 70},
    {"text": "Conduct secret test flights to gain advantage", "success_chance": 70},
    {"text": "Increase propaganda efforts to boost morale", "success_chance": 40},
    {"text": "Seek assistance from international partners", "success_chance": 50},
    {"text": "Seek advice from the Politburo", "success_chance": 55},
    {"text": "Conduct rigorous training simulations", "success_chance": 55},
    {"text": "Recruit more engineers and technicians", "success_chance": 80},
    {"text": "Invest in advanced propulsion research", "success_chance": 60},
    {"text": "Launch a propaganda campaign to inspire the nation", "success_chance": 50},
    {"text": "Conduct live-fire tests of spacecraft components", "success_chance": 70},
    {"text": "Delay mission to address unforeseen technical issues", "success_chance": 10},
    {"text": "Request additional resources from the government", "success_chance": 55},
    {"text": "Recruit experienced engineers from other sectors", "success_chance": 60},
    {"text": "Sacrifice quality control to meet tight deadlines", "success_chance": 15},
    {"text": "Conduct additional stress tests on critical components", "success_chance": 65},
    {"text": "Implement strict measures to prevent leaks of classified information", "success_chance": 70},
    {"text": "Allocate resources to improve living conditions for cosmonauts", "success_chance": 60},
    {"text": "Ignore safety protocols to rush mission", "success_chance": 10},
    {"text": "Cut corners in spacecraft construction", "success_chance": 0},
    {"text": "Use untested technology in mission", "success_chance": 5},
    {"text": "Sabotage rival's space program", "success_chance": 0},
    {"text": "Send untrained personnel on mission", "success_chance": 0},
    {"text": "Conduct mission without proper planning", "success_chance": 0},
    {"text": "Decrease funding for critical components", "success_chance": 20},
    {"text": "Neglect safety regulations to save costs", "success_chance": 10},
    {"text": "Seek advice from astrologers", "success_chance": 5},
    {"text": "Disband the space program", "success_chance": 0},
    {"text": "Blame failures on rival nations", "success_chance": 40},
]


class WH_USSR_Game:

    def reset_game(self):
        self.progress = 0
        self.funds = 200
        self.tech_level = 1
        self.gov_angry_level = 20
        self.update_status()
        RuleMessage(self.root)  

    def __init__(self, root):
        self.root = root
        RuleMessage(self.root)  
        self.progress = 0
        self.funds = 200
        self.tech_level = 1
        self.gov_angry_level = 20
        print(self.funds)

    def launch_mission(self):
        if self.gov_angry_level < 10 and self.tech_level >= 3:
            messagebox.showinfo("you have made it", "you have made it. You are going to the moon on the Soviets brand new Luna 2 space craft")
            messagebox.showinfo("Finished", "you have finished the game succesfully, Great job")
            messagebox.showinfo("Give grade", "Please give me an A")
            self.progress = 0
            self.funds = 200
            self.tech_level = 1
            self.gov_angry_level = 20
            self.reset_game()

        elif self.gov_angry_level > 10:
            messagebox.showwarning("Government Unhappy", "Make better decisions to ease your fellow government comrades.")
        elif self.tech_level < 3:
            messagebox.showwarning("Tech Level too low", "upgrade your tech to be able to invent spacecraft.")
        self.update_status()

    def upgrade_technology(self):
        upgrade_cost = 300
        if self.funds >= upgrade_cost:
            self.funds -= upgrade_cost
            self.tech_level += 1
            messagebox.showinfo("Technology Upgraded", "Technology upgraded! The Soviet Union advances its capabilities.")
        else:
            messagebox.showerror("Insufficient Funds", "Insufficient funds (you need 300). The progress of the Soviet space program is hindered.")
        self.update_status()

    def make_decision(self):
        dialog = DecisionDialog(self.root, DECISIONS, self.process_decision)

    def process_decision(self, selected_option):
        success_chance1 = selected_option["success_chance"] + random.randint(-5, 5)
        print(success_chance1)
        print(selected_option)
        if success_chance1 >70:
            self.progress += 1
            self.gov_angry_level -= 10
            self.funds += 300
            messagebox.showinfo("Decision Made", "You have made a positive decision. The Soviet Union forges ahead.")
        elif 30 < success_chance1 < 70:
            self.funds +=150
            self.progress +=0.5
            self.gov_angry_level -= 2
            messagebox.showinfo("Decision Made", "You have made an okay decision the soviet union will spare you.")
        elif success_chance1 <30:
            self.funds -= 100
            self.gov_angry_level += 15
            messagebox.showinfo("Decision Made", "You have made a negative decision. The Soviet Union faces setbacks.")
        self.update_status()

	@@ -115,38 +170,37 @@ def update_status(self):

    def play(self):
        self.progress = 0
        self.funds = 200
        self.tech_level = 1
        self.gov_angry_level = 20

        self.root.title("WH_USSR_GAME")

        self.root.geometry("1450x1100")

        status_frame = tk.Frame(self.root, bg="#330000", bd=2)
        status_frame.place(relx=0.8, rely=0.1, relwidth=0.2, relheight=0.8)
        self.status_var = tk.StringVar()
        status_label = tk.Label(status_frame, textvariable=self.status_var, fg="white", bg="#330000", justify="left", font=("Courier", 12))
        status_label.pack(fill="both", expand=True)
        self.update_status()

        button_frame = tk.Frame(self.root)
        button_frame.place(relx=0.1, rely=0.1, relwidth=0.6, relheight=0.8)

        style = ttk.Style()
        style.configure("Custom.TButton", foreground="white", background="#660000", font=("Arial", 12))
        launch_button = ttk.Button(button_frame, text="Launch Mission", command=self.launch_mission, style="Custom.TButton")
        launch_button.pack(side="top", pady=3, fill="both", expand=True)

        upgrade_button = ttk.Button(button_frame, text="Upgrade Technology", command=self.upgrade_technology, style="Custom.TButton")
        upgrade_button.pack(side="top", pady=3, fill="both", expand=True)

        decision_button = ttk.Button(button_frame, text="Make Decision", command=self.make_decision, style="Custom.TButton")
        decision_button.pack(side="top", pady=3, fill="both", expand=True)


root = tk.Tk()
simulator = WH_USSR_Game(root)
simulator.play()
root.mainloop()
