def count_vowels (string_original):
    vowels = "aeiouAEIOU"
    count_vowels = 0
    for char in string_original:
        if char in vowels:
            count_vowels += 1
    return count_vowels


def main():
    print(count_vowels ("HolA mundO"))


if __name__ == "__main__":
    main()
