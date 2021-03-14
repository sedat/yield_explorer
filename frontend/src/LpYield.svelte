<script>
  import { onMount } from "svelte";
  import Chart from "chart.js";
  onMount(async () => {
    // lp
    const requestLp = await fetch("http://localhost:9000/lp");
    const lp = await requestLp.json();
    const uniqueLp = [...new Set(lp.map((item) => item.pool))];
    const lpDates = lp.map((data) => new Date(data.date).toLocaleString());
    const colors = uniqueLp.map((pool) => {
      let n = (Math.random() * 0xffffe * 1000000).toString(16);
      return "#" + n.slice(0, 6);
    });
    var lpCtx = document.getElementById("lp").getContext("2d");
    new Chart(lpCtx, {
      type: "line",
      data: {
        labels: lpDates,
        datasets: uniqueLp.map((pool) => {
          return {
            label: pool,
            data: lp
              .filter((item) => item.pool === pool)
              .map((item) => item.deposit),
            borderColor: colors.pop(),
            fill: false,
          };
        }),
      },
      options: {
        responsive: false,
        title: {
          display: true,
          text: "Liquidity Pool Graph",
        },
      },
    });
  });
</script>

<main>
  <canvas id="lp" width="700" height="500" />
</main>
