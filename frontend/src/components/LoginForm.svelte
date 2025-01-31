<form method="post" class="">
    <h1 class="text-3xl font-bold text-center text-slate-200 mb-6">Login</h1>
    
    <div class="mb-4">
        <label for="username" class="block text-lg text-slate-300">Username</label>
        <input name="username" id="username" class="w-full px-4 py-2 mt-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent" required>
    </div>
    
    <div class="mb-6">
        <label for="password" class="block text-lg text-slate-300">Password</label>
        <input type="password" name="password" id="password" class="w-full px-4 py-2 mt-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-transparent" required>
    </div>
    
    <div class="flex justify-center">
        <button type="submit" class="w-full px-6 py-3 bg-slate-500 text-white text-lg font-semibold rounded-full shadow-md hover:bg-orange-600 transform hover:scale-105 transition duration-300 ease-in-out">Login</button>
    </div>
</form>
