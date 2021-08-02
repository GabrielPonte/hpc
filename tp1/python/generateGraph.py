import os
import subprocess
import random
import matplotlib.pyplot as plt


def plot_graph(x_axis_i,y_axis_i,x_axis_j,y_axis_j,languageType):
    legend = []
    
    plt.ylabel("Elapsed time (s)")
    plt.xlabel("Size of n")
    plt.title(f"Graph in {languageType}")

    
    plt.plot(x_axis_i, y_axis_i)
    legend.append('External i')

    plt.plot(x_axis_j, y_axis_j)
    legend.append('External j')

    plt.legend(legend)
    plt.savefig(os.getcwd())



n = 2

xc_external_i = []
yc_external_i = []

xc_external_j = []
yc_external_j = []


n_numbers = []

# C

os.chdir('.\c')

while n < 30000:    
    out_i = subprocess.check_output(['matMult.exe',str(n),'1'])
    elapsed_time_i = float(out_i.split()[2])

    out_j = subprocess.check_output(['matMult.exe',str(n),'2'])
    elapsed_time_j = float(out_j.split()[2])

    xc_external_i.append(n)
    xc_external_j.append(n)

    yc_external_i.append(elapsed_time_i)
    yc_external_j.append(elapsed_time_j)

    n += random.randint(n,2*n)
    n_numbers.append(n)

plt.clf()
plot_graph(xc_external_i,yc_external_i,xc_external_j,yc_external_j,'C')


# Fortran

xf95_external_i = []
yf95_external_i = []

xf95_external_j = []
yf95_external_j = []



os.chdir('..\\fortran')
print(len(n_numbers))

for n in n_numbers:
    
    out_i = subprocess.check_output(['matMult.exe',str(n),'1'])
    elapsed_time_i = float(out_i.split()[2])

    out_j = subprocess.check_output(['matMult.exe',str(n),'2'])
    elapsed_time_j = float(out_j.split()[2])

    xf95_external_i.append(n)
    xf95_external_j.append(n)

    yf95_external_i.append(elapsed_time_i)
    yf95_external_j.append(elapsed_time_j)
    

plt.clf()
plot_graph(xf95_external_i,yf95_external_i,xf95_external_j,yf95_external_j,'Fortran')

print(os.getcwd())