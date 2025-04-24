<template>
  <div class="dashboard-container">
    <h1>Dashboard</h1>

    <div class="charts-container">
      <!-- Gráfica de pastel -->
      <div class="chart-card pie-chart">
        <h2>Productos Más Vendidos</h2>
        <canvas ref="pieChart"></canvas>
      </div>

      <!-- Gráfica de barras -->
      <div class="chart-card bar-chart">
        <h2>Pago enviado y recibido (últimos 5 días)</h2>
        <canvas ref="barChart"></canvas>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import {
  Chart,
  ArcElement,
  PieController,
  BarElement,
  BarController,
  CategoryScale,
  LinearScale,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

Chart.register(
  ArcElement,
  PieController,
  BarElement,
  BarController,
  CategoryScale,
  LinearScale,
  Title,
  Tooltip,
  Legend
);

const pieChart = ref(null);
const barChart = ref(null);
const topSellingData = ref(null);

// Datos falsos para "Payment Sent & Received"
const paymentData = {
  labels: ["Mon", "Tue", "Wed", "Thu", "Fri"],
  datasets: [
    {
      label: "Pago enviado",
      data: [100, 150, 120, 200, 180],
      backgroundColor: "#483D8B",
    },
    {
      label: "Pago recibido",
      data: [120, 110, 160, 190, 210],
      backgroundColor: "#8B008B",
    },
  ],
};

// 🔹 Obtener datos de la API y actualizar la gráfica de pastel
async function fetchTopSellingProducts() {
  try {
    const response = await fetch("https://fakestoreapi.com/products");
    const data = await response.json();

    // Ordenar productos por rating
    const sortedProducts = data
      .sort((a, b) => b.rating.rate - a.rating.rate)
      .slice(0, 5);

    // Estructurar datos para el gráfico
    topSellingData.value = {
      labels: sortedProducts.map((product) => product.title),
      datasets: [
        {
          label: "Rating",
          data: sortedProducts.map((product) => product.rating.rate),
          backgroundColor: ["#6495ED", "#8B008B", "#9932CC", "#483D8B", "#1a237e"],
        },
      ],
    };

    createPieChart();
  } catch (error) {
    console.error("Error al obtener los productos:", error);
  }
}


// 🔹 Función para renderizar la gráfica de pastel
function createPieChart() {
  if (!topSellingData.value) return; // Evita errores si los datos aún no están listos

  new Chart(pieChart.value, {
    type: "pie",
    data: topSellingData.value,
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "bottom",
          
        },
      },
    },
  });
}

// 🔹 Función para renderizar la gráfica de barras
function createBarChart() {
  new Chart(barChart.value, {
    type: "bar",
    data: paymentData,
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "bottom",
        },
      },
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}

// 🔹 Ejecutamos las funciones cuando el componente se monta
onMounted(() => {
  fetchTopSellingProducts();
  createBarChart();
});
</script>

<style scoped>
.dashboard-container {
  margin: 20px;
}

.charts-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: flex-start;
}

/* Estilos generales para las tarjetas */
.chart-card {
  background: #fff;
  border-radius: 8px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  padding: 30px;
  margin-left: 70px;
  text-align: center;
}

/* Pie Chart: Más pequeño */
.pie-chart {
  flex: 1 1 300px;
  min-width: 250px;
  max-width: 350px;
}

/* Bar Chart: Más ancho */
.bar-chart {
  flex: 2 1 600px;
  min-width: 500px;
  max-width: 800px;
}
</style>
