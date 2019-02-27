'use strict';

const express = require('express');
const graphqlHTTP = require('express-graphql');
const {
  GraphQLSchema,
  GraphQLObjectType,
  GraphQLID,
  GraphQLString,
  GraphQLInt,
  GraphQLBoolean,
} = require('graphql');


const PORT = process.env.PORT || 3000;
const server = express();

const movieType = new GraphQLObjectType({
  name: 'Movie',
  description: 'Yadi yada',
  fields: {
    id: {
      type: GraphQLID,
      description: 'The ID of a movie',
    },
    title: {
      type: GraphQLString,
      description: 'The title of a movie',
    },
    duration: {
      type: GraphQLInt,
      description: 'The duration of a movie',
    },
    watched: {
      type: GraphQLBoolean,
      description: 'Whether watched',
    }
  }

});
const queryType = new GraphQLObjectType({
  name: 'QueryType',
  description: 'The root query type',
  fields: {
    movie: {
      type: movieType,
      resolve: () => new Promise((resolve) => {
        resolve({
          id: '1',
          title: 'Node.js',
          duration: 120,
          watched: true,
        });
      }),
    },
  },
});
const schema = new GraphQLSchema({
  query: queryType,
});

server.use('/graphql', graphqlHTTP({
  schema,
  graphiql: true,
}));


server.listen(PORT, (error) => {
  if (error) throw error;

  console.log(`Listening on http://localhost:${PORT}`);
});
