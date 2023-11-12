import mainPageRoutes from './mainPage/mainPage.routes'
import aboutModelRoutes from './aboutModel/aboutModel.routes'
import aboutUsRoutes from './aboutUs/aboutUs.routes'

export default {
  path: '',
  component: () => import('./Public.vue'),
  children: [
    {
      path: '',
      redirect: () => {
        return { name: 'main' }
      }
    },
    mainPageRoutes,
    aboutModelRoutes,
    aboutUsRoutes
  ]
}
