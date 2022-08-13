import { createRouter, createWebHistory } from 'vue-router';


const routes = [
   {path: '/',
      name: 'home',
      component: () => import('./views/Home.vue')
   },
   {path: '/introduction',
      name: 'introduction',
      component: () => import('./views/docs/Introduction.vue')
   },
   {path: '/qinput',
      name: 'qinput',
      component: () => import('./views/docs/widgets/QInput.vue')
   },
   {path: '/widgets/qinput/button',
      name: 'qinputbutton',
      component: () => import('./views/docs/widgets/QInputButton.vue')
   },
   {path: '/widgets/qinput/checkbox',
      name: 'qinputcheckbox',
      component: () => import('./views/docs/widgets/QInputCheckbox.vue')
   },
   {path: '/widgets/qinput/file',
      name: 'qinputfile',
      component: () => import('./views/docs/widgets/QInputFile.vue')
   },
   {path: '/widgets/qinput/radio',
      name: 'qinputradio',
      component: () => import('./views/docs/widgets/QInputRadio.vue')
   },
   {path: '/widgets/qinput/slider',
      name: 'qinputslider',
      component: () => import('./views/docs/widgets/QInputSlider.vue')
   },
   {path: '/qmedia',
      name: 'qmedia',
      component: () => import('./views/docs/medias/QMedia.vue')
   },
   {path: '/medias/qmedia/image',
      name: 'qmediaimage',
      component: () => import('./views/docs/medias/QMediaImage.vue')
   },
   {path: '/medias/qmedia/gif',
      name: 'qmediagif',
      component: () => import('./views/docs/medias/QMediaGif.vue')
   },
   {path: '/styles/string',
      name: 'stylesstring',
      component: () => import('./views/docs/styles/String.vue')
   },
   {path: '/styles/dict',
      name: 'stylesdict',
      component: () => import('./views/docs/styles/Dict.vue')
   }


]

const router = createRouter({
  history: createWebHistory(),
  routes,
})


export default router;