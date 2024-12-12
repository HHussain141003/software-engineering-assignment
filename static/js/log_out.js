document.addEventListener("DOMContentLoaded", function () {
  const logoutForm = document.getElementById("logout-form");

  if (logoutForm) {
    logoutForm.addEventListener("submit", function (event) {
      if (!confirm("Are you sure you want to log out?")) {
        event.preventDefault();
      }
    });
  }
});
