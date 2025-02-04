<div class="w-full max-w-[1200px] mx-auto p-5">
    <div class="animate-fade-in w-full bg-slate-700 p-6 sm:p-12 mb-12 rounded-lg shadow-lg">
        <h1 class="text-3xl sm:text-4xl text-center text-white font-extrabold bg-slate-600 p-6 rounded-md shadow-md transform hover:scale-105 transition duration-300 ease-in-out">
            Oops! Something Went Wrong
        </h1>
        <p class="text-center text-slate-300 mt-4 text-lg sm:text-xl">
            We couldn't find the page you're looking for. Please check the URL or try again later.
        </p>
        <div class="text-center mt-8">
            <a href="/">
                <div class="w-full sm:w-auto px-6 py-3 bg-slate-500 hover:bg-orange-600 text-base sm:text-lg font-semibold rounded-full shadow-lg transform hover:scale-110 transition duration-300 ease-in-out">
                    Go Back to Home
                </div>
            </a>
        </div>
    </div>
</div>

<style>
    @keyframes fade-in {
        0% {
            opacity: 0;
            transform: translateY(20px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .animate-fade-in {
        animation: fade-in 1s ease-out forwards;
    }
</style>
