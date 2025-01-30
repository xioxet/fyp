<script>
    import "../app.css";
    import Header from "../components/Header.svelte";

    let { children } = $props();
</script>

<div class="flex flex-col h-screen">
    <Header></Header>
    <div class="grow flex w-screen m-auto bg-slate-800">
        <div class="grow w-1/5 md:w-full relative flex mx-4 md:mx-[100px]">
            {@render children()}
        </div>
    </div>
</div>