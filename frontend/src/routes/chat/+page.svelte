<script>
    import Chat from "../../components/Chat.svelte";
    
	export let data;
    $: messages = data ? data.messages : undefined;

    console.log(data.messages);
</script>

<Chat {messages}/>