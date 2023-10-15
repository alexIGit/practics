// import { createApp, VueElement } from 'vue'
// import App from './App.vue'
// import router from './router'

import Vue from 'vue';
import App from './App.vue';
// import { createProvider } from './vue-apollo';
import { createProvider } from './vue-apollo'
import router from '@/router'

// createApp(App).use(router).mount('#app');

new Vue({
  router,

  apolloProvider: createProvider({
    httpEndpoint: 'http://127.0.0.1:8000/graphql',
    wsEndpoint: null,        
  }),
  render: h => h(App)
}).$mount('#app')
