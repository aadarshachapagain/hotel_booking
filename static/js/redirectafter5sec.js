window.setTimeout(function () {
   var base_url = window.location.origin;
   redirect_to = base_url + '/dashboard';
   window.location.href = redirect_to;
}, 5000);