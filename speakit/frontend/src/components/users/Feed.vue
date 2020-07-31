<template>
    <div>
        Bienvenido a speakit!
        {{message}}
    </div>
</template>

<script>
    export default{
        data() {
            return {
                message: "Welcome"
            }
        },
        created() {
            alert("Bienvenido al sistema");
        },
    }
</script>