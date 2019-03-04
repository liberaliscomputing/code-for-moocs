'use strict';

const { graphql, buildSchema } = require('graphql');


const schema = buildSchema(`
  type Movie {
    id: ID,
    title: String,
    duration: Int,
    watched: Boolean
  }

  type Query {
    movies: [Movie]
  }

  type Schema {
    query: Query
  }
`);

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
]

const resolvers = {
  movies: () => movies,
};

const query = `
  query queryString {
    movies {
      id,
      title,
      duration,
      watched
    }
  }
`;

graphql(schema, query, resolvers)
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.log(error);
  });
