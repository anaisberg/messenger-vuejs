const Msg = Vue.component('msg', {
    props: ['author', 'message'],
    template: '<div class="msg"><h4><em>{{ author }}</em></h4><p>{{ message }}</p></div>'
});

const app = new Vue({
    el: '#app',
    data: {
        newText: [],
        newAuthor: '',
        newTime: '',
        newMessage: '',
        newTexts: [],
        messages: [],
    },
    created: function() {
        var self = this;
        setInterval(async function() {
            const res = await fetch('/test/pull');
            const data = await res.json();
            self.messages = [];
            data.forEach(function (r, i) {
                self.messages.push(['Theo',r.content]);
            });
        }, 300);
    },
    computed: {
    },
    methods: {
        post: function(){
          fetch('/test/post/'+this.newMessage);
        }
    }
});



