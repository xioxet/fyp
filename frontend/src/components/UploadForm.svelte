<script>
    import { enhance } from '$app/forms';
</script>

<div class="mx-auto p-5 w-3/5">
    <form method="post" enctype="multipart/form-data" use:enhance>
        <div class="w-100 bg-slate-700 p-5 mb-5">
            <h1 class=text-2xl>Upload files</h1>
            <h2 class=mt-2>These files will be used to train the AI.</h2>
            <!-- not functional yet! -->
        </div>
        
        <div class="flex items-center justify-center w-full">
            <label for="file" class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600">
                <div class="flex flex-col items-center justify-center pt-5 pb-6">
                    <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                    </svg>
                    <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop</p>
                    <p class="text-xs text-gray-500 dark:text-gray-400">DOCX, PDF, PPTX or XLSX</p>
                </div>
                <input id="file" type="file" name="file" accept=".docx,.pdf,.pptx,.xlsx"/>
            </label>
        </div> 
        <div class="flex items-center my-5">
            <button class="hover:bg-orange-500 rounded-sm bg-slate-700 p-3 " href='/'>Submit</button>
            <div class="grow"></div>
        </div>
    </form>
</div>

