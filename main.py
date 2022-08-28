import requests

TOKEN = ' '

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)}



    def uploa_d(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file(self, file_path, filename):
        response_href = self.uploa_d(file_path=file_path)
        url = response_href.get('href', '')
        respons = requests.put(url, data=open(filename, 'rb'))
        respons.raise_for_status()
        if respons.status_code == 201:
            print('success')


if __name__ == '__main__':
    ya = YaUploader(token=TOKEN)
    ya.upload_file(file_path='/file.txt', filename='file.txt')



url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'
super_hero = ['Hulk', 'Captain America', 'Thanos']

def intel_ligence():
    dict_int = {}
    for hero in super_hero:
        hero_dict = requests.get(url + hero).json()['results']
        dict_int.setdefault(hero, hero_dict[0]['powerstats']['intelligence'])
        return print(f"Самый умный супергерой: {max(dict_int)}")


if __name__=='__main__':
    intel_ligence()


