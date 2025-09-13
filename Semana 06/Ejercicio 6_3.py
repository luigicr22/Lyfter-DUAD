def sum_list (list_to_sum):
    total_sum = 0
    for number in list_to_sum:
        total_sum += number
    return total_sum

def main():
    list_to_sum = [4, 6, 2, 29]
    print (sum_list(list_to_sum))


if __name__ == "__main__":
  main()