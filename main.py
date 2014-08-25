from matplotlib import pyplot as plt
import numpy as np


class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list(line.get_xdata())
        self.ys = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        print 'click', event
        if event.inaxes!=self.line.axes: return
        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_title('click to build line segments')
im = plt.imread("map.png");
plt.imshow(im);
ax.autoscale(False)

line = ax.plot(0,0)
print line
linebuilder = LineBuilder(line)

plt.show()
