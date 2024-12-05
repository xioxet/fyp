<script>
    import {onMount, afterUpdate} from 'svelte';
    import Message from "./Message.svelte";
    import { enhance } from '$app/forms';
    import UserInput from "./UserInput.svelte";
    import Loading from './Loading.svelte';

    let chat;
    let userinput;
    export let messages;
    export let waitingformessage = false;
    let initialmount = true;
    let tempmessagetext;

    onMount(() => scrollToBottom());
    afterUpdate(() => scrollToBottom());

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
<div class="relative mt-10 mx-auto bg-slate-800 p-5 h-[80h] w-10/12 max-w-[500px]"
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
            waitingformessage = true;
            tempmessagetext = formData.get('message');
            console.log(tempmessagetext);
            return async ({ update }) => {
                update().then(function() {
                    scrollToBottom();
                    waitingformessage = false;
                    userinput.focus();
                })
            }
        }} action="" method="POST" class="relative mt-5">
        <input bind:this={userinput} name=message class="w-full h-10 rounded-lg bg-slate-100 text-slate-700 px-3" placeholder="Ask something here...">
        <button type="submit" class="absolute end-2 text-xl text-slate-800 hover:text-orange-300">▶</button>
        </form>
    </div>
</div>

    
<style>
    button {
        transform: translateY(-50%);
        top: 50%;
    }
</style>    