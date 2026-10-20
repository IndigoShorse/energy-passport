export default defineNuxtConfig({
  //'@vueuse/nuxt', '@pinia/nuxt'
  modules: ['vuetify-nuxt-module', '@nuxt/icon', '@vee-validate/nuxt'],

  app: {
    buildAssetsDir: '/assets/',
    head: {
      link: [{rel: 'icon', type: 'image/png', href: '/oldLogo.svg'}]
    },
  },

  runtimeConfig: {
    public: {
      REQUEST_URL:  process.env.REQUEST_URL,
    }
  },

  devtools: { enabled: true },
  compatibilityDate: '2025-04-16'
})
