# with open("log.txt", "a") as f:
#   f.write("Program run successfully\n")
  
with open("log.txt","r") as f:
  log = f.read()
  print(f"Logs in the file are: \n{log}")  
  
  