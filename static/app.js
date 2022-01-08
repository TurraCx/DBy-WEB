const vm = new Vue({
    el: '#vm',
    delimiters: ['[[', ']]'],
    data: {
        api_key: "",
        search: "",
        torrents: []
    },
    methods: {
        searchTorrents() {
            if (this.api_key.length > 0) {
                axios.post('/search', { search: this.search, api_key: this.api_key }, { headers: { 'Content-Type': 'application/json' } }).then(resp => {
                    this.torrents = resp.data;
                });
            }
        },
        downloadTorrent(item) {
            axios.post('/download', { item: item }, { headers: { 'Content-Type': 'application/json' } }).then(resp => {
                window.open(resp.data.download_link)
            });
        },
        generateMagnet(item) {
            axios.post('/magnet', { item: item }, { headers: { 'Content-Type': 'application/json' } }).then(resp => {
                window.open(resp.data)
            });
        }
    }
})