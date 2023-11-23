// show mobile menu
const mobileMenu = document.querySelector('.md-tabs');
const mobileMenuActivator = document.querySelector('button#md-tabs-activator');

mobileMenuActivator.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');

    console.log(mobileMenuActivator.querySelector('i.fa'))

    if (mobileMenuActivator.querySelector('i.fa').classList.contains(fa-bars))
    {
        mobileMenuActivator.querySelector('i.fa').classList.remove('fa-bars');
        mobileMenuActivator.querySelector('i.fa').classList.add('fa-close');
    }
    else
    {
        mobileMenuActivator.querySelector('i.fa').classList.add('fa-bars');
        mobileMenuActivator.querySelector('i.fa').classList.remove('fa-close');
    }
})

// hero section img changer
const heroSection = document.querySelector('.hero');
const heroSideImgs = document.querySelectorAll('.side-imgs img');
const imgLocation = document.querySelector('.img-location');

let currentImgIndex = 0;

// const increaseImgIndex = () => currentImgIndex = currentImgIndex + 1;

const changeInterval = setInterval(() => {
    currentImgIndex = currentImgIndex + 1;
}, 5000);

heroSideImgs.forEach(img => {
    img.addEventListener('click', () => changeHeroBackground(img))
});

const changeHeroBackground = (img) => {
    const imgId = parseInt(img.dataset.index);
    currentImgIndex = imgId;
    imgLocation.querySelector('span').textContent = img.dataset.location;
    setHeroBackground();
}

// const autoImgChange = () => {
//     setInterval(() => {
//         if (currentImgIndex < heroSideImgs.length)
//         {
//             currentImgIndex++;
//         }
//         else
//         {
//             currentImgIndex = 0;
//         }
//         console.log(currentImgIndex)
//         setHeroBackground();
//     }, 5000);
// }

const setHeroBackground = () => {
    const imgUrl = heroSideImgs[currentImgIndex].src;
    heroSection.style.backgroundImage = `url(${imgUrl})`;

    imgLocation.querySelector('span').textContent = heroSideImgs[currentImgIndex].dataset.location;
    // autoImgChange();
}

// check if we are on homepage
if (document.querySelector('.hero'))
{
    setHeroBackground();
}


// destination detail
const destinationImgs = document.querySelectorAll('.destination-imgs img')
let detailImgIndex = 0;

const imgControls = document.querySelectorAll('.destination-imgs button');
const destinationImgSource = document.querySelector('#img-source')

    imgControls.forEach(cta => {
        cta.addEventListener('click', () => {
            if (cta.dataset.id === 'next')
            {
                if (detailImgIndex < destinationImgs.length - 1)
                {
                    detailImgIndex++;
                }
                else
                {
                    detailImgIndex = 0;
                }
            }
            else
            {
                if (detailImgIndex > 0)
                {
                    detailImgIndex--;
                }
                else
                {
                    detailImgIndex = destinationImgs.length - 1;
                }
            }
            console.log(detailImgIndex)
            setDetailImg();
        })
    })
const setDetailImg = () => {
    destinationImgs.forEach(img => {
        if (img.classList.contains('in-view'))
        {
            img.classList.remove('in-view');
        }
    })
    destinationImgs[detailImgIndex].classList.add('in-view');

    destinationImgSource.querySelector('#source').textContent = destinationImgs[detailImgIndex].dataset.source;

    destinationImgSource.href = destinationImgs[detailImgIndex].dataset.source;
}

if (window.location.href.includes('destination'))
{
    setDetailImg();
}

