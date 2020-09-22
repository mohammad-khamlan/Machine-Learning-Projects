import requests
import argparse
import keys
api_key = 'AIzaSyD0W6DrQKKl6k7kWCTJSvRX0M4ufMnpiuQ'
cse_id = "6b4614b0ca7d452d8"



def search():
    """
    This function reads the parameters from the console
    :param: none
    :return: the links to save the results in the JSON file
    """
    #Search on url by query and stored it in links
    url = f"https://www.googleapis.com/customsearch/v1?key={keys.api_key}&cx={keys.cse_id}&q={keys.query}"
    result = requests.get(url).json()
    links = result.get("items")
    return links


def write_on_json(links):
        """
    This function create a JSON file then store data in it
    :params: links
    :return: none
    """
    #Stored the results in JSON file
    with open('result.text', 'w', newline='') as file:
        for i in range(len(links)):
            file.write('URL: ' + links[i].get('link') + '\n')
            file.write('\n' + '-----------------------------------------------------------' + '\n')

def main():
    #Creating argument parser object
    parser = argparse.ArgumentParser(description='Search Engine API')
    #Filling argument parser with information about program 
    parser.add_argument('query', type = str, help = 'search engine')
    args = parser.parse_args()
    links = search()
    write_on_json(links)


if __name__ == '__main__':
    main()