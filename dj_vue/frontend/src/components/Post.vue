/* eslint-disable vue/multi-word-component-names */
<template>
  <div class="post" v-if="post">
      <h2>{{ post.title }}: {{ post.subtitle }}</h2>
      By <AuthorLink :author="post.author" />
      <div>{{ displayableDate(post.publishDate) }}</div>
    <p class="post__description">{{ post.metaDescription }}</p>
    <article>
      {{ post.body }}
    </article>
    <ul>
      <li class="post__tags" v-for="tag in post.tags" :key="tag.name">
        <router-link :to="`/tag/${tag.name}`">#{{ tag.name }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import gql from 'graphql-tag';
import AuthorLink from '@/components/AuthorLink';

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Post',
  components: {
    AuthorLink,
  },
  data () {
    return {
      post: null,
    }
  },
  async created() {
    const post = await this.$apollo.query({
      query: gql`query ($slug: String!) {
        postBySlug(slug: $slug) {
          title
          subtitlepublishDate
          metaDescriptionslug
          bodyauthor {
            user {
              username
              firstName
              lastName
            }
          }
          tags {
            name  
          }  
        }  
      }`,
      variables: {
          slug: this.$route.params.slug,
      },
    })
    this.post = post.data.postBySlug

  },
  methods: {
    displayableDate (date) {
      return new Intl.DateTimeFormat(
        'en-US',
        { dateStyle: 'full' },
      ).format(new Date(date))
    }
  },
}
</script>