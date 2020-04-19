<template lang="html">
    <div class="container">
       <div class="row">
           <div class="col text-left">
               <h2>Editar usuario</h2>
           </div>
       </div>

        <div class="row">
           <div class="col">
               <div class="card">
                   <div class="card-body">

                       <form>
                        <form @onSubmit="onSubmit">

                        <div class="form-group row">
                            <label for="Nombre" class="col-sm-2 col-form-label">Nombre</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Nombre" name="Nombre" class="form-control">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="Apellidos" class="col-sm-2 col-form-label">Apellidos</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Apellidos" name="Apellido" class="form-control">
                            </div>
                        </div>

                        <div class="form-group row">
                            <label for="Email" class="col-sm-2 col-form-label">Email</label>    
                            <div class="col-sm-6">
                             <input type="text" placeholder="Email" name="Email" class="form-control">
                            </div>
                        </div>

                        <div class="rows">
                            <div class="col text-left">
                            <b-button type="submit" variant="primary">Editar</b-button>
                            <b-button type="submit" class="btn-large-space" :to="{ name: 'ListUsuario'}">Cancelar</b-button>
                            </div>
                        </div>

                       </form>  


                       </form> 
                    </div>   
                </div>
            </div> 
        </div>       
    </div>  
</template>

<script>
export default {
}
</script>>

<style lang="css" scoped>
</style>