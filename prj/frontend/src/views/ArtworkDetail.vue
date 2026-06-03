<template>
    <main>
        <h2>Artwork Detail</h2>
        <p>Viewing artwork ID: {{ id }}</p>
    </main>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
const id = route.params.id
</script>