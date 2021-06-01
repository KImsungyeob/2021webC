print("게임시작")

# 만약에 내가 1이면 간다 2면 안간다
# my = 1
# 여기를 짤라낸다
def ck_idpw(ret):
    if ret != None: 
        return '로그인성공'
    else:
        return '가입되지 않은 아이디'

# 돈을 넣으면 2배가 뻥튀기
# m = 1000
def coin(m):
    return m * 2

# mym = coin(1000)
# print("내돈은 {0}".format(mym))