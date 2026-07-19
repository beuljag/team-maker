import random

def make_teams():
    names = input("이름들을 ,로 구분해서 입력하세요: ").split(",")
    names = [name.strip() for name in names if name.strip()]
    
    team_count = int(input("팀 개수를 입력하세요: "))
    
    random.shuffle(names)
    
    teams = [[] for _ in range(team_count)]
    for i, name in enumerate(names):
        teams[i % team_count].append(name)
    
    for idx, team in enumerate(teams, start=1):
        print(f"팀 {idx}: {', '.join(team)}")

if __name__ == "__main__":
    while True:
        make_teams()
        again = input("다시 팀을 짜시겠습니까? (y/n): ").lower()
        if again != "y":
            break
