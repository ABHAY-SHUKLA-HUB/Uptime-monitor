let responseChart = null;

function scrollToSection(id) {
  document.getElementById(id).scrollIntoView({
    behavior: "smooth"
  });

  document.querySelectorAll(".nav").forEach(item => {
    item.classList.remove("active");
  });

  event.target.classList.add("active");
}

async function addSite() {
  const name = document.getElementById("siteName").value.trim();
  const url = document.getElementById("siteUrl").value.trim();

  if (!name || !url) {
    alert("Please enter website name and URL");
    return;
  }

  await fetch("/api/add-site", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ name, url })
  });

  document.getElementById("siteName").value = "";
  document.getElementById("siteUrl").value = "";

  loadData();
}

async function checkAllSites() {
  await fetch("/api/check-all");
  loadData();
}

async function deleteSite(id) {
  const confirmDelete = confirm("Are you sure you want to delete this website?");
  if (!confirmDelete) return;

  await fetch(`/api/delete-site/${id}`, {
    method: "DELETE"
  });

  loadData();
}

async function loadSites() {
  const res = await fetch("/api/site-stats");
  const sites = await res.json();

  document.getElementById("totalSites").innerText = sites.length;

  const box = document.getElementById("sitesList");
  box.innerHTML = "";

  sites.forEach(site => {
    const uptime = site.uptime_percentage ?? 0;

    box.innerHTML += `
      <div class="site-card">
        <div class="site-top">
          <h4>${site.name}</h4>
          <button class="delete-btn" onclick="deleteSite(${site.id})">Delete</button>
        </div>

        <p>${site.url}</p>

        <div class="uptime-line">
          <span>Uptime</span>
          <strong>${uptime}%</strong>
        </div>

        <div class="progress">
          <div class="progress-bar" style="width:${uptime}%"></div>
        </div>
      </div>
    `;
  });
}

async function loadLogs() {
  const res = await fetch("/api/logs");
  const logs = await res.json();

  let latest = {};
  logs.forEach(log => {
    if (!latest[log.url]) latest[log.url] = log.status;
  });

  let up = 0, down = 0, slow = 0;

  Object.values(latest).forEach(status => {
    if (status === "UP") up++;
    if (status === "DOWN") down++;
    if (status === "SLOW") slow++;
  });

  document.getElementById("upSites").innerText = up;
  document.getElementById("downSites").innerText = down;
  document.getElementById("slowSites").innerText = slow;

  const table = document.getElementById("logsTable");
  table.innerHTML = "";

  logs.forEach(log => {
    table.innerHTML += `
      <tr>
        <td><strong>${log.name}</strong></td>
        <td>${log.url}</td>
        <td><span class="status ${log.status}">${log.status}</span></td>
        <td>${log.status_code ?? "-"}</td>
        <td>${log.response_time ?? "-"} ms</td>
        <td>${log.checked_at}</td>
      </tr>
    `;
  });

  loadChart(logs);
}

function loadChart(logs) {
  const ctx = document.getElementById("responseChart");

  if (!ctx) return;

  const latestLogs = logs.slice(0, 10).reverse();

  const labels = latestLogs.map(log => log.name);
  const data = latestLogs.map(log => log.response_time ?? 0);

  if (responseChart) {
    responseChart.destroy();
  }

  responseChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [{
        label: "Response Time ms",
        data: data,
        borderWidth: 3,
        tension: 0.4,
        fill: true
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          display: true
        }
      },
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}

function loadData() {
  loadSites();
  loadLogs();

  const time = new Date().toLocaleTimeString();
  const refresh = document.getElementById("lastRefresh");

  if (refresh) {
    refresh.innerText = "Last refresh: " + time;
  }
}

loadData();
setInterval(loadData, 10000);