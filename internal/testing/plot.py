import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)
figure = plt.gcf()
figure.set_size_inches(19.2, 10.80)
plt.savefig("myplot.png", dpi=100)
mng = plt.get_current_fig_manager()
mng.window.state("zoomed")
plt.show()
