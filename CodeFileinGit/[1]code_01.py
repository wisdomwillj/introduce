def stockSolution(param0):
    deposit = 100*1000*1000 # 예수금 1억원
    dept = 50*1000*1000 # 대출금 5천만원
    deptInput = 50*1000*1000 # 최초 대출금을 5천만원으로 둔다 --> 향후 input 값으로 함
    count_1 = 0
    deptOutput = 0
    flag = 0
    ls_day = []
    for i in range(len(param0)-1):# 날짜별로 주식을 살 경우
        count_1 += 1
        print("============================================================")
        print(f">>> i = {count_1}일째 구매한 경우: \n")
        price1st = param0[i] # i일 구매한 주식가격 고정값
        stock1st = int(deposit/price1st) # i일 구매한 보유주식수 고정값
        stockTotal = int(deposit/price1st) # i일 구매한 보유주식수
        total = stockTotal*price1st # i일 투자금 = 주식수 * 주가
        balance= deposit - total # i일 투자후 잔금 = 예수금 - 투자금
        cnt = 0 # 대출횟수
        count_2 = 0
        flag = 0
        dic = {0:dept} # 대출금이 input이 되면서 대출잔금 기억해두기
        for j in range(i+1,len(param0)): # 주식 구매 후 목표차익 실현되는 날이 있는 경우 찾기
            price = param0[j]       # j일 주식가격
            count_2 += 1
            print(f"구매 후 {count_2}일:...  \n")
            print("주식보유수: {:0,.0f} ".format(stockTotal))
            print("주식가격  : {:0,.0f} ".format(price))

            flag = 0
            if price <= price1st*0.5: # 주가가 첫날보다 50% 이상 떨어지면 대출받기
                cnt+=1 # 대출횟수
                print("min(dic.values()): ", min(dic.values()))
                dic[cnt] = min(dic.values()) - deptInput # 대출잔여금 기록
                print("대출잔금: ", dic.items())
                if min(dic.values()) < 0: # 대출금 현재 잔여금이 요청된 대출금 보다 작으면 대출불가
                    deptOutput = 0
                    print("대출불가")   
                    flag = 0             
                else: # 대출금 현재 잔여금이 요청된 대출금보다 크면 대출가능
                    deptOutput = deptInput
                    stockTotal += int((balance+deptOutput)/param0[j]) # j일에 대출을 받아 재구매
                    flag = 1 # 1이 되는 시점에서 주식보유수가 변해야함
            print("대출여부  : ", flag)
            print("판매가능금액: {:0,.0f}".format(param0[j]*stockTotal))
            sell = (param0[j]*stockTotal) # j일 주식가격과 전체 주식수를 곱 구하기
            sellPoint = decisionSell(sell) # sell로 판단해 True,False로 반환
            if sellPoint:
                day = j-i # sell로 판단될 경우 해당 색인번호와 주식 산 색인번호 차이로 일자를 계산
                print("판매가능  : ", sellPoint)
                print(" ")
                break
            else:
                day = -1
            print("판매가능  : ", sellPoint)
            print("")
        ls_day.append(day)
    ls_day.append(day)   
    answer = ls_day
    return answer

# stockSolution 함수에서 판매시점 분석
def decisionSell(sell): 
    dept = 50*1000*1000
    targetInvest = 1000*1000*1000
    result_decision = False
    sellPoint = sell-targetInvest-dept
    if sellPoint > 0:
        result_decision = True
        #print('판매금: ', end='')
        #print('{:,}'.format(sell))
        print('순자산: {:0,.0f}'.format(sell))
    else:
        result_decision = False
    return result_decision

dataset =  [34000,78000, 48000, 27000, 11000, 285000, 320000, 335100] # result : [5, 6, 3, 2, 1, -1, -1, -1]
#dataset = [78000, 48000, 27000, 285000, 320000, 335100] 	# result : [5, -1, 1, -1, -1, -1]
result = stockSolution(dataset)
print(result)