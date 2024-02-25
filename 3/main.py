import time,json,sys,os
os.system('cls')
try:
    with open("./adcode.json","r") as f:
        adcode = json.loads(f.read())
except FileNotFoundError:
    print("未找到adcode文件，按回车键退出")
    input()
    sys.exit()
print("欢迎使用身份证号验证系统v0.3.3\n作者：Inventocode\n")
while True:
    id = input("请输入您的第二代身份证号:")
    why_list = []
    r = 0
    for i in range(len(id)):
        if id[i] not in ["0","1","2","3","4","5","6","7","8","9"]:
            r += 1
            id = id.replace(id[i],"0")
    if id[-1] not in ["0","1","2","3","4","5","6","7","8","9","X"]:
        r += 1
        id = id.replace(id[-1],"0")
    if r>0:
        why_list.append("含有非法字符")
    if len(id)!=18:
        why_list.append("长度错误，应为18位")
        while len(id)!=18:
            id = id+"0" if len(id)<18 else id[:-1]
    if int(id[:6]) not in adcode:
        why_list.append("未知出生地或出生地已撤销，例：华县610521")
    try:
        t = time.mktime(time.strptime(id[6:14],"%Y%m%d"))
        if time.time() - t <= 0:
            why_list.append("出生日期错误，例：2123年3月16日")
    except ValueError:
        why_list.append("出生日期错误，例：2月31日")
    if r==0:
        n = 0
        for i in range(17):
            n += int(id[i])*((2**(17-i))%11)
        x = str(1 if n%11==0 else 0 if n%11==1 else "X" if n%11==2 else 12-n%11)
        if x!=id[17]:
            why_list.append("校验码错误，应为"+x)
    else:
        why_list.append("校验码无法计算")
    print()
    if len(why_list) == 0:
        print("身份证号验证完成")
    else:
        print("验证失败，原因如下：")
        for i in why_list:
            print(" -",i)
    input()
    os.system('cls')