#  1. WAP to create a CSV file from a list data and retrive that element  containing book number,
#     book name and price and retrive these data and print  in console

# import the csv module
import csv

# create a list 
book_list=[[101,"python programming",450],[102,"c programming",470],[103,"Data structure",350]]

# open csv file in write mode 'w'
with open("book.csv",'w') as myfile:
    # write the list data into the csv file using csv.writer()
     w_in_csv =csv.writer(myfile)
     w_in_csv.writerow(book_list)
      
# file automaticlly close the file because we use 'with open()' 

# now open file for read data csv.reader() 
with open("book.csv",'r') as myfile:
    # write the list data into the csv file using csv.writer()
     read_file =csv.reader(myfile)
     print(read_file)
     for row in read_file:
        print(row)    
