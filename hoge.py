from pylab import *
from numpy import *

x = np.arange(10)
y = x

# Plot junk and then a filled region
plot(x, y)

# Now lets make an arrow object
arr = Arrow(2, 2, 1, 1, edgecolor='white')

# Get the subplot that we are currently working on
ax = gca()

# Now add the arrow
ax.add_patch(arr)

# We should be able to make modifications to the arrow.
# Lets make it green.
arr.set_facecolor('g')
show()
