
        

def manager():
    print("관리자 모드에 진입하였습니다.\n")
    while(True):
        fc = int(input("기능을 선택해 주세요.\n1. 메뉴 추가\t\t2. 메뉴 삭제\t\t3. 가격변경\t\t4. 현재 받은 돈 출력\n5. 관리자 모드 끝내기\t\t\t"))
        if (fc == 1):
            add_menu()
        elif (fc == 2):
            delete_menu()
        elif (fc == 3):
            change_price()
        elif (fc == 4):
            money()
        else:
            break
        
        
def add_menu(): #메뉴 추가하기 함수
    print(menu_dic)
    want_menu = input("원하시는 메뉴를 입력해주세요.")
    menu_price = input("원하시는 메뉴의 가격을 입력해주세요. : ")
    menu_dic[len(menu_dic.keys())+1] = [want_menu, menu_price]
    print("원하시는 메뉴가 추가되었습니다.")
    
def delete_menu():  #메뉴 삭제하기 함수
    print(menu_dic)
    unwant_menu = input("삭제하시려는 메뉴를 입력해주세요. : ")
    select = input("정말로 삭제하시겠습니까? (Y/N)").upper()
    if (select == "Y"):
        for x in range(len(menu_dic.keys())):   #삭제하고 싶은 메뉴 찾기(반복문)
            if (unwant_menu == menu_dic[x+1][0]):
                del menu_dic[x+1][0]
                break
        print("원하시는 메뉴가 삭제되었습니다.\n\n")

def change_price():     #가격변경 함수
    print(menu_dic)
    menu = input("가격을 변경하시고 싶은 메뉴를 입력해주세요. : ")
    price = int(input("변경하시고 싶은 가격을 입력해주세요."))
    for x in range(len(menu_dic.keys())):
        if (menu == menu_dic[x+1][0]):      #가격을 변경하고 싶은 메뉴를 찾는 반복문
            before_price = menu_dic[x+1][1]
            menu_dic[x+1][1] = price
            print(f"{menu_dic[x+1][0]}의 가격이 {before_price}에서 {price}로 변경되었습니다!\n\n")
            break

def money():
    print(sum)


card = {"1234-1234-1234-1234" : '100,000'}
menu_dic = {1:["짜장면", 5000], 2:["짬뽕", 6000], 3:["군만두", 8000], 4:["탕수육", 10000]}
re_order = "Y"
sum = 0
while(re_order == "Y"):
    for x in range(len(menu_dic.keys())):
        print(menu_dic[x+1], end = "\t\t")
    print()
    menu = int(input("1. 위 메뉴 중 주문할 메뉴의 번호를 쓰세요 : "))
    
    if (menu == 5):
        manager()
    
    for x in range(len(menu_dic.keys())):       #관리자 모드를 끝내면 이전 리스트가 업데이트가 되어있지 않아, 업데이터 된 리스트를 출력하도록 함
        print(menu_dic[x+1], end = "\t\t")
    print()
    
    menu = int(input("1. 위 메뉴 중 주문할 메뉴의 번호를 쓰세요 : "))    
    num = int(input("2. 위 메뉴의 주문 수량을 쓰세요 : "))
    menu_sum = menu_dic[menu][1]*num
    sum += menu_sum
    print(f"주문하신 메뉴는 {menu_dic[menu][0]}이고 주문 수량은 {num}그릇이며 주문 금액은 {menu_dic[menu][1]*num} 입니다.\n\n\n")
    re_order = input("재주문 하시겠습니까? (Y/N) : ").upper()
    if (re_order == "N"):
        break
    
    
#결재 진행
print("주문이 종료되었습니다.")
print(f"지불하실 비용은 총 {sum}입니다.")
# credit_card = input("사용하실 카드번호를 입력해주세요.\n형식은 xxxx-xxxx-xxxx-xxxx입니다. : ")
# for ccard in card.keys():
#     if (ccard == credit_card):
#         if (card[credit_card] >= sum):
#             print("결제가 완료되었습니다.\n 카드를 챙겨주세요.")
#             print(f"잔액은 {card[credit_card]-sum} 입니다.")
#         else:
#             print("잔액이 부족합니다.")