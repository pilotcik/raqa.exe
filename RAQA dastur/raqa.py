print('Assalomu Aleykum Hush kelibsiz!')
yashik1=15*35*44
yashik2=20*30*50
hajmi1=400*200*300
hajmi2=450*300*200
ogirlik1=12000
ogirlik2=13000
massa1=25
massa2=44
n1=hajmi1//yashik1
n2=hajmi1//yashik2
n3=hajmi2//yashik1
n4=hajmi2//yashik2
m1=n1*massa1
m2=n2*massa2
m3=n3*massa1
m4=n4*massa2
cars= ['zil','kamaz','ural','man','vagon','arava',]
print(cars)
y='Transportni tanlang!\n'
x=''
qiymat=True
while qiymat:
      x=input(y)
      if x=='zil':
            print(f"zil ning yuk kotarish qobiliyati=> {ogirlik1}  kg")
            if m1<=ogirlik1:
                  n1-=1
            m1=n1*massa1
            print(f"zilga {hajmi1//yashik1} ta 9mm li yashik sigadi. Ularning massasi=> {m1} kg")
            if m2<=ogirlik2:
                   n2-=1
            m2=n2*massa2
            print(f"zilga {hajmi1//yashik2} ta 7,63mm li yashik sigadi. Ularning massasi=> {m2}  kg" )
      elif x=='kamaz':
            print(f"kamaz ning yuk kotarish qobiliyati=> {ogirlik2} kg")
            if m3<=ogirlik2:
                  n3-=1
            print(f"kamazga {hajmi2//yashik1} ta 9mm li yashik sigadi. Ularning massasi=> {m3} kg")
            m3=n3*massa1
            if m4<=ogirlik2:
                  n4-=1
            m4=n4*massa2
            print( f"kamazga {hajmi2//yashik2} ta 7,63mmli  yashik sigadi. Ularning massasi=> {m4} kg")
      elif x=='chiqish':
            print('dastur tugadi \n')
            qiymat=False
           
      else:
            print('Mudofaa Vazirligida bunday avtomobil turiga ruxsat etilmagan!')
            
      
