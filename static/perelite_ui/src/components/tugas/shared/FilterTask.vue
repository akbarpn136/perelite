<template>
    <!-- Main container -->
    <nav class="is-clearfix">
        <!-- Left side -->
        <div class="is-pulled-left">
            <div class="level-item">
                <p class="subtitle is-6">
                    Perolehan angka: <strong>123</strong>
                </p>
            </div>
        </div>

        <!-- Right side -->
        <div class="is-pulled-right">
            <div class="field has-addons">
                <p class="control">
                    <button class="button is-static is-small">Berdasarkan</button>
                </p>
                <p class="control">
                    <input class="input is-small"
                                       type="number"
                                       placeholder="Tahun"
                                       min="2015">
                </p>
            </div>
        </div>
    </nav>
</template>

<script>

</script>

<style scoped>
    nav.is-clearfix {
        width: 100%;
    }
</style>