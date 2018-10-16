<template>
  <div class="E-create e_link">
    <el-dialog
      :visible="dialogVisible"
      :show-close="false"
      :before-close="beforeClose"
      width="80%">
      <img src="../../assets/upload_bg.png" alt="" style="width: 100%;position: absolute;left: 0;top: 0;z-index: -1;">
      <h3 style="text-align: center;color: #681023;letter-spacing: 2px;">新建相册</h3>
      <div class="input" id="e_create">
        <svg viewBox="0 0 320 300" id="create_svg">
          <defs>
            <linearGradient
              inkscape:collect="always"
              id="linearGradient"
              x1="13"
              y1="193.49992"
              x2="307"
              y2="193.49992"
              gradientUnits="userSpaceOnUse">
              <stop
                style="stop-color:#fad0c4;"
                offset="0"
                id="stop876"/>
              <stop
                style="stop-color:#ffd1ff;"
                offset="1"
                id="stop878"/>
            </linearGradient>
          </defs>
          <path
            d="m 40,120.00016 239.99984,-3.2e-4 c 0,0 24.99263,0.79932 25.00016,35.00016 0.008,34.20084 -25.00016,35 -25.00016,35 h -239.99984 c 0,-0.0205 -25,4.01348 -25,38.5 0,34.48652 25,38.5 25,38.5 h 215 c 0,0 20,-0.99604 20,-25 0,-24.00396 -20,-25 -20,-25 h -190 c 0,0 -20,1.71033 -20,25 0,24.00396 20,25 20,25 h 168.57143"/>
        </svg>
        <el-input placeholder="" v-model="data.name" @focus="moveLine(0)" style="margin-top: 54px;" id="title">
          <template slot="prepend">标题</template>
        </el-input>
        <el-input placeholder="" v-model="data.point" @focus="moveLine(1)" style="margin-top: 114px;" id="point">
          <template slot="prepend">地点</template>
        </el-input>
      </div>
      <div class="submit" @touchend.stop="submit">创建</div>
    </el-dialog>
  </div>
</template>

<script>
  import anime from 'animejs'
  import axios from '../../router/axios'
  import bus from '../../router/bus'

  export default {
    name: 'E-create',

    components: {},
    data() {
      return {
        dialogVisible: false,
        data: {},
        current: null
      }
    },
    methods: {
      beforeClose(done) {
        done();
        this.$emit('shutdown');
      },
      submit() {
        var vm = this;
        console.log(vm.data);
        axios.get('/api/create_album/', vm.data, (data) => {
          if (data.data.e === 0) {
            bus.$emit('update');
            vm.$message({
              type: 'success',
              message: data.data.code
            });
            this.dialogVisible = false;
            this.$emit('shutdown');
          } else {
            vm.$message({
              type: 'error',
              message: data.data.code
            })
          }
        })
      },
      autoFocus(val) {
        console.log(document.querySelector('#title'))
        if (val === 0) {
          console.log(document.querySelector('#title'))
          document.querySelector('#title').focus();
        }
      },
      open(val) {
        this.dialogVisible = val;
      },
      moveLine(val) {
        if (this.current) this.current.pause();
        var value = 0;
        switch (val) {
          case 0 :
            value = 0;
            break;
          case 1 :
            value = -336;
            break;
          case 2 :
            value = -730;
            break;
        }
        this.current = anime({
          targets: '#create_svg path',
          strokeDashoffset: {
            value: value,
            duration: 700,
            easing: 'easeOutQuart'
          },
          strokeDasharray: {
            value: val === 2 ? '522 1386' : '240 1386',
            duration: 700,
            easing: 'easeOutQuart'
          }
        });
      },
    },
    mounted: function () {

    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
  .E-create {
    position: relative;
    svg {
      position: absolute;
      width: 300px;
      height: 270px;
      top: 52px;
      z-index: -1;
    }
    path {
      fill: none;
      stroke: url(#linearGradient);;
      stroke-width: 8;
      stroke-dasharray: 240, 1386;
    }
    .submit {
      width: 86px;
      height: 42px;
      line-height: 42px;
      border-radius: 8px;
      text-align: center;
      color: white;
      letter-spacing: 4px;
      font-size: 18px;
      background-color: #f34d61;
      margin: 228px auto 0;
    }
  }
</style>
