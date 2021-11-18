import my_toolbox as mtb
import matplotlib.pyplot as plt

f = open("stock_data_1.txt", 'r')

def my_test():      
    print("my tool")
    mtb.clear_screen(30)
    data = mtb.get_data_list()
   
    data2 = mtb.closingprice() #Test in progress
   

    xbar = mtb.mean(data)
    med = mtb.median(data)
    dif = mtb.updown(data)
    gl = mtb.gainloss(data)
    dc = mtb.dateconverter()
   
   
    dd = mtb.dateconverter2()
    xbar2 = mtb.mean(data2)
    med2 = mtb.median2(data2)
    dif2 = mtb.updown(data2)
    gl2 = mtb.gainloss(data2)
   
   
   
    num_range= range(0,len(gl))
    num_range2= range(0,len(dif))
    num_range3= range(0,len(xbar))
    num_range4= range(0,len(med))
    num_range5= range(0,len(gl2))
    num_range6= range(0,len(dif2))
    num_range7= range(0,len(xbar2))
    num_range8= range(0,len(med2))
   
    fig,axs = plt.subplots(4)
    fig.suptitle('Vertically stacked subplots')
    axs[0].plot(list(num_range),gl)
    axs[1].plot(list(num_range2),dif)
    axs[2].plot(list(num_range3),xbar)
    axs[3].plot(list(num_range4),med)
   
    fig,axs = plt.subplots(4)
    fig.suptitle('Vertically stacked subplots')
    axs[0].plot(list(num_range5),gl2)
    axs[1].plot(list(num_range6),dif2)
    axs[2].plot(list(num_range7),xbar2)
    axs[3].plot(list(num_range8),med2)    
   
   
   
    #1 Range list
    num_range= range(0,len(gl))
    plt.scatter(list(num_range),gl)
    #2 Range list
    num_range2= range(0,len(dif))
    plt.scatter(list(num_range2),dif)

    #3 Range list
    num_range3= range(0,len(xbar))
    plt.scatter(list(num_range3),xbar)
    #4 Range list
    num_range4= range(0,len(med))
    plt.scatter(list(num_range4),med)
   
   
    #1 Range list
    num_range5= range(0,len(gl2))
    plt.scatter(list(num_range5),gl2)
    #2 Range list
    num_range6= range(0,len(dif2))
    plt.scatter(list(num_range6),dif2)
    #3 Range list
    num_range7= range(0,len(xbar2))
    plt.scatter(list(num_range7),xbar2)
    #4 Range list
    num_range8= range(0,len(med2))
    plt.scatter(list(num_range8),med2)


    import csv
    from itertools import zip_longest

    d = [dc,xbar,med,dif,gl]
    export_data = zip_longest(*d, fillvalue = '')
    with open('outputfile1.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("Dates", "Mean","Median","Diference", "Growth Rate"))
        wr.writerows(export_data)
        myfile.close()
   
    d2 = [dd,xbar2,med2,dif2,gl2]
    export_data = zip_longest(*d2, fillvalue = '')
    with open('outputfile2.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("Dates", "Mean","Median","Diference", "Growth Rate"))
        wr.writerows(export_data)
        myfile.close()
       
       
       
def main():
    my_test()
   
if __name__ == '__main__' :
    main()
   