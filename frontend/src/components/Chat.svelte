<script>
    import {onMount, afterUpdate} from 'svelte';
    import Message from "./Message.svelte";
    import UserInput from "./UserInput.svelte";

    let chat;
    export let messages;

    onMount(() => scrollToBottom(chat))
    afterUpdate(() => scrollToBottom(chat))

    const scrollToBottom = async(node) => {
        node.scroll({top: node.scrollHeight, behavior: 'auto'})
    }

</script>

<div class="relative mt-10 mx-auto bg-slate-800 p-5 h-[80h] w-10/12 max-w-[500px]">
    <div class="h-[70vh] justify-end overflow-y-auto"
    bind:this={chat}>
        {#each messages as message}
        <Message 
        messageText={message.messagecontent} fromUser={message.fromuser}>
        </Message>
        {/each}
    </div>
    <div class="h-[10h]">
        <UserInput></UserInput>
    </div>
</div>