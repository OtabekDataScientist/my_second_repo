def clear_screen(x):
    print("\n" * x)
    print('screen cleared')
   
def dateconverter():    
    import datetime

    with open('stock_data_1.txt', newline='') as f:
        lines = f.readlines()
        lines = lines[1:]  # Removing header
        lines

    dates = []
    newDate = []

    for line in lines:
        dates.append(line.split(",")[0])
        timestamp = datetime.datetime.strptime("1900/01/03", '%Y/%m/%d')

    for index,val in enumerate(dates):
        newDate.append(timestamp.strftime('%Y-%m-%d'))
        timestamp += datetime.timedelta(days=1)

    return newDate
#for date in dates:
#    print(date)
#f.close()
   

def median2(data2):
    import statistics
    data2 = closingprice()
    mytoollist2 = []
    medlist =[]
    for median in data2:
        mytoollist2.append(median)
        median = statistics.median(mytoollist2)
        medlist.append(median)
    print(medlist)
    print(mytoollist2)
    print(median)
    return mytoollist2



def dateconverter2():    
    from datetime import datetime
    import re
    f = open("Stock_Data_2_v2.csv", 'r')
    content = f.read()
    pattern = (r'(\d+/\d+/\d+)')
    dates = re.findall(pattern, content)
    dates = [datetime.strptime(date, "%m/%d/%Y").date() for date in dates]
    converted_dates = [str(date) for date in dates]
#    lst_rev=[]  --> Reverse list list (Prototype)
#    lst_rev.append(converted_dates[::-1]) Reversing list
    return converted_dates #lst_rev --> return reversed list
   
def closingprice():
    import pandas as pd
    df = pd.read_csv("Stock_Data_2_v2.csv")
    close = df.Close.to_list()
    return close
   
def get_data_list():
    import re
    f = open("stock_data_1.txt", 'r')
    # extract the file's content
    content = f.read()
    # a regular expression pattern to match dates
    pattern = "\d+\.\d+"
    # find all the strings that match the pattern
    price = re.findall(pattern, content)
    #sclist = [int(content) for content in dates]
    #print([float(x) for x in price])
    nums = [float(x) for x in price]      
    return nums  


def updown(data_list):
    index = 0
    index2 = 1
    mytoollist3 = [0]
    for dif in range(len(data_list)-1):
        dif = data_list[index2] - data_list[index]
        index += 1
        index2 += 1
        mytoollist3.append(dif)
        my_formatted_list = [ '%.2f' % elem for elem in mytoollist3 ]
        my_formatted_list = list(map(float, my_formatted_list))
    print(my_formatted_list)
    return my_formatted_list
   
   
def mean(data_list):
    mytoollist = []
    ko = 0.0
    sum = 0.0
    for num in data_list:
        ko = ko + 1
        sum = sum + num
        summa = sum / ko
        mytoollist.append(summa)
        final = sum / len(data_list)
    print(mytoollist)  
    return mytoollist
   

   
def median(data_list):
    import statistics
    mytoollist2 = []
    medlist =[]
    for median in data_list:
        n = len(data_list)
        if n % 2 == 0:
            median1 = data_list[n//2]
            median2 = data_list[n//2 - 1]
            mediann = (median1 + median2)/2
        else:
            median = data_list[n//2]
        mytoollist2.append(median)
        median = statistics.median(mytoollist2)
        medlist.append(median)
    print(medlist)
    return medlist
   
   
         


def gainloss(data_list):
    index = 0
    index2 = 1
    mytoollist3 = [0]
    for dif in range(len(data_list)-1):
        dif = ((data_list[index2] - data_list[index])/data_list[index2])*100
        index += 1
        index2 += 1
        mytoollist3.append(dif)
        my_formatted_list = [ '%.2f' % elem for elem in mytoollist3 ]
        my_formatted_list = list(map(float, my_formatted_list))
    print(my_formatted_list)
    return my_formatted_list





def main():
    print('This is my_tools module called')
    data = get_data_list()
    result = median(data)
    print("Median: ", result)
       
if __name__ == '__main__' :
    main()
