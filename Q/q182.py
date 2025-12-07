ip = input()
text = list(ip) #直接把文字轉成list
# 原本寫法：
# text = []
# for i in ip:
#     text.append(i)
n = int(input())

for _ in range(n): #不重要的變數用“_”代替
    ls = []
    num = int(input())
    if num == 0:
        for i in range(0, len(text), 2):
            ls.append(text[i+1])
            ls.append(text[i])
    elif num == 1:
        pair = sorted([text[i],text[i+1]]) #每兩個為一組並且採升冪排列
        ls.extend(pair) #將列表展開加入元素進去
#        原本的寫法：
#        for i in range(0, len(text), 2):
#            temp = []
#            temp.append(text[i+1])
#            temp.append(text[i])
#            temp.sort()
#            for j in temp:
#                ls.append(j)
    elif num == 2:
        for i in range(0, int(len(text)/2)):
            ls.append(text[i])
            ls.append(text[(int((len(text))/2))+i])
    text = ls

print("".join(text)) #將text列表中全部以""連接起來組成文字
# 原本的寫法：
# for t in text:    
#    print(t, end="")

#總結： 原代碼 29行，新代碼 21行。