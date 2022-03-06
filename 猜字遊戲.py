#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random
words = ["antibody","humnanized","python"] #內鍵字詞
def game(): #定義主功能
    x = random.choice(words) #從內鍵字詞中隨機挑一個出來
    sec = "*"*len(x) #使用*號將表現該字詞的長度
    st = []#另外創一個list將有輸入過的字母放入
    while not sec == x: #迴圈，還沒找到全部單字時會持續
        print("本次單字:",sec,"請輸入英文字母(小寫)")
        guess = input("所猜的英文字母:")#輸入字母

        if len(guess)!= 1: #先設定只能輸入單一字母、並排除重複輸入的字母
            print("只能輸入單一英文字母")
                
        elif guess in st:
            print("已經輸入過了")
        else:
            if  guess in x:#判斷輸入字母是否與字詞吻合
                print("你猜中了!")
                sec = update_sec(x,sec,guess)#將符合的字母替換(另外定義功能)
                st.append(guess)
            else:
                print("猜錯了，字母不在其中")
                st.append(guess)
    if sec == x:
        print("你贏了!本次的字詞為:",x)
        
def update_sec(secret, cur_sec, rec_guess):#定義能將符合字母替換掉的功能
    result = ""#創一空字串
    for i in range(len(secret)):#根據字詞的長度重複進行
        if secret[i] == rec_guess:#若是所猜的字母有符合在字詞其中，就將先前sec(*號)的部分替換成該字母
            result = result + rec_guess
        else:
            result = result + cur_sec[i]#其餘的同樣為*號
    return result
    
game()

