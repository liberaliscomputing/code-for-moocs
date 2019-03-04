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
    movie: Movie
  }

  type Schema {
    query: Query
  }
`);

const resolvers = {
  movie: () => ({
    id: '1',
    title: 'bar',
    duration: 180,
    watched: true,
  }),
};

const query = `
  query queryString {
    movie {
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
