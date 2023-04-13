import requests
from bs4 import BeautifulSoup

filters = ["Apple Music","Spotify","Deezer","YouTube Music","music.apple.com", "open.spotify.com", "deezer.com", "music.youtube.com"]

query = input("Enter search query: ")
has_results = False
for page_number in range(1, 3):
    url = f"https://www.google.com/search?q={query}&start={(page_number-1)*10}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    results = soup.find_all('div', class_='tF2Cxc')

    if not results:
        print(f"No results found, double check your search.")
        exit()
    else:
        all_filtered = True
        for result in results:
            heading = result.find('h3').text
            link = result.find('a')['href']
            skip = False
            for result_filter in filters:
                if result_filter in heading or result_filter in link:
                    skip = True
                    break
            if not skip:
                all_filtered = False
                print(f"{heading}: {link}")
        if all_filtered and page_number == 1:
            print("No search results found on the first page, searching the second page...")
        elif all_filtered == False:
            exit()
        elif all_filtered == True and page_number == 2:
            print("No search results found on the first two pages, try rewording your search.")
            exit()