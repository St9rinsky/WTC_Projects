#ask user for file name
prompt = input("File name: ")

# edit file name (cases separating the fname and extention)
file_name = prompt.lower().split(".")

# extract the extention
extention = file_name[-1]

match extention:
    case "gif":
        print("image/gif")

    case "jpg":
        print("image/jpeg")

    case "jpeg":
        print("image/jped")

    case "png":
        print("image/png")

    case "pdf":
        print("application/pdf")

    case "txt":
        print("document/txt")

    case "zip":
        print("zipped/zip")
        
    case _:
        print("application/octet-stream")
