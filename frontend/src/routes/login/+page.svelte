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
    <div class="w-full md:w-4/5 max-w-[500px] mx-auto p-4 md:p-5 animate-fade-in">
        <div class="w-100 bg-slate-700 p-4 md:p-5 mb-5m rounded-lg shadow-lg">
            <form method="post" class="">
                <h1 class="text-3xl font-bold text-center text-slate-200 mb-6 animation-delay-200">Login</h1>
                
                <div class="mb-4 animation-delay-400">
                    <label for="username" class="block text-lg text-slate-300">Username</label>
                    <input name="username" id="username" class="text-slate-700 w-full px-4 py-2 mt-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent" required>
                </div>
                
                <div class="mb-6 animation-delay-600">
                    <label for="password" class="block text-lg text-slate-300">Password</label>
                    <input type="password" name="password" id="password" class="text-slate-700 w-full px-4 py-2 mt-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent" required>
                </div>
                
                <div class="flex justify-center animation-delay-800">
                    <button type="submit" class="w-full px-6 py-3 bg-slate-500 text-white text-lg font-semibold rounded-full shadow-md hover:bg-orange-600 transform hover:scale-105 transition duration-300 ease-in-out">Login</button>
                </div>
            </form>        
            {#if form?.error}
            <div class="error bg-red-500 p-3 mt-5 animation-delay-1000">{form.error}</div>
            {/if}
        </div>
    </div>
{:else}
    <PageLoading message="Backend is starting up, please wait..." />
{/if}

<style>
    @keyframes fade-in {
        0% {
            opacity: 0;
            transform: translateY(20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .animate-fade-in {
        animation: fade-in 1s ease-out forwards;
    }

</style>
