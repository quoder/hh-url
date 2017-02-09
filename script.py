from bs4 import BeautifulSoup
import webbrowser, time, urllib
url = "https://github.com/HackathonHackers/personal-sites/blob/master/README.md"
r = urllib.request.urlopen(url).read()
soup = BeautifulSoup(r, "html5lib")
bs4obj= soup.select("#readme ul > li > a")
sites = 0
websites = []
for links in bs4obj:
    sites += 1
    websites.append(links.get("href"))
print("Total Number of Urls: {0}\n".format(sites))
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