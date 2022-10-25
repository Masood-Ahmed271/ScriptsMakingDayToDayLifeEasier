# creating a WorkLog File
import os
import re

# Global Variables
PER_HOUR_RATE = 70     # random number
PATH_TO_FILE = "./Work_Log_File.txt"


'''
Description: This is a function that get's the work details and number of hours worked from the user
Parameters:  is_work_log --> Representing whether to input work or not
             work_data --> Details of the work stored in a list
             time_data_in_hours --> Number of hours spent per work
Return:      work_data --> Details of the work inserted 
             time_data_in_hours --> Number of hours spent

'''
def inputWorkLog(is_work_log,work_data,time_data_in_hours):
    if is_work_log == 1:
        while is_work_log == 1:
            data = input("Enter details of the work done: ")
            hours_spent = float(input("Enter numbers of hours work done: "))
            work_data.append(data)
            time_data_in_hours.append(hours_spent)
            is_work_log = int(input('Do You wanna input work detail logs, if yes, then enter 1 else enter 2: '))
    elif is_work_log == 'q':
        print("See you next time, have a happy day! ")
    return work_data, time_data_in_hours

'''
This is where the program starts
'''
if __name__ == "__main__":

    # CHECKING IF THIS FILE EXISTS OR NOT
    isExist = os.path.exists(PATH_TO_FILE)

    if isExist == False:
        work_log_file_txt = open("Work_Log_File.txt", "a+")
        
        # Taking input about what work has been done
        is_work_log = int(input('Do You wanna input work detail logs, if yes, then enter 1 else enter q to quite: '))
        work_data,time_data_in_hours = [],[]
        work_data, time_data_in_hours = inputWorkLog(is_work_log,work_data,time_data_in_hours)

        total_amount,total_hours = 0,0

        for i in range(len(work_data)):
            data_to_store = str(work_data[i]) + " | " + str(time_data_in_hours[i]) + " hours spent. \n"
            total_amount+=(time_data_in_hours[i]*PER_HOUR_RATE)
            total_hours+= time_data_in_hours[i]
            work_log_file_txt.write(data_to_store)

        total_hours_done = "Total Number of Hours Done = " + str(total_hours) + " hours \n"
        total_amount_earned = "Amount to be paid (hours x 70hkd/hour) = " + str(total_amount) + " HKD. \n"
        work_log_file_txt.write(total_hours_done)
        work_log_file_txt.write(total_amount_earned)
        work_log_file_txt.write("Thank You!")
        work_log_file_txt.close()

    else:
        work_log_file_txt = open("Work_Log_File.txt", "r+")
        lines = work_log_file_txt.readlines()
        if len(lines) > 0:
            previous_total_hours = float(re.findall(r"[-+]?(?:\d*\.\d+|\d+)", lines[-3])[0])
            previous_total_amount = float(re.findall(r"[-+]?(?:\d*\.\d+|\d+)", lines[-2])[-1])
            lines_to_be_added = lines[:-3]
            is_work_log = int(input('Do You wanna input work detail logs, if yes, then enter 1 else enter q to quite: '))
            work_data,time_data_in_hours = [],[]

            work_data, time_data_in_hours = inputWorkLog(is_work_log,work_data,time_data_in_hours)

            for i in range(len(work_data)):
                data_to_store = str(work_data[i]) + " | " + str(time_data_in_hours[i]) + " hours spent. \n"
                lines_to_be_added.append(data_to_store)
                previous_total_amount+=(time_data_in_hours[i]*PER_HOUR_RATE)
                previous_total_hours+= time_data_in_hours[i]
            
            total_hours_done = "Total Number of Hours Done = " + str(previous_total_hours) + " hours \n"
            total_amount_earned = "Amount to be paid (hours x 70hkd/hour) = " + str(previous_total_amount) + " HKD. \n"
            lines_to_be_added.append(total_hours_done)
            lines_to_be_added.append(total_amount_earned)
            lines_to_be_added.append("Thank You!")
        work_log_file_txt.close()
        work_log_file_txt = open("Work_Log_File.txt", "w+")
        for i in range(len(lines_to_be_added)):
            work_log_file_txt.write(lines_to_be_added[i])
        work_log_file_txt.close()
