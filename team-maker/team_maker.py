import random
import tkinter as tk
from tkinter import simpledialog, messagebox

def make_teams():
    root = tk.Tk()
    root.withdraw()  

    names_input = simpledialog.askstring("팀 메이커", "이름들을 ,로 구분해서 입력하세요:")
    if not names_input:
        return
    names = [name.strip() for name in names_input.split(",") if name.strip()]

    team_count = simpledialog.askinteger("팀 메이커", "팀 개수를 입력하세요:")
    if not team_count or team_count <= 0:
        return

    random.shuffle(names)
    teams = [[] for _ in range(team_count)]
    for i, name in enumerate(names):
        teams[i % team_count].append(name)

    result = "\n".join([f"팀 {i+1}: {', '.join(team)}" for i, team in enumerate(teams)])
    messagebox.showinfo("결과", result)

if __name__ == "__main__":
    make_teams()
