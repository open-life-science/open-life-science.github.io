document.addEventListener('DOMContentLoaded', () => {

  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Check if there are any navbar burgers
  if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach( el => {
      el.addEventListener('click', () => {

        // Get the target from the "data-target" attribute
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');

      });
    });
  }

});

document.addEventListener('DOMContentLoaded', function() {
	let cardToggles = document.getElementsByClassName('card-toggle');
	for (let i = 0; i < cardToggles.length; i++) {
		cardToggles[i].addEventListener('click', e => {
			e.currentTarget.parentElement.parentElement.childNodes[3].classList.toggle('is-hidden');
		});
	}
});

document.addEventListener('DOMContentLoaded', function() {
	let cardToggles = document.getElementsByClassName('expertise-toggle');
	for (let i = 0; i < cardToggles.length; i++) {
		cardToggles[i].addEventListener('click', e => {
			e.currentTarget.parentElement.querySelector(".peoples").classList.toggle('is-hidden');
		});
	}
});

document.addEventListener('DOMContentLoaded', function() {
	let cardToggles = document.getElementsByClassName('expertise-detail-toggle');
	for (let i = 0; i < cardToggles.length; i++) {
		cardToggles[i].addEventListener('click', e => {
			e.currentTarget.parentElement.parentElement.querySelector(".expertise-detail").classList.toggle('is-hidden');
		});
	}
});
document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {

        // Add a click event on each of them
        $navbarBurgers.forEach(el => {
            el.addEventListener('click', () => {

                // Get the target from the "data-target" attribute
                const target = el.dataset.target;
                const $target = document.getElementById(target);

                // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
                el.classList.toggle('is-active');
                $target.classList.toggle('is-active');

            });
        });
    }

});

document.addEventListener('DOMContentLoaded', function () {
    let cardToggles = document.getElementsByClassName('card-toggle');
    for (let i = 0; i < cardToggles.length; i++) {
        cardToggles[i].addEventListener('click', e => {
            e.currentTarget.parentElement.parentElement.childNodes[3].classList.toggle('is-hidden');
        });
    }
});

document.addEventListener('DOMContentLoaded', function () {
    let cardToggles = document.getElementsByClassName('expertise-toggle');
    for (let i = 0; i < cardToggles.length; i++) {
        cardToggles[i].addEventListener('click', e => {
            e.currentTarget.parentElement.querySelector(".peoples").classList.toggle('is-hidden');
        });
    }
});

document.addEventListener('DOMContentLoaded', function () {
    let cardToggles = document.getElementsByClassName('expertise-detail-toggle');
    for (let i = 0; i < cardToggles.length; i++) {
        cardToggles[i].addEventListener('click', e => {
            e.currentTarget.parentElement.parentElement.querySelector(".expertise-detail").classList.toggle('is-hidden');
        });
    }
});

document.addEventListener('DOMContentLoaded', () => {
    /* Selecting the image with the class schedule-overview. */
    let imageToModal = document.querySelector('.schedule-overview');
    /* Creating a modal window with the image in the center of the screen. */
    imageToModal.onclick = () => createModal(imageToModal);
    imageToModal.ondragend = () => createModal(imageToModal)
})

/**
 * It creates a modal window with the image in the center of the screen.
 * @param element - The element that was clicked on.
 */

var createModal = (element) => {
    let /* An object that contains the styles for the modal window. */
        modal = {
            mainStyle: `position: fixed; z-index:1000; background: rgba(0, 0, 0, 0.83); top: 0; left: 0; right: 0; bottom: 0; backdrop-filter: blur(5px)`,
            subStyle: 'position: fixed; width: 100%; height: 100%; transform:translate(-50%, -50%); top: 50%; left: 50%',
            imgStyle: 'width: 100%; height: 90%; margin: 20px 10px;',
            errStyle: 'position: fixed; background: white; padding: 20px; transform:translate(-50%, -50%); top: 50%; left: 50%'
        };
    var modalDiv = document.createElement('div'),
        div = document.createElement('div'),
        /* Creating an image element. */
        img = new Image();

    img.src = element.getAttribute('src');
    img.style = `${modal.imgStyle}`;

    /**** 
     * A function that is called when the image is not loaded. It removes the image and adds a div with
    the text "The requested content cannot be loaded".
    *
    ***/
    img.onerror = () => {
        img.remove()
        var err = document.createElement('div');
        err.style = `${modal.errStyle}`
        err.innerText = "The requested content cannot be loaded";
        modalDiv.appendChild(err)
    }

    modalDiv.style = `${modal.mainStyle}`;
    div.setAttribute('style', `${modal.subStyle}`);

    div.appendChild(img)
    modalDiv.appendChild(div)
    document.body.append(modalDiv)

    /* It removes the modal window when the user clicks on it. */
    modalDiv.onclick = () => {
        modalDiv.remove()
    }
}