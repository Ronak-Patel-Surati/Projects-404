#use match
file = input("Enter your File name :").lower()
file = file.strip()
#matching pun not intended fuck match, it does notsupoort pattern matching
#use ctrl + f on python.org



if file.endswith(".jpg") or file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".PDF"):
    print("application/pdf")
elif file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".txt"):
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
