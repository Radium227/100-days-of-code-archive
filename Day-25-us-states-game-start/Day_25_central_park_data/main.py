# # with open("weather_data.csv","r") as file:
# #      data=file.readlines()
# #      # print(data)
# # temp=[]
# # n=0
# # import csv
# # with open("weather_data.csv") as file:
# #     data=csv.reader(file)
# #     # print(data)
# #     for row in data:
# #         # print(row)
# #         n+=1
# #         if n>0:
# #             for n in data:
# #                 x=int(n[1])
# #                 temp.append(x)
# #
# # print(temp)
# import pandas
# total=0
# data=pandas.read_csv("weather_data.csv")
# max=data["temp"].max()
# # # for n in temp_list :
# # #     total+=n
# # #
# # #
# # # average=total/len(temp_list)
# # # print(f"The average is {average}")
# # #
# # # # print(data["condition"])
# # # # data_dict=data.to_dict()
# # # # print(data_dict)
# # monday=data[data.day== "Monday"]
# celsius=(monday.temp[0])*9/5+32
# print(celsius)
import pandas
data=pandas.read_csv("park_data.csv")
Gray=data[data["Primary Fur Color"]=="Gray"]
num_gray=len(Gray)
print(num_gray)

Cinnamon=data[data["Primary Fur Color"]=="Cinnamon"]
num_cinnamon=len(Cinnamon)
print(num_cinnamon)

Black=data[data["Primary Fur Color"]=="Black"]
num_black=len(Black)
print(num_black)

data_dict={

    "Fur Color": ["Gray____", "Cinnamon", "Black"],
    "Count" : [num_gray,num_cinnamon,num_black]
}
data=pandas.DataFrame(data_dict)
data.to_csv("fur_count.csv")