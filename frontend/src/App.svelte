<script>
  import Yield from "./Yield.svelte";
  import LpYield from "./LpYield.svelte";
</script>

<main>
  <h2>
    Made by <a href="https://github.com/sedat">Sedat.</a> If you'd like to tip me
    for my work my BSC wallet address: 0x878BC5bC7cBc369dffC00cdc6e1718478dc1D639
  </h2>
  <div id="flex">
    <Yield />
    <LpYield />
  </div>
</main>

<style>
  #flex {
    display: flex;
    flex-flow: wrap;
  }
</style>
