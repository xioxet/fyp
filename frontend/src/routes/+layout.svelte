<script>
    import "../app.css";
    import Header from "../components/Header.svelte";
    import Naoto from "../components/Naoto.svelte";
    import Sidebar from "../components/Sidebar.svelte";

    let { children } = $props();
</script>

<Header></Header>
<div class="h-5/6 gap-4 flex w-90 m-auto mt-2 h-full">
    <div class="w-1/5 -mt-2 border-r-2">
        <Sidebar></Sidebar>
    </div>
    <div class="w-3/5 mx-auto -mt-2">
        {@render children()}
        <Naoto></Naoto>
    </div>
</div>