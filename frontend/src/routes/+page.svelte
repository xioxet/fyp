<script>
    import { onMount } from 'svelte';
    import { writable } from 'svelte/store';
    import { PUBLIC_BACKEND_URL } from "$env/static/public";
    import Body from "../components/Body.svelte";
    import Home from "../components/Home.svelte";
    import Naoto from "../components/Naoto.svelte";
    import PageLoading from "../components/PageLoading.svelte";

    let backendReady = writable(false);

    const checkBackendHealth = async () => {
        try {
            const response = await fetch(`${PUBLIC_BACKEND_URL}`);
            if (response.ok) {
                console.log('Backend is ready');
                backendReady.set(true);
            } else {
                setTimeout(checkBackendHealth, 3000); // Retry after 3 seconds
            }
        } catch (error) {
            console.error('Error checking backend health:', error);
            setTimeout(checkBackendHealth, 3000); // Retry after 3 seconds
        }
    };

    onMount(() => {
        checkBackendHealth();
    });
</script>

{#if $backendReady}
    <Home />
{:else}
    <PageLoading message="Backend is starting up, please wait..." />
{/if}