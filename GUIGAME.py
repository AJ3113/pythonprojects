import tkinter as tk
import random
import winsound  # For simple sound effects (Windows only)

# Mapping
choices = {"s": 1, "w": -1, "g": 0}
reverse_dict = {-1: "🧃 Water", 0: "🔫 PewPew", 1: "🐍 Snek"}

# Score Variables
user_score = 0
comp_score = 0
draw_score = 0

# Sound effect function
def play_sound(choice):
    if choice == "s":   # Snake
        winsound.MessageBeep(400)  # Snake sound (basic beep)
    elif choice == "w":  # Water
        winsound.MessageBeep(600)  # Different pitch
    elif choice == "g":  # Gun
        winsound.MessageBeep(800)  # Higher pitch

# Button animation (flash pastel highlight)
def animate_button(btn, base_color, highlight):
    def flash(count=0):
        if count < 4:
            btn.config(bg=highlight if count % 2 == 0 else base_color)
            root.after(200, flash, count+1)
        else:
            btn.config(bg=base_color)
    flash()

# Game Logic
def play(user_choice, btn, base_color, highlight):
    global user_score, comp_score, draw_score

    play_sound(user_choice)
    animate_button(btn, base_color, highlight)

    computer = random.choice([-1, 0, 1])
    you = choices[user_choice]

    # Update selections
    user_label.config(text=f"You chose: {reverse_dict[you]}", fg="#6B5B95")
    comp_label.config(text=f"Computer chose: {reverse_dict[computer]}", fg="#FF6F61")

    # Result
    if computer == you:
        result = "It's a Draw 😐"
        color = "#FFD1DC"  # pastel pink
        draw_score += 1
    elif (computer == -1 and you == 0) or (computer == 0 and you == 1) or (computer == 1 and you == -1):
        result = "You Lose! 😞"
        color = "#FFB347"  # pastel orange
        comp_score += 1
    else:
        result = "You Win! 🎉"
        color = "#77DD77"  # pastel green
        user_score += 1

    # Flash animation for result
    def flash(count=0):
        if count < 6:
            result_label.config(fg=color if count % 2 == 0 else "#222")
            root.after(250, flash, count+1)
        else:
            result_label.config(fg=color)

    result_label.config(text=result, font=("Arial", 20, "bold"))
    flash()

    update_scoreboard()

# Update Scoreboard
def update_scoreboard():
    score_label.config(
        text=f"👤 You: {user_score}   🤖 Computer: {comp_score}   ⚖️ Draws: {draw_score}",
        fg="#444"
    )

# Reset Game
def reset_game():
    global user_score, comp_score, draw_score
    user_score = comp_score = draw_score = 0
    user_label.config(text="")
    comp_label.config(text="")
    result_label.config(text="")
    update_scoreboard()

# GUI Setup
root = tk.Tk()
root.title("Snake Water Gun Gen-Z Edition ✨")
root.geometry("650x550")
root.config(bg="#F8F8FF")  # pastel lavender background

# Title
title = tk.Label(root, text="🐍🧃🔫 Snake Water Gun ✨", 
                 font=("Comic Sans MS", 24, "bold"), fg="#FF6F61", bg="#F8F8FF")
title.pack(pady=20)

# Buttons Frame
frame = tk.Frame(root, bg="#F8F8FF")
frame.pack(pady=20)

snake_btn = tk.Button(frame, text="🐍 Snek", font=("Comic Sans MS", 16, "bold"), 
                      bg="#AEC6CF", fg="black", width=10, 
                      command=lambda: play("s", snake_btn, "#AEC6CF", "#77DD77"))
snake_btn.grid(row=0, column=0, padx=15)

water_btn = tk.Button(frame, text="🧃 Water", font=("Comic Sans MS", 16, "bold"), 
                      bg="#FFD1DC", fg="black", width=10, 
                      command=lambda: play("w", water_btn, "#FFD1DC", "#FFB347"))
water_btn.grid(row=0, column=1, padx=15)

gun_btn = tk.Button(frame, text="🔫 PewPew", font=("Comic Sans MS", 16, "bold"), 
                    bg="#B39EB5", fg="black", width=10, 
                    command=lambda: play("g", gun_btn, "#B39EB5", "#FF6961"))
gun_btn.grid(row=0, column=2, padx=15)

# Reset Button
reset_btn = tk.Button(root, text="🔄 Reset Game", font=("Arial", 14, "bold"), 
                      bg="#FFB347", fg="black", width=15, command=reset_game)
reset_btn.pack(pady=15)

# Labels for choices
user_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#F8F8FF")
user_label.pack(pady=5)

comp_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#F8F8FF")
comp_label.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="#F8F8FF")
result_label.pack(pady=20)

# Scoreboard
score_label = tk.Label(root, text="👤 You: 0   🤖 Computer: 0   ⚖️ Draws: 0",
                       font=("Arial", 16, "bold"), fg="#444", bg="#E6E6FA", pady=10, padx=10)
score_label.pack(side="bottom", fill="x")

# Run App
root.mainloop()