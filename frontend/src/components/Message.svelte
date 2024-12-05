<div class="w-auto block">
    <div class="w-fit z-5 min-w-10 bg-orange-500 px-5 py-3 my-2 rounded"
    class:ml-auto={fromUser}
    class:bg-orange-600={fromUser}>
        <p>
            {messageText} 
        </p>
    </div>
</div>

<script>
    let {messageText, fromUser} = $props();
</script>