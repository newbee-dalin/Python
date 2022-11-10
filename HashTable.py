import csv
nyc_weather = {}
with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(",")
        date = tokens[0]
        temperature = tokens[1]
        nyc_weather[date] = temperature

#print("nyc temperature is :", nyc_weather)

#3
output = {}
with open("poem.txt","r",encoding='utf-8') as p:
    for word in p:
        x = word.split(" ")
        for a in x:
            a = a.replace('\n','')
            if a in output:
                output[a] += 1
            else:
                output[a] = 1
print(output)




#i
sum_temp_weekly = 0
nyc_weather.pop("date")
for x in nyc_weather:
    if x == "Jan 8":
        break
    sum_temp_weekly += int(nyc_weather[x])
ave_temp = sum_temp_weekly / 7
print("the first weekl temperature is: ", ave_temp)

#ii
max_temp = []
for x in nyc_weather:
    temp = int(nyc_weather[x])
    if max_temp == []:
        max_temp.append(temp)
    elif temp > max_temp[0]:
        max_temp.pop()
        max_temp.append(temp)
print("max temperature is:",max_temp)

#2-i
temp = "Jan 9"
print("Temperature of Jan 9 is :",nyc_weather[temp])
print("Temperature of Jan 4 is :",nyc_weather["Jan 4"])
