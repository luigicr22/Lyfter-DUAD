def open_file_per_line(path):
    songs = []
    try: 
        
        with open(path) as file:
            print("OLD FILE")
            print(file.read())
            file.seek(0)
            for line in file.readlines():
                songs.append(line)
        
        songs[len(songs)-1] += "\n"
        songs.sort()  
        
        for song in songs:
            with open("new_file_songs.txt", "a", encoding='utf-8') as new_file:
                new_file.write(song)
        
        return "new_file_songs.txt"
    
    except FileNotFoundError:
        print("No se encuentra archivo para cargar")
        exit()


def main ():
    new_path = open_file_per_line('file_songs.txt')
        
    print("\nNEW FILE")
    with open(new_path) as file:
        print(file.read())
    

if __name__=="__main__":
    main()