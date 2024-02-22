import math,time,os,sys,threading
# 是否是质数
def is_prime(n):
    if n < 2 :
        return False
    if n == 2 :
        return True
    if n % 2 == 0:
        return False
    div = 3
    while div * div <= n:
        if n % div == 0:
            return False
        else:
            div += 2
    return True
# 线程函数
def main(n,id,end):
    global o,datas
    tick = time.time()-1
    e = 1
    d,hr,min,sec = 0,0,0,0
    datas[id-1]["run"] = True
    for i in range(n,n+end):
        even_num = 6 + 2 * i
        j = 3
        while j <= even_num//2 :
            if is_prime(j) and is_prime(even_num - j):
                break
            j += 2
        if j > even_num//2 :
            print(even_num, "：没找到'1+1'结构，你推翻了哥德巴赫猜想！！！")
            break
        l = len(str(even_num))-1
        p = (even_num-(n*2+6))/((end)*2+6)
        strp = str(math.floor(p*10000)/100)
        length = 60
        if time.time() - tick > 3:
            tick = time.time()-tick
            e = even_num-e
            t = ((n+end)*2+6-even_num)/(1/tick*e)
            d = math.floor(t/86400)
            hr = math.floor(t%86400/3600)
            min = math.floor(t%3600/60)
            sec = math.floor(t%60)
            tick = time.time()
            e = even_num
        datas[id-1]["id"] = str(id).zfill(3)
        datas[id-1]["l"] = l
        datas[id-1]["strp"] = strp
        datas[id-1]["p"] = p
        datas[id-1]["d"] = str(d).zfill(3)
        datas[id-1]["hr"] = str(hr).zfill(2)
        datas[id-1]["min"] = str(min).zfill(2)
        datas[id-1]["sec"] = str(sec).zfill(2)
        datas[id-1]["n"] = n
        datas[id-1]["end"] = end
    datas[id-1]["run"] = False
    o += 1
# 保留小数
def add_zero(text,n=2):
    text = str(text)
    return text+(n-len(text.split(".")[1]))*"0"
# 清屏
if sys.platform == "win32":
    os.system("cls")
elif sys.platform == "linux":
    os.system("clear")
# 初始化
threads,datas = [],[]
tr = 15
vvv = 300000
o = 0
# 读取i
with open("i.txt","r") as f:
    f = int(f.read())
input(f"验证区间{f*2+6}~{((tr-1)*vvv+f)*2+6}，回车确认")
# 添加线程
for i in range(tr):
    threads.append(threading.Thread(target=main, args=(i*vvv+f,i+1,vvv)))
    datas.append({"id":i+1})
# 启动线程
j = 0
for i in threads:
    i.start()
    j += 1
    print(f'\r启动线程#{str(j).zfill(3)} \033[32m{math.floor(j*80/tr)*"━"}\033[0m\033[31m{math.floor(80-j*80/tr)*"━"}\033[0m',end='')
# 展示信息直到验证完毕
while o<tr:
    if sys.platform == "win32":
        os.system("cls")
    elif sys.platform == "linux":
        os.system("clear")
    pp = 0
    for i in datas:
        id = i["id"]
        l = i["l"]
        strp = i["strp"]
        p = i["p"]
        d = i["d"]
        hr = i["hr"]
        min = i["min"]
        sec = i["sec"]
        n = i["n"]
        end = i["end"]
        length = 100
        pp += p
        if i["run"]:
            print(
                f'#{id} {n*2+6}~{(n+end)*2+6} {add_zero(strp)}% ',
                f'预计剩余{(d+"天" if int(d)>0 else "")+(hr+"时" if int(hr)>0 else "")+(min+"分" if int(min)>0 else "")+sec}秒'
                f'\033[32m{math.floor(p*length)*"━"}\033[0m\033[31m{(length-math.floor(p*length))*"━"}\033[0m',
                end='\n'
            )
        else:
            with open('iplus', 'w') as file:
                file.write(str(n+end))
            print(f'#{id} {n*2+6} => {(n+end)*2+6} 验证完毕')
    print(f'总进度 {add_zero(math.floor(pp*8000/tr)/100)}% \033[32m{math.floor(pp*length/tr)*"━"}\033[0m\033[31m{math.floor(length-pp*length/tr)*"━"}\033[0m')
    time.sleep(3)
# 保存i
with open('i.txt', 'w') as file:
    file.write(str((tr-1)*vvv+f))
# 输出信息
print(f"\a{f*2+6} => {((tr-1)*vvv+f)*2+6} 验证完毕")