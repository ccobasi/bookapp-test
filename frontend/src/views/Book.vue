<template>
  <div class="page-product">
    <div class="columns is-multiline">
      <div class="column is-9">
        <h1 class="title">{{ book.name }}</h1>

        <p>{{ book.author }}</p>
      </div>

      <div class="column is-3">
        <h2 class="subtitle">Information</h2>

        <p><strong>ISBN: </strong>${{ book.isbn }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Book",
  data() {
    return {
      book: {},
      quantity: 1,
    };
  },
  mounted() {
    this.getBook();
  },
  methods: {
    getBook() {
      const book_id = this.$route.params.book_id;

      axios.get(`/api/v1/books/${book_id}`);
      then((response) => {
        this.book = response.data;
      }).catch((error) => {
        console.log(error);
      });
    },
  },
};
</script>
