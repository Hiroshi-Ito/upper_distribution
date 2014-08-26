import sys
import matplotlib.pyplot as p
import time
import numpy
fig=p.figure();
ax = fig.add_subplot(1,1,1)

y=[];x=[];y1=[0,1000];x1=[0,0]
y=numpy.random.randn(1000,1)*100
x=numpy.arange(0,1000)
line1, = ax.plot(x,y,color='black');
ax.set_ylim(0, 1000);
line, = ax.plot(x1,y1,color='r',alpha=1,animated=True); # this is the line which i wanted to move over the graph w.r.t to time. ( i can also use axvline , but i guess its the same).
canvas = ax.figure.canvas
canvas.draw()
background = canvas.copy_from_bbox(ax.bbox); #my problem is here
starttime=time.time();
mytimer=0;
mytimer_ref=0;
def update(canvas,line,ax):
    canvas.restore_region(background) #my problem is here
    t=time.time()-starttime;
    mytimer=t+mytimer_ref;
    x1=[mytimer,mytimer];
    line.set_xdata(x1);
    ax.draw_artist(line)
    canvas.blit(ax.bbox) #my problem is here

def onclick(event):
    global starttime
    starttime=time.time();
    global mytimer_ref;
    mytimer_ref=event.xdata;
    print "starttime",starttime;


cid=line1.figure.canvas.mpl_connect('button_press_event',onclick); # when i click the mouse over a point, line goes to that point and start moving from there.
timer=fig.canvas.new_timer(interval=100);
args=[canvas,line,ax];
timer.add_callback(update,*args); # every 100ms it calls update function
timer.start();
p.show();
