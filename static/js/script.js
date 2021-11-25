M.AutoInit();

var toastMessage = document.querySelector('.message-container')
var toastClose = document.querySelector('.toast-action') 
M.toast({
  html: toastMessage,
  displayLength: 5000
})

toastClose.addEventListener('click', () => {
  var toastElement = document.querySelector('.toast');
  var toastInstance = M.Toast.getInstance(toastElement);
  toastInstance.dismiss();
})

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
  });
