<template>
  <div class="E-upload e_link">
    <el-dialog
      :visible="dialogVisible"
      :show-close="false"
      :before-close="beforeClose"
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
        :multiple="true"
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
        <svg viewBox="0 0 251 147" id="upload_svg">
          <defs>
            <linearGradient
              inkscape:collect="always"
              id="linearGradient"
              x1="1"
              y1="1"
              x2="480"
              y2="1"
              gradientUnits="userSpaceOnUse">
              <stop
                style="stop-color:#fad0c4;"
                offset="0"
                id="stop876" />
              <stop
                style="stop-color:#ffd1ff;"
                offset="1"
                id="stop878" />
            </linearGradient>
          </defs>
          <path d="M23.8,4.5H226.73s9.61,21.78,0,40.83H23.8s-10.68,21.78,0,40.84H226.73s8.54,24.5,0,40.83H23.8" />
        </svg>
        <el-input placeholder="" v-model="data.title" @focus="moveLine(0)">
          <template slot="prepend" style="background-color: #f7bcf1">标题</template>
        </el-input>
        <el-input placeholder="" v-model="data.point" @focus="moveLine(1)">
          <template slot="prepend">地点</template>
        </el-input>
        <el-select v-model="data.album_id" placeholder="" @focus="moveLine(2)">
          <span slot="prefix">相册</span>
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
  import bus from '../../router/bus'

export default {
  name: 'E-upload',

  components: {},
  data () {
    return {
      data: {
        type: 'picture',
        type_picture: '4'
      },
      options: [],
      type_pictures: [],
      typeData: [{'type': 'picture', 'name': '图片', 'label': '1', 'url': 'static/picture.png'},{'type': 'media', 'name': '视频', 'label': '2', 'url': 'static/media.png'}],
      dialogVisible: false,
      fileList: [],
      current: null
    }
  },
  methods: {
    beforeClose(done) {
      done();
      this.$emit('shutdown');
    },
    submit() {
      console.log(this.data);
      this.$refs.upload.submit();
    },
    success(response, file, fileList) {
      console.log(response, file, fileList);
      if (response.data.e === 0) {
        bus.$emit('update');
        this.dialogVisible = false;
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
        document.querySelector('.el-upload-list').style.height = '46px';
      } else {
        document.querySelector('.el-upload-list').style.width = '0';
        document.querySelector('.el-upload-list').style.height = '0';
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
        case 1 : value = -245; break;
        case 2 : value = -489; break;
        case 3 : value = -735; break;
      }
      this.current = anime({
        targets: '#upload_svg path',
        strokeDashoffset: {
          value: value,
          duration: 700,
          easing: 'easeOutQuart'
        },
        strokeDasharray: {
          value: '202 1386',
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
    margin: 278px auto 0;
  }
  svg {
    position: absolute;
    top: 212px;
    z-index: -1;
  }
  path {
    fill: none;
    stroke: url(#linearGradient);;
    stroke-width: 3;
    stroke-dasharray: 202, 1386;
  }
}
</style>
