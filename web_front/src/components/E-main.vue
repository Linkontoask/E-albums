<template>
  <div class="E-main">
    <el-button icon="el-icon-menu" type="primary" size="mini" style="margin: 12px 0 0 4px;"></el-button>
    <e_content></e_content>
  </div>
</template>

<script>
  import e_content from './E-main_content.vue'

export default {
  name: 'E-main',

  components: {e_content},
  data () {
    return {
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.E-main {

}
</style>
