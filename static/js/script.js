// Materialize JS

M.AutoInit();

var toastMessage = document.querySelector('.message-container')
var toastClose = document.querySelector('.toast-action') 
if (toastMessage) {
  M.toast({
    html: toastMessage,
    displayLength: 5000
  })
}

if (toastClose) {
  toastClose.addEventListener('click', () => {
    var toastElement = document.querySelector('.toast');
    var toastInstance = M.Toast.getInstance(toastElement);
    toastInstance.dismiss();
  })
}

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
    var modalElems = document.querySelectorAll('.modal');
    var modalInstances = M.Modal.init(modalElems, options);
  });

  // Gallery mouse move

  const galleryContainer = document.querySelector('.home-gallery')
  const galleryImages = document.querySelector('.gallery-images-section')

  galleryContainer.addEventListener('mousemove', (e)=> {
    let x = e.clientX - galleryContainer.getBoundingClientRect().left
    // let y = e.clientY - galleryContainer.getBoundingClientRect().top
    console.log(x);

    galleryImages.style.transform = `translate(-${x}px)`
  })

  // Loading

  const documentElements = [document.querySelector('.main-section'), document.querySelector('.header-about-section')]

  const timeline = gsap.timeline({defaults: {duration: 1}})

  window.addEventListener('load', () => {
    timeline.to(document.querySelector('.loading'), {
      opacity: 0,
      
      ease: "circ.out"
    }, '-=0.5').to(documentElements[0], {
      opacity: 1,
      y: '0',
      ease: "power1.out"
      
    }, '-=1').to(documentElements[1], {
      opacity: 1,
      x: '0',
      ease: "bounce.out",
      
    })
    document.body.classList.remove('post-load')
    })
