<script>
    import "../app.css";
    import Header from "../components/Header.svelte";
    import Naoto from "../components/Naoto.svelte";
    import Sidebar from "../components/Sidebar.svelte";

    let { children } = $props();
</script>

<div class="flex flex-col h-screen">
    <Header></Header>
    <div class="grow flex w-screen m-auto bg-slate-800">
        <div class="grow w-1/10 bg-slate-900">
            <Sidebar></Sidebar>
        </div>
        <div class="grow w-3/5 relative">
            {@render children()}
        </div>
    </div>
</div>