<script>
    let {messageText, fromUser, loading} = $props();
    import { fade } from 'svelte/transition';
</script>

<div class="w-auto block">
    <div class="message w-fit z-5 min-w-10 bg-orange-500 px-5 py-3 my-2 rounded text-sm md:text-lg"
    class:ml-auto={fromUser}
    class:bg-orange-700={fromUser}>
        <p>
            {messageText} 
            {#if loading}
            &nbsp;&nbsp;<svg class="inline-block" width=20px height=20px xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 150"><path fill="none" stroke="#FFFFFF" stroke-width="15" stroke-linecap="round" stroke-dasharray="300 385" stroke-dashoffset="0" d="M275 75c0 31-27 50-50 50-58 0-92-100-150-100-28 0-50 22-50 50s23 50 50 50c58 0 92-100 150-100 24 0 50 19 50 50Z"><animate attributeName="stroke-dashoffset" calcMode="spline" dur="2" values="685;-685" keySplines="0 0 1 1" repeatCount="indefinite"></animate></path></svg>
            {/if}
        </p>
    </div>
</div>

<style>
    .message {
        position: relative;
        z-index: 1;
    }
</style>