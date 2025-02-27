<script>
    import { onMount } from "svelte";

    let song_list = [];
    let searchQuery = "";
    onMount(async () =>{
        try{
            const response = await fetch("http://localhost:8000/songs");
            const data = await response.json();
            song_list = [...data.songs];
        }catch{
            console.error("error: " + err);
        }
        
    }
    );
</script>

<div class="flex flex-col item-center p-5 h-screen bg-gray-100">
    <h1 class="text-3xl text-center">OP-K</h1>
    <input
    type="text"
    bind:value={searchQuery}
    placeholder="Search for a song..."
    class="w-20px p-2 text-lg border border-gray-300 rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500"
    />
      

<ul class="mt-4 max-h-64 overflow-y-auto bg-white rounded-lg shadow">
    {#each song_list.filter(song => 
        searchQuery.split(" ").every(word => song.toLowerCase().includes(word.toLowerCase()))
    ) as song}
        <li class="p-3 border-b border-gray-200 hover:bg-gray-100 cursor-pointer">{song}</li>
    {/each}
</ul>

{#if song_list.filter(song => 
    searchQuery.split(" ").every(word => song.toLowerCase().includes(word.toLowerCase()))
).length === 0}
    <p class="text-center text-gray-500 mt-4">No songs found in local library.</p>
    <button class="text-center mt-4 bg-red">Search on Youtube</button>
{/if}
</div>
