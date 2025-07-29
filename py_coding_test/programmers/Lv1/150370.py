# 개인정보 수집 유효기간
def solution(today, terms, privacies):
    answer = []
    today_year = int(today[:4])
    today_month = int(today[5:7])
    today_day = int(today[8:])
    term_to_month = {}
    for term in terms:
        t, m= term.split()
        term_to_month[t] = int(m)
        
    i = 0
    for privacy in privacies:
        i += 1
        date, t = privacy.split()
        date_year, date_month, date_day = list(map(int, date.split(".")))
        date_month += term_to_month[t]
        date_day -= 1
        # 100일 경우 주의
        while date_month > 12:
            date_year += 1
            date_month -= 12 

        if date_day == 0:
            date_month -= 1
            date_day = 28
        
        if date_year < today_year:
            answer.append(i)
        elif date_year == today_year:
            if date_month < today_month:
                answer.append(i)
            elif date_month == today_month:
                if date_day < today_day:
                    answer.append(i)
        
    return answer