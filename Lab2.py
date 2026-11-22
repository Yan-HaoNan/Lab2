def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    numbers = input()
    x=numbers.split(",")
    results=[]
    for value in x:
        results.append(float(value))
    return results

def calc_average(temperature):
    total =0
    count =0
    for temp in temperature:
        total = total+temp
        count+=1
    average = total/count
    return average


def find_min_max(temperature):
    result=[]
    x=min(temperature)
    y=max(temperature)
    result.append(int(x))
    result.append(int(y))
    return result

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")


def main():
    display_main_menu()
    num_list=get_user_input()
    ave= calc_average(num_list)
    min_max=find_min_max(num_list)
    print(ave)
    print(min_max)

if __name__=="__main__":
    main()