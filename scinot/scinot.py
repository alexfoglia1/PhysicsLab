import sys
import numpy
import subprocess

def to_scinot(x):
    shift = 0
    while True:
        if x > 5:
            x /= 10
            shift += 1
        elif x <= 0.5:
            x *= 10
            shift -= 1
        if x > 0.5 and x <= 5:
            return float(numpy.format_float_positional(x)), shift
try:            
    x = float(sys.argv[1])
    dx = float(sys.argv[2])
except:
    print("Usage:\n\tpython3 {} [x] [Dx]".format(sys.argv[0]))
    print("Example:\npython3 {} 0.6713e2 5\n".format(sys.argv[0]))
    x = 0.6713e2
    dx = 5

x, shift = to_scinot(x)
dx, dshift = to_scinot(dx)

dxrnd0 = round(dx, 0)
dxrnd1 = round(dx, 1)
if "{}".format(dxrnd0)[0] == '1':
    dx = dxrnd1
else:
    dx = dxrnd0
dx = dx * 10**dshift / 10**shift

print("x = {} * 10^{}".format(numpy.format_float_positional(x),shift))
print("dx = {} * 10^{}".format(numpy.format_float_positional(dx),shift))

if dx == int(dx):
    print("\nx = ({} +/- {}) * 10^{}".format(int(round(x, 0)), int(dx), shift))
else:
    strdx = numpy.format_float_positional(dx)
    dxdotindex = strdx.index(".")
    dxdecpartlen = len(strdx) - dxdotindex - 1
    xnormalized = numpy.format_float_positional((round(x, dxdecpartlen)))
    xdotindex = xnormalized.index(".")
    xdecpartlen = len(xnormalized) - xdotindex - 1
    zerofill = ''.join(['0' for i in range(dxdecpartlen - xdecpartlen)])
    print("\nx = ({}{} +/- {}) * 10^{}".format(xnormalized, zerofill, numpy.format_float_positional(dx), shift))

