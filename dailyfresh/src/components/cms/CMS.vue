<template>
  <h1>CMS</h1>
</template>

<script>
  export default {
    created() {
      if (!this.$store.getters.getAdminId) {
        this.$router.push('/cms_login')
      }
    }
  }
</script>
