# Yiska Levi

def interleave(*iter_list):
    l_ans=[]
    dic_help={}
    num=1
    for li in iter_list:
        dic_help[num]=len(li)
        num=num+1
    max_len = max(dic_help.values())
    for i in range(max_len):
        num=1
        for li in iter_list:
            if i<dic_help[num]:
                l_ans.append(li[i])
            num = num + 1
    return l_ans

def interleave_generator (*iter_list):
    l_ans=[]
    dic_help={}
    num=1
    for li in iter_list:
        dic_help[num]=len(li)
        num=num+1
    max_len = max(dic_help.values())
    for i in range(max_len):
        num=1
        for li in iter_list:
            if i<dic_help[num]:
                num = num + 1
                yield li[i]
    return ''

print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
for i in interleave_generator('abc', [1, 2, 3], ('!', '@', '#')):
    print(i,end=', ')
