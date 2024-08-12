import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox
import random

class DecisionDialog(tk.Toplevel):
    def __init__(self, parent, options):
        super().__init__(parent)
        self.title("Make Decision")
        self.geometry("300x200")
        self.resizable(False, False)

        self.selected_option = tk.StringVar()

        label = tk.Label(self, text="Choose the best course of action:")
        label.pack(pady=10)

        for option in options:
            radio_button = tk.Radiobutton(self, text=option["text"], variable=self.selected_option, value=option["text"])
            radio_button.pack(anchor="w", padx=20)

        ok_button = ttk.Button(self, text="OK", command=self.ok)
        ok_button.pack(pady=10)

    def ok(self):
        self.destroy()

class SpaceRaceSimulator:
    def __init__(self):
        self.progress = 0
        self.funds = 1000
        self.tech_level = 1
        self.difficulty = "Normal"  

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def launch_mission(self):
  
        success_chance = self.tech_level * 10
        if self.difficulty == "Hard":
            success_chance -= 20
        elif self.difficulty == "Easy":
            success_chance += 20
        success_chance += random.randint(-10, 10)
        if success_chance > 0:
 
            self.progress += 1
            self.funds -= 200
            self.tech_level += 1
            messagebox.showinfo("Mission Successful", "Mission successful! The glory of the Soviet Union shines brightly in space!")
        else:
       
            self.funds -= 100
            messagebox.showerror("Mission Failed", "Mission failed. The failure brings disgrace upon the Soviet Union.")
        self.update_status()

    def upgrade_technology(self):

        upgrade_cost = 500
        if self.funds >= upgrade_cost:
            self.funds -= upgrade_cost
            self.tech_level += 1
            messagebox.showinfo("Technology Upgraded", "Technology upgraded! The Soviet Union advances its capabilities.")
        else:
            messagebox.showerror("Insufficient Funds", "Insufficient funds. The progress of the Soviet space program is hindered.")
        self.update_status()

    def make_decision(self):
       
        decision = random.choice(DECISIONS)
        dialog = DecisionDialog(self.root, [decision])
        dialog.grab_set()
        self.root.wait_window(dialog)
        selected_option_text = dialog.selected_option.get()
        selected_option = next(option for option in DECISIONS if option["text"] == selected_option_text)
        success_chance = selected_option["success_chance"] + random.randint(-10, 10)
        if success_chance > 0:
       
            self.tech_level += 1
            self.progress += 1
            messagebox.showinfo("Decision Made", "You have made a positive decision. The Soviet Union forges ahead.")
        else:
    
            self.funds -= 200
            messagebox.showinfo("Decision Made", "You have made a negative decision. The Soviet Union faces setbacks.")
        self.update_status()

    def update_status(self):
   
        status_text = f"Progress: {self.progress}\nFunds: {self.funds}\nTechnology level: {self.tech_level}\nDifficulty: {self.difficulty}"
        self.status_var.set(status_text)

    def play(self):
        self.root = tk.Tk()
        self.root.title("Space Race Simulator")

   
        def update_button_sizes(event):

            button_width = int(self.root.winfo_width() * 0.15)
            button_height = int(self.root.winfo_height() * 0.05)

            launch_button.config(width=button_width, height=button_height)
            upgrade_button.config(width=button_width, height=button_height)
            decision_button.config(width=button_width, height=button_height)
            quit_button.config(width=button_width, height=button_height)

        self.root.bind("<Configure>", update_button_sizes)

        self.root.geometry("600x400")  


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
        launch_button.pack(pady=10, fill="x")

        upgrade_button = ttk.Button(button_frame, text="Upgrade Technology", command=self.upgrade_technology, style="Custom.TButton")
        upgrade_button.pack(pady=10, fill="x")

        decision_button = ttk.Button(button_frame, text="Make Decision", command=self.make_decision, style="Custom.TButton")
        decision_button.pack(pady=10, fill="x")

        quit_button = ttk.Button(button_frame, text="Quit", command=self.root.destroy, style="Custom.TButton")
        quit_button.pack(pady=10, fill="x")

        self.root.mainloop()

if __name__ == "__main__":
    game = SpaceRaceSimulator()
    game.play()
