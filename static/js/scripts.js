function openTrailer(key) {
  const url = `https://www.youtube.com/embed/${key}`;
  const iframe = `<iframe width="560" height="315" src="${url}" allowfullscreen></iframe>`;
  document.getElementById('trailerModalContent').innerHTML = iframe;
  document.getElementById('trailerModal').style.display = 'block';
  document.getElementById('trailerModalClose').focus();
}

document.getElementById('trailerModal').addEventListener('click', function (event) {
  if (event.target === this) {
    this.style.display = 'none';
    document.getElementById('trailerModalContent').innerHTML = ''; // Stop the trailer
  }
});

document.getElementById('trailerModalClose').addEventListener('click', function () {
  document.getElementById('trailerModal').style.display = 'none';
  document.getElementById('trailerModalContent').innerHTML = ''; // Stop the trailer
});

document.getElementById('trailerModalClose').addEventListener('keydown', function (event) {
  if (event.key === 'Enter' || event.key === ' ') {
    document.getElementById('trailerModal').style.display = 'none';
    document.getElementById('trailerModalContent').innerHTML = ''; // Stop the trailer
  }
});
