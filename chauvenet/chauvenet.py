from math import erf

mean = lambda x : sum(x)/len(x)
sd = lambda x : (sum([(x[i] - mean(x))**2 for i in range(0,len(x))])/(len(x) - 1))**0.5
sqrt2 = 2**0.5
cnorm = lambda x : (1 + erf((x)/(sqrt2)))/2

measurements = [10.1, 10.0, 10.2, 10.3, 10.2, 10.1, 10.0, 10.2, 10.1, 10.2, 10.1, 10.3, 11.0, 11.5, 11.6]

flag = True
it = 0
while flag:
    print("Iteration #{}".format(it+1))
    print(measurements)
    it+=1
    
    m_sigma = sd(measurements)
    m_mean  = mean(measurements)
    n_meas  = len(measurements)

    std_deviations = []
    for measurements_i in measurements:
        dev_i = abs(measurements_i - m_mean)
        std_deviations.append(dev_i / m_sigma)
        
    expected_n = []
    for s_i in std_deviations:
        p_in = (cnorm(s_i) - cnorm(-s_i))
        p_out = 1 - p_in
        expected_n.append(n_meas * p_out)
        
    flag = False
    suspicious_measurements = []
    for i in range(0, n_meas):
        if expected_n[i] < 0.5:
            print("Measurement {} shall have {} observations, removed\n".format(measurements[i], expected_n[i]))
            suspicious_measurements.append(measurements[i])
            flag = True
    for measure in suspicious_measurements:
        measurements.remove(measure)
            

