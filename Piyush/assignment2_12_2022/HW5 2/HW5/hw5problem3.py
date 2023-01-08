import csv
def closingprices_list(stockfilename):
    with open(stockfilename) as f:
        csvfile = csv.reader(f)
        data = []
        for lines in csvfile:
            data.append((lines[0], lines[4]))
    data = [(x, float(y)) for x,y in data[1:]]
    return data



def best_days(stockfilename, n):
    data = closingprices_list(stockfilename)
    
    # Bubble sort
    for i in range(0, len(data)):
        for j in range(len(data)-i-1):
            if data[j][1]>data[j+1][1]:
                temp = data[j]
                data[j]=data[j+1]
                data[j+1]=temp
    data=data[::-1]
    return (data[:n])


def worst_days(stockfilename, n):
    data = closingprices_list(stockfilename)
    # Bubble sort
    for i in range(0, len(data)):
        for j in range(len(data)-i-1):
            if data[j][1]>data[j+1][1]:
                temp = data[j]
                data[j]=data[j+1]
                data[j+1]=temp
    return (data[:n])


def correlation_coeff(stockfilename1, stockfilename2):
    file1 = closingprices_list(stockfilename1)
    file2 = closingprices_list(stockfilename2)
    x = y = 0
    n = len(file1)
    for i in range(n):
        x+=file1[i][1]
        y+=file2[i][1]
    mx = x/n
    my = y/n

    num = 0
    sx_num = sy_num = 0
    for i in range(n):
        num += ((file1[i][1]-mx)*(file2[i][1]-my))
        sx_num += ((file1[i][1]-mx)**2)
        sy_num += ((file2[i][1]-my)**2)           #/(n-1))**0.5


    sx = (sx_num/n-1)**0.5
    sy = (sy_num/n-1)**0.5
    r = (num)/((n-1)*sx*sy)
    return (round(r, 2))
    
n=5
print(f"The {n} best days of Apple stock are as follows:")
print(best_days("AAPL.csv", n))
print(f"The {n} worst days of Apple stock are as follows:")
print(worst_days("AAPL.csv", n))

print(f"The {n} best days of Coke stock are as follows:")
print(best_days("COKE.csv", n))
print(f"The {n} worst days of Coke stock are as follows:")
print(worst_days("COKE.csv", n))

print("The corelation coefficient between Apple and Coke Stock (between the dates 2017-11-07 and 2022-11-04) is", correlation_coeff("AAPL.csv", "COKE.csv"))
