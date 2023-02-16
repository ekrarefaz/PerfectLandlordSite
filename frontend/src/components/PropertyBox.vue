<template>
    <div class="column is-3">
        <div class="box">
            <figure class="image mb-4">
                <img v-bind:src="property.get_thumbnail">
            </figure>

            <h3 class="is-size-4">{{ property.address }}</h3>
            <p class="is-size-6 has-text-grey">${{ property.price }}</p>

            <router-link v-bind:to="property.get_absolute_url" class="button is-dark mt-4">View details</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'PropertyBox',
    props: {
        property: Object
    }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
    width: 50%;
  }
</style>