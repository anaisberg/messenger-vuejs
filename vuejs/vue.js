const Msg = Vue.component('msg', {
    props: ['author', 'message', 'hour'],
    template: '<div class="msg"><h4><em>{{ author }}</em></h4><p>{{ message }}</p></div>'
});

const app = new Vue({
    el: '#app',
    data: {
        newAuthor: [],
        newMessage: [],
        messages: [],
    },
    created: function() {
        var self = this;
        setInterval(async function() {
            const res = await fetch('/test/pull');
            const data = await res.json();
            self.messages = [];
            data.forEach(function (r, i) {
                self.messages.push(this.receiveMsg(r.content,r.ts));
            });
        }, 300);
    },
    computed: {
        newMsg: function() {
            return newAuthor+'@'+newMessage
        },

    },
    methods: {
        post: function(){
          fetch('/test/post/'+this.newMsg);
        },
        receiveMsg: function(mes,time) {
            var n = mes.length;
            for (let i=0; i < n; i++) {
                if (mes[i].equals('@')) {
                    return [mes.substring(0,i),mes.substring(i+1,n),time]
                }
            }
            return ['none',me,time]
        }

    }
});



