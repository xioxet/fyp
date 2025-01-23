<script>
    export let message = "Loading, please wait...";
</script>

<div class="overlay">
    <div class="flex items-center justify-center h-full">
        <div class="flex flex-col items-center text-center">
            <div class="loader"></div>
            <p>{message}</p>
        </div>
    </div>
</div>

<style>
    .overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.233); /* Optional: Add a background color */
        z-index: 1000; /* Ensure it is on top of other elements */
    }

    .flex {
        display: flex;
    }

    .items-center {
        align-items: center;
    }

    .justify-center {
        justify-content: center;
    }

    .h-screen {
        height: 100vh;
    }

    .h-full {
        height: 100%;
    }

    .text-center {
        text-align: center;
    }

    .loader {
        border: 16px solid #f3f3f3;
        border-top: 16px solid #3498db;
        border-radius: 50%;
        width: 120px;
        height: 120px;
        animation: spin 2s linear infinite;
        margin-bottom: 16px; /* Add some space between the loader and the text */
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
</style>