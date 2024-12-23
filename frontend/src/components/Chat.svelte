<script>
    import {onMount, afterUpdate} from 'svelte';
    import Message from "./Message.svelte";
    import { enhance } from '$app/forms';
    import UserInput from "./UserInput.svelte";
    import Loading from './Loading.svelte';

    let chat;
    export let messages;
    export let waitingformessage = false;
    let initialmount = true;
    let tempmessagetext;

    onMount(() => scrollToBottom());
    afterUpdate(() => scrollToBottom());

    // i know this is a mess but there's something very fucky going on with how the messages render in
    // because i have to re-render them in and therefore i have to suppress it frmo scrolling to bottom
    // when i don't want it to
    // #trusttheprocess
    const scrollToBottom = async(node=chat) => {
        if (waitingformessage || initialmount) {
            node.scroll({top: node.scrollHeight, behavior: 'auto'})
            if (initialmount) {
                initialmount = false;
            }
        }
    }

</script>

{#if initialmount} 
    <Loading></Loading>
{/if}
<div class="relative mx-auto p-5"
     class:opacity-0={initialmount}>
    <div class="h-[70vh] justify-end overflow-y-auto"
    bind:this={chat}>
        {#each messages as message}
        <Message 
        messageText={message.messagecontent} fromUser={message.fromuser}>
        </Message>
        {/each}

        {#if waitingformessage}
        <Message messageText={tempmessagetext} fromUser={true}></Message>
        <Message messageText={"Loading..."} fromUser={false}></Message>
        {/if}
    </div>

    <!--userinput-->
    <div class="h-[10h]">
        <form use:enhance={({formData}) => {
            console.log(formData)
            waitingformessage = true;
            tempmessagetext = formData.get('message');
            return async ({ update }) => {
                console.log('does this ever get triggered')
                update().then(function() {
                    scrollToBottom();
                    waitingformessage = false;
                })
            }
        }} action="" method="POST" class="relative mt-5">
        <input autofocus name=message class="w-full h-10 rounded-lg bg-slate-100 text-slate-700 px-3" placeholder="Ask something here...">
        <button disabled={waitingformessage} type="submit" class="absolute end-2 text-xl text-slate-800 hover:text-orange-300">▶</button>
        </form>
    </div>
</div>

    
<style>
    button {
        transform: translateY(-50%);
        top: 50%;
    }
</style>    