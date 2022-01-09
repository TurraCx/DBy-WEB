const vm = new Vue({
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: {
        api_key: "",
        rss_key: "",
        search: "",
        torrents: [],
        mirrors: [
            {
                name: 'DanishBytes.club',
                link: 'https://danishbytes.club'
            }
        ],
        news: "Ingenting"
    },
    mounted() {
        axios.get('/mirrors').then(resp => {
            this.mirrors = resp.data;
        });
    },
    methods: {
        searchTorrents() {
            if (this.api_key.length > 0) {
                axios.post('/search', { search: this.search, api_key: this.api_key }, { headers: { 'Content-Type': 'application/json' } }).then(resp => {
                    this.torrents = resp.data.torrents;
                    this.rss_key = resp.data.rsskey;
                });
            }
        },
        downloadTorrent(item) {
            window.open(this.mirrors[0].link+"/torrent/download/"+item.id+"."+this.rss_key);
        },
        generateMagnet(item) {
            window.open("magnet:?dn="+item.name+"&xt=urn:btih:"+item.info_hash+"&as="+this.mirrors[0].link+"/torrent/download/"+item.id+"."+this.rss_key+"&xl="+item.size+"&tr=https://danishbytes.club/announce/e064ba0c35d252338572fd7720448cc5&tr=https://danishbytes.org/announce/e064ba0c35d252338572fd7720448cc5&tr=https://danishbytes2.org/announce/e064ba0c35d252338572fd7720448cc5&tr=https://danishbytes.art/announce/e064ba0c35d252338572fd7720448cc5");
        }
    }
})