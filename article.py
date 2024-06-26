from bs4 import BeautifulSoup

class Article:
    def __init__(self, feed_entry) -> None:
        self.title: str = feed_entry.title 
        self.description: str = self.__parse_description(feed_entry.description) 
        self.link: str = feed_entry.link 
    
    def __parse_description(self, description):
        paragraphs = []
        soup = BeautifulSoup(description, features="html.parser")
        img_tags = soup.find_all('img')
        p_tags = soup.find_all('p')

        for tag in p_tags:
            paragraphs.append(str(tag.text))

        if len(paragraphs) == 0:
            paragraphs.append(str(soup.text))

        return "\n\n".join(paragraphs)