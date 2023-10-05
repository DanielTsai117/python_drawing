import random
import csv
import os

print("=====================================")
print("請確保在同資料夾內有draw.csv")
print("=====================================")
print("=====================================")
print("本程式最佳的使用場景，是在")
print("1. 要抽籤的名單中，具有［如果一人有多票，都只有一票的權利］的狀況")
print("2. 只抽［一個獎項］，且最好是［中籤　與　沒中籤］")
print("=====================================")
print("=====================================")
draw_headcount = int(input("那麼，請告訴我這次要抽幾個～："))
print("=====================================")

with open('draw.csv', newline='') as csvfile:

    #讀取 CSV 檔內容，將每一列轉成一個 dictionary
    #rows = csv.DictReader(csvfile)
    # 讀取 CSV 檔內容，將每一列轉成一個 list
    rows = csv.reader(csvfile)


    #以迴圈輸出指定欄位
    data = [row[0] for row in rows]
    print("=====================================")
    print("要抽籤的名單為")
    print(data)
    print("=====================================")  
    
    lucky = []
    
    data_set = list(set(data))
    
    print("=====================================")
    print("去除重複後要抽籤的名單為")
    print(data_set)
    print("=====================================")  
    
    while(True):
        lucky_one = random.sample(data_set,1)
        if len(lucky) >= draw_headcount:
            break
        
        if lucky_one not in lucky:
            lucky.append(lucky_one)
            print("這個幸運兒是：",lucky_one)
#   #本版本名單去重了，不應該發生       
#        elif lucky_one in lucky:
#            print(lucky_one, "這個幸運兒已經中籤過了，我們再抽一位")    
#            continue
    print("=====================================")
    print("中獎名單為")
    print(lucky)
    print("=====================================")
   
    
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL,delimiter=';')
        writer.writerows(lucky)
        
    
    print("=====================================")
    print("您的中獎名單會在同資料夾裡的output.csv")
    print("感謝您的使用～")
    print("=====================================")
    os.system("pause")
