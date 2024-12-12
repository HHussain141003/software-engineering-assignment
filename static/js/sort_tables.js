document.addEventListener("DOMContentLoaded", function () {
  const table = document.querySelector("table");
  const headers = table.querySelectorAll("th");

  headers.forEach((header, index) => {
    header.addEventListener("click", () => {
      console.log(`Column ${index} clicked`);
      sortTable(table, index);
    });
  });
});

function sortTable(table, columnIndex) {
  const tbody = table.querySelector("tbody"); // Explicitly target tbody
  const rows = Array.from(tbody.querySelectorAll("tr")); // Get all rows within tbody

  const isAscending = table
    .querySelectorAll("th")
    [columnIndex].classList.contains("ascending");

  rows.sort((rowA, rowB) => {
    const cellA = rowA.cells[columnIndex].innerText.trim();
    const cellB = rowB.cells[columnIndex].innerText.trim();

    const valueA = isNaN(cellA) ? cellA : parseFloat(cellA);
    const valueB = isNaN(cellB) ? cellB : parseFloat(cellB);

    return isAscending ? (valueA > valueB ? 1 : -1) : valueA < valueB ? 1 : -1;
  });

  // Re-append rows in sorted order
  rows.forEach((row) => tbody.appendChild(row));

  // Toggle class to change sorting direction
  table
    .querySelectorAll("th")
    .forEach((th) => th.classList.remove("ascending", "descending"));
  table
    .querySelectorAll("th")
    [columnIndex].classList.toggle("ascending", !isAscending);
  table
    .querySelectorAll("th")
    [columnIndex].classList.toggle("descending", isAscending);
}
