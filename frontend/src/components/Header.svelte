<script>
    import { onMount } from "svelte";
    let loggedIn = true;
    let mobile = false;
    let username = null;
    onMount(() => {
        loggedIn = document.cookie.includes('loggedIn=true');
        username = document.cookie.split("username=")[1]
        console.log(username);
    })
</script>

<div>
    <div class="w-90 px-10 h-10border-b-2 flex items-center bg-slate-900">
        <div class="rounded-sm bg-slate-700 p-3 m-2">NYP CNC AI</div>
        {#if loggedIn}
        <div class="hover:bg-orange-500 rounded-sm bg-slate-800 p-3 m-2">welcome, {username}!</div>
        {/if}
        <div class=grow></div>

        <div class="hidden lg:flex grow items-center justify-end">
            <a class="hover:bg-orange-500 rounded-sm bg-slate-800 p-3 m-2" href='/'>home</a>
            <a class="hover:bg-orange-500 rounded-sm bg-slate-800 p-3 m-2" href='/chat'>chat</a>
            <a class="hover:bg-orange-500 rounded-sm bg-slate-800 p-3 m-2" href='/upload'>upload</a>
            <a class="hover:bg-orange-500 rounded-sm bg-slate-800 p-3 m-2" href='/classify'>classify</a>
            {#if !loggedIn}
            <a class="hover:bg-orange-500 rounded-sm bg-slate-800 p-3 m-2" href='/login'>login</a>
            {/if}
        </div>

        <div class="lg:hidden flex items-center ml-auto">
            <button aria-label=items on:click={() => mobile = !mobile} class="text-white">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-6 w-6">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>
        </div>

        <div class={`lg:hidden ${mobile ? 'block' : 'hidden'} absolute top-0 left-0 w-full bg-slate-900 py-5 px-10 z-5m`}>
            {#if !loggedIn}
            <a class="hover:bg-orange-500 rounded-sm bg-slate-800 p-3 m-2 block" href='/login'>login</a>
            {/if}
            <a class="hover:bg-orange-500 rounded-sm bg-slate-800 p-3 m-2 block" href='/upload'>upload</a>
            <a class="hover:bg-orange-500 rounded-sm bg-slate-800 p-3 m-2 block" href='/chat'>chat</a>
            <a class="hover:bg-orange-500 rounded-sm bg-slate-800 p-3 m-2 block" href='/classify'>classify</a>
            <a class="hover:bg-orange-500 rounded-sm bg-slate-800 p-3 m-2 block" href='/'>home</a>
        </div>
    </div>
</div>