if (window.scrollY != 0) {
  window.location.assign(window.location.href);
}
// Canvas particle system on loading page --- Learned Canvas drawing from https://www.youtube.com/c/Frankslaboratory 

const canvas = document.querySelector(".canvas-loading");
const ctx = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const particlesArray = [];
let randomColor = "#D2B48C";

window.addEventListener("resize", () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
});

const canvasMouse = {
  x: undefined,
  y: undefined,
};

canvas.addEventListener("mousemove", (e) => {
  canvasMouse.x = e.x;
  canvasMouse.y = e.y;

  for (let i = 0; i < 1; i++) {
    particlesArray.push(new Particle());
  }
});

class Particle {
  constructor() {
    this.x = canvasMouse.x;
    this.y = canvasMouse.y;
    this.size = Math.random() * 1 + 2;
    this.speedX = Math.random() * 3 - 1.5;
    this.speedY = Math.random() * 3 - 1.5;
    this.color = randomColor;
    this.blur = Math.random() * 5 + 5;
  }
  update() {
    this.x += this.speedX;
    this.y += this.speedY;
    this.size -= 0.01;
    if (this.size > 0.2) {
      this.size -= 0.1;
    }
  }
  draw() {
    ctx.fillStyle = this.color;
    ctx.shadowBlur = this.blur;
    ctx.shadowColor = this.color;
    ctx.beginPath();
    ctx.rect(this.x, this.y, this.size, this.size);
    ctx.fill();
  }
}

function handleParticles() {
  for (let i = 0; i < particlesArray.length; i++) {
    particlesArray[i].draw();
    particlesArray[i].update();
    if (particlesArray[i].size <= 0.1) {
      particlesArray.splice(i, 1);
      i--;
    }
  }
}

animate = () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  handleParticles();
  if (randomColor === "#E66C4E") {
    randomColor = "#D2B48C";
  } else {
    randomColor = "#E66C4E";
  }
  requestAnimationFrame(animate);
};
animate();



// ---------------------------------------------------------------------
// Main Landing Page elements
const documentElementsGsap = [document.querySelector('.main-section'), document.querySelector('.header-about-section')];
const landingSegmentsGsap = [
  document.querySelector('.home-landing-title'),
  document.querySelector('.home-landing-title h1'),
  document.querySelectorAll('.home-landing-title p'),
  document.querySelector('.home-landing-title .landing-buttons'),
  document.querySelectorAll('.home-landing-title .landing-buttons a'),
  document.querySelector('.home-landing-image')
];

// Categories Landing Page
const categoryContainerGsap = document.querySelector('.category-container');
const categoryHeaderGsap = document.querySelector('#home-products h2');
const categoriesGsap = gsap.utils.toArray('.category-container .category-card');
// Reviews Whole Site
const reviewContainerGsap = document.querySelector('.glider');
const reviewHeaderGsap = document.querySelector('#home-reviews h2');
// Site information Whole Site
const siteInfoContainerGsap = document.querySelector('.site-information-container');
const siteInfoSegmentsGsap = document.querySelectorAll('.site-info-content');
// Home about whole site
const homeAboutContainerGsap = document.querySelector('.home-about-section');
const homeAboutSegmentsGsap = [document.querySelector('.home-about-info h2'), document.querySelector('.home-about-info p'), document.querySelector('.home-about-info a')];

const timeline = gsap.timeline({
  defaults: {
    duration: 1
  }
});

// Materialize JS

M.AutoInit();

var toastMessage = document.querySelector('.message-container');
var toastClose = document.querySelector('.toast-action');
if (toastMessage) {
  M.toast({
    html: toastMessage,
    displayLength: 5000
  });
}

if (toastClose) {
  toastClose.addEventListener('click', () => {
    var toastElement = document.querySelector('.toast');
    var toastInstance = M.Toast.getInstance(toastElement);
    toastInstance.dismiss();
  });
}

document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems, options);
  var modalElems = document.querySelectorAll('.modal');
  var modalInstances = M.Modal.init(modalElems, options);
});

// Gallery mouse move

const galleryContainer = document.querySelector('.home-gallery');
const galleryImages = document.querySelector('.gallery-images-section');
const galleryImagesIndividual = document.querySelectorAll('.gallery-column img');

galleryContainer.addEventListener('mousemove', (e) => {
  let x = e.clientX - galleryContainer.getBoundingClientRect().left;
  galleryImages.style.transform = `translate(-${x}px)`;
  galleryImagesIndividual.forEach(image => {
    image.style.transform = `rotateY(${(x*0.01) - 10}deg)`;
  });
});

// Loading

window.addEventListener('load', () => {
  timeline.to(document.querySelector('.loading'), {
      opacity: 0,
      duration: 2,
      ease: "circ.out"
    })
    .to(document.querySelector('.canvas-loading'), {
      opacity: 0,
      duration: 2,
      ease: "circ.out"
    }, '-=2')
    .to(documentElementsGsap[0], {
      opacity: 1,
      y: '0',
      duration: 2,
      ease: "power1.out"

    }, '-=1');
  if (landingSegmentsGsap[0] != null) {
    timeline.to(landingSegmentsGsap, {
      opacity: 1,
      ease: "power1.out",
      stagger: 0.25
    });
    timeline.to(landingSegmentsGsap[5], {
      x: '15px',
      duration: 1.5,
      ease: "back.out(2)",
    }, '-=1');
    timeline.to(landingSegmentsGsap[4], {
      x: '0',
      duration: 0.25,
      ease: "power4.out",
      stagger: 0.1
    }, '-=2');
  }
  timeline.to(documentElementsGsap[1], {
    opacity: 1,
    x: '0',

    ease: "elastic.out(1, 0.75)",
    onComplete: postLoad
  });
});

// Once loading animation is complete
function postLoad() {
  document.body.classList.remove('post-load');
  document.querySelector('.loading').style.display = 'none';
  document.querySelector('.canvas-loading').style.display = 'none';
  // Scroll animations
  if (categoryHeaderGsap) {
    gsap.from(categoryHeaderGsap, {
      scrollTrigger: {
        trigger: categoryHeaderGsap,
        toggleActions: 'restart pause resume restart'
      },
      translateX: '50px',
      opacity: 0,
      duration: 0.5,
    });

    gsap.from(categoriesGsap, {
      scrollTrigger: {
        trigger: categoryContainerGsap,
        toggleActions: 'restart pause resume restart'
      },
      translateY: '50px',
      opacity: 0,
      duration: 1,
      stagger: 0.25
    });
  }
  if (reviewHeaderGsap) {
    gsap.from(reviewHeaderGsap, {
      scrollTrigger: {
        trigger: reviewHeaderGsap,
        toggleActions: 'restart pause resume restart'
      },
      translateX: '-50px',
      opacity: 0,
      duration: 1,
    });
    gsap.from(reviewContainerGsap, {
      scrollTrigger: {
        trigger: reviewHeaderGsap,
        toggleActions: 'restart pause resume restart'
      },
      translateY: `-100px`,
      opacity: 0,
      duration: 1,
    });
  }
  if (siteInfoContainerGsap) {
    gsap.from(siteInfoContainerGsap, {
      scrollTrigger: {
        trigger: siteInfoContainerGsap,
        toggleActions: 'restart pause resume restart'
      },
      duration: 2,
    });
    siteInfoSegmentsGsap.forEach((segment, i) => {
      const segmentChildren = gsap.utils.toArray(segment.children);
      const direction = (i == 0 || i == 2) ? '-' : '';
      gsap.from(segment, {
        scrollTrigger: {
          trigger: segment,
          toggleActions: 'restart pause resume restart'
        },
        translateX: `${direction}200px`,
        opacity: 0,
        duration: 1,
      });
      gsap.from(segmentChildren, {
        scrollTrigger: {
          trigger: segment,
          toggleActions: 'restart pause resume restart'
        },
        translateX: `${direction}200px`,
        opacity: 0,
        duration: 1,
        stagger: 0.25
      });
    });

  }
  if (homeAboutContainerGsap) {
    gsap.from(homeAboutContainerGsap, {
      scrollTrigger: {
        trigger: homeAboutContainerGsap,
        toggleActions: 'restart pause resume restart'
      },
      duration: 1,
    });

    gsap.from(homeAboutSegmentsGsap, {
      scrollTrigger: {
        trigger: homeAboutSegmentsGsap,
        toggleActions: 'restart pause resume restart'
      },
      translateY: '100px',
      opacity: 0,
      duration: 0.75,
      stagger: 0.25

    });

  }
}