<script>
  import Yield from "./Yield.svelte";
  import LpYield from "./LpYield.svelte";
  export let author;
  export let walletAddress;
</script>

<main>
  <h2>
    Made by <a href="https://github.com/sedat">{author}.</a> If you'd like to
    tip me for my work my BSC wallet address: {walletAddress}
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
