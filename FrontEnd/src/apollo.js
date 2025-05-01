import { ApolloClient, InMemoryCache, createHttpLink } from '@apollo/client/core';
import { DefaultApolloClient } from '@vue/apollo-composable';
import { provide } from 'vue';


const apolloClient = new ApolloClient({
  uri:  'http://localhost:5000/graphql',
  cache: new InMemoryCache(),
});

// Función para inyectarlo en Vue
export function provideApollo(app) {
  app.provide(DefaultApolloClient, apolloClient);
}
