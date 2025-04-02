#simple music player to repeat automatically


if command == 'r':
    
            repeat = not repeat
            
            status = "ON" if repeat else "OFF"
            
            print(f"Repeat is now {status}")
            
elif command == 'q':
    
            print("Exiting music player.")
            
         break
        
while repeat:
            
            print("Playing music...")
            
            time.sleep(2)  # Simulates music playing for a short period
            
            command = input("Enter command (r to toggle repeat, q to quit): ").strip().lower()
            
            if command == 'r':
                
                repeat = not repeat
                
                print("Repeat is now OFF")
                
            elif command == 'q':
                
                print("Exiting music player.")
                
                return

if __name__ == "__main__":
    
    music_player()
