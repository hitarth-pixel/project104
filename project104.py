import csv
from collections import Counter
with open("SOCR-HeightWeight.csv",newline='') as f:
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
newData=[]
newData2=[]
data=range(len(fileData))
for x in data:
    nNum=fileData[x][1]
    nNum2=fileData[x][2]
    newData.append(float(nNum))
    newData2.append(float(nNum2))
n1=len(newData)
n2=len(newData2)
#function of mean
def mean():
    total1=0
    total2=0
    for i in newData:
        total1+=i
    for y in newData2:
        total2+=y
    mean1=total1/n1
    mean2=total2/n2
    print("mean of height-- "+str(mean1))
    print("mean of weight-- "+str(mean2))
mean()
# function of median
def medians():
    newData.sort()
    newData2.sort()
    if(n1%2==0 and n2%2==0):
        median1_first1=float(newData[n1//2])
        median1_first2=float(newData[n1//2-1])
        median2_first1=float(newData2[n2//2])
        median2_first2=float(newData2[n2//2-1])
        median1=(median1_first1+median1_first2)/2
        median2=(median2_first1+median2_first2)/2
    else:
        median1=newData[n1//2]
        median2=newData2[n2//2]
    print("median of height-- "+str(median1))
    print("median of weight-- "+str(median2))
medians()
#function of mode
def modes():

    data=Counter(newData)
    data2=Counter(newData2)
    mode_data={
        "50-75":0,
        "75-100":0,
        "100-125":0,
        "125-150":0
    }
    for height,occerence1 in data.items():
        if 50<float(height)<75:
            mode_data["50-75"]+=occerence1
        elif 75<float(height)<100:
            mode_data["75-100"]+=occerence1
        elif 100<float(height)<125:
            mode_data["100-125"]+=occerence1
        elif 125<float(height)<150:
            mode_data["125-150"]+=occerence1
    for weight,occerence2 in data2.items():
        if 50<float(weight)<75:
            mode_data["50-75"]+=occerence2
        elif 75<float(weight)<100:
            mode_data["75-100"]+=occerence2
        elif 100<float(weight)<125:
            mode_data["100-125"]+=occerence2
        elif 125<float(weight)<150:
            mode_data["125-150"]+=occerence2
    mode_range_height,mode_occerrance_height,mode_range_weight,mode_occerrance_weight=0,0,0,0
    for mode_height,mode_occerance in mode_data.items():
        if mode_occerance>mode_occerrance_height:
            mode_range_height,mode_occerrance_height=[int(mode_height.split("-")[0]),int(mode_height.split("-")[1])],mode_occerance
    for mode_weight,mode_occeranceWeight in mode_data.items():
        if mode_occeranceWeight>mode_occerrance_weight:
            mode_range_weight,mode_occerrance_weight=[int(mode_weight.split("-")[0]),int(mode_weight.split("-")[1])],mode_occeranceWeight
    mode1=float((mode_range_height[0]+mode_range_weight[1])/2)
    mode2=float((mode_range_weight[0]+mode_range_weight[1]/2))
    print("mode of height-- "+str(mode1))
    print("mode of weight-- "+str(mode2))
modes()  