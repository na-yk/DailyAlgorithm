import copy

def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    today_date = convert_date_string_to_list(today)

    # terms 리스트->딕셔너리로 변환
    for term in terms:
        temp = term.split()
        term_dict[temp[0]] = int(temp[1])
        
    for i in range(len(privacies)):
        privacy = privacies[i]
        temp = privacy.split()
        date = convert_date_string_to_list(temp[0]) # 개인정보 수집일자
        term_no = temp[1]   # 약관 번호
        
        exp = cal_exp(date, term_dict[term_no])        
        comp_result = comp_date(today_date, exp)
        
        if (comp_result <= 0):
            answer.append(i+1)
        else:
            continue
    
    return answer

# 파기일을 계산하는 함수
def cal_exp(date, after):
    exp = copy.deepcopy(date)
    
    year = date[0]
    month = date[1]

    exp[0] += after//12
    exp[1] += after%12
    
    if (exp[1] > 12):
        exp[0]+=1
        exp[1]=exp[1]-12
        
    return exp

# 날짜 문자열->리스트 변환하는 함수
def convert_date_string_to_list(date):
    date_list = date.split(".")
    for i in range(3):
        date_list[i] = int(date_list[i])
    
    return date_list

# 리스트 형식의 날짜를 비교하는 함수
def comp_date(today, standard):
    for i in range(3):
        if today[i] < standard[i]:
            return 1
        elif today[i] > standard[i]:
            return -1
        else:
            continue
    
    return 0