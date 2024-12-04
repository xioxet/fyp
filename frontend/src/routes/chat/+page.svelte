<script>
    import Chat from "../../components/Chat.svelte";
    
	export let data;
    $: messages = data ? data.messages : undefined;
</script>

<Chat {messages}/>