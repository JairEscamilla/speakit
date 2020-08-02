<template>
    <div>
        Bienvenido a speakit!
        {{$store.state.token}}
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
            console.log(this.$store.state.token);
            console.log("hello");
        },
    }
</script>