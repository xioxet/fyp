<script>
    import LoginForm from "../../components/LoginForm.svelte";
    let { data , form } = $props();
</script>

<div class="w-full md:w-4/5 max-w-[500px] mx-auto p-4 md:p-5">
    <div class="w-100 bg-slate-700 p-4 md:p-5 mb-5m">
        <LoginForm></LoginForm>

        {#if form?.error}
        <div class="error bg-red-500 p-3 mt-5">{form.error}</div>
        {/if}

    </div>
</div>