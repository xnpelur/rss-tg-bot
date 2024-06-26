from bs4 import BeautifulSoup


class Article:
    def __init__(self, feed_entry) -> None:
        self.title: str = feed_entry.title.strip()
        self.description, self.image_url = self.__parse_description(feed_entry.description) 
        self.link: str = feed_entry.link 
    
    
    def __parse_description(self, description):
        paragraphs = []
        image_url = ""

        soup = BeautifulSoup(description, features="html.parser")
        img_tag = soup.find('img')
        if img_tag and img_tag['src']:
            image_url = img_tag['src']
        p_tags = soup.find_all('p')

        for tag in p_tags:
            paragraphs.append(str(tag.text))

        if len(paragraphs) == 0:
            paragraphs.append(str(soup.text))

        return self.__normalize_description("\n\n".join(paragraphs)), image_url
    

    def __normalize_description(self, description):
        description = description.strip()
        max_length = 980 - len(self.title)

        if len(description) <= max_length:
            return description

        words = []
        currentLength = 0
        for word in description.split():
            if currentLength + len(word) + 1 > max_length - 3:
                return " ".join(words) + "..."
            words.append(word)
            currentLength += len(word) + 1