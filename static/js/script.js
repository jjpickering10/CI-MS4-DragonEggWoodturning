const documentElementsGsap = [document.querySelector('.main-section'), document.querySelector('.header-about-section')]
const landingSegmentsGsap = [
  document.querySelector('.home-landing-title'),
  document.querySelector('.home-landing-title h1'),
  document.querySelectorAll('.home-landing-title p'),
  document.querySelector('.home-landing-title .landing-buttons'),
  document.querySelectorAll('.home-landing-title .landing-buttons a'),
  document.querySelector('.home-landing-image')
]

// Categories Landing Page
const categoryContainerGsap = document.querySelector('.category-container')
const categoryHeaderGsap = document.querySelector('#home-products h2')
const categoriesGsap = gsap.utils.toArray('.category-container .category-card')
// Reviews Whole Site
const reviewContainerGsap = document.querySelector('.glider')
const reviewHeaderGsap = document.querySelector('#home-reviews h2')
console.log(reviewContainerGsap);
// Gallery Whole site
const galleryContainerGsap = document.querySelector('.home-gallery')
// Site information Whole Site
const siteInfoContainerGsap = document.querySelector('.site-information-container')
const siteInfoSegmentsGsap = document.querySelectorAll('.site-info-content')
const siteInfoSegmentHeaders = document.querySelectorAll('.site-info-content h3')
const siteInfoSegmentText = document.querySelectorAll('.site-info-content p')

const timeline = gsap.timeline({
  defaults: {
    duration: 1
  }
})
const segmentTimeline = gsap.timeline()

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

  console.log(landingSegmentsGsap);

  window.addEventListener('load', () => {
    timeline.to(document.querySelector('.loading'), {
      opacity: 0,
      duration: 2,
      ease: "circ.out"
    })
    .to(documentElementsGsap[0], {
      opacity: 1,
      y: '0',
      ease: "power1.out"
      
    }, '-=1')
    if (landingSegmentsGsap[0] != null) {
      timeline.to(landingSegmentsGsap, {
        opacity: 1,
        ease: "power1.out",
        stagger: 0.25
      })
      timeline.to(landingSegmentsGsap[5], {
        x: '0',
        duration: 1.5,
        ease: "bounce.out",
      }, '-=2')
      timeline.to(landingSegmentsGsap[4], {
        x: '0',
        duration: 0.25,
        ease: "power4.out",
        stagger: 0.1
      }, '-=2')
    }
    timeline.to(documentElementsGsap[1], {
      opacity: 1,
      x: '0',
      ease: "bounce.out",
      onComplete: postLoad
    })
  })

  function postLoad() {
    document.body.classList.remove('post-load')
      // Scroll animations
    console.log(categoriesGsap);
    if (categoryHeaderGsap) {
      gsap.from(categoryHeaderGsap, {
        scrollTrigger: {
          trigger: categoryHeaderGsap,
          toggleActions: 'restart pause resume restart'
        },
        translateX: '50px',
        opacity: 0,
        duration: 0.5,
      })
      // categoriesGsap.forEach(category => {
      //   gsap.from(category, {
      //     scrollTrigger: {
      //       trigger: category,
      //       toggleActions: 'restart pause resume restart'
      //     },
      //     // translateX: '-50px',
      //     // translateY: '50px',
      //     opacity: 0,
      //     // duration: 0.5,
      //     // delay: Math.abs(Math.random() - 0.5)
      //   })
      // })
      gsap.from(categoriesGsap, {
        scrollTrigger: {
          trigger: categoryContainerGsap,
          toggleActions: 'restart pause resume restart'
        },
        translateY: '50px',
        opacity: 0,
        duration: 1,
        stagger: 0.25
      })
    }
    if (reviewHeaderGsap) {
      gsap.from(reviewHeaderGsap, {
        scrollTrigger: {
          trigger: reviewHeaderGsap,
          toggleActions: 'restart pause resume restart'
        },
        translateX: '-50px',
        opacity: 0,
        duration: 0.5,
      })
      gsap.from(reviewContainerGsap, {
        scrollTrigger: {
          trigger: reviewHeaderGsap,
          toggleActions: 'restart pause resume restart'
        },
        translateY: `-100px`,
        opacity: 0,
        duration: 1,
      })
    }
    if (galleryContainerGsap) {
      gsap.from(galleryContainerGsap, {
        scrollTrigger: {
          trigger: galleryContainerGsap,
          toggleActions: 'restart pause resume restart'
        },
        translateX: '-100px',
        // translateY: '-100px',
        opacity: 0,
        duration: 0.5,
      })
    }
    if (siteInfoContainerGsap) {
      gsap.from(siteInfoContainerGsap, {
        scrollTrigger: {
          trigger: siteInfoContainerGsap,
          toggleActions: 'restart pause resume restart'
        },
        // translateX: '-50px',
        // translateY: '-100px',
        opacity: 0,
        duration: 2,
      })
      siteInfoSegmentsGsap.forEach((segment, i) => {
        const segmentChildren = gsap.utils.toArray(segment.children)
        console.log(segmentChildren);
        // console.log(i, segment);
        const direction = (i == 0 || i == 2) ? '-' : ''
        // console.log(direction);
        gsap.from(segment, {
          scrollTrigger: {
            trigger: segment,
            toggleActions: 'restart pause resume restart'
          },
          opacity: 0,
          duration: 2,
        })
        gsap.from(segmentChildren, {
          scrollTrigger: {
            trigger: segment,
            toggleActions: 'restart pause resume restart'
          },
          translateX: `${direction}200px`,
          // opacity: 0,
          duration: 2,
          stagger: 0.5
        })
      })
      
    }
  }
  