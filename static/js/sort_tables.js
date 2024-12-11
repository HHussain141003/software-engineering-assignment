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
  const rows = Array.from(table.querySelectorAll("tr:nth-child(n+2)")); // Skip header row (row 1)
  const isAscending = table
    .querySelectorAll("th")
    [columnIndex].classList.contains("ascending");

  rows.sort((rowA, rowB) => {
    const cellA = rowA.cells[columnIndex].innerText;
    const cellB = rowB.cells[columnIndex].innerText;
    const valueA = isNaN(cellA) ? cellA : parseFloat(cellA);
    const valueB = isNaN(cellB) ? cellB : parseFloat(cellB);

    return isAscending ? (valueA > valueB ? 1 : -1) : valueA < valueB ? 1 : -1;
  });

  // Re-append rows in sorted order
  rows.forEach((row) => table.appendChild(row));

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
