'use strict';

const express = require('express');
const { buildSchema } = require('graphql');
const graphqlHTTP = require('express-graphql');


const PORT = process.env.PORT || 3000;
const server = express();

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

server.use('/graphql', graphqlHTTP({
  schema,
  graphiql: true,
  rootValue: resolvers,
}));

server.listen(PORT, (error) => {
  if (error) throw error;

  console.log(`Listening on http://localhost:${PORT}`);
});
