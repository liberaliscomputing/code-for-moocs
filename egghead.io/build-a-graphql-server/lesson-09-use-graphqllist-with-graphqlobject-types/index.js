'use strict';

const express = require('express');
const {
  GraphQLSchema,
  GraphQLObjectType,
  GraphQLList,
  GraphQLNonNull,
  GraphQLID,
  GraphQLString,
  GraphQLInt,
  GraphQLBoolean,
} = require('graphql');
const graphqlHTTP = require('express-graphql');

const { 
  getMovieById,
  getMovies,
} = require('./src/data');


const PORT = process.env.PORT || 3000;
const server = express();

const movieType = new GraphQLObjectType({
  name: 'Movie',
  description: 'Movie information',
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
    },
  },
});
const queryType = new GraphQLObjectType({
  name: 'QueryType',
  description: 'The root query type',
  fields: {
    movies: {
      type: new GraphQLList(movieType),
      resolve: getMovies,
    },
    movie: {
      type: movieType,
      args: {
        id: {
          type: new GraphQLNonNull(GraphQLID),
          description: 'The ID of a movie',
        },
      },
      resolve: (_, args) => {
        return getMovieById(args.id);
      },
    },
  },
});
const schema = new GraphQLSchema({
  query: queryType,
});

server.use('/graphql', graphqlHTTP({
  schema,
  graphiql: true
}));

server.listen(PORT, (error) => {
  if (error) throw error;

  console.log(`Listening on http://localhost:${PORT}`);
});
