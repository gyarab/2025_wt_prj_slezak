<template>
    <main>
        <h2>Artworks</h2>
        <ul>
            <li v-for="artwork in artworks" :key="artwork.id">
                <RouterLink :to="`/artwork/${artwork.id}`">
                    {{ artwork.name }}
                </RouterLink>
            </li>
        </ul>
    </main>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

const artworks = ref([
    { id: 1, name: 'Artwork One' },
    { id: 2, name: 'Artwork Two' },
    { id: 3, name: 'Artwork Three' },
])
</script>