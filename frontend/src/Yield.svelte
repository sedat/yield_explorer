<script>
  import { onMount } from "svelte";
  import Chart from "chart.js";
  onMount(async () => {
    // yield
    const requestYield = await fetch("http://localhost:9000/yield");
    const yieldData = await requestYield.json();
    const uniquePools = [...new Set(yieldData.map((item) => item.pool))];
    let colors = uniquePools.map((pool) => {
      let n = (Math.random() * 0xffffe * 1000000).toString(16);
      return "#" + n.slice(0, 6);
    });
    const dates = yieldData.map((data) => new Date(data.date).toLocaleString());
    const data = yieldData.map((data) => {
      return { label: data.pool, data: data.deposit };
    });
    console.log(data);
    const yieldCtx = document.getElementById("yield").getContext("2d");
    new Chart(yieldCtx, {
      type: "line",
      data: {
        labels: dates,
        datasets: uniquePools.map((pool) => {
          return {
            label: pool,
            data: yieldData
              .filter((item) => item.pool === pool)
              .map((item) => item.deposit),
            borderColor: colors.pop(),
            fill: false,
          };
        }),
      },
      options: {
        responsive: false,
      },
    });
  });
</script>

<main>
  <canvas id="yield" width="600" height="400" />
</main>
