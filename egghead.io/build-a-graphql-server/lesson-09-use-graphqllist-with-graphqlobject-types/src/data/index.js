const movies = [
  {
    id: '1',
    title: 'Node.js',
    duration: 120,
    watched: true,
  },
  {
    id: '2',
    title: 'React.js',
    duration: 240,
    watched: false,
  }
];
const getMovieById = (id) => new Promise((resolve) => {
  const [movie] = movies.filter((movie) => {
    return movie.id === id;
  });

  resolve(movie);
});
const getMovies = () => new Promise((resolve) => {
  return resolve(movies);
});

module.exports = { 
  getMovieById,
  getMovies,
};
