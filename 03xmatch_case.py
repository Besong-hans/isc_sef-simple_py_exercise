status_code = 404

match status_code:
    case 200:
      print("OK: The request was successful.")
    
    case 301:
      print("Moved Permanently: The resource has been permanently moved.")
    
    case 404:
      print("Not Found: The requested resource was not found.")
    
    case 500:
      print("Internal Server Error: The server encountered an error.")
    
    case _:
      print(f"Unknown status code: {status_code}")
      
      
      