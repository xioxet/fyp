<script>
    import { enhance } from '$app/forms';
    import { onMount } from 'svelte';
    import { writable } from 'svelte/store';
    import { PUBLIC_BACKEND_URL } from "$env/static/public";
    import PageLoading from "../../components/PageLoading.svelte";

    let { data , form } = $props();
    let waitingfordata = $state(false);
    let submitted_filename = $state(null);
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
    <div class="mx-auto p-4 md:p-5 w-full md:w-3/5">
        <form method="post" enctype="multipart/form-data" use:enhance={({ formData }) => {
            waitingfordata = true;
            return async ({ update }) => {
                update().then(function () {
                    waitingfordata = false;
                });
            };
        }}>
            <div class="rounded-lg shadow-lg w-full bg-slate-700 p-4 md:p-5 mb-4 md:mb-5 opacity-0 animate-fade-in">
                <h1 class="text-xl md:text-2xl text-white font-extrabold">Upload files</h1>
                <h2 class="mt-2 text-sm md:text-base text-slate-300">These files will be used to train the AI.</h2>
                {#if waitingfordata}
                <div class="bg-slate-500 p-3 mt-4 md:mt-5">
                    Uploading... &nbsp;&nbsp;
                    <svg class="inline-block animate-spin" width="20px" height="20px" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 150">
                        <path fill="none" stroke="#FFFFFF" stroke-width="15" stroke-linecap="round" stroke-dasharray="300 385" stroke-dashoffset="0" d="M275 75c0 31-27 50-50 50-58 0-92-100-150-100-28 0-50 22-50 50s23 50 50 50c58 0 92-100 150-100 24 0 50 19 50 50Z">
                            <animate attributeName="stroke-dashoffset" calcMode="spline" dur="2" values="685;-685" keySplines="0 0 1 1" repeatCount="indefinite"></animate>
                        </path>
                    </svg>
                </div>
                {:else if form?.success}
                <div class="bg-green-500 p-3 mt-4 md:mt-5 opacity-0 animate-fade-in animation-delay-200">Upload succeeded!</div>
                {:else if form?.error}
                <div class="error bg-red-500 p-3 mt-4 md:mt-5 opacity-0 animate-fade-in animation-delay-200">Upload failed with error: {form.error}</div>
                {/if}
            </div>

            <!-- File Upload Section -->
            <div class="flex items-center justify-center w-full opacity-0 animate-fade-in animation-delay-400">
                <label for="file" class="flex flex-col items-center justify-center w-full h-48 md:h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                    <div class="flex flex-col items-center justify-center pt-5 pb-6">
                        <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                        </svg>
                        <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop</p>
                        <p class="text-xs text-gray-500 dark:text-gray-400">DOCX, PDF, PPTX or XLSX</p>
                    </div>
                    <input style="display:none" bind:value={submitted_filename} id="file" type="file" name="file" accept=".docx,.pdf,.pptx,.xlsx"/>
                    <div class="mb-2 text-sm md:text-base text-gray-500 dark:text-gray-400">
                        {submitted_filename ? `File uploaded: ${submitted_filename.split(/(\\|\/)/g).pop()}` : `No file uploaded!`}
                    </div>
                </label>
            </div>

            <!-- Submit Button -->
            <div class="flex mt-5 opacity-0 animate-fade-in animation-delay-600">
                <button type="submit" class="w-3/5 md:w-2/5 px-6 py-3 bg-slate-500 text-white text-lg font-semibold rounded-full shadow-md hover:bg-orange-600 transform hover:scale-105 transition duration-300 ease-in-out">Upload</button>
            </div>
        </form>
    </div>
{:else}
    <PageLoading message="Backend is starting up, please wait..." />
{/if}

<!-- Scroll Animation Keyframes -->
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

    .animation-delay-200 {
        animation-delay: 0.1s;
    }

    .animation-delay-400 {
        animation-delay: 0.2s;
    }

    .animation-delay-600 {
        animation-delay: 0.3s;
    }
</style>
