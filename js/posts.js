// Searchbar functionality

function searchPosts() {
  // Find the cards
  let cards = document.querySelectorAll('.card')
  // Locate search input
  let search_query = document.getElementById('searchbar').value;
  // Loop through the cards
  for (var i = 0; i < cards.length; i++) {
    // If text is in the card:
    if (cards[i].innerHTML.toLowerCase()
    // AND if the text matches the search query:
      .includes(search_query.toLowerCase())) {
        // THEN remove the '.is-hidden' class
        cards[i].classList.remove('is-hidden');
      } else {
        // Otherwise, add the class:
        cards[i].classList.add('is-hidden');
      }
  }
};
