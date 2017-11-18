<template>
    <div class="box">Manage Tugas</div>
</template>

<script>
    export default {
        created() {
            this.$store.commit('setShowParent', false);
        }
    }
</script>