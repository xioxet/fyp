<script>
    import {onMount} from 'svelte';
    import Message from "./Message.svelte";
    import Textbox from "./Textbox.svelte";

    let chat;
    onMount(() => scrollToBottom(chat))

    const scrollToBottom = async(node) => {
        node.scroll({top: node.scrollHeight, behavior: 'auto'})
    }

    // temporary store for Illustrative Purposes
    let messages = [
        {
            "messageText":"top text",
            "fromUser":false,
        },
        {
            "messageText":"I use arch btw",
            "fromUser":true,
        },
        {
            "messageText":"ipsum",
            "fromUser":true,
        },
        {
            "messageText":"ipsum",
            "fromUser":true,
        },
        {
            "messageText":"ipsum",
            "fromUser":true,
        },        {
            "messageText":"ipsum",
            "fromUser":true,
        },
        {
            "messageText":"ipsum",
            "fromUser":true,
        },
        {
            "messageText":"ipsum",
            "fromUser":true,
        },
        {
            "messageText":"ipsum",
            "fromUser":true,
        },
        {
            "messageText":"ipsum",
            "fromUser":true,
        },
        {
            "messageText":"bottom text",
            "fromUser":false,
        }
    ]
</script>

<div class="relative mt-10 mx-auto bg-slate-800 p-5 h-[80h] w-10/12 max-w-[500px]">
    <div class="h-[70vh] justify-end overflow-y-auto"
    bind:this={chat}>
        {#each messages as message}
        <Message 
        messageText={message.messageText} fromUser={message.fromUser}>
        </Message>
        {/each}
    </div>
    <div class="h-[10h]">
        <Textbox></Textbox>
    </div>
</div>