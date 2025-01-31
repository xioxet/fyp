<script>
    import { onMount } from "svelte";
    import { afterNavigate } from "$app/navigation";
    
    let loggedIn = true;
    let mobile = false;
    let username = null;

    onMount(() => {
        loggedIn = document.cookie.includes('loggedIn=true');
        username = document.cookie.split("username=")[1];
        console.log(username);
    });

    afterNavigate(() => {
        if (mobile) {
            mobile = false;
        }
    });
</script>

<div class="w-full sticky top-0 z-50 bg-slate-900 shadow-lg">
    <div class="w-90 px-10 py-2 flex items-center justify-between bg-slate-900">
        <div class="flex items-center justify-between px-4 py-2">
            <div class="rounded-sm bg-slate-700 p-3 font-bold text-lg sm:text-xl text-white">
                NYP CNC AI
            </div>
            {#if loggedIn}
            <div class="text-white rounded-sm p-3 text-sm sm:text-base">
                {username ? `Welcome, ${username}!` : 'Welcome!'}
            </div>
            {/if}
        </div>
        

        <!-- Desktop Menu -->
        <div class="hidden lg:flex items-center space-x-4">
            <a class="hover:bg-orange-500 text-white bg-slate-700 rounded-lg p-3 duration-300m" href="/">Home</a>
            <a class="hover:bg-orange-500 text-white bg-slate-700 rounded-lg p-3 duration-300m" href="/chat">Chat</a>
            <a class="hover:bg-orange-500 text-white bg-slate-700 rounded-lg p-3 duration-300m" href="/upload">Upload</a>
            <a class="hover:bg-orange-500 text-white bg-slate-700 rounded-lg p-3 duration-300m" href="/classify">Classify</a>
            {#if !loggedIn}
            <a class="hover:bg-orange-500 text-white rounded-sm p-3" href="/login">Login</a>
            {/if}
        </div>

        <!-- Mobile Menu Toggle Button -->
        <div class="lg:hidden flex items-center">
            <button aria-label="Toggle Menu" on:click={() => mobile = !mobile} class="text-white transition-all duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-6 w-6">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>
        </div>
    </div>

    <!-- Mobile Menu -->
    <div class={`lg:hidden ${mobile ? 'block' : 'hidden'} bg-slate-900 text-white p-4 absolute top-0 left-0 w-full h-screen z-10 transform transition-all ease-in-out duration-300`}>
        <div class="flex items-center justify-between">
            <div class="rounded-sm bg-slate-700 p-3 m-2 font-bold text-lg text-white">
                NYP CNC AI
            </div>
            <button aria-label="Close Menu" on:click={() => mobile = !mobile} class="text-white transition-all duration-300">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-6 w-6">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
            </button>
        </div>

        <div class="mt-5">
            {#if !loggedIn}
            <a class="hover:bg-orange-500 rounded-sm bg-slate-800 p-3 m-2 block transition-all duration-300" href="/login">Login</a>
            {/if}
            <a class="hover:bg-orange-500 rounded-lg bg-slate-800 p-3 m-2 block transition-all duration-300" href="/upload">Upload</a>
            <a class="hover:bg-orange-500 rounded-lg bg-slate-800 p-3 m-2 block transition-all duration-300" href="/chat">Chat</a>
            <a class="hover:bg-orange-500 rounded-lg bg-slate-800 p-3 m-2 block transition-all duration-300" href="/classify">Classify</a>
            <a class="hover:bg-orange-500 rounded-lg bg-slate-800 p-3 m-2 block transition-all duration-300" href="/">Home</a>
        </div>
    </div>
</div>
