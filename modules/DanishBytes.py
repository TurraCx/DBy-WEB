import requests

class DanishBytes():
    def __init__(self, session=None, api_key=None):
        self.s = requests.Session()
        if session != None:
            self.session = session
            self.s.cookies.update({"db_session": self.session})
        if api_key != None:
            self.api_key = api_key
        self.s.headers.update({"User-Agent": "DenGladeFilmMand x DBy Film Søger Script | Fork af Turra"})
        pass
    
    def set_api(self, api_key):
        self.api_key = api_key
        return

    def find_movie(self, search_name):
        r = self.s.get(f"https://danishbytes2.org/api/torrents/filter?search={search_name}&api_token={self.api_key}")
        if len(r.json()) > 0:
            return r.json()
        r = self.s.get(f"https://danishbytes2.org/api/torrents/filter?imdb={search_name}&api_token={self.api_key}")
        if len(r.json()) > 0:
            return r.json()
        r = self.s.get(f"https://danishbytes2.org/api/torrents/filter?tvdb={search_name}&api_token={self.api_key}")
        if len(r.json()) > 0:
            return r.json()
        r = self.s.get(f"https://danishbytes2.org/api/torrents/filter?tmdb={search_name}&api_token={self.api_key}")
        if len(r.json()) > 0:
            return r.json()
        return None
    
    def get_torrent(self, id):
        return self.s.get(f"https://danishbytes2.org/api/torrents/{id}?api_token={self.api_key}").json()

    def download_torrent(self, link):
        r = self.s.get(link)
        torrent = b''
        for data in r.iter_content(chunk_size=4096):
            torrent += data
        return torrent
    
    def check_mirrors(self):
        working = []
        for mirror in [
            {"name": "DanishBytes.club", "link":"https://danishbytes.club"},
            {"name": "DanishBytes2.club", "link":"https://danishbytes2.club"},
            {"name": "DanishBytes.org", "link":"https://danishbytes.org"},
            {"name": "DanishBytes2.org", "link":"https://danishbytes2.org"},
            {"name": "DanishBytes.art", "link":"https://danishbytes.art"},
            {"name": "DanishBytes2.art", "link":"https://danishbytes2.art"}
        ]:
            try:
                r = self.s.get(mirror['link'], timeout=2.5)
                if r.status_code == 200 and 'db_session' in r.cookies:
                    return [mirror]
            except Exception:
                continue
        return working