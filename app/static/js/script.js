$(document).ready(function () {
  var path = window.location.pathname;
  path = path.replace(/^\/|\/$/g, "");

  // Find the menu item link that matches the current URL path
  // and add the active class to the li element
  $('a[href="' + path + '"]').each(function () {
    $(this).addClass("active");
  });
});
