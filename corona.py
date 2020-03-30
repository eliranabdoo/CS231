import matplotlib.pyplot as plt
import numpy as np

cases = np.asarray([12, 12, 15, 16, 20, 22, 37, 39, 59, 77, 99, 130, 164, 200, 253, 318, 421, 524, 677, 838, 943, 1207, 1552, 2000, 2463, 3011,3404]) #,3824,4256,4347])
examined = np.asarray([305, 348, 393, 429, 457, 472, 485, 560, 618, 722, 845, 979, 1094, 1252, 1412,1585,1811,1934, 2111,2413,2800,3275, 3843,4343,4832,5523,6234,6843,7932,9145,11177,13735,16085,18558,20427,23522,27265,32332,37572,42579,48143][-len(cases):])

plt.subplot(2, 1, 1)
plt.plot(np.log(cases))
plt.ylabel('cases')

plt.subplot(2, 1, 2)
plt.plot(np.log(examined))
plt.ylabel('examined')
plt.show()

normed_cases = (cases - np.average(cases)) / cases.std()
normed_examined = (examined - np.average(examined)) / examined.std()

plt.plot(normed_cases, 'r')
plt.plot(normed_examined, 'b')
plt.show()

ratio = cases / examined

plt.plot(ratio)
plt.title('ratio')
plt.show()
