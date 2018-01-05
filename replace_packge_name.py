import os
import re
import os.path


currentStr = 'aaa.bbb'
replaceStr = 'zachary.findceshi'
directory = 'D:\works\FindCeShi'

def Test3(rootDir, level=1):
    if level==1: print(rootDir)
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        houzui = os.path.splitext(lists)[1][1:]
        if houzui == 'xml' or houzui == 'java' or houzui == 'gradle':
            try:
                fp = open(path, 'r')
                content = fp.readlines()
                temp = ''
                for s in content:
                    if re.search(currentStr,s):
                        print(s)
                        s = re.sub(currentStr, replaceStr,s)
                        temp+=s
                    else:
                        temp+=s
                wp = open(path,'w')
                wp.write(temp)
                fp.close()
                wp.close()
            except Exception as err:
                print(err)
        if os.path.isdir(path):
            Test3(path, level+1)

def test():
    path = directory
    filelist = [os.path.join(os.path.abspath(path), x[0]) for x in os.walk(os.path.abspath(path))]
    changeStyle = currentStr.replace('.','\\')
    temparry = []
    for x in filelist:
        if changeStyle in x:
            temparry.append(x)

    for d in temparry:
        for f in temparry:
            if d == f:
                continue
            if d in f:
                temparry.remove(f)

    for ipath in temparry:
        oldpath = ipath
        newpath = ipath.replace(changeStyle,replaceStr.replace('.','\\'))
        try:
            os.renames(oldpath, newpath)
        except:
            print('错误')


currentStr = input('请输入当前包名:')
replaceStr = input('请输入目标包名:')
directory = input('请输入项目根路径:')

Test3(directory)
test()
