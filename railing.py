import math

def railing_list(cyber_str,l):
    '''
    #以加密字符串长度为循环，带入周期函数表达式里面，取得对应栏数，以此获得多维数组
    需要加密字段及栏数，or填充字符串
    :return: 加密多维数组
    '''
    railing =[[0 for m in range(x)]for t in range(l)]
    for t in range (x):
        k =math.floor(t/w)
        #print(t,k)
        if t in range (int(0+w*k),int(w/2+w*k)):
            #n = int(w / 2 + w * k - t)
            n = t - w*k
            railing[n][t] = cyber_str[t]
        elif t in range (int(w/2+w*k),int(w+w*k)):
            #n = int(t - w / 2 - w * k)
            n = w*(k+1)-t
            railing[n][t] = cyber_str[t]
    for i in range(l):
        print(railing[i])

    return railing

def encrypted(railing):
    '''
    输出加密字符串
    :param railing:
    :return:
    '''
    encyber_str = ''
    for m in range(l):
        for t in range(x):
            if railing[m][t]:
                encyber_str+=railing[m][t]
    return encyber_str

def decrypt(railing):
    '''
    输入加密字符串，输出解密多维数组
    :param railing:
    :return:
    '''
    T = 0
    for m in range (l):
        for t in range(x):
            if railing[m][t]:
                railing[m][t] =cyber_str[T]
                T += 1
    decrypted_str = ''
    for t in range(x):
        for m in range(l):
            if railing[m][t]:
                decrypted_str+=railing[m][t]
    return decrypted_str

if __name__ == '__main__':
    print('1.加密')
    print('2.解密\n')
    get_n = input('get you choice\t')
    cyber_str = input('输入字符串\t')
    l = int(input('栏数\t'))
    x = len(cyber_str)
    w = (l - 1) * 2

    if get_n == '1':
        railing =railing_list(cyber_str,l)
        encrypted_str = encrypted(railing)
        print('\nthe string you want is \n'+ encrypted_str)
        input()
    elif get_n == '2':
        re_str = [True for t in range(x)]
        railing = railing_list(re_str,l)
        railing = decrypt(railing)
        print('\nthe string you want is \n' + railing)
        input()


