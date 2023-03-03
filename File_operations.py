# # File operations: Operations that we can perform on the files..

# # To Perform anything you have to open the file first..

# # opening the file can be done in 2 ways..


# # 3 modes
#     # reading -r
#     # writing - w
#     # appending - a

# # 1st way
# # open(filepath,mode)

# # 2nd Way
# """
# with open(filepath,mode) as file_data:
#     statements
# """

# # file_data = open('dialogues.txt','r')

# # print(file_data)

# # print(file_data.closed)

# # file_data.close() # This will close the opened file..

# # print(file_data.closed)


# # with open('dialogues.txt','r') as file_data:
# #     pass

# # print(file_data.closed)

# # with will automatically close the file once the cursor comes outside of with block.

# # reading -- 
#     # read() -- will read the complete content in the file at once..
#     # readline() -- It will read one line at a time..
#     # readlines() -- It will read the complete content but line by line format..


# # with open('dialogues.txt','r') as file_data:
# #     # print(file_data.read())
# #     # print(file_data.readline())
# #     # print(file_data.readline())
# #     data = file_data.readlines()[1:]
# #     for ele in data:
# #         print(ele)


# # writing(w): This will overwrite the data in the file..
#     # write()
#     # writelines()

# # if file is not present it will create the file during writing and appending mode.
# # with open('C:/Users/reddy/OneDrive/Desktop/dialogues.txt','w') as file_data:
# #     # file_data.write('Seat kadukada assembly gate kuda takanivvavu\n')
# #     # file_data.write('Narikakoddi neku alupu vastadi emo naku oopu vastadi.')
# #     file_data.writelines(['Seat kadukada assembly gate kuda takanivvavu\n', 'Narikakoddi neku alupu vastadi emo naku oopu vastadi.\n', 'Breaks leni buldozer ni tokkipadestha\n'])



# # appending(a) : This is for adding the content to the previous content..
#     # write ()
#     # writelines()
# # with open('C:/Users/reddy/OneDrive/Desktop/dialogues.txt','a') as file_data:
# #     file_data.write('Sarvejana sukinobavanthu okka veedu tappa.\n')
# #     # file_data.write('Narikakoddi neku alupu vastadi emo naku oopu vastadi.')
# #     file_data.writelines(['Seat kadukada assembly gate kuda takanivvavu\n', 'Narikakoddi neku alupu vastadi emo naku oopu vastadi.\n', 'Breaks leni buldozer ni tokkipadestha\n']) 

# # first.txt
#     # a=5
#     # b=6
# # second.txt
#     # c=a+b 

# # third.txt
#     # c=???

# # File Operations on CSV files:

# # CSV - Comma Seperated Values

# # csv -- Its for working on csv files..

# import csv

# # reading of csv..

# # with open('first_cls.csv','r') as file_data:
# #     # print(file_data)
# #     # print(file_data.read())
# #     csv_data = csv.reader(file_data)
# #     # print(list(csv_data))
# #     # next(csv_data)
# #     # print(list(csv_data)[2:5])
# #     # for ele in csv_data:
# #     #     if ele[1] == 'chiranjeevi':
# #     #         print(ele)

# # writing 

#     # writerow
#     # writerows
# # with open('second_cls.csv','w',newline='') as file_data:
# #     csv_write_data = csv.writer(file_data)
#     # csv_write_data.writerow(['movie_name','actor_name'])
#     # csv_write_data.writerow(['indra','chiru'])
#     # csv_write_data.writerows([['samarasimhareddy','balakrishna'],['kushi','pawankalyan'],['okkadu','maheshbabu']])


# # appending --  will add the new row data to the previous rows in the file..


# with open('second_cls.csv','a',newline='') as file_data:
#     csv_write_data = csv.writer(file_data)
#     csv_write_data.writerow(['indra','chiru'])

# json -- javascript object notation..

# [{
#     "name":"ramaesh",
#     "address":"Hyderabad",
#     "email":"ramesh@gmail.com",
#     "mobile" : ["8398298829","9474848444"]
# },
# {
#     "name":"suresh",
#     "address":"Vizag",
#     "email":"suresh@gmail.com",
#     "mobile" : ["9778377348","54784873873"]
# }]

import json

# sample_data = '[{"name":"ramesh","email":"ramesh@gmail.com","mobile":["73782287872","732778782"]}]'

# print(type(sample_data))

# data = json.loads(sample_data)

# print(data)
# print(type(data))

data = open('sample_data.json')

new_Data = json.load(data)

# print(new_Data)

# print(type(new_Data))

final_data = []
for ele in new_Data:
    # print(ele)
    if "e" in ele['first_name']:
        final_data.append(ele)

# print(final_data)

# with open('sample_new.json','w') as file_data:
#     json.dump(final_data,file_data,indent=4)
#     print(dir(file_data))
# print((json.dumps(final_data,indent=4)))


# print(help(json))