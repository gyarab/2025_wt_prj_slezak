<template>
    <header>
        <RouterLink to="/">
            <h1>Bauhaus (vue)</h1>
        </RouterLink>
    </header>
    <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>