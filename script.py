import webbrowser, time
print("Enter the filename\n")
file_name = input()
f = open(file_name,'r', encoding='utf-8')
# os_type = platform.system()
# # if os_type == 'Windows':
# #     webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")
# # elif os_type == 'Linux':
sites = 0
websites = []
for line in f:
    sites += 1
    tmp = line.split()
    link = tmp[-1]
    fl = link.find("www")
    if fl == -1:
        fl = link.find("http")
    if fl == -1:
        link = "http://" + link
    websites.append(link)
print("No of lines in the file is: {0}\n".format(sites))
print("Now, keep entering the range of line number for each site you want to open (press e to exit): \n")
while True:
    start = input()
    if start == 'e':
        print("Terminating...\n")
        time.sleep(1)
        break
    try:
        start = int(start)
    except ValueError:
        print("Enter valid integer!!\n")
        continue
    end = input()
    try:
        end = int(end)
    except ValueError:
        print("Enter valid integer!!\n")
        continue
    if start == 0:
        print("Using 1 based indexing, enter again\n")
        continue
    elif end > sites:
        print("Input exceeds the line limit, opening till end only\n")
        end = sites
    elif end - start > 30:
        print("Trust me, you don't wanna open so many links at once, it may break your system, try again\n")
        continue
    print("Opening links...\n")
    time.sleep(2)
    for i in range(start-1, end):
        webbrowser.open(websites[i])