from math import erf

mean = lambda x : sum(x)/len(x)
sd = lambda x : (sum([(x[i] - mean(x))**2 for i in range(0,len(x))])/(len(x) - 1))**0.5
sqrt2 = 2**0.5
cnorm = lambda x : (1 + erf((x)/(sqrt2)))/2

x = [10.1, 10.0, 10.2, 10.3, 10.2, 10.1, 10.0, 10.2, 10.1, 10.2, 10.1, 10.3, 11.0, 11.5, 11.6]

flag = True
it = 0
while flag:
    print("Iteration #{}".format(it+1))
    it+=1
    
    s = sd(x)
    m = mean(x)
    n = len(x)

    sds = []

    for x_i in x:
        d_i = abs(x_i - m)
        sds.append(d_i / s)
        
    expected_n = []
    for s_i in sds:
        p_i = 1 - (cnorm(s_i) - cnorm(-s_i))
        expected_n.append(n * p_i)
        
    flag = False
    for i in range(0,n):
        if expected_n[i] < 0.5:
            print("{} shall have {} observations, removed.".format(x[i], expected_n[i]))
            x.remove(x[i])
            print(x)
            flag = True

