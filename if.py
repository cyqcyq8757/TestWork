height = input("키가 몇이세요?(센치 단위)")
gender = input("성별이 무엇인가요?(남자/여자)")
height = int(height)

def std_weight(height, gender):
    if 80 <= height <= 250:
        if gender == "남자":
            weight = (height * height * 22 / 10000)
            print(f"키 {height}cm 남자의 표준 체중은 {weight}kg 입니다.")
        elif gender == "여자":
            weight = (height * height * 21  / 10000)
            print(f"키 {height}cm 여자의 표준 체중은 {weight}kg 입니다.")
        else:
            print("성별을 다시 확인 해 주세요.")
    else:
        print("올바른 단위로 키를 적어 주세요.")
std_weight(height, gender)