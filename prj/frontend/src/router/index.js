import { createRouter, createWebHistory } from "vue-router"
import Artwork from "../views/Artwork.vue"
import ArtworkDetail from "../views/ArtworkDetail.vue"

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', name: 'home', component: Artwork },
        { path: '/artwork/:id', name: 'artwork', component: ArtworkDetail }
    ]
})

export default router