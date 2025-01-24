<script>
    import LoginForm from "../../components/LoginForm.svelte";
    import { onMount } from 'svelte';
    import { writable } from 'svelte/store';
    import { PUBLIC_BACKEND_URL } from "$env/static/public";
    import PageLoading from "../../components/PageLoading.svelte";

    let { data , form } = $props();
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
    <div class="w-4/5 max-w-[500px] mx-auto p-5">
        <div class="w-100 bg-slate-700 p-5 mb-5m">
            <LoginForm></LoginForm>

            {#if form?.error}
            <div class="error bg-red-500 p-3">{form.error}</div>
            {/if}

        </div>
    </div>
{:else}
    <PageLoading message="Backend is starting up, please wait..." />
{/if}