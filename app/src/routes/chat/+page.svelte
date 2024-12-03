<script>
    import Chat from "../../components/Chat.svelte";
    
    /** @type {{ data: import('./$types').PageData }} */
	export let data;
</script>

<Chat messages={ data.messages }/>