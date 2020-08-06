<template>
    <div>
        Resultados de la búsqueda
        {{ this.query }}
        {{this.search}}
    </div>
</template>

<script>
    export default{
        data() {
            return {
                results: [],
                search: "asd"
            }
        },
        props: {
            query: String
        },
        created() {
            this.getUsers(this.query)
        },
        updated() {
            this.getUsers(this.query)
        },
        methods: {
            getUsers(search){
                var info = {user: search}
                var data = new FormData()
                data.append("json", JSON.stringify(info))

                fetch(this.$store.state.api + 'search_users/', {
                    method: "POST",
                    body: data 
                }).then((response) => response.json())
                .then((data) => {
                    console.log("Respuesta del servidor");
                    console.log(data);
                })
            }
        },
    }
</script>