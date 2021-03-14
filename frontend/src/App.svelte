<script>
  import Yield from "./Yield.svelte";
  import LpYield from "./LpYield.svelte";
</script>

<main>
  <div id="flex">
    <Yield id="canvas" />
    <LpYield id="canvas" />
  </div>
</main>

<style>
  #flex {
    display: flex;
    flex-flow: wrap;
  }
</style>
