def count_words (path):
    list_words= []
    
    try:
        with open (path) as file:
            print("FILE:\n")
            print(file.read())
            file.seek(0)
            for line in file.readlines():
                list_words.append(line.split(" "))
    
        count = 0
        for index in range(len(list_words)):
            count += len(list_words[index-1]) 

        print (f"\nEste archivo contiene {count} palabras")

    except FileNotFoundError:
        print("No se encuentra archivo para cargar")
        exit()

def main ():
    count_words ("text_count.txt")


if __name__=="__main__":
    main()