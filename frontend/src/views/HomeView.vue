<template>
  <section class="hero is-medium is-info mb-6">
    <div class="hero-body has-text-centered">
      <p class="title mb-6">Book App</p>
      <p class="subtitle">The best book store online</p>
    </div>
  </section>
  <div class="columns is-multiline">
    <div class="column is-12">
      <h2 class="is-size-2 has-text-centered">List of Books</h2>
    </div>

    <div
      class="column is-3"
      v-for="book in bookLists"
      v-bind:key="book.id"
      v-bind:book="book"
    >
      <div>
        <h3 class="is-size-4">{{ book.name }}</h3>
        <p class="is-size-6 has-text-grey">{{ book.author }}</p>

        <router-view
          v-bind:to="book.get_absolute_url"
          class="button is-primary mt-4"
        >
          View Details
        </router-view>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomeView",
  data() {
    return {
      bookLists: [],
    };
  },
  components: {},
  mounted() {
    this.getBookLists();
  },
  methods: {
    getBookLists() {
      axios
        .get("/api/v1/book-lists/")
        .then((response) => {
          this.bookLists = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
