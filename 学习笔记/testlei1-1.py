from testlei1 import Notebook
wt = "你喜欢哪个骚逼？"
my_wt = Notebook(wt)

my_wt.show_wt(wt)
print("Enter 'q'to anytime to quit !!!")
while True:
    daan = input("哪位：")
    if wt == 'q':
        break
    my_wt.cc_wt(wt)

print("谢谢参与！！")
my_wt.qb_wt(daan)

