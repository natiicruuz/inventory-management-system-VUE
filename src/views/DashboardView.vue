<template>
  <div class="dashboard-container">
    <h1>Dashboard</h1>

    <div class="charts-container">
      <!-- Gráfica de pastel -->
      <div class="chart-card pie-chart">
        <h2>Productos Mas Vendidos</h2>
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
  BarElement,
  BarController,
  CategoryScale,
  LinearScale,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

// Registrar los componentes que usaremos de Chart.js
Chart.register(
  ArcElement,
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

// Datos falsos para la gráfica de pastel (Top Selling Products)
const topSellingData = {
  labels: ["Mens Casual Premium Slim Fit T-Shirts", "SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s", "White Gold Plated Princess", "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops", "Solid Gold Petite Micropave"],
  datasets: [
    {
      label: "Sales",
      data: [30, 50, 40, 20, 10], // Cantidades simuladas
      backgroundColor: ["#6495ED", "#8B008B", "#9932CC", "#483D8B", "#1a237e"],
    },
  ],
};

// Datos falsos para la gráfica de barras (Pagos)
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

onMounted(() => {
  createPieChart();
  createBarChart();
});

function createPieChart() {
  // Creamos la gráfica de pastel
  new Chart(pieChart.value, {
    type: "pie",
    data: topSellingData,
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

function createBarChart() {
  // Creamos la gráfica de barras
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
  margin-left:70px;
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

