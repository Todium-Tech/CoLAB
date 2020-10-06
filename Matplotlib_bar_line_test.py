import matplotlib.pyplot as plt
year=[2015,2016,2017,2018,2019]
per=[12.5,35.9,23.45,67.9,97.4]
a=input("enter bar for barchart and line for line chart")
if a=="bar":
    plt.bar(year,per)
    plt.show()
else:
    plt.plot(year,per)
    plt.show()
