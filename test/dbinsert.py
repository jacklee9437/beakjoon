import pymysql
con = pymysql.connect(host='mafiarte.cqxnljsntkmd.ap-northeast-2.rds.amazonaws.com', user='std248', password='team248!',
                       db='STD248', charset='utf8') # 한글처리 (charset = 'utf8')
cur = con.cursor()

while True :
    print("\033[33m- Please select db table : user, gameword, citizen\033[0m")
    print("\033[33m- If you want to exit, just input 'exit'.\033[0m")
    table = input().rstrip()
    if table == "gameword" :
        print("\033[33m- Enter category and word with seperator ' '(space) in order\033[0m")
        print("\033[33m- If you want to insert into other table, just input 'back'\033[0m")
        while True :
            columns = input().split()
            if columns[0] == 'back' :
                break
            else :
                sql = """INSERT INTO GAMEWORD (category, word) VALUES (%s, %s)"""
                cur.execute(sql, (columns[0], columns[1]))
                con.commit()
                print(f"\033[32m- {columns} INSERT 완료\033[0m")
    elif table == "user" :
        print("\033[31m- Not serviced \033[0m")
    elif table == "citizen" :
        print("\033[31m- Not serviced \033[0m")
    elif table =="exit" :
        break
    else :
        print("\033[31m- You entered invalid command.\033[0m")

con.close()