// 异步组件
const Layout = () => import('@views/layout/Layout');

const routes = [
  {
    path: '/',
    redirect: '/home',
    component: Layout,
    children: []
  }
];

export default routes;
