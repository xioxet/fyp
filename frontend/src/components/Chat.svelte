<script>
    import {onMount, afterUpdate} from 'svelte';
    import Message from "./Message.svelte";
    import { enhance } from '$app/forms';
    import UserInput from "./UserInput.svelte";
    import Loading from './Loading.svelte';

    let chat;
    let messageinput;
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

    console.log(messageinput);

</script>

{#if initialmount} 
    <Loading></Loading>
{/if}
<div class="relative mx-auto p-5 flex flex-col max-h-[90vh] flex-1"
     class:opacity-0={initialmount}>
    <div class="justify-end overflow-y-auto"
    bind:this={chat}>
        {#each messages as message}
        <Message 
        messageText={message.messagecontent} fromUser={message.fromuser} loading={false}>
        </Message>
        {/each}

        {#if waitingformessage}
        <Message messageText={tempmessagetext} fromUser={true} loading={false}></Message>
        <Message messageText={"Loading..."} fromUser={false} loading={true}></Message>
        {/if}
    </div>
    <!--userinput-->
    <div class="h-[10h] mt-auto">
        <form use:enhance={({formData}) => {
            waitingformessage = true;
            tempmessagetext = formData.get('message');
            messageinput.value = "";
            return async ({ update }) => {
                update().then(function() {
                    scrollToBottom();
                    waitingformessage = false;
                })
            }
        }} action="" method="POST" class="relative mt-5">
        <input bind:this={messageinput} autofocus name=message class="w-full h-10 rounded-lg bg-slate-100 text-slate-700 px-3" placeholder="Ask something here...">
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