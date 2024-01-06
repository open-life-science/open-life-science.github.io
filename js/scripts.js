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

  bulmaCollapsible.attach();
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


$(document).ready(function() {
    $('#dataframe').DataTable( {
        "sScrollX": "100%",
        "dom": "Qlfrtip",

        responsive: {
            details: {
                type: 'column'
            }
        },
        "bAutoWidth": false,
        columnDefs: [ {
            className: 'control',
            orderable: false,
            targets:   [ 0 ],
            width: 100,
        },
        { type: 'natural', targets: 1 } // allow normal sorting
        ],

    });
});