document.addEventListener("DOMContentLoaded", function () {
  const cancelLink = document.getElementById("cancel-link");

  if (cancelLink) {
    cancelLink.addEventListener("click", function (event) {
      if (
        !confirm(
          "You will lose all unsaved information if you exit. To continue please press OK"
        )
      ) {
        event.preventDefault(); // Prevent navigation if "Cancel" is clicked
      }
    });
  }
});
