x = [(2.00,0.01), (2.0,0.2), (2.01,0.10)]

weights = [1.0/(x[i][1]**2) for i in range(0, len(x))]
xwav = sum([x[i][0]*weights[i] for i in range(0, len(x))])/sum(weights)
sxwav = 1/(sum(weights))**0.5
print("Final result: {} +/- {}".format(xwav, sxwav))

