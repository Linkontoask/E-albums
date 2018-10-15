<template>
  <div class="E-upload">
    <el-dialog
      :visible.sync="dialogVisible"
      :show-close="false"
      width="80%">
      <img src="../../assets/upload_bg.png" alt="" style="width: 100%;position: absolute;left: 0;top: 0;z-index: -1;">
      <el-upload
        ref="upload"
        class="upload_main"
        action="/api/upload/"
        :on-success="success"
        :on-change="upload_change"
        :on-remove="upload_remove"
        :auto-upload="false"
        :multiple="false"
        :limit="1"
        :data="data"
        :file-list="fileList">
        <el-button size="small" type="primary"><img src="../../assets/upload.png" alt="">选择文件</el-button>
      </el-upload>
      <div class="type">
        <div v-for="(item, index) in typeData" :key="index">
          <img :src="item.url" alt="" @touchend.stop="checkRadio(item.type)">
          <p class="e-label">
            <el-radio v-model="data.type" :label="item.type" fill="#f2465b" text-color="#f2465b"><em>{{ item.name }}</em></el-radio>
          </p>
        </div>
      </div>
      <div class="input">
        <svg viewBox="0 0 320 300">
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
                style="stop-color:#ff00ff;"
                offset="0"
                id="stop876" />
              <stop
                style="stop-color:#ff0000;"
                offset="1"
                id="stop878" />
            </linearGradient>
          </defs>
          <path d="m 40,120.00016 239.99984,-3.2e-4 c 0,0 24.99263,0.79932 25.00016,35.00016 0.008,34.20084 -25.00016,35 -25.00016,35 h -239.99984 c 0,-0.0205 -25,4.01348 -25,38.5 0,34.48652 25,38.5 25,38.5 h 215 c 0,0 20,-0.99604 20,-25 0,-24.00396 -20,-25 -20,-25 h -190 c 0,0 -20,1.71033 -20,25 0,24.00396 20,25 20,25 h 168.57143" />
        </svg>
        <el-input placeholder="" v-model="data.title" @focus="moveLine(0)">
          <template slot="prepend">标题</template>
        </el-input>
        <el-input placeholder="" v-model="data.point" @focus="moveLine(1)">
          <template slot="prepend">地点</template>
        </el-input>
        <el-select v-model="data.album_id" placeholder="" @focus="moveLine(2)">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </div>
      <div class="submit" @touchend.stop="submit">上传</div>
    </el-dialog>
  </div>
</template>

<script>
  import anime from 'animejs'
  import axios from '../../router/axios'

export default {
  name: 'E-upload',

  components: {},
  data () {
    return {
      data: {
        type: 'picture'
      },
      options: [],
      typeData: [{
        'type': 'picture',
        'name': '图片',
        'label': '1',
        'url': 'static/picture.png'
      },{
        'type': 'media',
        'name': '视频',
        'label': '2',
        'url': 'static/media.png'
      }],
      dialogVisible: false,
      fileList: [],
      current: null
    }
  },
  methods: {
    submit() {
      console.log(this.data);
      this.$refs.upload.submit();
    },
    success(response, file, fileList) {
      console.log(response, file, fileList);
      if (response.data.e === 0) {
        this.$message({
          type: 'success',
          message: response.data.code
        })
        this.$emit('shutdown');
      } else {
        this.$message({
          type: 'error',
          message: response.data.code
        })
      }
      this.dialogVisible = false;
    },
    upload_change(file, fileList) {
      if (fileList.length !== 0) {
        document.querySelector('.el-upload-list').style.width = '130px';
      } else {
        document.querySelector('.el-upload-list').style.width = '0';
      }
    },
    upload_remove(file, fileList) {
      this.upload_change(file, fileList);
    },
    checkRadio(val) {
      this.data.type = val;
    },
    open(val) {
      this.dialogVisible = val;
    },
    get_album() {
      // 获取所有相册信息
      var vm = this;
      axios.post('/api/get_album_info/', {}, (e) => {
        vm.options = e.data;
      })
    },
    moveLine(val) {
      if (this.current) this.current.pause();
      var value = 0;
      switch (val) {
        case 0 : value = 0; break;
        case 1 : value = -336; break;
        case 2 : value = -730; break;
      }
      this.current = anime({
        targets: 'path',
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
  mounted:function () {
    this.get_album();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.E-upload {
  position: relative;
  .type {
    display: flex;
    align-items: center;
    justify-content: space-around;
    width: 80%;
    height: 60px;
    margin: 14px auto;
    text-align: center;
    z-index: 2;
    em {
      font-style: normal;
    }
    img {
      width: 34px;
    }
  }
  .input {
    margin-top: 44px;
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
  svg {
    position: absolute;
    width: 300px;
    height: 270px;
    top: 102px;
    z-index: -1;
  }
  path {
    fill: none;
    stroke: url(#linearGradient);;
    stroke-width: 3;
    stroke-dasharray: 240, 1386;
  }
}
</style>
