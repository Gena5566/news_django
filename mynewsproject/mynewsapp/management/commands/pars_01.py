from bs4 import BeautifulSoup
import requests
import asyncio
import aiohttp

async def my_coroutine():
    url = "https://habr.com/ru/hub/programming"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    pagination_block = soup.find("div", class_="tm-pagination__pages")
    pages_count = pagination_block.find_all("a", class_="tm-pagination__page")[-1].text.strip()
    print(f"category: {url} | pages: {pages_count}")

    for page in range(int(pages_count)):
        page_next_count = page+1
        page_next = f"{url}/articles/page{page_next_count}"
        print(page_next)

        response = requests.get(page_next)
        if response.status_code == 200:
            print(response)

            soup = BeautifulSoup(response.text, 'html.parser')
            news_items_page = soup.find_all(class_='tm-title tm-title_h2')
            print(news_items_page)


            for item in news_items_page:
                title = item.find(class_='tm-title__link').text.strip()
                link = item.find(class_='tm-title__link')['href']

                print(f"https://habr.com{link}")
                print(title)
                print()


    await asyncio.sleep(1)
    print('End')





asyncio.run(my_coroutine())

