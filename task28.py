extensions = ['txt', 'jpg', 'gif', 'html']
fileName = input("შეიყვანეთ ფაილის სახელი: ")
fileExtension = fileName.split('.')[1]

print('Yes' if extensions.count(fileExtension) > 0 else 'No')
