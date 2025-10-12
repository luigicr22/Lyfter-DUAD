def count_cases (string_to_count):
    count_upper = 0
    count_lower = 0
    for char in string_to_count:
        if str(char).isupper():
            count_upper += 1
        elif str(char).islower():
            count_lower += 1
    return(f"There’s {count_upper} upper cases and {count_lower} lower cases")



def main():
    original_string = "I love Nación Sushi"
    print(count_cases(original_string))


if __name__ == "__main__":
  main()
