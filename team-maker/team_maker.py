import random

def make_teams():
    # 첫 줄: 이름 입력
    names = input("이름들을 ,로 구분해서 입력하세요: ").split(",")
    names = [name.strip() for name in names if name.strip()]  # 공백 제거
    
    # 두 번째 줄: 팀 개수 입력
    team_count = int(input("팀 개수를 입력하세요: "))
    
    # 이름 섞기
    random.shuffle(names)
    
    # 팀 나누기 (최대한 균등하게)
    teams = [[] for _ in range(team_count)]
    for i, name in enumerate(names):
        teams[i % team_count].append(name)
    
    # 결과 출력
    for idx, team in enumerate(teams, start=1):
        print(f"팀 {idx}: {', '.join(team)}")

if __name__ == "__main__":
    while True:
        make_teams()
        again = input("다시 팀을 짜시겠습니까? (y/n): ").lower()
        if again != "y":
            break
