#get user output
user_input = input("Enter a filename")
filename = user_input.lower()

#if gif or png or jpg or jpeg, print"image/type"
if ".gif" in filename:
    print("image/gif")
elif ".png" in filename:
    print("image/png")
elif ".jpg" in filename:
    print("image/jpeg")
elif ".jpeg" in filename:
    print("image/jpeg")
#if pdf or zip, print "application/type"
elif ".zip" in filename:
    print("application/zip")
elif ".pdf" in filename:
    print("application/pdf")
#if text, print "text/plain"
elif ".txt" in filename:
    print("text/plain")
#otherwise, print "application/octet-stream"
else:
    print("application/octet-stream")
